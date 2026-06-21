---
type: research
status: completed
updated_at: 2026-06-21
gate: weak
---

# 研究

## 要回答的问题

- 推荐插件是否真的都已经安装？
- 当前线程能不能实际调用这些插件提供的能力？
- 哪些插件能立刻改善 SignalProof 的调研、验证、产物、反馈和资产化流程？
- 哪些插件只是“看起来有用”，但当前缺少账号授权、工具暴露或真实数据源？

## 已确认事实

- `codex plugin list` 当前显示 178 个 marketplace 插件，其中 36 个已安装启用、142 个未安装。
- `docs/codex-plugin-audit.md` 的 A 级推荐条目为 40 个，其中 36 个是 marketplace 插件，4 个是 primary-runtime 插件。
- Codex 官方手册说明：插件可包含 Skills、Apps 和 MCP servers；安装后通常需要开启新线程并在需要时连接外部 app。
- 重启后新线程探针 `019ee803-b71e-7b01-a7b6-1608b91e9916` 确认 A 级推荐 marketplace 插件无缺失，更多 Skills 可见，但 app connector 专用工具仍未通过 tool_search 暴露。
- App connector 类插件如 Readwise、Scite、Semrush、Similarweb、Brand24、Amplitude、Mixpanel、Datadog、Dovetail、Mem 在当前线程没有直接暴露可调用工具。
- `SENTRY_AUTH_TOKEN`、`POSTHOG_API_KEY`、`MIXPANEL_TOKEN`、`AMPLITUDE_API_KEY`、`DATADOG_API_KEY`、`SEMRUSH_API_KEY` 当前均未配置。
- 补跑 case 1 已实际运行 `last30days`，得到 GitHub/Reddit/YouTube 共 13 条证据，同时暴露 X 额度、YouTube 评论、HN 缺失等来源缺口。
- 补跑 case 3 已实际生成 DOCX、PDF、PPTX、HyperFrames HTML 等产物，证明产物类插件不再只是候选。

## 实际试跑结果

| 能力 | 试跑方式 | 结果 | 证据文件 | 结论 |
| --- | --- | --- | --- | --- |
| GitHub | `gh repo view sunny-kobe/SignalProof`、`gh issue list` | 成功读取公开仓库；issues 为空数组 | `evidence/github-repo-view.json`、`evidence/github-issues.json` | 默认纳入开源信号、发布和反馈阶段 |
| Hugging Face | Dataset Viewer API、model API | 公开 API 成功；`hf` CLI 不存在 | `evidence/hf-dataset-valid.json`、`evidence/hf-dataset-splits.json`、`evidence/hf-model-openai-gpt-oss-20b.json` | 模型/数据集信号有用；CLI 需另装 |
| Zotero | 本地 helper `status --json` | `127.0.0.1:23119` refused，Zotero 未运行 | `evidence/zotero-status.json` | 有 Zotero 资料库时条件启用 |
| Record & Replay | `event_stream_status` | 成功返回 `isRecording=false`，最大录制 1800 秒 | 工具输出记录在过程日志 | 强烈建议保留，用于把用户演示转 Skill |
| Computer Use | `list_apps`、`get_app_state(Codex)` | `list_apps` 成功；`get_app_state(Codex)` 返回 macOS 错误 `-1743` | 工具输出记录在过程日志 | 入口可响应，但具体 App 读取需先确认权限 |
| Browser | Browser 插件 setup | 失败：`codex/sandbox-state-meta: missing field sandboxPolicy` | 工具输出记录在过程日志 | 当前不可作为默认验收依赖 |
| Spreadsheets | 生成 XLSX、PNG preview、inspect | 成功 | `vault/assets/plugin-test/workbook/outputs/` | 高价值，适合工具账本和反馈台账 |
| Data Visualization | 生成 HTML 汇总页 | 成功生成文件；Browser 验收失败 | `vault/assets/plugin-test/visual/plugin-eval-summary.html` | 高价值，但浏览器验收链路待修 |
| last30days | 查询 `AI coding repo context loss` 最近 30 天讨论 | 成功，13 条证据，3 类来源；X/HN/YouTube 评论有缺口 | `vault/cases/2026-06-21-插件试跑-case-1-ai-coding-repo-context-loss-调研验证/evidence/ai-coding-repo-context-loss-raw-plugintrial.md` | 调研初筛明显增强，但必须带来源质量门 |
| Documents | 生成 DOCX 简报 | 成功，结构检查标题、段落、表格通过 | `vault/assets/plugin-test/document/outputs/plugin-eval-brief.docx` | 适合正式文档交付件，按场景启用 |
| PDF | 生成 PDF 并抽取文本 | 成功；缺 `pdftoppm/pdfinfo`，未做图片渲染 | `vault/assets/plugin-test/pdf/outputs/plugin-eval-brief.pdf` | 适合正式报告，正式交付前补渲染依赖 |
| Presentations | 生成 PPTX、slide PNG、montage、inspect | 成功 | `vault/assets/plugin-test/presentation/outputs/plugin-eval-deck.pptx` | 分享/复盘场景强增益 |
| HyperFrames | 生成 HTML composition 并 lint | `ok=true`，0 error，2 warning；缺 `ffmpeg` 未导出 mp4 | `vault/assets/plugin-test/hyperframes/index.html`、`outputs-lint.json` | 适合传播素材，视频导出需补依赖 |
| 新线程插件暴露探针 | `codex_app.create_thread` + `tool_search` | 推荐插件无缺失；更多 Skills 可见；app connector 工具仍未暴露 | `evidence/restart-thread-plugin-deepcheck-receipt.md`、`tool-ledger.md`、`process-log.md` | 账号类插件继续保持条件启用 |

## 证据强度

- 强：插件安装状态、GitHub 只读读取、Record & Replay 状态、Spreadsheets 产物生成、Presentations 多格式导出。
- 中：Hugging Face 公开 API、Data Visualization HTML 文件、last30days 调研初筛、Documents/PDF/HyperFrames 产物、官方手册插件口径。
- 弱或阻塞：Browser 当前调用失败；Computer Use 入口可响应但具体目标读取可能失败；App connector 类调研/反馈插件当前缺少授权或工具入口。

## 当前判断

推荐插件已经安装到位，但“全部默认使用”不成立。当前应该进入三层策略：

- 默认用：GitHub、Record & Replay、Spreadsheets、Data Visualization、OpenAI Docs、SignalProof 本地 skill；真实趋势 case 默认候选 `last30days`。
- 条件用：Hugging Face、Zotero、Documents、PDF、Presentations、HyperFrames、Sentry、PostHog、Semrush、Similarweb、Brand24、Readwise、Scite、Dovetail、Mem、Notion、Google Drive、Airtable。
- 暂不默认：Browser；Computer Use 只作为条件候选，直到目标 App 权限和读取路径确认。
