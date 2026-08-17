# WeChat Article Workflow Skill

中文 | [English](#english)

一个可复用的 Codex Skill，用于把公众号文章从“原始想法/初稿”推进到“图文排版完成并发送到微信公众号草稿箱”。它适合个人 IP、创始人札记、行业观点、客户案例、产品营销和技术科普类文章。

> 核心目标：让写公众号变成一套稳定流程，而不是每次从零摸索。

## 功能概览

- 将原始想法、提纲或初稿润色成更自然、更有人味的公众号文章。
- 保留作者个人判断，减少 AI 味、空话和模板感。
- 文章不设固定字数，篇幅由主题、证据和论证完整度决定。
- 把标题当作传播入口：先生成多个标题候选，再选择更具体、更有冲突和转发动力的版本，默认不超过 32 字。
- 生成或选择封面图、正文图，并处理“封面图是否也要进入正文”的问题。
- 默认准备 3-5 张与段落精准匹配的配图，避免为了装饰而堆图。
- 支持贴图优先：先制作 5-8 张有明确观点和证据的卡片，再按需要派生短视频和长文。
- 支持 AI 项目雷达：从 X、GitHub、Kickstarter、TikTok、YouTube、中文互联网等来源筛选高增长、可复现、有实际价值的项目。
- 用读者痛点、即时收益、证据、复现难度和原创判断筛选选题，避免只追热点和改写 README。
- 用原创度审计卡检查一手贡献、五个信息增量、两个作者独有判断和事实边界，避免“低创作度”和空洞内容。
- 把一个选题派生为图文卡片、短视频脚本、朋友圈、X 帖子和可选长文，但不在未经授权时自动发布。
- 记录阅读、分享、收藏和净增粉，用真实数据调整选题与标题，而不是只看总阅读量。
- 生成微信公众号兼容的 HTML，尽量使用内联样式，减少草稿箱排版丢失。
- 使用 `md2wechat inspect` 检查标题、作者、摘要、图片和草稿发布条件。
- 通过微信官方接口上传正文图片、上传封面素材并创建草稿。
- 支持把文章、HTML、图片、发布结果归档到 Obsidian 或其它知识库。

### 主版本能力

- 写作上优先编辑作者原始思考，保留第一人称、判断和真实案例。
- 排版前先做标题、结构密度、图片、重复标题和敏感配置检查。
- 按项目类型选择图文贴图、30-60 秒短视频、公众号长文或多形态发布。
- 实用项目必须先建立证据卡，区分官方事实、第三方说法、作者实测和推断。
- 发布失败时保存具体错误，尤其是微信公众号 `40164 invalid ip` 白名单错误，方便后续重试。

### 长度与结构原则

- 不设固定字数上限，也不默认要求控制在 1000 字以内。
- 简单观点短写；研究、客户案例、技术解释和个人经历需要时可以充分展开。
- 每一节都必须推进中心论点，删除重复表达、空洞过渡和无关背景。
- 长文使用清晰的小标题与自然过渡，让读者快速浏览也能理解完整逻辑。
- 只有用户明确提出字数要求时，才把字数作为硬性验收条件。

### 原创度与信息密度

- AI 可以研究、质疑、整理和润色，但不能虚构作者经历、客户反馈或“我实测”。
- 工具与行业文章应尽量包含一个一手贡献、两个主来源、一个非共识判断和一个可立即使用的资产。
- 每约 250-300 个汉字应新增事实、案例、机制、比较、方法、结果、限制或决策中的至少一项。
- 发布前复制并完成 `assets/originality_audit.md`；未通过则留在研究阶段，不靠扩写凑成文章。
- 标题里的 Star、增长、金额、价格、速度和结果必须在发布当天重新核验并注明时间。

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
├── CHANGELOG.md
├── assets/
│   ├── daily_topic_radar.csv
│   ├── growth_log.csv
│   └── originality_audit.md
├── scripts/
│   └── publish_wechat_direct.py
├── templates/
│   ├── evidence_card.md
│   └── graphic_post.md
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

1. 收集作者原始想法，或运行多平台 AI 项目雷达。
2. 扫描最近 24 小时至 30 天的一手来源，建立带时间戳的 `evidence_card.md`。
3. 按 40 分制选择一个主选题和两个备选选题；不合格时宁可少报，不凑数。
4. 锁定目标读者、搜索关键词、核心判断和内容形态。
5. 贴图优先时先生成 `graphic_post.md`，锁定标题、封面和 5-8 张卡片。
6. 需要深度时再生成 `article.md`；只有用户明确提出时才执行字数限制。
7. 完成 `originality_audit.md`，确认一手贡献、五个信息增量、两个作者独有判断和 `PASS` 结果。
8. 优先生成或选择真实证据图，再补充封面和解释性图片。
9. 生成微信公众号安全 HTML 或图文贴图素材，使用平台原生结尾。
10. 使用 `md2wechat inspect` 或图文负载检查标题、图片顺序和发布条件。
11. 经用户授权后上传正文图、封面并创建微信草稿；其它平台同样需要单独授权。
12. 保存 `draft_result.json` 或 `draft_error.json`，归档证据、文案、图片和发布信息。
13. 派生短视频、朋友圈和 X 文案，但不自动发布。
14. 发布后记录 2 小时、24 小时和 7 天数据，按净增粉与分享率复盘。

## 文章目录建议

```text
YYYY-MM-DD_article_slug/
├── evidence_card.md
├── originality_audit.md
├── graphic_post.md
├── article.md
├── article_wechat.html
├── article_wechat_uploaded.html
├── draft_result.json
├── draft_error.json
├── distribution_kit.md
├── growth_snapshot.csv
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
- Use no fixed article word count; length follows the topic, evidence, and completeness of the argument.
- Treat the title as a distribution lever: generate several candidates and choose a specific, high-curiosity title under 32 characters by default.
- Generate or select cover and body images.
- Use 3-5 focused images by default, each matched to a specific paragraph or argument.
- Handle the difference between WeChat cover images and in-body images.
- Build image-first `5-8` card posts before deriving video or long-form copy when reach is the primary goal.
- Run an AI project radar across X, GitHub, Kickstarter, TikTok, YouTube, first-party product pages, and local-language sources.
- Use an originality audit to require first-party contribution, five information gains, two author-specific judgments, and explicit claim boundaries.
- Derive a short-video script, Moments post, X post, and optional long article from one verified evidence set without auto-publishing.
- Track reads, shares, saves, and net followers so topic and title decisions improve from real data.
- Build WeChat-compatible HTML with inline styles.
- Use `md2wechat inspect` to check title, author, digest, images, and draft readiness.
- Upload body images, upload cover material, and create WeChat drafts through official APIs.
- Archive article source, final copy, images, HTML, and publishing results.

### Main Version Capabilities

- Start from the author's own reflections and preserve first-person judgment and real cases.
- Check title metadata limits, structural density, image count, duplicate-title risk, and sensitive configuration before publishing.
- Create a dated evidence card for practical projects and distinguish official facts, third-party claims, first-party observations, and inference.
- Choose between graphic post, `30-60` second video, long article, or multi-format package according to the proof and reader value.
- Persist concrete publish failures, especially WeChat `40164 invalid ip` whitelist errors, so the draft can be retried safely.

### Length and Structure

- There is no fixed word-count ceiling or default 1,000-character target.
- Keep simple ideas short; allow research, customer cases, technical explanations, and personal experience the space they genuinely need.
- Every section must advance the central thesis. Remove repetition, filler transitions, and irrelevant background.
- Use clear headings and natural transitions in longer articles so the logic remains easy to scan.
- Treat length as a hard acceptance criterion only when the user explicitly requests it.

### Originality and Information Density

- AI may research, challenge, structure, and polish, but it must not invent experience, customer feedback, or hands-on results.
- A researched piece should contain one first-party contribution, two primary sources when available, one non-obvious judgment, and one immediately useful artifact.
- Roughly every `250-300` Chinese characters should add a fact, example, mechanism, comparison, instruction, result, limitation, or decision.
- Copy and complete `assets/originality_audit.md` before publishing. Failed work stays in research instead of being padded into an article.
- Recheck volatile title claims such as stars, growth, price, funding, delivery, speed, and results on publication day.

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
├── CHANGELOG.md
├── assets/
│   ├── daily_topic_radar.csv
│   ├── growth_log.csv
│   └── originality_audit.md
├── scripts/
│   └── publish_wechat_direct.py
├── templates/
│   ├── evidence_card.md
│   └── graphic_post.md
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

1. Collect the author's source notes or run the multi-platform AI project radar.
2. Scan the latest `24 hours` to `30 days` and create a timestamped `evidence_card.md` from primary sources.
3. Use the `40`-point gate to select one recommendation and two backups. Report fewer rather than adding weak topics.
4. Lock the reader, search keywords, thesis, and content format.
5. For image-first work, create `graphic_post.md` first and lock the title, cover, and `5-8` cards.
6. Create `article.md` only when deeper reasoning is justified. Enforce a length limit only when requested.
7. Complete `originality_audit.md` and require first-party contribution, five information gains, two author-specific elements, and `PASS`.
8. Select proof visuals first, then add cover and explanatory art.
9. Build WeChat-safe HTML or image-post assets with platform-native endings.
10. Run `md2wechat inspect` or inspect the image-post payload, card count, and image order.
11. Publish only after authorization; save the exact success or failure result.
12. Archive evidence, copy, visuals, HTML, and publication metadata.
13. Prepare short-video, Moments, and X derivatives without auto-publishing.
14. Record `2h/24h/7d` data and review by net followers and share rate.

## Recommended Article Folder

```text
YYYY-MM-DD_article_slug/
├── evidence_card.md
├── originality_audit.md
├── graphic_post.md
├── article.md
├── article_wechat.html
├── article_wechat_uploaded.html
├── draft_result.json
├── draft_error.json
├── distribution_kit.md
├── growth_snapshot.csv
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
