# 重启后插件深测回执

## 基本信息

- 深测线程：`019ee803-b71e-7b01-a7b6-1608b91e9916`
- 来源线程：`019ee4dc-96da-7502-83d5-0f6276b3ba8e`
- 回执时间：2026-06-21 10:31:18 CST
- 执行边界：只读探测；未改文件、未登录外部服务、未部署、未创建外部资源。

## 插件安装统计

| Marketplace | 总数 | installed/enabled | not installed |
| --- | ---: | ---: | ---: |
| `openai-bundled` | 5 | 4 | 1 |
| `openai-curated` | 173 | 32 | 141 |
| 合计 | 178 | 36 | 142 |

推荐 marketplace 插件缺失清单：无。

额外说明：`latex@openai-bundled` 未安装，但不是本轮 A 级推荐项。

## 已安装启用的推荐插件

`browser`、`chrome`、`computer-use`、`record-and-replay`、`github`、`google-drive`、`notion`、`airtable`、`deepnote`、`posthog`、`mixpanel`、`amplitude`、`sentry`、`datadog`、`brand24`、`semrush`、`similarweb`、`scite`、`readwise`、`zotero`、`hugging-face`、`openai-developers`、`codex-security`、`build-web-data-visualization`、`hyperframes`、`canva`、`figma`、`vercel`、`netlify`、`cloudflare`、`linear`、`box`、`superpowers`。

Primary runtime 能力可见：`documents`、`pdf`、`spreadsheets`、`presentations`，对应 runtime bundle 为 `26.619.11828`。

## 当前线程真实可见入口

| 类型 | 结果 |
| --- | --- |
| `Record & Replay` MCP | `event_stream_status` 可调用，返回 `isRecording=false`。 |
| `Computer Use` MCP | `list_apps` 可调用，返回本机 app 列表。 |
| Workspace runtime | `load_workspace_dependencies` 可调用，返回 Node/Python/pnpm/git 和文档/表格/演示依赖。 |
| Browser / Chrome | 插件 installed/enabled，skills 可见；当前线程未暴露直接 browser/chrome MCP namespace。 |
| GitHub / Notion / Google Drive / Airtable / Deepnote 等 | skills 或 plugin manifest 可见；外部系统直连 tool 未通过 `tool_search` 暴露。 |
| PostHog / Mixpanel / Amplitude / Sentry / Datadog / Brand24 / Semrush / Similarweb / Scite / Readwise | 插件已安装，但当前线程未看到直接外部 connector tool；仍需授权或工具暴露。 |

## 无副作用探针结果

| 探针 | 结果 | 结论 |
| --- | --- | --- |
| `codex plugin list` | 成功 | 178 个 marketplace 插件中 36 个已安装启用。 |
| `python3 scripts/signalproof.py diagnose` | 成功 | `last30days` 脚本存在；`bird_authenticated=false`；Safari cookie 权限不足。 |
| `python3 scripts/signalproof.py capabilities` | 成功 | SignalProof 能力矩阵能识别 Browser、Chrome、Computer Use、Record & Replay 和文档 runtime。 |
| `mcp__event_stream.event_stream_status` | 成功 | Record & Replay 入口真实可响应。 |
| `mcp__computer_use.list_apps` | 成功 | Computer Use 工具入口真实可响应；不等于所有 App 状态读取都可用。 |
| `tool_search` 多组查询 | 成功但外部 connector tool 未暴露 | 安装和 skill 可见不等于外部 SaaS 数据可读。 |

## 分类结论

| 分类 | 插件或能力 | 判断 |
| --- | --- | --- |
| `blocked/auth` | `last30days` 的 Bird/X、Safari cookie 抽取；私有 GitHub/Drive/Notion/Airtable 等用户数据 | 需要账号、权限或系统授权。 |
| `blocked/auth-or-tool` | PostHog、Mixpanel、Amplitude、Sentry、Datadog、Brand24、Semrush、Similarweb、Scite、Readwise | 已安装但本线程未看到直连 tool；后续还可能需要账号授权。 |
| `failed/tool` | 本次重启后深测没有关键失败；历史主线程 Browser setup 失败、Computer Use `get_app_state(Codex)` 失败仍保留为旧证据 | 当前策略应区分“工具入口可响应”和“具体目标读取失败”。 |
| `condition-only` | Browser、Chrome、Computer Use、Record & Replay、Documents、PDF、Spreadsheets、Presentations、Canva、Figma、HyperFrames、Data Visualization、Codex Security、OpenAI Developers | 按 case 阶段触发，不默认全跑。 |

## 整合建议

- 默认使用：SignalProof 本地脚本、Markdown vault、`check-all`、`export-all`、`capabilities`、Codex 线程工具、必要的 Git/GitHub 只读检查。
- 条件触发：Browser/Chrome 用于网页或登录态证据核验；Computer Use/Record & Replay 用于 GUI 或用户操作流程证明；Documents/PDF/Spreadsheets/Presentations 用于文件产物验收；Data Visualization/HyperFrames/Canva/Figma 用于资产表达。
- 需要授权后使用：GitHub、Google Drive、Notion、Airtable、Deepnote、PostHog/Mixpanel/Amplitude、Sentry/Datadog、Brand24/Semrush/Similarweb/Scite/Readwise/Zotero。
- 暂不纳入默认流：所有需要外部登录、付费账号、私有数据或未暴露 tool 入口的插件。

明确声明：安装不等于授权，工具调用不等于证据合格。SignalProof 仍必须判断来源质量、覆盖缺口和结果是否真的改变结论。
