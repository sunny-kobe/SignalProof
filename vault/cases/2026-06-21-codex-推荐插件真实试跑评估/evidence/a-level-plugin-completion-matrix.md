---
type: evidence
status: completed
updated_at: 2026-06-21
gate: passed-with-blockers
---

# A 级推荐插件逐项完成审计矩阵

## 口径

本矩阵按 `docs/codex-plugin-audit.md` 中去重后的 A 级推荐能力逐项核对。总数为 40 个：36 个 marketplace 插件，加 4 个 primary-runtime 能力。

完成状态分为：

- `called`：本轮已真实调用或生成可检查产物。
- `failed/tool`：已真实调用，但当前工具或环境失败。
- `failed/local-app`：已真实调用，但依赖本地 App 或服务未运行。
- `blocked/auth`：已确认工具路径，但缺少账号、API key 或真实数据源。
- `blocked/auth-or-tool`：已安装，但当前线程未暴露 app connector 工具，或还未完成账号授权。
- `condition-only`：已安装，但本轮没有安全的真实目标或没有必要触发外部副作用，不应默认使用。

## 总览

| 状态 | 数量 | 说明 |
| --- | ---: | --- |
| `called` | 11 | 已产生命令输出、工具输出或文件产物。 |
| `failed/tool` | 1 | Browser 当前环境失败。 |
| `failed/local-app` | 1 | Zotero Desktop 本地 API 未运行。 |
| `blocked/auth` | 4 | Sentry、PostHog、Amplitude、Datadog 缺账号/API/项目数据。 |
| `blocked/auth-or-tool` | 15 | app connector 类插件当前线程未暴露专用工具或未授权。 |
| `condition-only` | 8 | Computer Use、部署、设计稿、安全扫描或 Chrome 登录态目标需要按 case 条件触发，不应强行触发。 |

## 逐项矩阵

