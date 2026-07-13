---
name: wechat-article-workflow
description: Use when creating, polishing, illustrating, formatting, publishing, or archiving WeChat Official Account articles. Covers the workflow from source notes to humanized article, image generation, md2wechat checks, WeChat draft upload, and local knowledge-base archive.
---

# WeChat Article Workflow

This skill is for personal-brand WeChat articles. Default to editing the author's own reflections, not generic ghostwriting.

## Voice Rules

- Start from the user's notes and preserve his personal judgment.
- Keep the article concise, usually under 1000 Chinese characters unless requested otherwise.
- Prefer plain, sharp, reflective writing over polished marketing language.
- Avoid AI-heavy patterns: formulaic openings, over-explaining, slogan endings, excessive lists, and generic inspirational tone.
- Use a local `humanizer-zh` skill when available and apply its rules.

## Title Rules

- Treat the title as a growth lever, not a label. A good title can matter more than a good paragraph.
- Before finalizing, generate 5-10 candidate titles and choose the one with the strongest curiosity gap, specificity, and forwarding impulse.
- Prefer titles with concrete hooks: numbers, extreme contrast, hidden origin stories, surprising causal claims, famous names, or high-stakes consequences.
- Use the user's proven pattern as a benchmark: `一篇文章到底讲了啥？让硅谷集体失眠，24小时内疯传，7000万阅读`.
- Good title directions:
  - `X诞生前，先发生了一个没人重视的小故事`
  - `真正改变X的，不是Y，而是Z`
  - `为什么我越来越相信：X比融资更重要`
  - `一个被忽视的小实验，后来长成了X`
- Keep the final WeChat title within 32 Chinese characters when possible, but do not make it bland just to be short.
- Avoid flat summary titles such as `关于XX的思考`, `XX给我的启发`, `读XX有感`, unless the user explicitly wants a low-key diary tone.

## Standard Workflow

1. Clarify the article angle only if genuinely needed. Otherwise make a reasonable editorial judgment.
2. Write or polish `article.md` with frontmatter:
   - `title`: final WeChat title, max 32 chars.
   - `author`: configured author name.
   - `digest`: max 128 chars.
3. Before locking the title, create a short title shortlist internally and pick the strongest one. If the user criticizes the title, revise the title first and republish if needed.
4. Check length with non-whitespace count and keep it near the requested limit. Around 1000 Chinese characters is acceptable when the story needs breathing room.
5. Generate or select images:
   - Prefer Codex built-in image generation for article art unless the user explicitly requests a provider.
   - Generated images are usually under `$CODEX_HOME/generated_images/...`; copy the chosen images into the article `images\` folder and leave originals in place.
   - Default to 3-5 total in-body images per article, including the cover if it should appear in the body.
   - Use one strong 16:9 cover plus 2-4 body images that match specific paragraphs or arguments.
   - Each image must have a job: prove authenticity, explain a concept, create emotional atmosphere, show a product/object, or summarize a key model. Do not add generic decoration.
   - When the user provides real photos, prefer them for authenticity and place them early if they strengthen trust.
   - For AI-generated images, make prompts specific to the paragraph: people, objects, scene, metaphor, mood, color palette, and explicit `no text, no logos` constraints.
   - Avoid cheap futuristic imagery, random robots, generic business icons, and images that only loosely match the paragraph.
   - If the user expects every generated image to appear in the article body, embed the cover as the first body image too; WeChat cover material alone does not display inside article content.
6. Build WeChat-safe HTML:
   - Use inline styles only.
   - Avoid relying on `<style>` tags for final WeChat body.
   - Keep the official WeChat title out of the body H1 to avoid duplicate title risk.
7. Run `md2wechat inspect` before publishing:
   - Confirm title, author, digest, images, upload readiness, draft readiness.
   - If md2wechat API theme conversion fails, use the local inline HTML path and direct WeChat draft script.
8. Publish to WeChat draft:
   - Prefer a direct draft script that explicitly sets title, author, digest, content, and cover media id.
   - Never use a flow that may create a default title such as "AI测试文章".
   - If WeChat returns `40164 invalid ip ... not in whitelist`, report the exact IP shown by WeChat. This IP can differ from generic public-IP lookup services, so trust the WeChat error.
9. Archive to Obsidian:
   - Base path: the configured local knowledge-base root.
   - Article path: `50_输出成果\IP文章成品\YYYY\YYYY-MM\YYYY-MM-DD_文章标题\` when using the default Obsidian layout.
   - Save `原始感想.md`, `文章.md`, `article_wechat.html`, `发布信息.md`, and `素材\`.
   - Update `50_输出成果\IP文章成品\IP文章时间轴.md`.

## Directory Convention

Desktop working directory:

```text
<workspace>\YYYY-MM-DD_slug\
```

Recommended files:

```text
article.md
article_wechat.html
publish_wechat_direct.py
draft_result.json
draft_error.json
images\cover.png
images\body_01.png
images\body_02.png
images\body_03.png
```

## Publishing Helper

Use `scripts\publish_wechat_direct.py` from this skill when md2wechat conversion or `test-draft` is unreliable.

Example:

```powershell
python scripts\publish_wechat_direct.py `
  --root C:\path\to\article_folder `
  --html article_wechat.html `
  --cover images\cover.png `
  --inline images\kpt_formula.png `
  --title "别迷信天赋，成功靠知识和实践" `
  --author "Author Name" `
  --digest "MIT教授Patrick Winston的一个公式，让我重新理解创业：别迷信天赋，先积累知识，再走进真实世界练习。"
```

The helper reads WeChat `appid` and `secret` from `~\.config\md2wechat\config.yaml`, uploads body images with `uploadimg`, uploads cover as permanent material, creates a draft via `/cgi-bin/draft/add`, and writes `draft_result.json` or `draft_error.json`.

## Final Response Checklist

- State whether the WeChat draft was created.
- If successful, include draft `media_id`.
- Include the final title.
- Mention the number of in-body images if the article was prepared for publishing.
- Link to local article and Obsidian archive paths.
- Mention any real blocker, especially IP whitelist errors.
