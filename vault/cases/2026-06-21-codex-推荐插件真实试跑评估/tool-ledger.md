---
type: tool_ledger
status: completed
updated_at: 2026-06-21
gate: passed
---

# 工具账本

## 口径

本账本区分四件事：

- 已安装：`codex plugin list` 显示 `installed, enabled`。
- 已授权：外部 app connector 或 API key 可用。
- 当前线程可见：本线程实际暴露了对应工具或 Skill。
- 已实际调用：本 case 中有命令、工具输出或文件证据。

安装成功不等于已实际调用；未授权或当前线程未暴露工具时，写 `blocked/auth-or-tool`。

## A 级推荐插件安装结果

| 口径 | 数量 | 证据 |
| --- | ---: | --- |
| marketplace 总数 | 178 | `evidence/codex-plugin-list-current.txt` |
| marketplace 已安装启用 | 36 | `codex plugin list` |
| marketplace 未安装 | 142 | `codex plugin list` |
| primary-runtime 插件 | 4 | `documents`、`pdf`、`spreadsheets`、`presentations` |
| A 级推荐条目 | 40 | `docs/codex-plugin-audit.md` |

## 第二轮新线程暴露探针

历史探针线程：`019ee5fc-4bb9-74e0-99d0-0555618313fc`。

重启后复核线程：`019ee803-b71e-7b01-a7b6-1608b91e9916`。

重启后证据文件：`evidence/restart-thread-plugin-deepcheck-receipt.md`。

目的：验证安装后开启新线程，是否能看到更多插件能力，以及 app connector 工具是否暴露。

结果：

| 项目 | 结论 |
| --- | --- |
| marketplace 总数 | 178 |
| installed/enabled | 36 |
| not installed | 142 |
| A 级推荐 marketplace 插件缺失 | 无 |
| primary-runtime | `documents`、`pdf`、`spreadsheets`、`presentations` 可见 |
| 新线程初始可见 Skills 增量 | `browser`、`chrome`、`computer-use`、`record-and-replay`、`github`、`hugging-face`、`posthog`、`sentry`、`zotero`、`spreadsheets`、`documents`、`presentations`、`build-web-data-visualization`、`hyperframes`、`codex-security`、`openai-developers`、`notion`、`google-drive`、`airtable`、`figma`、`canva` 等 |
| 新线程初始不可见的 app-only 插件 | `readwise`、`scite`、`semrush`、`similarweb`、`brand24`、`mixpanel`、`amplitude`、`datadog`、`dovetail`、`mem` |
| tool_search 探针 | 搜索 PostHog、Mixpanel、Amplitude、Semrush、Similarweb、Brand24、Readwise、Scite、Dovetail、Mem、Notion、Google Drive、Airtable、Figma、Canva 等后，仍未暴露外部 SaaS 直连工具 |
| Record & Replay 探针 | `event_stream_status` 成功，`isRecording=false` |
| Computer Use 探针 | `list_apps` 成功，但历史 `get_app_state(Codex)` 仍失败；入口可响应不等于所有 App 可读 |
| 结论 | 新线程确实让更多 Skills 可见，但没有让外部 app connector 专用工具自动可用；这些插件仍需账号授权、tool 入口和真实数据源后才能算实际调用 |

边界：新线程探针没有改文件、没有登录外部服务、没有写入第三方系统。

## 实际调用账本

