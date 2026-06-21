# Codex 推荐插件接入流程

SignalProof 不应该把所有插件都默认跑一遍。每个阶段先判断“这个能力是否会改变决策、减少不确定性或验收产物”，再决定是否调用，并把结果写入 `tool-ledger.md`。

重启后当前结论：

- 36 个推荐 marketplace 插件已安装启用，A 级推荐缺失为 0。
- Documents、PDF、Spreadsheets、Presentations 四个 primary-runtime 能力可见。
- Record & Replay、Computer Use 的 MCP 入口能响应，但 Computer Use 读取具体 App 状态仍可能受系统权限影响。
- 调研/反馈类 app connector 已安装不等于已授权，也不等于当前线程有直连 tool。
- `codex plugin list` 会同时显示已安装和未安装插件；只看 `STATUS = installed, enabled` 判断当前是否装好。

## 阶段能力计划

| 阶段 | 优先目标 | Codex 自带插件候选 | 使用条件 | 记录位置 |
| --- | --- | --- | --- | --- |
| signal | 捕捉信号和边界 | GitHub、Browser、Chrome、Record & Replay、OpenAI Docs | 信号来自仓库、网页、登录态页面、用户演示或 Codex 自身能力问题 | `signal.md`、`tool-ledger.md` |
| research | 收集证据并判断准确性 | GitHub、last30days、OpenAI Docs、Hugging Face、Readwise、Scite、Semrush、Similarweb、Brand24、Zotero、Browser、Chrome、Documents、PDF、Spreadsheets、Data Visualization | 公开趋势、技术事实、论文反证、竞品流量、品牌提及、阅读库或资料库会改变判断时；账号类插件必须先授权；按 `docs/research-quality-gate.md` 记录来源覆盖、交叉验证、反证和结论许可 | `research.md`、`vault/assets/research/`、`tool-ledger.md` |
| debate | 反方审查 | Scite、GitHub、Readwise、Zotero、Browser、Chrome、Documents、PDF | 关键反对意见依赖论文、外部页面、长文档或历史资料 | `debate.md` |
| thesis | 做继续/收窄/暂停/放弃判断 | 通常不直接用插件 | 判断缺证据时回退到 research/debate 补用插件 | `thesis.md` |
| validation | 验收实验和产物 | 本地脚本、Spreadsheets、Browser、Computer Use、Sentry、PostHog、Datadog、Codex Security、Documents、PDF、Presentations | 产物有界面、图形界面、运行态、错误日志、安全风险或文件质量要求；外部数据类插件必须有真实项目 | `validation.md`、`flow-review.md` |
| artifact | 生成产物 | Spreadsheets、Data Visualization、Documents、PDF、Presentations、HyperFrames、Canva、Figma | 产物不只是 Markdown，或需要排版、视觉、表格、演示、视频化表达 | `artifact.md`、`vault/assets/` |
| publication | 发布触达 | GitHub、Vercel、Netlify、Cloudflare、Browser、Chrome | 需要确认公开 URL、仓库入口、部署状态、截图、登录态后台或用户授权渠道操作 | `feedback.md`、`day2-execution.md` |
| feedback | 回收反馈 | GitHub、Brand24、PostHog、Mixpanel、Amplitude、Sentry、Datadog、Dovetail、Spreadsheets、Record & Replay、Chrome、Browser | 反馈来自 issue/star、品牌提及、产品埋点、错误日志、访谈库、登录态渠道或表格数据 | `feedback.md`、`vault/assets/feedback/` |
| decision | 做最终决策 | 通常不直接用插件 | 决策依赖未核验反馈、指标或产物验收时回退补用 | `decision.md` |
| asset | 沉淀资产 | Record & Replay、Spreadsheets、Data Visualization、Documents、PDF、Presentations、Mem、Notion、Google Drive、Airtable、Browser | 资产要变成资料包、知识库、文档、表格、PPT、可录制流程或公开页面；外部库必须授权 | `asset.md`、`vault/assets/` |
| flow-review | 审计流程 | Browser、Computer Use、Record & Replay、Documents、PDF、Spreadsheets、Presentations、Codex Security | 需要证明报告可读、界面可用、文件格式正确、操作流程真实可跑或安全风险可控 | `flow-review.md`、`vault/runs/` |

## 执行顺序

1. 开始案例前运行：

```bash
python3 scripts/signalproof.py capabilities
```

