# SignalProof 案例报告：2026-06-21-插件试跑-case-2-signalproof-报告发布与验收

## 信号

---
type: signal
title: 插件试跑 case 2：SignalProof 报告发布与验收
case_type: plugin-trial
status: captured
created_at: 2026-06-21
gate: passed
---



## 原始信号

用验证类和发布类插件检查 SignalProof 报告/HTML/仓库入口是否更容易验收

## 为什么值得进入流程

- 这条信号可以检验 SignalProof 是否能把模糊想法推进为可判断资产。
- 本 case 会跳过真实外部反馈和发布渠道，只验证内部协议闭环。

## 初步用户

- 高频使用 Codex / Claude Code / MCP / 本地 AI coding 工作流的人。
- 想把机会判断沉淀为可复用个人资产的人。

## 当前边界

- 不声称市场验证。
- 不默认产品化。
- 不做 SaaS 或 dashboard。

## 研究

---
type: research
status: completed
updated_at: 2026-06-21
gate: weak
---



## 要回答的问题

- 验证类插件是否能让 SignalProof 报告、HTML 索引和本地页面验收更可靠？
- Browser、Computer Use、Record & Replay 在当前环境下是否能作为默认验收 gate？
- 如果 GUI/浏览器插件失败，SignalProof 是否有降级验收路线？

## 已确认事实

- Record & Replay 的 `event_stream_status` 可见，返回 `isRecording=false`，最大录制 1800 秒。
- Computer Use 调用 `get_app_state(app="Codex")` 失败，返回 macOS 错误 `-1743`。
- Browser 插件 setup 失败，错误为 `codex/sandbox-state-meta: missing field sandboxPolicy`。
- `vault/reports/index.html` 和插件评估 HTML 文件存在，可以走文件级检查，但不能写成 Browser 视觉验收通过。
- GitHub CLI 可读取仓库公开状态，适合验证发布入口；当前 GitHub issues 为空，不能作为外部反馈。

## 证据强度

| 能力 | 结果质量 | 说明 |
| --- | --- | --- |
| Record & Replay | 强 | 工具状态可读，适合后续把用户演示转为 Skill。 |
| GitHub CLI | 强 | 能读取公开仓库，适合发布入口和开源反馈检查。 |
| Browser | 失败 | 当前环境 setup 失败，不能作为硬性验收 gate。 |
| Computer Use | 失败 | 当前 macOS 权限或目标 App 状态读取失败，不能作为默认 gate。 |
| 文件级检查 | 中 | 能证明 HTML/报告文件存在，但不能证明浏览器渲染正常。 |

## 当前判断

验证类插件有价值，但当前默认策略应是：Record & Replay 默认候选；GitHub CLI 默认检查公开入口；Browser/Computer Use 先保持条件候选并提供降级路线。

## 辩论

---
type: debate
status: completed
updated_at: 2026-06-21
gate: passed
---



## 正方

- 该 case 能验证 SignalProof 的阶段文件、工具账本和流程自检是否可复用。
- 不依赖外部发布即可发现协议问题。
- 产物可以沉淀为模板、脚本或规则。

## 反方

- 没有真实外部反馈时，容易把内部顺畅误认为需求成立。
- 批量 case 可能变成形式主义。
- 如果工具账本只记录“用了什么”，没有判断质量，价值会很低。

## 最强反对意见

内部流程成功不等于真实市场成功。

## 收窄后的判断

继续，但只把结论限定为内部协议验证。

## 判断

---
type: thesis
status: accepted
updated_at: 2026-06-21
gate: passed
---



## 当前结论

继续内部验证。

## 最小切口

把信号跑成完整证明案例，并记录工具覆盖和流程优化。

## 不做清单

- 不做真实发布。
- 不做真实用户反馈收集。
- 不做 SaaS。
- 不做 Web dashboard。

## 成功标准

- 必需阶段文件完整。
- 工具覆盖账本完整。
- 流程日志能复盘每轮优化。
- 自检脚本通过。

## 放弃条件

- case 文件无法产生可复用规则。
- 自检发现反复过度声称。
- 工具账本无法帮助下一轮优化。

## 验证计划

---
type: validation
status: planned
updated_at: 2026-06-21
gate: passed
---



## 验证对象

验证报告发布与验收阶段是否应默认启用 Browser、Computer Use、Record & Replay、GitHub。

## 验证方式

1. 查询 Record & Replay 状态。
2. 尝试读取 Codex App 状态，记录 Computer Use 失败。
3. 尝试 Browser setup，记录失败。
4. 检查报告索引和 HTML 产物文件是否存在。
5. 用 GitHub CLI 检查仓库公开入口和 issue 反馈状态。
6. 把失败能力写成 `failed/tool`，而不是让流程卡死。

## 执行结果

- Record & Replay：通过，可作为资产化入口。
- GitHub CLI：通过，可作为公开入口检查。
- Browser：失败，不作为默认硬 gate。
- Computer Use：失败，不作为默认硬 gate。
- HTML/报告文件级检查：通过，但不等于浏览器渲染验收。

## 成功标准

