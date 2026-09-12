# 公众号交付、发布与归档

## 固定结尾

每篇公众号长文末尾恰好追加以下两段。第一段加粗，第二段普通文字；除非用户明确改变，否则其后不再添加来源、CTA、口号或个人介绍。来源说明放在固定结尾之前。

**以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。**

作者：胡楠楠，aiwei.ai公司联合创始人、CTO&FDE，前华为、腾讯金牌架构师。持续分享最新AI工具、Agent、端侧AI和AI硬件实践，欢迎关注。

## 成稿文件

工作目录默认：

`C:\Users\cughn\Desktop\IP文章\YYYY-MM-DD_slug\`

按任务保存：

- `article.md`：标题、作者、摘要、关键词、来源、扫描时间和正文。
- `article_wechat.html`：最终微信安全 HTML。
- `evidence_card.md`：事实、来源、扫描时间、推断与待验证边界。
- `originality_audit.md`：作者贡献与信息密度审计。
- `graphic_post.md`、`distribution_kit.md`：需要时生成。
- `images\`：封面、正文图与来源记录。
- `draft_result.json` / `draft_error.json`：真实微信回执。
- `growth_snapshot.csv`：发布后数据。

不要为了齐全创建空文件。

## HTML 与检查

- 最终微信公众号正文使用微信可接受的内联样式；可在制作阶段用 class/style 组织，但交付前确认已安全转换。
- 标题、摘要不在正文 H1 重复；封面是否进入正文要明确。封面素材不会自动显示在文章内部。
- 图片、图注和正文使用当前版本检查点的文字；排版不能临时添加未经事实审查的新结论。
- 使用 `md2wechat inspect` 或当前已验证检查路径确认标题、作者、摘要、图片、重复 H1 和草稿条件。
- 主题转换失败时可使用本技能的本地内联 HTML 与 `scripts/publish_wechat_direct.py`，但不能跳过事实和视觉检查。

## 授权与状态机

- `本地成稿`：允许保存本地文件，不等于上传。
- `草稿就绪`：检查已通过，但没有调用微信接口。
- `已创建草稿`：只有 `draft/add` 成功并取得 `media_id`；最好再用 `draft/get` 回读确认。
- `已发布`：只有用户明确要求正式发布，且看到微信官方成功状态、内容 ID 或发布链接。

创建草稿、上传图片和正式发布是分开的外部动作。普通“写一篇、准备、同步文件”不授权微信操作；“发到草稿箱”授权草稿动作，不自动授权群发或正式发布。

如果微信返回 `40164 invalid ip ... not in whitelist`，记录微信错误中显示的 IP；它可能不同于普通公网 IP 查询结果。失败时保留 `draft_error.json`，不虚报草稿已创建。

## 草稿辅助脚本

需要直接创建草稿时，可在授权后使用：

```powershell
python C:\Users\cughn\.codex\skills\nannan-wechat-article\scripts\publish_wechat_direct.py `
  --root C:\path\to\article_folder `
  --html article_wechat.html `
  --cover images\cover.png `
  --inline images\body_01.png `
  --title "最终标题" `
  --author "胡楠楠" `
  --digest "文章摘要"
```

脚本从用户本机 md2wechat 配置读取凭据，不在文章目录、日志或 Git 中写入密钥。不要使用可能产生默认“AI测试文章”标题的测试发布路径。

## Obsidian 归档

现有知识底座：`C:\Users\cughn\Documents\Obsidian Vault`，不新建平行知识库。

归档路径：

`50_输出成果\IP文章成品\YYYY\YYYY-MM\YYYY-MM-DD_文章标题\`

保存原始感想、文章、微信 HTML、发布信息与素材，并更新 `50_输出成果\IP文章成品\IP文章时间轴.md`。归档默认复制，不移动或删除桌面原稿；保留来源、日期和发布状态。

## 交付回报

最终说明：最终标题、正文图片数、固定结尾是否恰好一次、本地文件、Obsidian 路径、草稿/发布状态、`media_id` 或平台证据、真实阻断项。未执行外部操作时明确写 `未上传、未创建草稿、未发布`。