2. 在每个阶段开始时，从阶段能力计划里选候选插件。
3. 只调用能改变判断或能验收产物的插件。
4. 结果写入 `tool-ledger.md`，包括：候选、是否使用、结果质量、跳过原因、下一步。
5. 如果插件失败，写成能力缺口，不把失败当成反证。
6. 研究阶段额外执行 `docs/research-quality-gate.md`：至少检查公开讨论、项目和数据、官方和一手资料、反证和替代方案四类来源；证据弱或阻塞时，只能给出继续研究、低成本实验、暂停或放弃。

## 实际调用闭环

从 `2026-06-20-codex-plugin-real-call-flow` 开始，SignalProof 把插件接入从“能力矩阵”推进到“真实调用”。

标准闭环：

| 步骤 | 动作 | 写入位置 |
| --- | --- | --- |
| 1 | 运行 `capabilities`，确认候选插件 | `vault/runs/`、`tool-ledger.md` |
| 2 | 选择一个真正影响判断或验收的插件 | `validation.md` |
| 3 | 读取该插件 skill，并按推荐入口调用 | `process-log.md` |
| 4 | 保存成功输出或失败错误 | `research.md`、`tool-ledger.md` |
| 5 | 判断结果质量：强 / 中 / 弱 / 失败 | `tool-ledger.md` |
| 6 | 失败后先记账，再选择降级路径 | `flow-review.md` |
| 7 | 把下一轮优化写清楚 | `flow-review.md`、`asset.md` |

本轮实际结果：

| 插件 | 调用方式 | 结果 | 结论 |
| --- | --- | --- | --- |
| Browser | 按 Browser skill 使用 in-app Browser 接入步骤 | 历史失败：`codex/sandbox-state-meta: missing field sandboxPolicy` | 作为历史风险记录；有网页验收目标时重新只读探针 |
| Computer Use | `list_apps` | 成功 | 工具入口可响应 |
| Computer Use | `get_app_state(Codex)` | 失败：macOS 错误 `-1743` | 具体 App 状态读取仍受权限影响，暂不做硬 gate |
| Record & Replay | `event_stream_status` | 成功 | 可作为用户演示到 skill 的默认候选 |
| Chrome | Chrome 插件只读复查 + 本机窗口清单 | 可看到 GitHub/X/Readwise 相关状态，但未证明研究增强 connector 可读 | 只在需要用户 Chrome 登录态时启用 |
| App connector 类插件 | `tool_search` + manifest 检查 | 多数未暴露直连 tool 或未授权 | 需要账号、tool 入口和真实数据源后再用 |

执行原则：

- 不用插件成功覆盖插件失败；
- 不把降级路径写成原插件成功；
- 不把可见页面写成外部反馈；
- 不把 app connector 未授权写成“没有需求”或“0 结果”；
- 后续每新增一个插件实际调用，都要新增或更新一个案例，而不是只改说明文档。

## 分层默认

| 层级 | 能力 | 规则 |
| --- | --- | --- |
| 默认基础层 | SignalProof 脚本、Markdown vault、OpenAI Docs、GitHub、Spreadsheets、Data Visualization、Record & Replay | 能在无额外授权下提高证据、验收或资产化质量。 |
| 调研增强层 | last30days、Hugging Face、Readwise、Scite、Semrush、Similarweb、Brand24、Zotero | last30days 可做趋势默认候选；账号类调研插件需授权和真实对象。 |
| 验证增强层 | Browser、Chrome、Computer Use、Sentry、PostHog、Datadog、Codex Security | 有页面、登录态、GUI、运行态或安全扫描目标时触发。 |
| 产物增强层 | Documents、PDF、Presentations、HyperFrames、Canva、Figma | 有正式交付、演示、视频化或视觉表达目标时触发。 |
| 外部知识/数据层 | Notion、Google Drive、Airtable、Deepnote、Linear、Box、Mem、Dovetail、Mixpanel、Amplitude | 只有 tool 入口、账号授权、真实数据源三者同时成立才进入证据链。 |

## 当前第一步边界

本文件不强制所有案例自动调用插件。每加一个真实插件调用，都要有一个具体案例验证它是否真的提高结果质量，并记录失败、降级路径和下次优化。

## 安装和迁移补充

安装状态、界面不可见原因和迁移边界见 [`docs/codex-plugin-status-and-migration.md`](codex-plugin-status-and-migration.md)。

最小复核命令：

```bash
codex plugin marketplace list
codex plugin list
python3 scripts/signalproof.py plugin-status
```
