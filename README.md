# WeChat Article Workflow Skill

中文 | [English](#english)

一个可复用的 Codex Skill，用于把公众号文章从“原始想法/初稿”推进到“图文排版完成并发送到微信公众号草稿箱”。它适合个人 IP、创始人札记、行业观点、客户案例、产品营销和技术科普类文章。

> 核心目标：让写公众号变成一套稳定流程，而不是每次从零摸索。

## 功能概览

- 将原始想法、提纲或初稿润色成更自然、更有人味的公众号文章。
- 保留作者个人判断，减少 AI 味、空话和模板感。
- 把标题当作传播入口：先生成多个标题候选，再选择更具体、更有冲突和转发动力的版本，默认不超过 32 字。
- 生成或选择封面图、正文图，并处理“封面图是否也要进入正文”的问题。
- 默认准备 3-5 张与段落精准匹配的配图，避免为了装饰而堆图。
- 生成微信公众号兼容的 HTML，尽量使用内联样式，减少草稿箱排版丢失。
- 使用 `md2wechat inspect` 检查标题、作者、摘要、图片和草稿发布条件。
- 通过微信官方接口上传正文图片、上传封面素材并创建草稿。
- 支持把文章、HTML、图片、发布结果归档到 Obsidian 或其它知识库。

### 主版本能力

- 写作上优先编辑作者原始思考，保留第一人称、判断和真实案例。
- 排版前先做标题、字数、图片、重复标题和敏感配置检查。
- 发布失败时保存具体错误，尤其是微信公众号 `40164 invalid ip` 白名单错误，方便后续重试。

## 适用场景

- 个人 IP 公众号文章。
- 创业者、CTO、产品经理、架构师的个人思考。
- 行业热点评论和深度观点。
- 客户案例复盘。
- 产品介绍、技术方案介绍、招商和品牌营销文章。
- 需要“写作、配图、排版、草稿箱发布”一条龙的内容团队。

## 不适合什么

- 自动群发或自动发布正式文章。
- 绕过微信公众号后台审核。
- 生成虚假事实、虚假客户案例或夸大收益承诺。
- 在仓库中保存公众号密钥、API Key 或客户敏感信息。

## 仓库结构

```text
wechat-article-workflow-skill/
├── SKILL.md
├── README.md
├── scripts/
│   └── publish_wechat_direct.py
└── .gitignore
```

## 安装

把整个目录复制到 Codex Skills 目录，例如：

```powershell
Copy-Item -Recurse wechat-article-workflow-skill C:\Users\<you>\.codex\skills\wechat-article-workflow
```

安装后，在 Codex 对话里可以说：

```text
请按 wechat-article-workflow 流程，把这篇初稿润色、配图、排版并发到公众号草稿箱。
```

## 依赖

- Python 3
- Python package: `requests`
- `md2wechat` CLI
- 微信公众号 AppID 和 AppSecret
- 可选：Obsidian 或其它本地知识库

安装 `requests`：

```powershell
python -m pip install requests
```

## 微信配置

发布脚本默认从下面文件读取微信公众号配置：

```text
~/.config/md2wechat/config.yaml
```

配置示例：

```yaml
wechat:
  appid: "YOUR_WECHAT_APPID"
  secret: "YOUR_WECHAT_APP_SECRET"
```

注意：

- 不要把真实 `appid`、`secret`、API Key 提交到 GitHub。
- 微信公众号后台需要把当前出口 IP 加入白名单。
- 如果接口返回 `40164 invalid ip ... not in whitelist`，以微信错误里显示的 IP 为准，不一定等于普通公网 IP 查询结果。

## 标准工作流

1. 收集作者原始想法、提纲或初稿。
2. 保留作者判断，去除填充语和明显 AI 写作痕迹。
3. 生成 5-10 个标题候选，选择具体、有冲突和转发动力的标题。
4. 生成 `article.md`，写入标题、作者、摘要，并检查长度限制。
5. 生成或选择 3-5 张与正文精准匹配的封面图和正文图。
6. 生成微信公众号安全 HTML，优先使用内联样式。
7. 使用 `md2wechat inspect` 检查标题、图片和草稿发布条件。
8. 上传正文图片到微信图床。
9. 上传封面图为永久素材。
10. 调用微信草稿箱接口创建草稿。
11. 保存 `draft_result.json` 或 `draft_error.json`。
12. 归档文章、HTML、图片和发布信息。

## 文章目录建议

```text
YYYY-MM-DD_article_slug/
├── article.md
├── article_wechat.html
├── article_wechat_uploaded.html
├── draft_result.json
├── draft_error.json
└── images/
    ├── cover.png
    └── body_01.png
```

## 发布脚本用法

脚本路径：

```text
scripts/publish_wechat_direct.py
```

示例：

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

参数说明：

| 参数 | 说明 |
| --- | --- |
| `--root` | 文章目录 |
| `--html` | 已排版好的公众号 HTML |
| `--cover` | 用于公众号封面的图片 |
| `--inline` | 需要上传并替换到正文里的图片，可传多次 |
| `--title` | 微信草稿标题，最长 32 字 |
| `--author` | 作者名 |
| `--digest` | 摘要，最长 128 字 |
| `--config` | 可选，指定 md2wechat 配置文件路径 |

说明：

- 公众号封面不会自动显示在正文里。
- 如果希望封面图也出现在正文，请同时传入 `--inline images\cover.png`。
- 脚本会生成 `article_wechat_uploaded.html`，其中本地图片路径会被替换成微信图片 URL。

## 常见问题

### 1. 草稿标题变成“AI测试文章”怎么办？

不要使用会自动生成测试标题的发布路径。优先使用本仓库的 `publish_wechat_direct.py`，它会显式写入标题、作者和摘要。

### 2. 为什么正文只显示一张图？

微信公众号封面素材不会自动进入正文。如果希望正文也显示封面图，需要把封面图同时作为正文图片插入 HTML，并作为 `--inline` 参数上传。

### 3. IP 白名单报错怎么办？

如果返回：

```text
40164 invalid ip xxx.xxx.xxx.xxx not in whitelist
```

请到微信公众号后台把错误中显示的 IP 加入白名单。注意这个 IP 可能不同于 `ipify` 等公网查询服务显示的 IP。

### 4. md2wechat API 转换失败怎么办？

可以继续使用本 skill 的本地内联 HTML 工作流，再通过 `publish_wechat_direct.py` 直接创建草稿。

## 安全说明

- 本仓库不包含真实公众号密钥。
- 不包含任何用户文章、客户案例、图片素材或商业敏感内容。
- `.gitignore` 已排除草稿结果、错误日志、图片目录、环境变量文件和配置文件。
- 发布前建议运行敏感信息扫描，例如：

```powershell
rg -n "secret|token|appid|sk-|wx|password|api_key" .
```

---

## English

Reusable Codex Skill for turning rough notes into polished WeChat Official Account drafts. It is designed for personal-brand writing, founder notes, industry commentary, customer stories, product marketing, and technical explainers.

> Goal: make WeChat article production a repeatable workflow instead of a manual one-off process.

## Features

- Polish raw notes, outlines, or drafts into natural WeChat articles.
- Preserve the author's point of view while reducing AI-like tone.
- Treat the title as a distribution lever: generate several candidates and choose a specific, high-curiosity title under 32 characters by default.
- Generate or select cover and body images.
- Use 3-5 focused images by default, each matched to a specific paragraph or argument.
- Handle the difference between WeChat cover images and in-body images.
- Build WeChat-compatible HTML with inline styles.
- Use `md2wechat inspect` to check title, author, digest, images, and draft readiness.
- Upload body images, upload cover material, and create WeChat drafts through official APIs.
- Archive article source, final copy, images, HTML, and publishing results.

### Main Version Capabilities

- Start from the author's own reflections and preserve first-person judgment and real cases.
- Check title length, article length, image count, duplicate-title risk, and sensitive configuration before publishing.
- Persist concrete publish failures, especially WeChat `40164 invalid ip` whitelist errors, so the draft can be retried safely.

## Use Cases

- Personal-brand WeChat articles.
- Founder, CTO, product manager, or architect reflections.
- Industry commentary and trend analysis.
- Customer-case writeups.
- Product introductions and technical solution explainers.
- Content teams that need writing, images, formatting, and draft upload in one workflow.

## Not For

- Automatic mass publishing.
- Bypassing WeChat review.
- Fabricating facts, customers, or results.
- Storing WeChat credentials or sensitive customer data in a repository.

## Repository Structure

```text
wechat-article-workflow-skill/
├── SKILL.md
├── README.md
├── scripts/
│   └── publish_wechat_direct.py
└── .gitignore
```

## Installation

Copy the folder into your Codex skills directory:

```powershell
Copy-Item -Recurse wechat-article-workflow-skill C:\Users\<you>\.codex\skills\wechat-article-workflow
```

Then ask Codex:

```text
Use the wechat-article-workflow skill to polish, illustrate, format, and upload this article to my WeChat draft box.
```

## Requirements

- Python 3
- Python package: `requests`
- `md2wechat` CLI
- WeChat Official Account AppID and AppSecret
- Optional: Obsidian or another local knowledge base

Install `requests`:

```powershell
python -m pip install requests
```

## WeChat Configuration

The publishing helper reads WeChat credentials from:

```text
~/.config/md2wechat/config.yaml
```

Example:

```yaml
wechat:
  appid: "YOUR_WECHAT_APPID"
  secret: "YOUR_WECHAT_APP_SECRET"
```

Important:

- Do not commit real `appid`, `secret`, API keys, or access tokens.
- Add your current outbound IP to the WeChat Official Account IP whitelist.
- If WeChat returns `40164 invalid ip ... not in whitelist`, trust the IP shown in the WeChat error. It may differ from normal public-IP lookup services.

## Standard Workflow

1. Collect the author's raw notes, outline, or draft.
2. Preserve the author's judgment and remove filler and obvious AI writing traces.
3. Generate 5-10 title candidates and choose a specific, high-curiosity title.
4. Create `article.md` with title, author, digest, and length checks.
5. Generate or choose 3-5 focused cover and body images.
6. Build WeChat-safe HTML with inline styles.
7. Run `md2wechat inspect` to verify metadata, images, and draft readiness.
8. Upload in-body images to WeChat.
9. Upload the cover image as permanent material.
10. Create a WeChat draft through the draft API.
11. Save `draft_result.json` or `draft_error.json`.
12. Archive article files, images, HTML, and publication metadata.

## Recommended Article Folder

```text
YYYY-MM-DD_article_slug/
├── article.md
├── article_wechat.html
├── article_wechat_uploaded.html
├── draft_result.json
├── draft_error.json
└── images/
    ├── cover.png
    └── body_01.png
```

## Publishing Helper

Script:

```text
scripts/publish_wechat_direct.py
```

Example:

```powershell
python scripts\publish_wechat_direct.py `
  --root C:\path\to\article_folder `
  --html article_wechat.html `
  --cover images\cover.png `
  --inline images\cover.png `
  --inline images\body_01.png `
  --title "Do Not Worship Talent" `
  --author "Author Name" `
  --digest "Article summary"
```

Arguments:

| Argument | Description |
| --- | --- |
| `--root` | Article folder |
| `--html` | Final WeChat-compatible HTML |
| `--cover` | Cover image used as WeChat draft cover |
| `--inline` | Image to upload and replace in the HTML body. Can be passed multiple times |
| `--title` | Draft title, max 32 chars |
| `--author` | Author name |
| `--digest` | Draft digest, max 128 chars |
| `--config` | Optional md2wechat config path |

Notes:

- A WeChat cover image does not automatically appear inside the article body.
- If you want the cover to appear in the article, also include it as an in-body image and pass it with `--inline`.
- The script writes `article_wechat_uploaded.html` after replacing local image paths with WeChat image URLs.

## Troubleshooting

### Draft title becomes "AI测试文章"

Use `publish_wechat_direct.py` instead of test-only draft helpers. This script explicitly sets title, author, and digest.

### Only one image appears in the article

The cover image is separate from body images. Embed the cover in the HTML body and pass it as `--inline` if it should appear in the article.

### IP whitelist error

If WeChat returns:

```text
40164 invalid ip xxx.xxx.xxx.xxx not in whitelist
```

Add the IP shown in the WeChat error to the Official Account IP whitelist. This IP can differ from generic public-IP lookup services.

### md2wechat API conversion fails

Use a local inline-HTML workflow, then publish with `publish_wechat_direct.py`.

## Security

- This repository does not include real WeChat credentials.
- It does not include private drafts, customer cases, images, or company-sensitive content.
- `.gitignore` excludes draft results, error logs, images, environment files, and config files.
- Before publishing changes, run a secret scan such as:

```powershell
rg -n "secret|token|appid|sk-|wx|password|api_key" .
```
