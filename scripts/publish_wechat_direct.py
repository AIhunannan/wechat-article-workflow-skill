from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import requests


def clean_value(value: str) -> str:
    value = value.strip()
    if value.startswith(("'", '"')) and value.endswith(("'", '"')):
        return value[1:-1]
    return value


def load_wechat_config(config: Path) -> tuple[str, str]:
    section = ""
    appid = ""
    secret = ""
    for raw in config.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if not raw.startswith((" ", "\t")) and raw.rstrip().endswith(":"):
            section = raw.strip().rstrip(":")
            continue
        if section != "wechat":
            continue
        line = raw.strip()
        if line.startswith("appid:"):
            appid = clean_value(line.split(":", 1)[1])
        if line.startswith("secret:"):
            secret = clean_value(line.split(":", 1)[1])
    if not appid or not secret:
        raise RuntimeError("Missing wechat appid/secret in md2wechat config")
    return appid, secret


def get_access_token(appid: str, secret: str) -> str:
    response = requests.get(
        "https://api.weixin.qq.com/cgi-bin/token",
        params={"grant_type": "client_credential", "appid": appid, "secret": secret},
        timeout=30,
    )
    response.raise_for_status()
    data = response.json()
    token = data.get("access_token")
    if not token:
        raise RuntimeError(json.dumps({"stage": "token", "response": data}, ensure_ascii=False, indent=2))
    return token


def upload_content_image(token: str, path: Path) -> str:
    with path.open("rb") as fp:
        response = requests.post(
            "https://api.weixin.qq.com/cgi-bin/media/uploadimg",
            params={"access_token": token},
            files={"media": (path.name, fp, "image/png")},
            timeout=60,
        )
    response.raise_for_status()
    data = response.json()
    url = data.get("url")
    if not url:
        raise RuntimeError(json.dumps({"stage": "upload_content_image", "path": str(path), "response": data}, ensure_ascii=False, indent=2))
    return url


def upload_cover_material(token: str, path: Path) -> str:
    with path.open("rb") as fp:
        response = requests.post(
            "https://api.weixin.qq.com/cgi-bin/material/add_material",
            params={"access_token": token, "type": "image"},
            files={"media": (path.name, fp, "image/png")},
            timeout=60,
        )
    response.raise_for_status()
    data = response.json()
    media_id = data.get("media_id")
    if not media_id:
        raise RuntimeError(json.dumps({"stage": "upload_cover_material", "path": str(path), "response": data}, ensure_ascii=False, indent=2))
    return media_id


def create_draft(token: str, title: str, author: str, digest: str, content: str, thumb_media_id: str) -> dict[str, Any]:
    payload = {
        "articles": [
            {
                "title": title,
                "author": author,
                "digest": digest,
                "content": content,
                "content_source_url": "",
                "thumb_media_id": thumb_media_id,
                "need_open_comment": 0,
                "only_fans_can_comment": 0,
            }
        ]
    }
    response = requests.post(
        "https://api.weixin.qq.com/cgi-bin/draft/add",
        params={"access_token": token},
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        timeout=60,
    )
    response.raise_for_status()
    data = response.json()
    if "media_id" not in data:
        raise RuntimeError(json.dumps({"stage": "create_draft", "response": data}, ensure_ascii=False, indent=2))
    return data


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a WeChat draft from finalized inline HTML.")
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--html", required=True)
    parser.add_argument("--cover", required=True)
    parser.add_argument("--inline", action="append", default=[])
    parser.add_argument("--title", required=True)
    parser.add_argument("--author", required=True)
    parser.add_argument("--digest", required=True)
    parser.add_argument("--config", type=Path, default=Path.home() / ".config" / "md2wechat" / "config.yaml")
    args = parser.parse_args()

    root = args.root.resolve()
    html_path = root / args.html
    cover_path = root / args.cover
    inline_paths = [root / item for item in args.inline]

    appid, secret = load_wechat_config(args.config)
    token = get_access_token(appid, secret)

    html = html_path.read_text(encoding="utf-8")
    uploads: dict[str, str] = {}
    for image in inline_paths:
        url = upload_content_image(token, image)
        uploads[image.name] = url
        html = html.replace(image.as_posix(), url)
        html = html.replace(str(image), url)
        html = html.replace(image.relative_to(root).as_posix(), url)
        html = html.replace(str(image.relative_to(root)), url)

    uploaded_html = root / "article_wechat_uploaded.html"
    uploaded_html.write_text(html, encoding="utf-8")

    thumb_media_id = upload_cover_material(token, cover_path)
    draft = create_draft(token, args.title, args.author, args.digest, html, thumb_media_id)
    result = {
        "success": True,
        "title": args.title,
        "author": args.author,
        "digest": args.digest,
        "html": str(uploaded_html),
        "content_images": uploads,
        "cover_media_id": thumb_media_id,
        "draft": draft,
    }
    (root / "draft_result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        error = {"success": False, "error": str(exc)}
        try:
            root_arg = None
            import sys

            for i, value in enumerate(sys.argv):
                if value == "--root" and i + 1 < len(sys.argv):
                    root_arg = Path(sys.argv[i + 1])
                    break
            if root_arg:
                (root_arg / "draft_error.json").write_text(json.dumps(error, ensure_ascii=False, indent=2), encoding="utf-8")
        finally:
            raise