| A 级能力 | 形态 | 本轮状态 | 证据 | 判断 |
| --- | --- | --- | --- | --- |
| `documents` | primary-runtime | `called` | `vault/assets/plugin-test/document/outputs/plugin-eval-brief.docx` | 适合正式文档交付；缺 LibreOffice 时只能做结构级检查。 |
| `pdf` | primary-runtime | `called` | `vault/assets/plugin-test/pdf/outputs/plugin-eval-brief.pdf`、`plugin-eval-brief.text.txt` | 适合报告归档；缺 Poppler 时不能做页面截图级验收。 |
| `spreadsheets` | primary-runtime | `called` | `vault/assets/plugin-test/workbook/outputs/plugin-eval-workbook.xlsx`、预览 PNG、inspect | 强增益，建议默认用于证据矩阵和反馈台账。 |
| `presentations` | primary-runtime | `called` | `vault/assets/plugin-test/presentation/outputs/plugin-eval-deck.pptx`、slide PNG、montage | 强增益，适合复盘、演示和分享。 |
| `build-web-data-visualization` | skill | `called` | `vault/assets/plugin-test/visual/plugin-eval-summary.html` | 能把插件评估转成可读图表资产；Browser 验收待修。 |
| `hyperframes` | skill | `called` | `vault/assets/plugin-test/hyperframes/index.html`、`outputs-lint.json` | 适合视频化表达；缺 `ffmpeg` 时不能导出 mp4。 |
| `superpowers` | skill | `called` | 读取 `verification-before-completion` 技能并按其要求完成矩阵一致性检查、`check-all`、`git diff --check` | 对“完成前必须有证据”的流程质量有实际提升，但不需要每个 case 都全量套用。 |
| `record-and-replay` | skill+mcp | `called` | `process-log.md` 迭代 4；`event_stream_status` 返回 `isRecording=false`、`maxDurationSeconds=1800` | 强增益，建议默认作为“用户演示 -> Skill”资产化入口；不在用户未准备时强行录制。 |
| `browser` | skill | `failed/tool` | `process-log.md` 迭代 4；错误 `codex/sandbox-state-meta: missing field sandboxPolicy` | 高价值但当前失败，不能作为硬性验收 gate。 |
| `readwise` | app-only | `blocked/auth-or-tool` | `evidence/plugin-app-only-blockers.md` | 有个人阅读库时很有价值；当前未暴露 connector 工具，不能算实际读取。 |
| `scite` | app-only | `blocked/auth-or-tool` | `evidence/plugin-app-only-blockers.md` | 适合论文反证；当前未暴露 connector 工具。 |
| `zotero` | skill | `failed/local-app` | `evidence/zotero-status.json` | 本地 API 拒绝连接；需先运行 Zotero Desktop。 |
| `amplitude` | app-only | `blocked/auth` | `process-log.md` 迭代 6；环境变量缺失 | 有真实产品事件后才有强反馈价值。 |
| `deepnote` | skill+app | `blocked/auth-or-tool` | Deepnote skill 明确要求使用 app tools；tool_search 未暴露 `get_me`、`list_projects`、`get_notebook` 等工具 | 适合数据分析 notebook；当前不能假装已 inspected hosted Deepnote state。 |
| `mixpanel` | app-only | `blocked/auth-or-tool` | `evidence/plugin-app-only-blockers.md` | 有 Mixpanel 项目后可验证漏斗；当前无工具入口和授权。 |
| `posthog` | skill+app | `blocked/auth` | `process-log.md` 迭代 6；当前无项目数据源 | 真实产品反馈阶段很有价值；没有埋点数据时不启用。 |
| `similarweb` | app-only | `blocked/auth-or-tool` | `evidence/plugin-app-only-blockers.md` | 适合竞品流量侧证；当前未暴露 connector 工具。 |
| `airtable` | skill+app | `blocked/auth-or-tool` | `tool-ledger.md` 第二轮新线程暴露探针 | 适合反馈台账外部化；当前未读取真实 Airtable 数据。 |
| `box` | skill+app | `blocked/auth-or-tool` | `tool-ledger.md` 第二轮新线程暴露探针 | 适合私有文档库；当前未授权、未读取外部资料。 |
| `brand24` | app-only | `blocked/auth-or-tool` | `evidence/plugin-app-only-blockers.md` | 适合品牌/关键词监听；当前未暴露 connector 工具。 |
| `chrome` | skill | `condition-only` | `evidence/plugin-manifest-capabilities.csv`、Chrome skill 说明 | 只在需要用户现有 Chrome 登录态时启用；本轮不应无目标读取用户浏览状态。 |
| `computer-use` | skill+mcp | `condition-only` | 重启后深测 `list_apps` 成功；`process-log.md` 迭代 4 记录 `get_app_state(Codex)` macOS 错误 `-1743` | 入口可响应，但具体 App 读取要先确认权限和目标，不作为默认 GUI 验收 gate。 |
| `dovetail` | app-only | `blocked/auth-or-tool` | `evidence/plugin-app-only-blockers.md` | 有访谈库时价值高；当前未暴露 connector 工具。 |
| `google-drive` | skill+app | `blocked/auth-or-tool` | `tool-ledger.md` 第二轮新线程暴露探针 | 适合外部资料库；当前未授权、未读取外部资料。 |
| `jam` | app-only | `blocked/auth-or-tool` | `evidence/plugin-app-only-blockers.md` | 适合问题录制；当前无工具入口，也无具体录制目标。 |
| `linear` | skill+app | `blocked/auth-or-tool` | `tool-ledger.md` 第二轮新线程暴露探针 | 适合任务闭环；当前未读取 Linear workspace。 |
| `mem` | app-only | `blocked/auth-or-tool` | `evidence/plugin-app-only-blockers.md` | 有个人知识库时可补历史上下文；当前未暴露 connector 工具。 |
| `notion` | skill+app | `blocked/auth-or-tool` | `tool-ledger.md` 第二轮新线程暴露探针 | 可做资料同步；SignalProof 主战场仍应保留本地 vault。 |
| `semrush` | app-only | `blocked/auth-or-tool` | `evidence/plugin-app-only-blockers.md` | 适合 SEO/关键词专项；当前未暴露 connector 工具。 |
| `cloudflare` | skill+mcp | `condition-only` | `evidence/plugin-manifest-capabilities.csv` | 有部署/Workers/域名目标时启用；本轮不应强行部署。 |
| `datadog` | app-only | `blocked/auth` | `process-log.md` 迭代 6；环境变量缺失 | 有线上日志/指标后再启用。 |
| `github` | skill+app | `called` | `evidence/github-repo-view.json`、`evidence/github-issues.json` | 强增益，建议默认用于开源信号、发布入口和 issue 反馈检查。 |
| `hugging-face` | skill+app | `called` | `evidence/hf-model-openai-gpt-oss-20b.json`、Dataset Viewer 证据 | 适合 AI 模型/数据集初筛；公开 API 可用。 |
| `netlify` | skill+app | `condition-only` | `evidence/plugin-manifest-capabilities.csv` | 有公开报告页或站点发布目标时启用；本轮未部署。 |
| `openai-developers` | skill+app+mcp | `called` | `process-log.md` 迭代 3；Codex manual 刷新成功 | 对 Codex 插件和官方口径有强增益；优先用于 OpenAI/Codex 自身事实核对。 |
| `sentry` | skill | `blocked/auth` | `process-log.md` 迭代 6；helper 可运行但 `SENTRY_AUTH_TOKEN` 缺失 | 有线上错误数据后再启用。 |
| `vercel` | skill+app | `condition-only` | `evidence/plugin-manifest-capabilities.csv` | 有公开演示应用时启用；本轮未部署。 |
| `canva` | skill+app | `condition-only` | `tool-ledger.md` 第二轮新线程暴露探针 | 适合内容卡片/封面；本轮没有设计产物目标。 |
| `figma` | skill+app | `condition-only` | `tool-ledger.md` 第二轮新线程暴露探针 | 适合设计稿读取/视觉验证；本轮没有设计稿目标。 |
| `codex-security` | skill | `condition-only` | `evidence/plugin-manifest-capabilities.csv`、插件 manifest | 适合代码发布前安全扫描；本轮是流程/资产审计，没有安全扫描范围。 |

## 完成判断

本轮已经完成：

- 36 个 marketplace A 级推荐插件全部安装启用。
- 4 个 primary-runtime 能力全部可用并至少生成过一个文件级产物。
- 能在当前线程安全调用的能力均已调用、生成证据或完成无副作用技能探针。
- 不能调用的 app connector 插件均明确记录为 `blocked/auth-or-tool` 或 `blocked/auth`。
- 不适合当前 case 强行触发的部署、设计、Chrome 登录态和安全扫描插件均标为 `condition-only`，不写成真实调用。

本轮没有完成，也不应该伪造成完成：

- 未授权第三方 app connector 的真实数据读取。
- Browser/Computer Use 的页面级或 GUI 级验收。
- Vercel/Netlify/Cloudflare 的外部部署。
- Canva/Figma/Jam 的外部设计或录制产物。

因此，结论是：推荐插件已完成安装和当前环境下的实际试跑覆盖；真实外部账号类能力需要单独授权 case，不能计入本轮“已验证有效”。