| 插件 / 能力 | 阶段 | 已安装 | 当前线程可见 | 已实际调用 | 结果质量 | 结果 | 下一步 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OpenAI Docs / Codex manual | research | 是 | 是 | 是 | 强 | 刷新并读取官方手册，确认插件包含 Skill / App / MCP，安装后通常新线程使用。 | 保留为 Codex 自身能力事实来源。 |
| GitHub | research / publication / feedback | 是 | 本线程未暴露 app 工具，但 `gh` 可用 | 是 | 强 | `gh repo view` 成功读取 `sunny-kobe/SignalProof`；issue list 为空。 | 默认纳入开源信号、发布和反馈阶段。 |
| Hugging Face | research | 是 | app 工具未暴露，公开 API 可用 | 是 | 中 | model API 和 Dataset Viewer 成功；`hf` CLI 缺失。 | 用公开 API 做模型/数据集初筛；需要 CLI 时再安装。 |
| Zotero | research | 是 | helper 可运行 | 是 | blocked/local-app-not-running | 本地 API `127.0.0.1:23119` 拒绝连接。 | 只有 Zotero Desktop 运行且资料库有价值时启用。 |
| Record & Replay | asset / flow-review | 是 | 是 | 是 | 强 | `event_stream_status` 返回 `isRecording=false`，最大录制 1800 秒。 | 默认作为“用户演示 -> Skill”能力。 |
| Computer Use | validation / flow-review | 是 | 是 | 是 | mixed | 重启后 `list_apps` 成功；历史 `get_app_state(Codex)` 返回 macOS 错误 `-1743`。 | 可作为条件候选；读取具体 App 状态前先做无副作用探针。 |
| Browser | validation / publication | 是 | 技能可读，Node REPL setup 失败 | 是 | failed/tool | setup 报 `codex/sandbox-state-meta: missing field sandboxPolicy`。 | 暂不作为默认验收依赖。 |
| Spreadsheets | artifact / feedback | runtime | 是 | 是 | 强 | 生成 `plugin-eval-workbook.xlsx`、预览 PNG、inspect。 | 默认用于插件矩阵、反馈台账、证据表。 |
| Data Visualization | artifact / report | 是 | 技能可读 | 是 | 中 | 生成 `plugin-eval-summary.html`；浏览器验收失败。 | 默认用于把审计结果转成可读资产。 |
| last30days | research | 技能可用 | 是 | 是 | 中 | 查询 `AI coding repo context loss` 得到 13 条证据，覆盖 GitHub/Reddit/YouTube；X/HN/YouTube 评论有缺口。 | 真实趋势 case 默认候选，但必须记录来源质量。 |
| Documents | artifact | runtime | 是 | 是 | 中 | 生成 `plugin-eval-brief.docx`，结构检查通过；未做 LibreOffice 页面渲染。 | 需要正式文档交付时启用。 |
| PDF | artifact | runtime | 是 | 是 | 中 | 生成 `plugin-eval-brief.pdf`，文本抽取通过；缺 `pdftoppm/pdfinfo`。 | 正式报告启用，补 Poppler 后增强验收。 |
| Presentations | artifact / publication | runtime | 是 | 是 | 强 | 生成 `plugin-eval-deck.pptx`、slide PNG、montage、inspect。 | 复盘/分享场景默认候选。 |
| HyperFrames | artifact / publication | 是 | 是 | 是 | 中 | HTML composition lint `ok=true`；缺 `ffmpeg` 未导出 mp4。 | 视频化发布场景启用，先补 ffmpeg。 |
| Sentry | feedback / validation | 是 | Skill 可读，API token 缺失 | 部分 | blocked/auth | helper 可用；`SENTRY_AUTH_TOKEN` 缺失。 | 有线上应用和 token 后再启用。 |
| PostHog | feedback / validation | 是 | app 工具未暴露，API key 缺失 | 部分 | blocked/auth-or-tool | 当前线程无法查询真实项目数据。 | 真实产品埋点后再启用。 |
| Mixpanel | feedback | 是 | app 工具未暴露，token 缺失 | 部分 | blocked/auth-or-tool | 当前不能读取真实事件。 | 有项目 token 后专项跑。 |
| Amplitude | feedback | 是 | app 工具未暴露，API key 缺失 | 部分 | blocked/auth-or-tool | 当前不能读取真实漏斗。 | 有项目数据后专项跑。 |
| Datadog | feedback / validation | 是 | app 工具未暴露，API key 缺失 | 部分 | blocked/auth-or-tool | 当前不能读取日志/指标。 | 部署后再用。 |
| Readwise | research | 是 | app 工具未暴露 | 否 | blocked/auth-or-tool | 只能确认 manifest 为 app 集成。 | 你有 Reader/Readwise 资料库时授权后跑。 |
| Scite | research / debate | 是 | app 工具未暴露 | 否 | blocked/auth-or-tool | 只能确认 manifest 为 app 集成。 | 论文反证型 case 再跑。 |
| Semrush | research / publication | 是 | app 工具未暴露，API key 缺失 | 否 | blocked/auth-or-tool | 只能确认 manifest 为 app 集成。 | SEO/竞品专项 case 再跑。 |
| Similarweb | research | 是 | app 工具未暴露 | 否 | blocked/auth-or-tool | 只能确认 manifest 为 app 集成。 | 竞品流量专项 case 再跑。 |
| Brand24 | research / feedback | 是 | app 工具未暴露 | 否 | blocked/auth-or-tool | 只能确认 manifest 为 app 集成。 | 品牌/关键词监听专项 case 再跑。 |
| Dovetail | feedback | 是 | app 工具未暴露 | 否 | blocked/auth-or-tool | 只能确认 manifest 为 app 集成。 | 有访谈库时启用。 |
| Mem | asset / research | 是 | app 工具未暴露 | 否 | blocked/auth-or-tool | 只能确认 manifest 为 app 集成。 | 有 Mem 知识库时启用。 |
| Notion / Google Drive / Airtable / Linear / Box | research / asset | 是 | Skill 或 manifest 可见，app 工具未直连暴露 | 否 | blocked/auth-or-tool | 已安装但未读取真实外部资料。 | 资料确实在对应系统且完成授权时再启用。 |
| Vercel / Netlify / Cloudflare | publication / validation | 是 | 技能可读，未部署 | 否 | not-needed-this-case | 本轮没有公开部署目标。 | 有 HTML/站点发布任务时启用。 |
| Canva / Figma | artifact | 是 | app 工具未暴露 | 否 | not-needed-this-case | 本轮没有设计稿或社媒图产物。 | 视觉传播专项 case 再跑。 |