- 验证插件失败时有明确降级路线。
- 不把文件存在写成浏览器视觉验收通过。
- 不把 GitHub issue 为空写成没有需求。

## 本轮 gate

`weak-to-medium`。流程可继续，但 Browser/Computer Use 不能进入默认验收 gate。

## 产物

---
type: artifact
status: created
updated_at: 2026-06-21
gate: passed
---



## 产物

本 case 的产物是报告/验收类插件的降级验收记录。

## 文件与入口

| 文件 | 状态 | 说明 |
| --- | --- | --- |
| `vault/reports/index.html` | 存在 | 报告索引，文件级可检查。 |
| `vault/reports/2026-06-21-codex-推荐插件真实试跑评估.md` | 存在 | 主评估报告。 |
| `vault/assets/plugin-test/visual/plugin-eval-summary.html` | 存在 | Data Visualization HTML 产物。 |
| `tool-ledger.md` | 已更新 | 记录 Browser/Computer Use/Record & Replay/GitHub 的真实结果。 |

## 产物边界

Browser 插件本轮失败，因此 HTML 只算文件级通过，不算浏览器级视觉验收通过。

## 反馈

---
type: feedback
status: skipped-real-feedback
updated_at: 2026-06-21
gate: weak
---



## 当前反馈状态

真实反馈为空。

## 为什么为空

用户明确要求本轮先跳过真实外部反馈和发布渠道。

## 内部反馈

- 通过 case 自检判断协议是否可运行。
- 通过流程自检记录优化空间。

## 不能得出的结论

- 不能写验证成功。
- 不能声称市场已验证。
- 不能声称用户需要这个产品。
- 不能进入 SaaS 化结论。

## 决策

---
type: decision
status: accepted-internal
decision: continue-internal-protocol-validation
updated_at: 2026-06-21
gate: passed
---



## 决策

继续内部协议验证。

## 理由

- 本轮目标是验证 SignalProof 流程和自动化，而不是市场。
- 真实反馈为空，因此只能做内部继续/收窄判断。

## 下一步

- 如果本 case 暴露流程缺口，把缺口写入 `flow-review.md`。
- 如果缺口可脚本化，更新 `scripts/signalproof.py`。

## 边界

真实反馈为空，不能声称验证成功。

## 资产

---
type: asset
status: reusable-internal
created_at: 2026-06-21
gate: passed
---



## 资产名称

SignalProof 报告/页面验收降级策略

## 资产类型

验证插件使用规则 + 失败降级路线。

## 可复用内容

- Record & Replay 可作为“用户演示 -> Skill”默认候选。
- GitHub CLI 可作为公开仓库入口和 issue 反馈检查。
- Browser/Computer Use 失败时，先用文件级检查、runtime inspect、导出图片或人工复核降级。
- 不能把“文件存在”写成“浏览器验收通过”。

## 可复用边界

只适用于当前环境。修复 Browser/Computer Use 权限后，需要重新跑视觉/GUI 验收。

## 流程自检

---
type: flow_review
status: completed
updated_at: 2026-06-21
case_stage: full-internal-loop
gate: passed
---



## 阶段完整性

| 阶段 | 状态 | 说明 |
| --- | --- | --- |
| signal | passed | 已记录原始信号。 |
| research | weak-to-medium | 已获得验证插件真实成功/失败状态。 |
| debate | passed | 已记录正反方。 |
| thesis | passed | 已明确继续内部验证。 |
| validation | weak-to-medium | Record & Replay/GitHub 可用；Browser/Computer Use 失败。 |
| artifact | passed | 已记录报告/HTML 文件级验收入口。 |
| feedback | weak | 真实反馈为空。 |
| decision | passed | 未过度声称。 |
| asset | passed | 已沉淀内部资产。 |

## 证据质量

- 强：Record & Replay 状态可读；GitHub CLI 可读取公开仓库。
- 中：报告/HTML 文件存在，可做文件级检查。
- 失败：Browser setup 与 Computer Use App 状态读取失败。
- 弱：真实发布反馈为空，GitHub issue 为空不能代表无需求。

## 过度声称检查

没有把真实反馈为空写成验证成功。

## 插件结论

验证类插件不能一刀切默认启用。Record & Replay 值得默认候选；Browser/Computer Use 当前只能作为条件能力，失败时不阻断 case，但必须写入账本。

## 优化空间

- 修复 Browser setup 后，补一次 `vault/reports/index.html` 截图验收。
- 修复 Computer Use 权限后，补一次本地 App 或浏览器窗口验收。
- 把“浏览器级通过”和“文件级通过”拆成两个 gate。

## 工具账本

---
type: tool_ledger
status: completed
updated_at: 2026-06-21
gate: passed
---



## 候选能力账本

