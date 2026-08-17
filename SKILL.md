---
name: wechat-article-workflow
description: Use when researching, creating, polishing, illustrating, formatting, publishing, growing, or archiving personal-brand WeChat content. Covers practical AI topic radar, originality review, graphic-first distribution, humanized writing, md2wechat checks, WeChat draft upload, cross-platform derivatives, growth review, and knowledge-base archive.
---

# WeChat Article Workflow

This skill is for personal-brand WeChat articles. Default to editing the author's own reflections, not generic ghostwriting.

## Voice Rules

- Start from the user's notes and preserve their personal judgment.
- Do not impose a fixed word or character limit. Let the subject, evidence, and argument determine the necessary length.
- Prefer plain, sharp, reflective writing over polished marketing language.
- Avoid AI-heavy patterns: formulaic openings, over-explaining, slogan endings, excessive lists, and generic inspirational tone.
- Use a local `humanizer-zh` skill when available and apply its rules.

## Practical AI Tool Daily Mode

Use this mode for growth-oriented content about AI tools, agents, Skills, websites, workflows, products, hardware, and open-source projects.

- Prefer projects that are new, useful, high-growth, or gaining credible momentum on X, GitHub, Kickstarter, TikTok, YouTube, or product communities.
- Verify the original repository or product page, documentation, installation path, recent activity, limitations, permissions, cost, delivery status, and security before writing.
- Do not behave like a news-repost account. Install, inspect, or run the core workflow when feasible, and separate verified results from project claims.
- Keep titles simple and direct. Use numbers, stars, growth, pricing, shipment, performance, or outcomes only when the body contains dated evidence.
- Use pain point, scenario, solution, value, real example or test, and editorial judgment as a reasoning checklist, not a rigid heading template.
- Give readers something they can use immediately: a safe command, prompt, checklist, workflow, buying rule, comparison, or decision framework.
- Do not promise investment returns or guaranteed income. For money-related tools, focus on research quality, business efficiency, and decision discipline.
- Do not default to a group-join CTA. Use one configured article closing at most, and keep platform endings native.

## Graphic-First Distribution Mode

When the goal is reach, saves, shares, or follower growth, treat the image post as the primary artifact instead of adding decorative images after a long article.

- Default content mix: roughly `70%` image-first posts, `20%` short-video derivatives, and `10%` deep articles. Adjust from real platform data.
- A graphic post normally contains `5-8` cards. Each card has one idea, short copy, and a visual task that directly supports the claim.
- Recommended card sequence: concrete hook, reader pain, tool/project or scene, how it works, evidence or limitation, operator judgment, and same-day action.
- Put a real screenshot, hardware photo, command/output, pricing detail, workflow result, or customer scenario on at least one evidence-bearing card. Never fill a carousel with generic AI imagery.
- Generate at least three title and cover directions, then choose the one whose promise is fully repaid by the cards.
- For WeChat image posts, use `md2wechat create_image_post` or `newspic` when available. For Xiaohongshu, use a `3:4` or `4:5` layout and publish through an authorized connector only.
- A long article is the depth layer. Do not expand a thin tool announcement into a long article merely to increase word count.

### Graphic Post Template

Use `templates/graphic_post.md` for image-first work. It keeps the title, cover direction, card copy, evidence, platform captions, and preflight checks in one reviewable artifact.

## Originality and Information-Density Gate

This gate is mandatory before formatting or draft upload. The goal is genuine information gain and identifiable authorship, not detector evasion.

### Authorship Rules

- The author's notes, experience, experiment, customer scene, or original judgment must supply the thesis. AI may research, challenge, structure, compress, polish, and verify, but must not invent lived experience.
- X posts, news, README files, videos, and other articles are discovery inputs, not publishable copy. Do not translate, paraphrase, reorder, or stitch them into an article.
- Never claim `I tested`, `our customer said`, `we deployed`, or a performance result without first-party evidence. If execution was not possible, say that only public material was reviewed and state the limitation.
- Do not generate batches of near-identical articles from one template. Every piece needs a distinct question, evidence chain, and conclusion.
- Use platform AI-assisted-content disclosure when required. Never claim fully manual authorship when AI generated a substantial part of the text or visuals.

### Minimum Original Value

For a researched tool, product, or industry article, require all of the following:

- At least one first-party contribution: installation result, command output, original screenshot, comparison, calculation, customer scenario, product decision, or technical experiment.
- At least two primary sources when available: repository, official documentation, paper, release, filing, product page, full interview, or maintainer statement.
- At least one non-obvious author judgment that explains the mechanism, boundary, or business meaning rather than repeating features.
- At least one useful artifact that the reader can apply immediately.
- A concise source note for researched facts and third-party visuals.

For a personal reflection, require a concrete first-person scene, a specific detail, the resulting judgment, and a connection to current work. Generic motivational expansion does not count.

### Information-Density Test

- Every roughly `250-300` Chinese characters should deliver a new fact, example, mechanism, comparison, instruction, result, limitation, or decision.
- Use the proof chain `fact -> interpretation -> reader consequence`.
- Before approval, list at least five distinct information units learned by the reader. Reworded versions of one conclusion count once.
- Remove generic openings, broad AI background, empty transitions, ceremonial conclusions, repeated slogans, and copied feature lists.

### Identifiable-Author Test

Ask: `If the author's name were removed, what could not be written by a generic AI account?`

Require at least two defensible answers, such as a real experiment, customer observation, engineering judgment, founder decision, original framework, or candid limitation. If there are fewer than two, collect more material or change the topic.

Copy `assets/originality_audit.md` into the content folder, complete it, and mark the work `PASS` before formatting. A failed piece stays in research and must not be padded into publishable length.

## AI Project Topic Radar

Use a multi-source radar before selecting practical AI topics. The purpose is not to collect hot links, but to choose a project that gives the reader a concrete result.

1. Use a recent-trend researcher such as `last30days` for a rolling `30-day` scan across X, GitHub, YouTube, Hacker News, Reddit, and the open web. For named projects, run its planning or preflight flow first and preserve the scan date.
2. Use an AI product radar such as `ai-product-radar-skill` to shortlist products from Kickstarter, TikTok, GitHub, YouTube, X, Amazon, and public product pages. Its default daily window is `24 hours`; expand to `7-30 days` if the signal is thin.
3. Use a multi-backend research tool such as `agent-reach` to fill gaps. Run its doctor/preflight command before multi-backend research, route each question to the proper web, social, GitHub, or video connector, and combine X momentum with repository or first-party evidence and local-language context.

### Source Roles

- `X`: launch momentum, demos, founder claims, user pain, and early reaction. Use it for discovery and sentiment, not proof by itself.
- `GitHub`: stars and velocity, releases, commits, issues, license, install friction, and whether the project is active.
- Chinese-language public sources: local scenarios, pricing, distribution, user questions, and whether a project fits Chinese users and companies.
- Kickstarter, TikTok, Amazon, and YouTube: purchase intent, viral product behavior, physical product quality, demonstrations, delivery signals, and the gap between marketing and experience. A viral clip is discovery evidence, not proof of sales or delivery.
- First-party documentation, repositories, release notes, product pages, and maintainer posts outrank commentary. Distinguish fact, inference, and editorial judgment.

### Priority Topics

Prefer concrete projects in these areas:

1. Practical Skills, agents, and high-growth open-source projects that can produce a same-day outcome and have a reproducible path.
2. AI hardware and edge AI: validated Kickstarter or TikTok products, local inference, chips, voice devices, wearables, cameras, developer boards, robots, and AI toys.
3. AI income, productivity, and business workflows: research, lead generation, content, sales, automation, service delivery, and decision support. Teach a reproducible workflow; never promise guaranteed income.
4. AI companions and emotional value: voice agents, memory, emotional computing, companion devices, and elder, child, or pet scenarios.
5. Real customer cases and original judgment: deployment lessons, product trade-offs, cost decisions, failures, and practical conclusions.

Useful discovery keywords include `AI hardware`, `edge AI`, `AI companion`, `voice agent`, `robotics`, `AI toy`, `emotional AI`, `Skill`, `agent`, `AI automation`, `AI productivity`, and `AI income`, combined with `GitHub`, `X`, `Kickstarter`, `TikTok`, `deployment`, `benchmark`, `shipping`, or a concrete user scenario.

### Radar Score and Evidence Gate