## App-only 推荐插件阻塞证据

这些插件 manifest 中 `skills_count=0`、`apps_count>0`，没有本地 Skill 可读。新线程也没有暴露专用 connector 工具，因此当前只能记为 `blocked/no-tool-exposed` 或 `blocked/auth-or-tool`。

| 插件 | 本轮状态 | 当前结论 |
| --- | --- | --- |
| `readwise` | app-only，tool_search 未暴露工具 | 有 Reader/Readwise 资料库且授权后再跑 |
| `scite` | app-only，tool_search 未暴露工具 | 论文反证专项 case 再跑 |
| `amplitude` | app-only，tool_search 未暴露工具 | 有产品事件数据后再跑 |
| `mixpanel` | app-only，tool_search 未暴露工具 | 有项目 token/connector 后再跑 |
| `similarweb` | app-only，tool_search 未暴露工具 | 竞品流量专项 case 再跑 |
| `brand24` | app-only，tool_search 未暴露工具 | 关键词监听专项 case 再跑 |
| `dovetail` | app-only，tool_search 未暴露工具 | 有访谈库后再跑 |
| `jam` | app-only，tool_search 未暴露工具 | 有问题录制需求再跑 |
| `mem` | app-only，tool_search 未暴露工具 | 有 Mem 知识库后再跑 |
| `semrush` | app-only，tool_search 未暴露工具 | SEO/关键词专项 case 再跑 |
| `datadog` | app-only，tool_search 未暴露工具 | 有运行态日志/指标后再跑 |

## 40 个 A 级能力逐项完成审计

已补充逐项证据文件：`evidence/a-level-plugin-completion-matrix.md`。

去重后 A 级能力共 40 个：36 个 marketplace 推荐插件，加 4 个 primary-runtime 能力。逐项审计结果：

| 状态 | 数量 | 结论 |
| --- | ---: | --- |
| `called` | 11 | 当前环境能安全调用、生成产物或完成无副作用技能探针的能力已实际试跑。 |
| `failed/tool` | 1 | Browser 已真实调用但当前环境失败。 |
| `failed/local-app` | 1 | Zotero 已调用，但 Zotero Desktop 本地 API 未运行。 |
| `blocked/auth` | 4 | Sentry、PostHog、Amplitude、Datadog 缺账号/API/真实项目数据。 |
| `blocked/auth-or-tool` | 15 | app connector 类插件已安装，但当前线程未暴露专用工具或未授权。 |
| `condition-only` | 8 | Computer Use、部署、设计、Chrome 登录态、安全扫描等本轮没有稳定或安全真实目标，不强行调用。 |

完成判断：

- 已安装和当前环境可调用的插件，不再停留在“推荐”层，均已有实际调用、产物、失败或阻塞证据。
- Superpowers 已通过 `verification-before-completion` 技能参与最终验收；Deepnote 改为 `blocked/auth-or-tool`，因为其技能要求 app tools，当前线程未暴露。
- 无授权 app connector 不计为真实调用。
- `condition-only` 插件不删除，但不进入默认流程；只有当 case 明确需要部署、设计、Chrome 登录态或安全扫描时才启用。

## 阶段能力结论

| 阶段 | 默认插件 | 条件插件 | 暂不默认 |
| --- | --- | --- | --- |
| signal | GitHub、OpenAI Docs | Browser、Chrome、Hugging Face | Computer Use |
| research | GitHub、Hugging Face API、last30days | Readwise、Scite、Semrush、Similarweb、Brand24、Zotero、Notion、Google Drive | 无授权 app connector |
| validation | Spreadsheets、脚本自检 | Sentry、PostHog、Datadog、Browser、Computer Use、Codex Security | Browser 当前环境失败；Computer Use 需先确认目标 App 权限 |
| artifact | Spreadsheets、Data Visualization | Documents、PDF、Presentations、Canva、Figma、HyperFrames | 缺 LibreOffice/Poppler/ffmpeg 时降级验收 |
| feedback | GitHub | PostHog、Mixpanel、Amplitude、Sentry、Dovetail、Brand24 | 无真实数据源时不启用 |
| asset | Record & Replay、Spreadsheets、Data Visualization | Mem、Notion、Google Drive、Airtable | 无 |

## 本轮总判断

真正带来明显提升的不是“所有插件都打开”，而是：

1. 让 GitHub 成为开源信号和反馈的默认证据源。
2. 让 Record & Replay 承担“用户演示 -> Skill”的资产化入口。
3. 让 `last30days` 成为真实趋势调研的默认候选，但始终带来源质量门。
4. 让 Spreadsheets、Data Visualization、Documents、PDF、Presentations、HyperFrames 把工具账本变成可检查资产。
5. 对 app connector 类调研/反馈插件保持条件启用，避免没有授权时制造假证据。
