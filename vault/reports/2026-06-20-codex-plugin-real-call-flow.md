# SignalProof 案例报告：2026-06-20-codex-plugin-real-call-flow

## 信号

---
type: signal
title: Codex 插件实际调用流程验证
status: captured
source_type: internal-workflow
source_url:
captured_at: 2026-06-20
tags:
  - SignalProof
  - Codex 插件
  - 流程自检
---



## 这是什么

当前 SignalProof 已经有 Codex 自带插件能力矩阵，但能力矩阵只能说明插件文件和入口存在，不能证明真实调用路径可用。

这次信号是：按“插件实际调用”的方式跑一遍流程，把成功、失败、降级和下一步都写入案例，而不是只停留在文档设计。

## 为什么引起注意

SignalProof 的价值不只是生成案例文件，还要让 Codex 在每个阶段判断该用什么能力、实际调用、记录结果质量，并把流程缺口沉淀成下次优化。

如果 Browser、Computer Use、Chrome 等插件只是列在能力矩阵里，却没有真实调用记录，后续流程会高估自动化能力。

## 初步用户

- 当前用户本人：希望把个人 Codex 工作流从“会写文档”推进到“能调用插件并审计流程”。
- 未来使用 SignalProof 的 Codex 高阶用户：需要知道哪个阶段该用哪个插件，以及插件失败时怎么记录和降级。

## 初步机会

把“能力矩阵 -> 实际调用 -> 工具账本 -> 流程自检 -> 下一轮优化”固化成 SignalProof 的标准验证环节。

## 相关证据

- `python3 scripts/signalproof.py capabilities` 可生成 Codex 自带插件能力矩阵。
- Browser 插件按自身 skill 的接入方式调用时失败，错误为 `codex/sandbox-state-meta: missing field sandboxPolicy`。
- Computer Use 插件 `list_apps` 调用成功，能读取本机正在运行的应用列表。
- Computer Use 插件 `get_app_state` 读取 Google Chrome 成功，确认 Chrome 打开的是 `github.com/sunny-kobe/SignalProof`。

## 进入研究的理由

这是 SignalProof 插件化流程的关键内部验证。它能证明当前流程是否已经从“文档规划”进入“真实工具调用和失败记录”阶段。

## 暂不研究的理由

本案例不做外部市场研究，也不需要 `last30days`。它验证的是本地 Codex 插件调用链，不是用户需求热度。

## 研究

---
type: research
status: researched
updated_at: 2026-06-20
gate: passed
---



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

## 辩论

---
type: debate
status: debated
updated_at: 2026-06-20
gate: passed
---



## 正方：为什么值得继续

- 这次流程已经从“插件可发现”推进到“插件真实调用”。
- Browser 失败被明确记录，避免后续文档误以为 Browser 已可用。
- Computer Use 成功读取 Chrome 页面，证明至少有一条 Codex 自带插件路径能做本机图形界面验收。
- 新案例可以成为后续接入其他插件的样例。

## 反方：为什么可能不成立

- Browser 插件没有成功，最理想的网页验收路径仍然 blocked。
- Computer Use 读取 Chrome 页面只能证明图形界面状态可见，不能替代 DOM 级浏览器自动化。
- Chrome 页面可能是未刷新的 GitHub 页面，不能证明远程仓库已经展示最新提交。
- 这仍然是内部流程验证，不是外部用户反馈。

## 产品视角

SignalProof 不应该把“插件接入”包装成一个新产品功能，而应该把它作为案例流程里的能力审计层。

## 商业视角

没有商业结论。它能增强未来服务或开源项目的可信度，但当前只证明内部工作流更稳。

## 执行视角

最小可行做法是：每次重要案例先跑 `capabilities`，再挑一个会改变判断的插件实际调用，最后把成功、失败和降级写入 `tool-ledger.md`。

## 开源视角

公开仓库里保留这种失败记录是加分项。它能让其他人看懂 SignalProof 不是只展示顺滑 demo，而是把工具边界也纳入证据。