Score each candidate from `0-5` on reader pain, immediate usefulness, evidence and reproducibility, freshness, audience fit, save/share potential, differentiated judgment, and first-party evidence. Add a separate concrete-value check:

- Can a reader reproduce, buy, deploy, or use it within a day?
- Is there a public evidence card with URL, platform, scan time, metric and date, update date, license, installation path, cost or permissions, and limitations?
- Is there a demo, screenshot, hardware photo, workflow output, or customer scenario?
- What can the author add that a README or news rewrite cannot?

Normally publish only when the total is at least `28/40`, first-party evidence is at least `3/5`, and concrete value is at least `3/5`. Reject high heat without a usable outcome, high stars without recent activity, and any number that cannot be verified. Each daily scan should output exactly one recommended topic and two backups; if fewer than three qualify, report fewer rather than filling the list with weak topics.

### Choose the Content Shape

- `Graphic post`: default for one tool, Skill, project, hardware product, or sharp method that can be understood and saved quickly.
- `Short video`: use when a demo, before/after, screen recording, voice interaction, or physical behavior is the proof. Keep one promise and one scene within `30-60` seconds.
- `Long article`: use for multi-source synthesis, customer cases, architecture trade-offs, or original worldview. Do not stretch a weak topic into a long article.
- `Multi-format`: when evidence and reader value are both high, publish the graphic first and derive the video and article within `72` hours while preserving the same facts and caveats.

The daily decision must answer: why this topic now, what the reader can do today, and what original judgment the author adds.

## Configurable Audience-Growth System

Set a measurable follower goal and deadline in the project configuration. Calculate the operating target as `(goal - current followers) / remaining months`, then replace assumptions with actual channel data. A target is an operating guide, never a guarantee.

### North Star

- Optimize first for `net new followers per post`, then shares per 100 readers, completion, saves or `在看`, search traffic, and total reads.
- Do not mistake high reads for success when a post attracts no relevant followers.
- Build trust by repeatedly helping readers solve real problems. Never use forced follows, incentivized sharing, fake scarcity, or unsupported income claims.

### Default Content Portfolio

Use this starting mix and adjust from measured conversion:

- `50%` high-growth AI projects with hands-on verification.
- `25%` reusable workflows, Skills, prompts, and practical tutorials.
- `15%` edge AI, AI hardware, AI companions, and productization practice.
- `10%` real customer cases and original practitioner judgment.

Daily utility brings traffic; original judgment and real cases build a durable personal brand. Publish at least two deeper original or customer-case pieces each month, and ensure every tool article includes a clear practitioner judgment.

### Daily Topic Gate

Score three or more candidates from `0-5` on:

1. Reader pain intensity.
2. Immediate usefulness.
3. Evidence and reproducibility.
4. Freshness and discussion momentum.
5. Fit with the author's expertise and audience.
6. Share and save potential.
7. Differentiated personal judgment.
8. Available first-party evidence.

Normally reject a total below `28/40` or first-party evidence below `3/5`. A fast-growing small project may outrank an old high-star project when velocity, activity, utility, and audience fit are stronger.

Before writing, build an evidence card with source URLs, scan time, star or usage count, update date, license, installation method, permissions, dependencies, cost, delivery status, limitations, and security risks. Recheck volatile claims on publication day.

Lock one primary reader before writing. Reject topics that are hot but produce no useful outcome, rely only on promotional copy, or repeat the previous `30` days without a meaningful update.

### Title and First-Screen Conversion

- Generate `10` titles, shortlist `3`, and select `1` only after checking every number, name, speed, and result against evidence.
- Prefer simple titles that expose the project, proof, contrast, and reader outcome. Do not use `guaranteed profit`, `effortless income`, `crushes`, `revolutionary`, or similar claims without exceptional evidence.
- The first card or first `180` Chinese characters must answer: what is it, why now, what can the reader do today, and what is the author's conclusion?
- Put the strongest screenshot, real photo, output, parameter, or explanatory visual near the first screen. Do not begin with long history or generic AI trends.

### Practical Value Standard

Every practical piece should contain:

- One real pain point and one concrete user scenario.
- A verified solution path, not a feature list.
- A `3-minute start` block with the shortest safe usage path.
- A truthful test block with environment, observed result, failures, and limitations; omit it if no test was run.
- Who should use it and who should not.
- At least one reusable command, prompt, checklist, template, workflow, buying rule, or decision framework.
- The author's original judgment about technical boundary, product value, or commercial meaning.
- A source note distinguishing official facts, third-party claims, and first-party observations.