| 能力 | 是否相关 | 是否使用 | 结果质量 | 说明 | 下次动作 |
| --- | --- | --- | --- | --- | --- |
| Skill: signalproof | 是 | 是 | 中 | repo 级 skill 提供本地流程规则。 | 保留。 |
| Skill: personal-opportunity-os | 是 | 是 | 中 | 提供长期方向和流程边界。 | 保留为上层方法论。 |
| Skill: last30days | 否 | 否 | not-needed | 本 case 不是趋势调研。 | 调研 case 1 已实际运行。 |
| Browser | 是 | 是 | 失败 | setup 报 `codex/sandbox-state-meta: missing field sandboxPolicy`，不能做浏览器级验收。 | 修复后补验收截图。 |
| Computer Use | 是 | 是 | 失败 | `get_app_state(app="Codex")` 返回 macOS 错误 `-1743`。 | 修权限或换目标 App 后再跑。 |
| Record & Replay | 是 | 是 | 强 | `event_stream_status` 可读，适合录制用户演示。 | 默认作为资产化候选。 |
| GitHub CLI | 是 | 是 | 强 | 可读取 `sunny-kobe/SignalProof` 和 issues；issues 当前为空。 | 默认用于公开入口和开源反馈检查。 |
| Plugin | 是 | 是 | 中 | 已建立插件草案骨架。 | 后续安装测试。 |
| MCP | 中 | 否 | 弱 | 可接 OpenAI Docs、Context7、GitHub 等，但本轮先记录映射。 | 后续按阶段接入。 |
| Hooks | 中 | 否 | 弱 | 可用于强制 check-case。 | 后续加入。 |
| Automation | 中 | 否 | 弱 | 可用于 72h 反馈复查。 | 等发布渠道恢复后启用。 |

## 阶段能力计划

运行：

```bash
python3 scripts/signalproof.py capabilities
```

然后把本 case 各阶段真正考虑过的 Codex 自带插件记录到这里：

| 阶段 | 候选 Codex 插件 | 是否使用 | 结果质量 | 跳过或失败原因 | 下一步 |
| --- | --- | --- | --- | --- | --- |
| signal | Browser / Chrome / Record & Replay | 部分 | 强 | Record & Replay 状态可读；未启动录制。 | 用户演示时再录。 |
| research | GitHub / Browser / Chrome | 部分 | 强 | GitHub CLI 可读公开仓库；Browser 失败。 | Browser 修复后补网页级检查。 |
| debate | Browser / Chrome / Documents / PDF | 否 | not-needed | 本 case 不依赖外部长文档。 | 保留为候选。 |
| validation | Browser / Computer Use / GitHub / 文件级检查 | 是 | weak-to-medium | GitHub/文件级通过；Browser/Computer Use 失败。 | 拆分文件级与浏览器级 gate。 |
| artifact | Data Visualization / Reports / Presentations | 部分 | 中 | HTML 文件存在，但未完成 Browser 渲染验收；演示类产物在 case 3 通过 Presentations 试跑。 | 产物类详见 case 3。 |
| publication | Browser / Chrome / GitHub | 部分 | 中 | GitHub 仓库可读；无真实发布操作。 | 发布时再启用。 |
| feedback | Chrome / Browser / GitHub / Spreadsheets | 部分 | 弱 | GitHub issues 为空；不能代表无需求。 | 有反馈后再统计。 |
| asset | Record & Replay / Browser | 部分 | 强 | Record & Replay 可作为演示录制资产入口。 | 后续录一次真实发布/反馈流程。 |
| flow-review | Browser / Computer Use / 文件级检查 | 是 | weak-to-medium | 失败能力已记录并提供降级路线。 | 修复后补跑。 |

## 能力结论

本 case 证明验证插件需要分层：Record & Replay/GitHub 可默认候选，Browser/Computer Use 当前只能条件启用并保留降级路线。

## 过程日志

---
type: process_log
status: completed
updated_at: 2026-06-21
gate: passed
---



## 迭代 1

命令：

```bash
python3 scripts/signalproof.py init-case "插件试跑 case 2：SignalProof 报告发布与验收"
```

结果：

- 生成完整 case 文件。

自检：

- 文件齐全。
- 真实反馈为空边界明确。

优化：

- 后续把重复检查脚本化。

## 迭代 2

命令：

```bash
mcp__event_stream.event_stream_status
mcp__computer_use.get_app_state(app="Codex")
mcp__node_repl.js 通过 Browser 插件 setup in-app Browser
gh repo view sunny-kobe/SignalProof --json nameWithOwner,url,isPrivate,stargazerCount,forkCount
gh issue list --repo sunny-kobe/SignalProof --limit 5 --json number,title,state,updatedAt
```

结果：

- Record & Replay 状态可读。
- Computer Use 失败：macOS 错误 `-1743`。
- Browser setup 失败：`codex/sandbox-state-meta: missing field sandboxPolicy`。
- GitHub CLI 读取公开仓库成功；issues 为空数组。

自检：

- 验证插件失败不能阻断整个 SignalProof case。
- GitHub issues 为空不能写成“无人需要”。
- HTML 文件存在只能证明文件级通过，不能证明浏览器渲染通过。

优化：

- 增加“文件级 gate / 浏览器级 gate / GUI gate”的区分。

## 迭代 3

命令：

```bash
python3 scripts/signalproof.py check-all
```

结果：

- 等待总自检统一运行。

自检：

- 本 case 已补齐 Browser、Computer Use、Record & Replay、GitHub 等结果质量。

优化：

- Browser/Computer Use 修复后补跑报告截图与 GUI 验收。