## 个人优势视角

这符合用户当前的 AI workflow expert 方向：不是教别人“怎么用 AI 写代码”，而是沉淀可复用、可审计、可迁移的 Codex 工作流。

## 最可能失败的原因

- 后续案例只写“候选插件”，没有真的调用。
- 插件失败后直接换工具完成任务，但没有在账本里记录失败。
- 把 Computer Use 的截图或可见页面误当成完整验收。

## 必须砍掉的范围

- 不做独立插件控制台。
- 不做自动调用所有插件。
- 不把 Browser 失败修复扩展成运行时源码排查任务。
- 不把本案例写成外部需求证据。

## 什么证据会改变判断

- Browser 插件能稳定打开并读取本地报告索引，会把网页验收路径从 blocked 改成 passed。
- Chrome 插件能直接读取登录态页面，会补强登录态证据路径。
- Computer Use 在多个应用上稳定读取状态，会提高图形界面验收权重。

## 判断

---
type: thesis
status: proposed
updated_at: 2026-06-20
gate: passed
---



## 当前判断

继续，但只继续优化 SignalProof 的“真实插件调用和工具账本”流程，不扩大成独立应用或全插件自动化系统。

## 是否继续

- 继续 / 收窄 / 暂停 / 放弃：继续，范围收窄到案例级插件调用闭环。

## 第一批用户

- 当前用户本人。
- 需要把 Codex 工作流沉淀为本地协议、模板和可审计案例的高阶使用者。

## 最小切口

每个需要插件验证的案例增加一个固定动作：

1. 运行能力矩阵。
2. 选择一个真正影响判断或验收的插件。
3. 实际调用。
4. 把成功、失败、结果质量和降级动作写入 `tool-ledger.md`。
5. 在 `flow-review.md` 写下次优化。

## 不做清单

- 不自动调用所有 Codex 插件。
- 不把 Browser、Chrome、Computer Use 混成同一种能力。
- 不把工具调用成功等同于证据有效。
- 不把内部插件流程写成市场反馈。

## 成功标准

- 至少一个插件真实调用成功，并写入案例。
- 至少一个插件失败被保留为流程证据，而不是被忽略。
- 文档能指导下一次按同样步骤补跑插件。
- `check-all` 和 `check-goal --min-cases 6` 通过。

## 放弃条件

- 如果后续所有 Codex 自带插件都只能停留在文件检测，不能实际调用，则先暂停插件化叙事，只保留脚本和 Markdown 协议。

## 下一步验证动作

- 修复或复查 Browser 插件运行时字段问题。
- 用 Browser 或 Computer Use 对 `vault/reports/index.html` 做一次页面级验收。
- 在后续真实产物里分别验证 Documents、PDF、Spreadsheets、Presentations。

## 验证计划

---
type: validation
status: validated-internally
updated_at: 2026-06-20
gate: passed
---



## 验证目标

验证 SignalProof 是否能按插件实际调用流程完整跑一轮，并把真实结果写回案例。

## 验证步骤

1. 运行 `python3 scripts/signalproof.py capabilities`，确认 Codex 自带插件候选。
2. 按 Browser 插件 skill 的接入路径尝试连接 in-app Browser。
3. 调用 Computer Use 的 `list_apps`，确认本机应用可读。
4. 调用 Computer Use 的 `get_app_state` 读取 Google Chrome。
5. 把 Browser 失败、Computer Use 成功、Chrome 可见页面写入研究和工具账本。
6. 更新流程文档，形成后续可复用的插件调用循环。

## 成功标准

- 能明确区分“插件文件可发现”和“插件真实调用可用”。
- Browser 失败有错误类型、影响和补救动作。
- Computer Use 成功有可核对的目标应用、窗口标题和 URL。
- 工具结果质量被分级为强、中、弱或失败。
- 自检命令通过。

## 实际结果

