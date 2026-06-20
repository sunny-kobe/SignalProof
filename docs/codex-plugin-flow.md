# Codex 自带插件接入流程

SignalProof 不应该把所有插件都默认跑一遍。每个阶段先判断“这个能力是否会改变决策、减少不确定性或验收产物”，再决定是否调用，并把结果写入 `tool-ledger.md`。

## 阶段能力计划

| 阶段 | 优先目标 | Codex 自带插件候选 | 使用条件 | 记录位置 |
| --- | --- | --- | --- | --- |
| signal | 捕捉信号和边界 | Browser、Chrome、Record & Replay | 信号来自网页、登录态页面、用户演示或另一个 Codex 线程 | `signal.md`、`tool-ledger.md` |
| research | 收集证据 | Browser、Chrome、Documents、PDF、Spreadsheets、Data Visualization | 证据来自网页、登录态页面、文档、PDF、表格或需要可视化分析 | `research.md`、`vault/assets/research/` |
| debate | 反方审查 | Browser、Chrome、Documents、PDF | 关键反对意见依赖外部页面或长文档证据 | `debate.md` |
| thesis | 做继续/收窄/暂停/放弃判断 | 通常不直接用插件 | 判断缺证据时回退到 research/debate 补用插件 | `thesis.md` |
| validation | 验收实验和产物 | Browser、Computer Use、Documents、PDF、Spreadsheets、Presentations | 产物有界面、图形界面、文档、表格、演示文稿或 PDF 质量要求 | `validation.md`、`flow-review.md` |
| artifact | 生成产物 | Documents、PDF、Spreadsheets、Presentations、HyperFrames、Data Visualization | 产物不只是 Markdown，或需要排版、视觉、表格、演示、视频化表达 | `artifact.md`、`vault/assets/` |
| publication | 发布触达 | Browser、Chrome | 需要确认公开 URL、截图、登录态后台或用户授权渠道操作 | `feedback.md`、`day2-execution.md` |
| feedback | 回收反馈 | Chrome、Browser、Spreadsheets、Record & Replay | 反馈来自登录态渠道、公开页面、表格数据或用户演示 | `feedback.md`、`vault/assets/feedback/` |
| decision | 做最终决策 | 通常不直接用插件 | 决策依赖未核验反馈、指标或产物验收时回退补用 | `decision.md` |
| asset | 沉淀资产 | Documents、PDF、Spreadsheets、Presentations、Record & Replay、Browser | 资产要变成资料包、文档、表格、PPT、可录制流程或公开页面 | `asset.md`、`vault/assets/` |
| flow-review | 审计流程 | Browser、Computer Use、Documents、PDF、Spreadsheets、Presentations | 需要证明报告可读、界面可用、文件格式正确或图形界面流程真实可跑 | `flow-review.md`、`vault/runs/` |

## 执行顺序

1. 开始案例前运行：

```bash
python3 scripts/signalproof.py capabilities
```

2. 在每个阶段开始时，从阶段能力计划里选候选插件。
3. 只调用能改变判断或能验收产物的插件。
4. 结果写入 `tool-ledger.md`，包括：候选、是否使用、结果质量、跳过原因、下一步。
5. 如果插件失败，写成能力缺口，不把失败当成反证。

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
| Browser | 按 Browser skill 使用 in-app Browser 接入步骤 | 失败：`codex/sandbox-state-meta: missing field sandboxPolicy` | 当前不能作为页面验收主路径 |
| Computer Use | `list_apps` | 成功 | 本机图形界面插件可用 |
| Computer Use | `get_app_state Google Chrome` | 成功 | 可读取 Chrome 中的 GitHub 仓库页面 |
| Chrome | 未直接调用 | 不适用 | 本次 Chrome 只是 Computer Use 读取对象 |

执行原则：

- 不用插件成功覆盖插件失败；
- 不把降级路径写成原插件成功；
- 不把可见页面写成外部反馈；
- 后续每新增一个插件实际调用，都要新增或更新一个案例，而不是只改说明文档。

## 当前第一步边界

本文件不强制所有案例自动调用插件。每加一个真实插件调用，都要有一个具体案例验证它是否真的提高结果质量，并记录失败、降级路径和下次优化。
