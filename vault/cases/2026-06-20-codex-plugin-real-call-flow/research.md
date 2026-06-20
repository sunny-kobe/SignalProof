---
type: research
status: researched
updated_at: 2026-06-20
gate: passed
---

# 研究

## 要回答的问题

- 当前 SignalProof 流程是否已经能发现 Codex 自带插件？
- Browser 插件是否能按官方 skill 的接入路径实际连接？
- Computer Use 插件是否能真实读取本机应用和 Chrome 页面状态？
- 插件失败后，SignalProof 应如何记录失败类型和降级路径？

## 已确认事实

- `scripts/signalproof.py capabilities` 已检测到 Browser、Chrome、Computer Use、Record & Replay、Documents、PDF、Spreadsheets、Presentations、Data Visualization、HyperFrames 等候选插件。
- Browser 插件的真实调用失败，失败发生在 `setupBrowserRuntime` 后获取 in-app Browser 文档阶段，错误为 `codex/sandbox-state-meta: missing field sandboxPolicy`。
- Computer Use 插件 `list_apps` 调用成功，返回 Google Chrome、Codex、Cursor、Safari、Douyin、CC Switch 等本机应用。
- Computer Use 插件 `get_app_state` 调用 Google Chrome 成功，返回窗口标题 `sunny-kobe/SignalProof: SignalProof：Codex 优先的个人信号到资产证明协议`，地址栏值为 `github.com/sunny-kobe/SignalProof`。
- Chrome 本身没有通过 Chrome 插件直接调用；本次只是作为 Computer Use 读取的目标应用。

## 一手来源

- 本仓库脚本输出：`python3 scripts/signalproof.py capabilities`。
- Browser 插件真实调用输出：Node REPL MCP 返回 `missing field sandboxPolicy`。
- Computer Use MCP 输出：`list_apps` 和 `get_app_state` 的原始工具结果。
- Chrome 可见页面：GitHub 仓库 `sunny-kobe/SignalProof`。

## 工具覆盖

- 已使用：SignalProof skill、personal-opportunity-os skill、Browser 插件、Computer Use 插件、MCP、Git、本地脚本。
- 未使用但相关：Chrome 插件、Record & Replay、Documents、PDF、Spreadsheets、Presentations。
- 跳过原因：Chrome 插件不需要额外登录态操作；Record & Replay 不需要录制用户演示；Documents、PDF、Spreadsheets、Presentations 不影响这次插件调用判断。
- 是否需要补跑：需要补跑 Browser 插件接入修复；需要后续用 Browser 或 Computer Use 对 `vault/reports/index.html` 做可视化验收。

## 查询计划

| 查询层 | 查询 | 目标问题 | 预期来源 | 实际来源 | 原始记录 |
| --- | --- | --- | --- | --- | --- |
| 本地能力 | `python3 scripts/signalproof.py capabilities` | 插件是否可发现 | 本地脚本 | 能力矩阵输出 | `vault/runs/2026-06-20-codex-capability-matrix.md` |
| Browser 调用 | Browser skill 接入代码 | in-app Browser 是否能连接 | Browser 插件 MCP | 失败，缺 `sandboxPolicy` | `process-log.md` |
| Computer Use 调用 | `list_apps` | 本机图形界面插件是否可用 | Computer Use MCP | 成功 | `process-log.md` |
| Chrome 状态 | `get_app_state Google Chrome` | 是否能读取仓库页面 | Computer Use MCP | 成功 | `process-log.md` |

## 来源覆盖

| 来源 | 是否相关 | 是否成功 | 结果数量 | 失败原因 | 是否需要补跑 |
| --- | --- | --- | ---: | --- | --- |
| 本地能力矩阵 | 是 | 是 | 1 | 无 | 后续每次阶段前可跑 |
| Browser 插件 | 是 | 否 | 0 | `missing field sandboxPolicy` | 是 |
| Computer Use 插件 | 是 | 是 | 2 | 无 | 否 |
| Chrome 插件 | 中 | 未使用 | 0 | 本次没有直接 Chrome 插件需求 | 后续登录态页面再用 |
| last30days | 低 | 未使用 | 0 | 本案例不判断市场热度 | 否 |

## 工具失败记录

| 工具 | 时间 | 失败类型 | 错误信息 | 对结论影响 | 补救动作 |
| --- | --- | --- | --- | --- | --- |
| Browser 插件 | 2026-06-20 | 运行时 schema 缺字段 | `codex/sandbox-state-meta: missing field sandboxPolicy` | Browser 不能作为当前验收主路径 | 记录为能力缺口，后续修复插件运行时或换 Computer Use 验收 |
| Safari Computer Use | 2026-06-20 | 图形界面状态读取超时 | `timeoutReached` | 不影响 Chrome 路径，但说明图形界面读取有应用差异 | 优先读取 Chrome 或 Codex，必要时重试 |

## 证据相关性

- 强相关：Browser 插件真实错误、Computer Use 成功读取 Chrome 页面。
- 中相关：能力矩阵证明插件文件可发现。
- 弱相关：Chrome 页面截图显示的远程仓库状态可能是浏览器缓存，不等于最新远程提交状态。
- 噪音：本机其他正在运行应用只用于证明 Computer Use 可读取应用列表，不参与机会判断。

## 研究质量门

- 是否有至少 3 类来源：有，本地脚本、Browser MCP、Computer Use MCP。
- 是否有真实用户原话：不适用，这是内部流程验证。
- 是否有反证：有，Browser 插件真实调用失败。
- 是否保存原始证据：已在 `process-log.md` 保存关键命令、调用和错误。
- 是否需要补跑：需要补跑 Browser 修复和报告索引视觉验收。
- 当前研究状态：passed，用于内部插件调用流程；不用于外部需求判断。

## 用户原话或真实讨论

- 用户要求：“再以插件实际调用的流程来完整跑一下”。

## 替代品和已有方案

- 只写能力矩阵：不足，因为无法发现运行时错误。
- 直接用普通 Playwright：能验收页面，但不能证明 Codex 自带 Browser 插件链路。
- Computer Use 作为降级路径：能证明本机图形界面可读，但操作粒度和稳定性低于专用 Browser 插件。

## 开源项目和相关工具

- SignalProof 本地 vault 和脚本。
- Codex Browser 插件。
- Codex Computer Use 插件。
- GitHub 仓库 `sunny-kobe/SignalProof`。

## 证据缺口

- Browser 插件尚未成功读取 in-app Browser 文档或页面。
- Chrome 插件没有直接调用。
- `vault/reports/index.html` 尚未用 Browser 或 Computer Use 做页面级视觉验收。

## 当前判断

第一轮“真实插件调用流程”已经成立：成功记录了 Browser 失败和 Computer Use 成功，证明 SignalProof 需要记录实际调用结果质量，而不是只记录能力存在。

## 下一步还需要查什么

- 修复或确认 Browser 插件 `sandboxPolicy` 字段问题。
- 用可用插件对报告索引做一次页面级验收。
- 后续为 Documents、PDF、Spreadsheets、Presentations 各选择一个真实产物场景再接入。