- 能力矩阵：通过，插件候选可发现。
- Browser 插件：失败，错误为 `codex/sandbox-state-meta: missing field sandboxPolicy`。
- Computer Use `list_apps`：通过，能读取本机应用列表。
- Computer Use `get_app_state Google Chrome`：通过，能读取 GitHub 仓库页面。

## 验证边界

- 这不是外部用户反馈。
- 这不是登录态 Chrome 插件直接调用。
- 这不是 Browser 页面级验收完成。
- 这只能证明第一轮插件实际调用流程已经跑通，并暴露了下一步缺口。

## 产物

---
type: artifact
status: produced
updated_at: 2026-06-20
gate: passed
---



## 本轮产物

- 新增案例：`vault/cases/2026-06-20-codex-plugin-real-call-flow/`。
- 更新流程文档：`docs/current-flow.md`。
- 更新插件接入文档：`docs/codex-plugin-flow.md`。
- 通过导出命令生成报告索引和案例报告。

## 产物用途

这组文件作为 SignalProof 的“真实插件调用流程样例”。后续每次接入新的 Codex 自带插件，都可以按这个案例的结构记录：

- 候选插件；
- 调用方式；
- 真实输出；
- 错误信息；
- 结果质量；
- 降级路径；
- 下一步优化。

## 产物边界

本产物不替代 Browser 插件修复，也不替代外部发布触达。它只是把当前插件调用状态沉淀成可复用流程资产。

## 反馈

---
type: feedback
status: no-real-feedback
updated_at: 2026-06-20
gate: weak
---



## 真实反馈状态

真实反馈为空。

## 内部执行反馈

- Browser 插件真实调用失败，暴露了运行时接入缺口。
- Computer Use 插件真实调用成功，证明图形界面读取路径可用。
- Chrome 页面可被 Computer Use 读取，但页面内容可能不是最新远程状态，需要用 Git 或 GitHub CLI 继续确认提交状态。

## 反馈质量

- 外部用户反馈：无。
- 内部工具反馈：中。
- 对流程优化的价值：强。

## 不能据此得出的结论

- 不能说明外部用户需要 SignalProof。
- 不能说明 Browser 插件路径已经可用。
- 不能说明所有 Codex 自带插件都适合默认调用。

## 下一步反馈来源

- 用户试用这个插件调用案例后的主观判断。
- 后续 Browser 修复后的页面验收结果。
- 后续真实公开仓库收到的 issue、star、fork 或评论。

## 决策

---
type: decision
status: continue-internal-optimization
updated_at: 2026-06-20
gate: passed
---



## 决策结论

继续推进 SignalProof 的插件实际调用流程，但只作为内部协议能力增强。

## 决策理由

- Browser 插件失败提供了真实能力边界，值得进入工具账本。
- Computer Use 成功提供了可用的图形界面读取路径。
- 这次流程证明 SignalProof 可以把插件调用结果沉淀成案例，而不是停留在聊天过程。

## 真实反馈边界

真实反馈为空。本决策只基于内部执行结果，不基于外部用户反馈。

## 下一步

- 把“先记录失败，再选择降级路径”的原则写入流程文档。
- 对报告索引补一次可视化验收。
- 对 Browser 运行时字段问题做单独排查。

## 暂不做

- 暂不做独立界面。
- 暂不做全插件自动编排。
- 暂不把当前内部验证包装成对外承诺。

## 资产

---
type: asset
status: reusable
updated_at: 2026-06-20
gate: passed
---



## 可复用资产名称

SignalProof 插件实际调用验证循环。

## 资产内容

```text
能力矩阵
-> 选择阶段候选插件
-> 读取对应 Skill
-> 真实调用插件
-> 记录原始结果
-> 判断结果质量
-> 记录失败和影响
-> 选择降级路径
-> 更新 tool-ledger.md
-> 更新 flow-review.md
-> 进入下一轮优化
```

## 可复用 prompt

