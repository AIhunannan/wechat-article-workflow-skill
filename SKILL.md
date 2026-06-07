---
name: wechat-article-workflow
description: Use when creating, polishing, illustrating, formatting, publishing, or archiving WeChat Official Account articles. Covers the full workflow from draft notes to humanized article, image generation, md2wechat checks, WeChat draft upload, and local knowledge-base archive.
---

# WeChat Article Workflow

This skill turns rough article notes into a polished WeChat Official Account draft. It is designed for personal-IP, founder notes, industry commentary, and customer-case articles.

## Voice Rules

- Start from the user's own notes and preserve their point of view.
- Prefer editing and restructuring over generic ghostwriting.
- Keep articles concise by default, often under 1000 Chinese characters unless the user asks for depth.
- Use plain, sharp, reflective writing instead of generic marketing language.
- Avoid AI-heavy patterns: formulaic openings, over-explaining, slogan endings, excessive lists, and generic inspirational tone.
- If a humanizer skill is available, apply it before final formatting.

## Standard Workflow

1. Clarify the article angle only if needed. Otherwise make a reasonable editorial judgment.
2. Create or polish `article.md` with frontmatter:
   - `title`: final WeChat title, max 32 chars.
   - `author`: configured author name.
   - `digest`: max 128 chars.
3. Check length with non-whitespace count and keep it under the requested limit.
4. Generate or select images:
   - Prefer built-in image generation for article art unless the user explicitly requests a provider.
   - Copy selected generated images into the article `images\` folder and leave originals in place.
   - Use one strong 16:9 cover and one focused 16:9 body image when possible.
   - If the user expects every generated image to appear in the article body, embed the cover as the first body image too; WeChat cover material alone does not display inside article content.
5. Build WeChat-safe HTML:
   - Use inline styles for the final WeChat body.
   - Avoid relying on `<style>` tags for final WeChat content.
   - Keep the official WeChat title out of the body H1 to avoid duplicate title risk.
6. Run `md2wechat inspect` before publishing:
   - Confirm title, author, digest, images, upload readiness, and draft readiness.
   - If md2wechat API theme conversion fails, use a local inline HTML path and direct WeChat draft script.
7. Publish to WeChat draft:
   - Prefer a direct draft script that explicitly sets title, author, digest, content, and cover media id.
   - Never use a flow that may create a default title such as "AI测试文章".
   - If WeChat returns `40164 invalid ip ... not in whitelist`, report the exact IP shown by WeChat. This IP can differ from generic public-IP lookup services.
8. Archive:
   - Save source notes, `article.md`, `article_wechat.html`, images, publish result, and a publication note.
   - If using Obsidian or another knowledge base, archive by date and update the timeline/index.

## Directory Convention

Recommended working directory:

```text
<workspace>\YYYY-MM-DD_article_slug\
```

Recommended files:

```text
article.md
article_wechat.html
article_wechat_uploaded.html
draft_result.json
draft_error.json
images\cover.png
images\body_01.png
```

## Publishing Helper

Use `scripts\publish_wechat_direct.py` when md2wechat conversion or `test-draft` is unreliable.

Example:

```powershell
python scripts\publish_wechat_direct.py `
  --root C:\path\to\article_folder `
  --html article_wechat.html `
  --cover images\cover.png `
  --inline images\cover.png `
  --inline images\body_01.png `
  --title "别迷信天赋，成功靠知识和实践" `
  --author "作者名" `
  --digest "一篇文章摘要"
```

The helper reads WeChat `appid` and `secret` from `~\.config\md2wechat\config.yaml`, uploads body images with `uploadimg`, uploads the cover as permanent material, creates a draft via `/cgi-bin/draft/add`, and writes `draft_result.json` or `draft_error.json`.

## Final Response Checklist

- State whether the WeChat draft was created.
- If successful, include draft `media_id`.
- Include the final title.
- Link to local article and archive paths.
- Mention any real blocker, especially IP whitelist errors.
