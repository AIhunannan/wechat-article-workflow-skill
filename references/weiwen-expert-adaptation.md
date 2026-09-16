# 微文专家能力适配记录

## 当前基线

- 适配日期：2026-09-16。
- 微文代码基线：`aiwei-ai/wechat-writer` commit `8d1c776`（`feat: add editorial visual direction gate`）。
- 原生专家入口：本机 WorkBuddy `wechat-official-account-expert/1.0.2`，微文运行标识 `workbuddy-native-v1`。
- 活动技能入口：`C:\Users\cughn\.codex\skills\nannan-wechat-article\SKILL.md`。
- 本轮 WorkBuddy 方法来源：`C:\Users\cughn\Documents\AgentCore\snapshots\weiwen-experts-20260909-01\sources\wechat-official-account-expert\`。
- 2026-09-16 合并前回滚快照位于 `C:\Users\cughn\Documents\AgentCore\skill-archives\nannan-wechat-article\before-consolidation-20260916-144822\`。

## 已核对的来源指纹

- 微文工作流入口：SHA256 `9B45D77FD18FF2E62C90848FF11DAE204E633186088330033DD888BF5EF33A27`。
- 原生适配规则：SHA256 `8C1E217F7EABEEC1382B2C97A78F6884AB52F2E179A8816AC44D1CFC0023B742`。
- 原生专家角色：SHA256 `C8DAB8C2178BFCD10231F008A7BEBC2E7C3E3801423A3F381260BD9705ED94E3`。
- 微文创作执行规则：SHA256 `6CCEBC0FC2FB31FA64C44417D86F90DABD631825720DAF1316D9FB09D3722FED`。
- 视觉方向门禁：SHA256 `EB8AF4023C3714DFCF68E302A11BE2A1543BBA1F15967E792FDE8C0F720F72CE`。

原生包内有少数组件级 LICENSE，但未发现覆盖本次参考的完整专家包、允许整包公开再分发的统一许可。本技能迁移的是用户已拥有环境中的工作方法和本地产品门禁，不复制供应商脚本或整包源码；对外 Git 仓库不宣称获得第三方品牌或代码授权。

## 迁移的能力

- 原生专家的读者价值、内容支柱、标题 8 选 1、移动阅读与关系运营方法。
- 原生专家的选题大纲、文风 DNA、正文合规检查和 humanizer 方法；标题情绪和对比改为可选，避免为了点击牺牲可信度。
- 微文的正文检查点、当前版本事实审查、旧审查失效、固定模板/局部修改/样式事实隔离。
- 微文的图片优先级、系列一致性、概念图标识与图片核对。
- 微文 `plan_visual_direction -> preview_layout -> submit` 思路及确定性视觉门禁。
- 长文按产品故事、架构解释、实操教程、案例叙事和个人思考选择编辑模式与视觉语法；三卡图文不再作为长文前置模板。
- 微文运营面板的分母纪律、审稿覆盖、积压、失败、耗时、成本计量与缺失数据边界。

## 保留的个人能力与边界

- 胡楠楠的定位、固定结尾、端侧 AI/AI 硬件/Agent 优先级、40 分选题门禁和 Obsidian 归档。
- 公众号草稿与正式发布分离；外部操作逐级授权。
- 微文服务器工具名只表示等价能力，不假设个人技能运行时一定存在同名工具。
- 原生专家的行业指标、发布频率、营销承诺和自动发布能力不作为本账号事实或权限。

## 升级流程

再次升级前：读取 AgentCore `core/CORE.md`，创建并校验新快照；记录旧/新 SHA256；确认来源版本、许可、运行加载路径、输出契约和发布边界；在代表任务上验证标题、正文事实、三卡图文、长文视觉、草稿状态与运营复盘后再同步 Git。