```text
请按 SignalProof 的插件实际调用流程推进这个案例：
1. 先运行 capabilities，列出本阶段候选 Codex 插件；
2. 只选择一个会改变判断或验收结果的插件；
3. 读取该插件对应 Skill 后真实调用；
4. 把成功、失败、错误信息、结果质量和降级动作写入 tool-ledger.md；
5. 在 flow-review.md 写清楚这次工具覆盖是否足够，以及下次要补跑什么；
6. 真实反馈为空时，不要写成外部需求已被证实。
```

## 适用场景

- Browser 验收本地 HTML 或公开页面。
- Computer Use 读取本机图形界面状态。
- Chrome 读取用户已登录页面。
- Documents、PDF、Spreadsheets、Presentations 验收非 Markdown 产物。
- Record & Replay 沉淀用户演示流程。

## 不适用场景

- 单纯写 Markdown 文件。
- 不需要工具证据的纯判断。
- 外部市场反馈为空但想快速包装对外说法。

## 维护方式

每新增一个插件真实调用案例，就把本资产里的步骤和失败分类补充一次。

## 流程自检

---
type: flow_review
title: Codex 插件实际调用流程验证
status: completed
updated_at: 2026-06-20
gate: passed
---



## 阶段完整性

| 阶段 | gate | 证据 | 结论 |
| --- | --- | --- | --- |
| signal | passed | 用户要求跑插件实际调用流程 | 信号明确 |
| research | passed | Browser 失败、Computer Use 成功 | 内部工具证据充足 |
| debate | passed | 记录专用 Browser 和图形界面降级路径的利弊 | 边界清楚 |
| thesis | passed | 决定继续内部优化 | 范围收窄 |
| validation | passed | 真实调用路径已跑 | 第一轮成立 |
| artifact | passed | 新案例和文档更新 | 可复用 |
| feedback | weak | 真实反馈为空 | 不能外推 |
| decision | passed | 继续内部流程优化 | 不做过度承诺 |
| asset | passed | 插件调用循环 | 可复用 |

## 工具覆盖审计

- Skill：已使用 `personal-opportunity-os`、`user-working-profile`、`signalproof`。
- Plugin：已按 Browser skill 真实调用 Browser 插件，但失败。
- MCP：已使用 Node REPL MCP 和 Computer Use MCP。
- Browser：失败，结果质量为失败。
- Computer Use：成功读取应用列表和 Chrome 页面，结果质量为中到强。
- Chrome：作为目标应用被读取；Chrome 插件本身未直接调用。
- last30days：本案例不涉及最近真实讨论，跳过原因成立。
- Documents、PDF、Spreadsheets、Presentations、Record & Replay：本案例不涉及对应产物，跳过原因成立。

## 证据强度

- 插件调用流程证据：中到强。
- Browser 可用性证据：失败，但失败记录强。
- 图形界面读取证据：中。
- 外部需求证据：无。

## 风险

- 如果后续只保留 Computer Use 路径，可能丢失 DOM 级网页验收能力。
- 如果 Browser 错误不修复，报告索引的自动化浏览器验收仍然 blocked。
- Chrome 页面可见不等于仓库最新状态，需要 Git/GitHub CLI 做提交级确认。

## 优化

- 下次先把插件失败记录写入 `tool-ledger.md`，再选择降级路径。
- 下次 Browser 成功后，补一次 `vault/reports/index.html` 的页面级验收。
- 下次接入 Documents、PDF、Spreadsheets、Presentations 时，每个插件只绑定一个真实产物场景。

## 当前结论

流程可以继续。第一轮真实插件调用已经跑通了“成功和失败都入账”的机制，但 Browser 页面验收路径仍需修复或替代。

## 工具账本

---
type: tool_ledger
title: Codex 插件实际调用流程验证
status: completed
updated_at: 2026-06-20
gate: passed
---



## 候选能力账本

