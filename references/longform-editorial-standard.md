# 公众号长文编辑与视觉标准

这份标准保留 2026-09-04 GenieX 返修中确认的深度边界，并吸收微文 2026-09-11 的视觉总编门禁：技术架构文章默认到职责、关系与产品后果，不自动深入源码；视觉先从本篇内容形成一个方向，再制作 HTML，不把历史文章样式或固定卡片墙套到所有主题。

## 历史参考不是固定模板

The immediately preceding long-form reference is:

`C:/Users/cughn/Desktop/IP文章/2026-09-03_microduck_edge_ai_signal/article_local_preview.html`

它可借鉴的部分是实物/场景图、具体开头、短段落、克制强调和清楚收尾。只有用户要求连续性时才继承相近的暖白与橙色；其它主题应重新判断深浅、字体、配色、图像媒介和节奏。不得复制旧文章事实、未经证实的说法、具体修辞或发布授权。路径不存在时，检查最近一篇相关且已被接受的本地文章。

## Architecture-depth writing

- Explain what each system is, what it owns, what it calls, what can be replaced, and how it changes a product scenario.
- Use necessary architecture terms, defined in plain Chinese on first use. Prefer components and data flow over function names, fields, version lists, source paths and instructions.
- Keep the named subject central. Related platforms clarify its place; do not turn the article into three unrelated product brochures.
- Preserve detail through causal explanation and tradeoffs, not abbreviations and table density.
- Use a real or clearly labeled illustrative scene to connect perception, understanding, decision, action and result.
- Do not force a “3-minute start” or “what I tested” block into an architecture explainer. Put reproducible commands and source inspection into a separate technical appendix when useful.
- Cite significant facts near their claims with a small unobtrusive reference; consolidate the full bibliography in a short source section before the hook/fixed ending. Repeated disclaimers and 20 inline document links can overwhelm the narrative.
- Distinguish current integration from architectural possibility in one clear relevant passage. Never imply formal partnership, shared ownership or turnkey compatibility merely by drawing adjacent boxes.

## 单一视觉方向

写 HTML 前先锁定并记录：一句编辑意图、深/浅主题、画布色、主文字色、弱文字色、强调色、标题字体逻辑、图片通栏/内收/混合节奏、直角/圆角倾向，以及首屏—中段—结尾的节奏。方向由读者、阅读目的和品牌气质决定，不向用户丢一组风格选项代替编辑判断。

- 年轻产品可以大胆利落；技术文章优先解释关系；人物故事让细节和时间推进。这些是判断示例，不是三套模板。
- 系统宋体/衬线可形成书页感，无衬线可强调清楚与力量；不用外链字体，必须有通用字体回退。
- 真实官方图片合适时优先使用。抽象软件需要生成场景时标明概念图，不虚构品牌产品和测试结果。
- 关系图通常一张足够，聚焦 3–5 个主组件，短标签、清楚箭头，不为显示专业塞入字段和后端名。
- 图片承担不同任务：首屏场景、硬件/产品证据、机制关系、情绪转场。不能用重复文字卡凑数量。
- 图文贴默认 3 张、最多 5 张；长文图片数量按内容决定，3 张有明确任务的图片通常已经足够。
- 保留原始比例或明确裁切，不切掉产品关键细节和来源，不在没有标注时改变真实产品。

## Typography and mobile acceptance

- WeChat body: inline styles, about 17px body text, line-height about 1.9, paragraphs separated by 14–18px. Use a reliable quoted Chinese/system sans-serif stack.
- Headings about 22–24px; restrained accent marker; no forced 01–08 manual-like numbering for every section.
- Do not turn every bold sentence into a box. Use a few emphasis panels where the reasoning benefits.
- Default to left-aligned text to avoid stretched Chinese/English spacing; inspect actual glyph rendering and font fallback rather than trusting the CSS string.
- Mobile at 390px: inspect the opening, a middle architecture passage, and the hook/author ending. Review diagram label readability at rendered size. Also inspect desktop width.
- Quality gate includes reader fit and visual judgment. No overflow, valid metadata and a correctly counted footer are necessary but insufficient.

## 最终排版门禁

- 在最终安全 HTML 上核对画布色、主文字色和强调色是否真正落实，不能只存在于生图提示词或源 CSS。
- 主文字、摘要和图注与背景对比度至少 `4.5:1`；长文主文字尽量接近 `7:1`。
- 80 字以上正文段落不低于 `15px`，行高不低于 `1.65`；更常用的是 `16–17px` 与 `1.8–1.9`。
- 连续 5 个纯正文段或约 760 字符没有图片、引语或章节转场时，检查节奏是否单一；不因此机械插图。
- 长文至少呈现三种有内容作用的节奏元素，例如章节、图片、引语、清单/表格或重点模块。一个元素没有必要就不添加。
- 阻断问题必须修复；非阻断审美建议最多做一轮有实质变化的整页修正。HTML 检查不是微信客户端截图验收，未做实机检查时要说明边界。

## Revision report

When asked whether this skill caused a poor article, distinguish a rule conflict, a missing standard and execution mistakes. Back up before making a targeted skill correction. Deliver the regenerated article, describe concrete improvements briefly, and state publication status. Preserve prior versions for comparison.