Treat these as reasoning requirements, not mandatory headings. The result should read like a practitioner sharing a discovery, not a generated manual.

### Search, Series, and Follow Conversion

- Select one primary WeChat search keyword and `2-4` secondary keywords. Use them naturally; never stuff keywords.
- Save `primary_keyword`, `secondary_keywords`, `source_urls`, `topic_type`, `project_metric_at_scan`, and `scan_time` in metadata.
- Link related pieces into a repeatable series so one successful post leads to the next useful post.
- Use at most one configured closing. Xiaohongshu captions must not copy WeChat-only language such as `在看` or `星标`.

### One Topic, Four Assets

After the graphic post is ready, prepare but do not automatically publish:

- A `60-second` short-video script derived from the strongest card.
- An `80-120` Chinese-character Moments post.
- One concise X post.
- Three alternative title and cover directions for later A/B learning.
- A long-form WeChat article only when the topic needs deeper reasoning or durable reference value.

Reuse the same verified evidence while adapting the hook and CTA to each platform. Do not auto-publish without explicit authorization.

### Growth Measurement Loop

Record the exact title, topic type, keyword, publication time, evidence snapshot, traffic sources, readers at `2h/24h/7d`, shares, saves or `在看`, new followers, unfollows, and net followers.

- Use `assets/growth_log.csv` as the field template and `assets/daily_topic_radar.csv` for scoring.
- Review weekly by net followers per post and shares per 100 readers, not only total reads.
- Extract one reusable pattern from the top `20%`: topic, title, first screen, evidence, image, or distribution source.
- Publish a useful adjacent follow-up within `72` hours when demand is clear; solve the next question instead of rewriting the same post.
- Diagnose the bottom `20%`: weak topic, weak title, title-body mismatch, insufficient proof, poor first screen, or wrong audience.
- After four weeks, establish channel-specific baselines from actual data. Do not invent thresholds before evidence exists.

## Length and Structure Rules

- Optimize for a clear theme and complete reasoning, not a target word count.
- State the central judgment early. Every section should add evidence, a case, an explanation, a counterpoint, or a useful conclusion.
- Remove repeated claims, empty transitions, generic background, and paragraphs that do not move the argument forward.
- Use a short article when the idea is simple. Allow a longer article when research, customer cases, technical explanation, or personal experience genuinely needs space.
- For longer articles, use clear section headings and natural transitions so readers can understand the argument even when scanning quickly.
- Prefer the shortest version that fully explains the idea, but never cut necessary reasoning merely to stay under an arbitrary limit.

## Title Rules

- Treat the title as a growth lever, not a label. A good title can matter more than a good paragraph.
- Before finalizing, generate 5-10 candidate titles and choose the one with the strongest curiosity gap, specificity, and forwarding impulse.
- Prefer titles with concrete hooks: numbers, extreme contrast, hidden origin stories, surprising causal claims, famous names, or high-stakes consequences.
- Use the author's historically strong titles as benchmarks, but copy the underlying mechanism rather than repeating their wording.
- Good title directions:
  - `X诞生前，先发生了一个没人重视的小故事`
  - `真正改变X的，不是Y，而是Z`
  - `为什么我越来越相信：X比融资更重要`
  - `一个被忽视的小实验，后来长成了X`
- Keep the final WeChat title within 32 Chinese characters when possible, but do not make it bland just to be short.
- Avoid flat summary titles such as `关于XX的思考`, `XX给我的启发`, `读XX有感`, unless the user explicitly wants a low-key diary tone.

## Standard Workflow

1. Clarify the article angle only if genuinely needed. Otherwise make a reasonable editorial judgment.
2. For growth-oriented content, run the topic radar. Output one recommendation and two backups, lock one primary reader, and save a dated evidence card.
3. Choose the distribution mode. When reach is the main goal, create `graphic_post.md` first; make long-form copy only when deeper reasoning is justified.
4. Lock one primary search keyword, `2-4` secondary keywords, the cover promise, and the first-screen evidence.
5. Write or polish `graphic_post.md` with `templates/graphic_post.md`. Keep the same evidence and adapt only the platform-specific opening and CTA.
6. Write or polish `article.md` when needed, with frontmatter:
   - `title`: final WeChat title, max 32 chars.
   - `author`: configured author name.
   - `digest`: max 128 chars.
   - `primary_keyword`: main WeChat search phrase when applicable.
   - `secondary_keywords`: `2-4` related phrases when applicable.
   - `source_urls`: primary evidence sources.
   - `scan_time`: verification time for volatile claims.