| 能力 | 是否相关 | 是否使用 | 结果质量 | 说明 | 下次动作 |
| --- | --- | --- | --- | --- | --- |
| Skill: personal-opportunity-os | 是 | 是 | 强 | 约束本案例不能扩大成独立应用，必须写工具覆盖和流程自检。 | 保留。 |
| Skill: user-working-profile | 是 | 是 | 中 | 对齐用户偏好：中文、证据边界、执行到结果。 | 保留。 |
| Skill: signalproof | 是 | 是 | 强 | 明确必需文件、真实反馈为空边界、工具账本规则。 | 保留。 |
| Plugin: Browser | 是 | 是 | 失败 | 按 Browser skill 接入步骤调用失败，缺 `sandboxPolicy` 字段。 | 修复或复查 Browser 运行时。 |
| Plugin: Computer Use | 是 | 是 | 强 | `list_apps` 和 `get_app_state Google Chrome` 成功。 | 作为图形界面验收降级路径。 |
| Plugin: Chrome | 中 | 否 | 弱 | Chrome 页面被 Computer Use 读取，但 Chrome 插件未直接调用。 | 登录态页面场景再补跑。 |
| Plugin: Record & Replay | 低 | 否 | 弱 | 本案例没有用户演示录制需求。 | 用户演示流程时再用。 |
| Plugin: Documents | 低 | 否 | 弱 | 本案例没有 DOCX 或长文档产物。 | 文档产物案例再用。 |
| Plugin: PDF | 低 | 否 | 弱 | 本案例没有 PDF 产物。 | PDF 导出或验收时再用。 |
| Plugin: Spreadsheets | 低 | 否 | 弱 | 本案例没有表格数据产物。 | 反馈统计或数据分析时再用。 |
| Plugin: Presentations | 低 | 否 | 弱 | 本案例没有演示文稿产物。 | 做 deck 时再用。 |
| MCP: Node REPL | 是 | 是 | 失败 | Browser 插件必须通过 Node REPL 调用，但当前 Browser 连接失败。 | 记录错误并修复环境。 |
| MCP: Computer Use | 是 | 是 | 强 | 本机应用和 Chrome 窗口状态可读。 | 保留为验证工具。 |
| last30days | 低 | 否 | 弱 | 本案例不判断最近 30 天市场讨论。 | 进入外部需求判断时再用。 |
| Git / GitHub CLI | 中 | 待补 | 弱 | Computer Use 只能看到页面，提交级状态应由 Git 确认。 | 提交前用 Git 校验。 |

## 阶段能力计划

| 阶段 | 候选 Codex 插件 | 是否使用 | 结果质量 | 跳过或失败原因 | 下一步 |
| --- | --- | --- | --- | --- | --- |
| signal | Browser / Chrome / Record & Replay | 使用 Browser 作为候选 | 失败 | Browser 连接缺 `sandboxPolicy` | 记录为信号：能力矩阵不等于真实可用 |
| research | Browser / Chrome / Documents / PDF / Spreadsheets / Data Visualization | 使用 Browser、Computer Use | 中 | Browser 失败，Computer Use 成功 | 形成插件调用证据 |
| debate | Browser / Chrome / Documents / PDF | 未额外调用 | 中 | 反方基于已取得的一手工具输出足够 | 后续补 Browser 成功路径 |
| validation | Browser / Computer Use / Documents / PDF / Spreadsheets / Presentations | 使用 Browser、Computer Use | 中 | Browser blocked，Computer Use 降级路径可用 | 补报告索引页面验收 |
| artifact | Documents / PDF / Spreadsheets / Presentations / HyperFrames / Data Visualization | 未使用 | 弱 | 本轮产物是 Markdown 和文档更新 | 对非 Markdown 产物再接入 |
| publication | Browser / Chrome | Computer Use 读取 Chrome 页面 | 中 | 没有执行发布动作 | 用 Git/GitHub CLI 确认远程状态 |
| feedback | Chrome / Browser / Spreadsheets / Record & Replay | 未使用 | 弱 | 真实反馈为空 | 等外部反馈出现后再用 |
| asset | Documents / PDF / Spreadsheets / Presentations / Record & Replay / Browser | 未使用 | 中 | 资产是流程模板，不需要格式插件 | 后续做资料包时再接入 |
| flow-review | Browser / Computer Use / Documents / PDF / Spreadsheets / Presentations | 使用 Computer Use | 中 | Browser blocked | 下次优先修复 Browser |

