# WeChat Article Workflow Skill

中文 | [English](#english)

一个可复用的 Codex Skill，用于把公众号文章从“原始想法/初稿”推进到“图文排版完成并发送到微信公众号草稿箱”。它适合个人 IP、创始人札记、行业观点、客户案例、产品营销和技术科普类文章。

> 核心目标：让写公众号变成一套稳定流程，而不是每次从零摸索。

## 功能概览

- 将原始想法、提纲或初稿润色成更自然、更有人味的公众号文章。
- 保留作者个人判断，减少 AI 味、空话和模板感。
- 把标题当作传播杠杆处理，优先生成更抓眼球、更有转发欲的标题。
- 生成或选择 3-5 张精准匹配正文的图片，并处理“封面图是否也要进入正文”的问题。
- 生成微信公众号兼容的 HTML，尽量使用内联样式，减少草稿箱排版丢失。
- 使用 `md2wechat inspect` 检查标题、作者、摘要、图片和草稿发布条件。
- 通过微信官方接口上传正文图片、上传封面素材并创建草稿。
- 支持把文章、HTML、图片、发布结果归档到 Obsidian 或其它知识库。

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
2. 润色成自然、克制、有观点的公众号文案。
3. 生成 `article.md`，写入标题、作者、摘要。
4. 生成 5-10 个标题候选，优先选择最有好奇心、具体性和转发冲动的标题。
5. 控制标题不超过 32 字，摘要不超过 128 字。
6. 生成或选择 3-5 张精准匹配正文段落的图片。
7. 生成微信公众号安全 HTML，优先使用内联样式。
8. 使用 `md2wechat inspect` 检查草稿发布条件。
9. 上传正文图片到微信图床。
10. 上传封面图为永久素材。
11. 调用微信草稿箱接口创建草稿。
12. 保存 `draft_result.json` 或 `draft_error.json`。
13. 归档文章、HTML、图片和发布信息。

## 标题策略

标题不是文章标签，而是分发入口。工作流默认把标题当作增长杠杆处理。

好标题通常具备至少一个特点：

- 有具体数字，例如“100个蓝盒子”“24小时”“7000万阅读”。
- 有强反差，例如“不是从车库开始的，而是从一个小实验开始”。
- 有隐藏起点，例如“大公司诞生前的小作品”。
- 有反常识判断，例如“融资不是创业的起点”。
- 有名人或事件钩子，例如乔布斯、沃兹、硅谷、OpenAI、Anthropic。

避免过平的标题，例如“读XX有感”“关于XX的思考”“XX给我的启发”。如果标题不够抓人，应先改标题，再发草稿。

## 配图策略

每篇文章默认保持 3-5 张正文图。图片必须和内容精确匹配，不能只是装饰。

推荐组合：

- 1 张封面图：承担第一眼吸引力。
- 1-2 张真实图片：增强可信度，例如实物、书、客户现场、产品、截图。
- 1-2 张概念图：解释核心模型、冲突、流程、方法论或产品价值。

每张图都应该有明确任务：证明真实性、解释概念、制造情绪、展示对象、总结模型。不要使用廉价未来感、随机机器人、空泛商务图标或和段落无关的图片。

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
    ├── body_01.png
    ├── body_02.png
    └── body_03.png
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
- Treat the title as a distribution lever and create more clickable, shareable headline candidates.
- Generate or select 3-5 images that precisely match the article's paragraphs and arguments.
- Handle the difference between WeChat cover images and in-body images.
- Build WeChat-compatible HTML with inline styles.
- Use `md2wechat inspect` to check title, author, digest, images, and draft readiness.
- Upload body images, upload cover material, and create WeChat drafts through official APIs.
- Archive article source, final copy, images, HTML, and publishing results.

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
2. Polish the article into a natural, concise, opinionated draft.
3. Create `article.md` with title, author, and digest.
4. Create 5-10 title candidates and choose the one with the strongest curiosity gap, specificity, and forwarding impulse.
5. Keep title under 32 characters and digest under 128 characters.
6. Generate or choose 3-5 images that match specific paragraphs or arguments.
7. Build WeChat-safe HTML with inline styles.
8. Run `md2wechat inspect` to verify draft readiness.
9. Upload in-body images to WeChat.
10. Upload the cover image as permanent material.
11. Create a WeChat draft through the draft API.
12. Save `draft_result.json` or `draft_error.json`.
13. Archive article files, images, HTML, and publication metadata.

## Title Strategy

The title is not just a label. It is the entry point for distribution.

Strong WeChat titles usually include at least one of these hooks:

- Concrete numbers, such as "100 prototypes", "24 hours", or "70 million reads".
- Sharp contrast, such as "it did not start in the garage".
- Hidden origin stories, such as the small experiment before a major company.
- Counterintuitive claims, such as "funding is not the starting point".
- Famous people, companies, or events, such as Steve Jobs, Wozniak, Silicon Valley, OpenAI, or Anthropic.

Avoid flat titles like "Thoughts on X", "Reflections after reading X", or "What X taught me" unless the user explicitly wants a quiet diary tone. If the title feels weak, revise the title first before publishing.

## Image Strategy

Default to 3-5 in-body images per article. Images must precisely match the content, not decorate it.

Recommended mix:

- 1 cover image for first-impression value.
- 1-2 real images for authenticity, such as objects, books, customer scenes, products, or screenshots.
- 1-2 conceptual images to explain the model, conflict, process, methodology, or product value.

Every image needs a clear job: prove authenticity, explain a concept, create emotional atmosphere, show an object, or summarize a model. Avoid cheap sci-fi, random robots, generic business icons, or images loosely related to the paragraph.

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
    ├── body_01.png
    ├── body_02.png
    └── body_03.png
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