7. Generate `10` evidence-backed titles, shortlist `3`, and select `1`. If the user rejects the title, revise the cover/title before republishing.
8. Perform the first-screen, card-density, and long-form structure edit. Confirm that every swipe or major passage adds evidence, mechanism, instruction, limitation, or judgment.
9. Copy and complete `assets/originality_audit.md`. Require five information units, two identifiable-author elements, truthful first-party claims, source attribution, and a `PASS` decision.
10. Confirm practical value: a `3-minute start`, truthful test status, limitations, target-user guidance, and one reusable asset.
11. Generate or select visuals:
   - Prioritize proof images: original screenshots, command output, real product photos, data charts, comparison tables, and original diagrams.
   - Use generated visuals for the cover or explanation, not as a substitute for evidence.
   - Generated images are usually under `$CODEX_HOME/generated_images/...`; copy selected files into `images\` and leave originals in place.
   - A long article normally uses one strong `16:9` cover plus `2-4` precise body images. A graphic post normally uses `5-8` matching `3:4` or `4:5` cards.
   - Each image must have a job: prove authenticity, explain a concept, create emotional atmosphere, show a product/object, or summarize a key model. Do not add generic decoration.
   - When the user provides real photos, prefer them for authenticity and place them early if they strengthen trust.
   - For AI-generated images, make prompts specific to the paragraph: people, objects, scene, metaphor, mood, color palette, and explicit `no text, no logos` constraints.
   - Avoid cheap futuristic imagery, random robots, generic business icons, and images that only loosely match the paragraph.
   - If the user expects every generated image to appear in the article body, embed the cover as the first body image too; WeChat cover material alone does not display inside article content.
12. Append the configured article closing exactly once when one exists. Do not add a second profile or CTA after it.
13. Build WeChat-safe HTML or image-post assets:
   - Use inline styles only.
   - Avoid relying on `<style>` tags for final WeChat body.
   - Keep the official WeChat title out of the body H1 to avoid duplicate title risk.
14. Run `md2wechat inspect` for long articles, or inspect the image-post payload and card count for graphic posts:
   - Confirm title, author, digest, image order, upload readiness, and draft readiness.
   - If md2wechat API theme conversion fails, use the local inline HTML path and direct WeChat draft script.
15. Publish only after authorization:
   - Use `md2wechat create_image_post` or `newspic` for a WeChat image post when available. Do not force it through the long-article conversion path.
   - Prefer a direct draft script that explicitly sets title, author, digest, content, and cover media id.
   - Never use a flow that may create a default title such as "AI测试文章".
   - If WeChat returns `40164 invalid ip ... not in whitelist`, report the exact IP shown by WeChat. This IP can differ from generic public-IP lookup services, so trust the WeChat error.
   - Publish Xiaohongshu or other channels only through an authorized connector and only after explicit approval.
16. Archive to the configured knowledge base:
   - Base path: the configured local knowledge-base root.
   - Article path: `50_输出成果\IP文章成品\YYYY\YYYY-MM\YYYY-MM-DD_文章标题\` when using the default Obsidian layout.
   - Save the source notes, evidence card, `graphic_post.md`, `article.md`, HTML, publication metadata, originality audit, and visuals.
   - Update `50_输出成果\IP文章成品\IP文章时间轴.md`.
17. Prepare the four-channel derivative assets and save them beside the topic. Do not publish them without permission.
18. After publication data is available, append the growth log and run the weekly or monthly review.

## Directory Convention

Desktop working directory:

```text
<workspace>\YYYY-MM-DD_slug\
```

Recommended files:

```text
article.md
graphic_post.md
article_wechat.html
publish_wechat_direct.py
draft_result.json
draft_error.json
evidence_card.md
originality_audit.md
distribution_kit.md
growth_snapshot.csv
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