## 工具结果质量结论

- 强：Computer Use 读取本机应用和 Chrome 状态。
- 中：能力矩阵和 Chrome 可见页面。
- 弱：未直接调用 Chrome 插件、Documents、PDF、Spreadsheets、Presentations。
- 失败：Browser 插件真实调用。

本账本足够支持内部流程优化，不足以支持外部需求判断。

## 过程日志

---
type: process_log
title: Codex 插件实际调用流程验证
status: completed
updated_at: 2026-06-20
gate: passed
---



## 迭代 1：确认能力矩阵

命令 / Command：

```bash
python3 scripts/signalproof.py capabilities
```

结果：

- 发现 Browser、Chrome、Computer Use、Record & Replay、Documents、PDF、Spreadsheets、Presentations、Data Visualization、HyperFrames 等候选插件。
- 生成 `vault/runs/2026-06-20-codex-capability-matrix.md`。

自检 / Self-check：

- 能力矩阵只能证明插件可发现，不能证明真实调用可用。

优化 / Optimization：

- 下一步必须至少选一个插件做实际调用，并把失败也写入账本。

## 迭代 2：尝试 Browser 插件真实调用

命令 / Command：

```js
const { setupBrowserRuntime } = await import('/Users/rust/.codex/plugins/cache/openai-bundled/browser/26.616.41845/scripts/browser-client.mjs');
await setupBrowserRuntime({ globals: globalThis });
globalThis.browser = await agent.browsers.get('iab');
nodeRepl.write(await browser.documentation());
```

结果：

```text
Mcp error: -32602: js: codex/sandbox-state-meta: missing field `sandboxPolicy`
```

自检 / Self-check：

- Browser 插件已经实际调用，但当前环境接入失败。
- 失败不能被隐藏，也不能用 Computer Use 成功覆盖掉。

优化 / Optimization：

- 在 `tool-ledger.md` 标为失败，并把 Browser 修复列为下一步。

## 迭代 3：调用 Computer Use 插件

命令 / Command：

```text
mcp__computer_use.list_apps({})
mcp__computer_use.get_app_state({"app":"Google Chrome"})
```

结果：

- `list_apps` 成功，返回本机运行应用列表。
- `get_app_state` 成功，读取到 Google Chrome 当前窗口。
- Chrome 窗口标题为 `sunny-kobe/SignalProof: SignalProof：Codex 优先的个人信号到资产证明协议`。
- 地址栏值为 `github.com/sunny-kobe/SignalProof`。

自检 / Self-check：

- Computer Use 可作为本机图形界面验收的降级路径。
- 这不是 Chrome 插件直接调用，也不是 DOM 级 Browser 验收。

优化 / Optimization：

- 在流程文档中补充“先记录失败，再选择降级路径”的规则。

## 迭代 4：写入案例和文档

命令 / Command：

```bash
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py export-all
python3 scripts/signalproof.py check-goal --min-cases 6
```

结果：

- `check-all` 通过，6 个案例全部通过。
- `export-all` 重新生成 6 份报告和报告索引。
- `check-goal --min-cases 6` 通过，报告索引路径为 `vault/reports/index.html`。

自检 / Self-check：

- 新案例必须包含 13 个必需文件。
- `feedback.md` 必须写明真实反馈为空。
- `tool-ledger.md` 必须包含 Skill、Plugin、MCP、Browser、Computer Use、Chrome、Documents、PDF、Spreadsheets、Presentations 和结果质量。
- 本轮上述条件已满足。

优化 / Optimization：

- 如果校验失败，优先修正案例结构和边界语言，不扩大功能范围。
