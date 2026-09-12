# nannan-wechat-article

胡楠楠的公众号内容与运营 Skill。它把选题、证据、写作、标题、视觉、三卡图文、公众号草稿、发布边界和增长复盘连成一套可追溯流程。

当前版本：`2026.09.12`

## 这次升级解决什么

- 接入微文 `workbuddy-native-v1` 的原生公众号专家方法。
- 新稿内部完成选题/大纲、正文、8 个标题候选和人性化润色，不把策划过程当成稿件。
- 先形成完整正文检查点，再做当前版本事实审查；正文改动后旧审查失效。
- 写 HTML 前锁定一个视觉方向，并在最终安全 HTML 上检查配色、对比、字号、行高和阅读节奏。
- 图文贴默认 3 张，信息确有独立价值时最多 5 张；旧七卡模板不再作为默认。
- 把公众号经营拆成内容支柱、4 周日历、欢迎语/关键词/菜单、系列索引、读者结果和生产健康。
- 每个比率保留分子、分母和观察窗口；缺失数据写“未知”，样本不足不宣布趋势。
- 保留胡楠楠的作者定位、固定结尾、端侧 AI/AI 硬件优先级、40 分雷达、草稿/发布双授权和 Obsidian 归档。

## 文件结构

```text
SKILL.md
references/
  editorial-production.md
  daily-ai-radar.md
  graphic-distribution.md
  growth-operations.md
  longform-editorial-standard.md
  publishing-archive.md
  weiwen-expert-adaptation.md
assets/
  daily_topic_radar.csv
  growth_log.csv
  originality_audit.md
templates/
  evidence_card.md
  graphic_post.md
scripts/
  publish_wechat_direct.py
```

`SKILL.md` 是路由入口。不同任务只读取所需参考文件，避免一次加载全部写作、雷达、分发和运营规则。

## 使用示例

```text
用 nannan-wechat-article 做今天的 AI 选题雷达，只给一个首选和合格备选。
```

```text
用 nannan-wechat-article 把这些素材写成公众号长文，完成事实检查、配图和微信排版，但不要上传。
```

```text
用 nannan-wechat-article 复盘近 30 天公众号数据，区分读者增长和内容生产健康。
```

## 安装

将仓库复制到 Codex Skills 目录，并保持文件夹名与 frontmatter 的 `name` 一致：

```powershell
Copy-Item -Recurse . C:\Users\<you>\.codex\skills\nannan-wechat-article
```

## 验证

```powershell
python -X utf8 C:\Users\<you>\.codex\skills\.system\skill-creator\scripts\quick_validate.py .
python -m py_compile scripts\publish_wechat_direct.py
```

还应检查：

- 所有 `SKILL.md` 路由链接可读取。
- 固定结尾只保存在发布参考中一次。
- 三卡模板没有残留的 Card 06/Card 07。
- 标题、事实审查、视觉方向、运营分母和草稿/发布边界均存在。
- 仓库没有真实 AppID、Secret、Token、客户资料、文章素材或托管记忆。

## 发布边界

本地成稿、草稿就绪、创建草稿和正式发布是四个不同状态。创建草稿需要明确授权；正式发布需要再次授权，并以微信官方回执、内容 ID 或链接为准。打开编辑器、上传图片或生成文件都不等于发布成功。

## 来源与许可说明

本版本参考用户本机微文代码基线 `aiwei-ai/wechat-writer@8d1c776` 和 WorkBuddy `wechat-official-account-expert/1.0.2` 的工作方法。原生包内有少数组件级 LICENSE，但未发现覆盖完整专家包、允许整包公开再分发的统一许可。因此本仓库只提交重新整理的工作流、个人配置和本地门禁，不包含供应商脚本或原生专家整包源码，也不宣称获得第三方品牌或代码授权。具体指纹见 `references/weiwen-expert-adaptation.md`。

## 安全

- 不提交公众号凭据、访问令牌、客户资料、未公开文章、图片素材或本机配置。
- 发布脚本只在用户明确要求创建草稿时使用，凭据留在用户本机配置中。
- 历史文章和样式样本只能提供表达规律，不能成为新文章事实。
- Git 同步不等于微信上传或发布。
