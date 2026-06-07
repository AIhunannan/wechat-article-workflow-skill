# WeChat Article Workflow Skill

A reusable Codex skill for turning rough notes into WeChat Official Account drafts.

## What It Does

- Polishes user notes into concise personal-IP or commentary articles.
- Applies humanized writing rules to reduce AI-like tone.
- Guides image selection or generation for cover and body visuals.
- Produces WeChat-safe HTML with inline styles.
- Checks metadata and readiness with `md2wechat`.
- Publishes WeChat drafts through a direct API helper.
- Archives source, final copy, images, and publish results.

## Install

Copy this folder into a Codex skills directory, for example:

```powershell
Copy-Item -Recurse wechat-article-workflow-skill C:\Users\<you>\.codex\skills\wechat-article-workflow
```

## Requirements

- Python 3
- `requests`
- `md2wechat` CLI
- WeChat Official Account `appid` and `secret` configured in `~/.config/md2wechat/config.yaml`

## Notes

This repository intentionally does not contain WeChat credentials, article drafts, generated images, or private company content.
