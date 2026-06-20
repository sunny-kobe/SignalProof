# SignalProof 案例报告：2026-06-20-research-tool-coverage-gap

## 信号

---
type: signal
title: 研究工具覆盖和结果质量缺口
status: captured
updated_at: 2026-06-20
gate: passed
---



## 原始信号

一个案例即使用了研究工具，也可能只得到弱证据，所以 SignalProof 需要结果质量门。

## 为什么值得进入流程

- 这是一个真实 SignalProof 工作流问题。
- 它能检验协议是否能从信号推进到资产。

## 当前边界

- 真实外部反馈和发布渠道本轮跳过。
- 本 case 只能证明内部协议能力。

## 研究

---
type: research
title: 研究工具覆盖和结果质量缺口
status: completed
updated_at: 2026-06-20
gate: weak
---



## 研究结论

新的 last30days 运行暴露了典型失败模式：planner/rerank 因 HTTP 402 回退，Reddit 只有 2 条弱命中，X/YouTube/HN/GitHub 都是 0。diagnose 显示来源可用，但来源可用不等于结果有用。

## 证据强度

- 内部流程证据：中到强。
- 外部市场证据：弱或为空。

## 证据缺口

- 真实用户原话为空。
- 真实发布反馈为空。
- 真实 before/after 为空。

## 辩论

---
type: debate
title: 研究工具覆盖和结果质量缺口
status: completed
updated_at: 2026-06-20
gate: passed
---



## 正反方结论

正方很清楚：质量账本能阻止虚假信心。反方是：过多记录可能拖慢轻量探索。

## 最强反对意见

内部协议跑通不等于外部需求成立。

## 收窄后判断

继续内部验证，不进入市场验证结论。

## 判断

---
type: thesis
title: 研究工具覆盖和结果质量缺口
status: accepted
updated_at: 2026-06-20
gate: passed
---



## 当前判断

继续。工具质量判断是 SignalProof 的核心能力，不是可选文书工作。

## 成功标准

- 全部阶段文件存在。
- 工具账本记录结果质量。
- 流程日志记录迭代和优化。
- 自检脚本通过。

## 验证计划

---
type: validation
title: 研究工具覆盖和结果质量缺口
status: planned
updated_at: 2026-06-20
gate: passed
---



## 验证方式

把 `tool-ledger.md` 设为必需文件，并检查它覆盖 last30days、Browser、Computer Use、Skill、Plugin、MCP 和工具结果质量。

## 命令

```bash
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py export-all
python3 scripts/signalproof.py check-goal --min-cases 5
```

## 产物

---
type: artifact
title: 研究工具覆盖和结果质量缺口
status: created
updated_at: 2026-06-20
gate: passed
---



## 产物内容

脚本现在会提醒过薄的工具账本，`check-goal` 要求出现优化记录。

## 产物边界

该产物是内部协议验证，不是外部市场验证。

## 反馈

---
type: feedback
title: 研究工具覆盖和结果质量缺口
status: skipped-real-feedback
updated_at: 2026-06-20
gate: weak
---



## 当前反馈状态

真实反馈为空。

## 内部反馈

- 本 case 用脚本自检和流程审计替代外部反馈。
- 这只适合内部协议迭代。

## 不能得出的结论

- 不能写验证成功。
- 不能声称市场已验证。
- 不能声称用户需要这个产品。

## 决策

---
type: decision
title: 研究工具覆盖和结果质量缺口
status: accepted-internal
updated_at: 2026-06-20
gate: passed
---



## 决策

继续内部协议验证。

## 理由

继续。工具质量判断是 SignalProof 的核心能力，不是可选文书工作。

## 边界

真实反馈为空，不能声称验证成功。

## 资产

---
type: asset
title: 研究工具覆盖和结果质量缺口
status: reusable-internal
updated_at: 2026-06-20
gate: passed
---



## 复用资产

可复用资产：研究质量账本模式。

## 如何复用

- 作为后续 SignalProof 案例的模板或规则来源。
- 作为脚本、skill、plugin 迭代的证据。

## 边界

不能替代真实外部反馈。

## 流程自检

---
type: flow_review
title: 研究工具覆盖和结果质量缺口
status: completed
updated_at: 2026-06-20
gate: passed
---



## 阶段完整性

| 阶段 | 状态 | 说明 |
| --- | --- | --- |
| signal | passed | 真实流程信号已记录。 |
| research | weak | 有内部证据，外部证据不足。 |
| debate | passed | 已写最强反对意见。 |
| thesis | passed | 已限定为内部继续。 |
| validation | passed | 已绑定脚本检查。 |
| artifact | passed | 已生成可复用产物。 |
| feedback | weak | 真实反馈为空。 |
| decision | passed | 未声称验证成功。 |
| asset | passed | 已沉淀内部资产。 |

## 优化空间

新增按阶段预设的候选能力：研究、产物验收、发布、反馈、决策。

## 过度声称检查

未把 synthetic demo、假设反馈或内部流程反馈写成市场验证。

## 工具账本

---
type: tool_ledger
title: 研究工具覆盖和结果质量缺口
status: completed
updated_at: 2026-06-20
gate: passed
---



## 候选能力账本

| 能力 | 是否相关 | 是否使用 | 结果质量 | 说明 | 下次动作 |
| --- | --- | --- | --- | --- | --- |
| Skill: signalproof | 是 | 是 | 中 | repo 级 skill 约束本地案例。 | 保留。 |
| Skill: personal-opportunity-os | 是 | 是 | 中 | 上层个人机会 OS 方法论。 | 保留。 |
| Skill: last30days | 视主题而定 | 视主题而定 | 弱 | last30days diagnose：用于可用性判断时强；last30days research run：用于市场证据时弱；脚本自检：强。 | 真实趋势判断时补跑更窄查询。 |
| Browser | 视产物而定 | 待验证 | 中 | 适合验证报告索引或本地预览。 | 用文件预览检查报告页。 |
| Computer Use | 低到中 | 否 | 失败 | 插件文件存在，但当前没有直接控制工具暴露。 | 工具可用后再接入只能通过 GUI 操作的流程。 |
| Plugin | 是 | 是 | 中 | 已创建插件草案骨架。 | 后续安装测试。 |
| MCP | 中 | 否 | 弱 | 已映射能力，未绑定服务器。 | 按阶段接 OpenAI Docs / Context7 / GitHub。 |
| Hooks | 中 | 否 | 弱 | 可强制 case check。 | 后续加 pre-finish hook。 |
| Automation | 中 | 否 | 弱 | 可做 72 小时反馈复查。 | 等发布渠道恢复后启用。 |

## 工具结果质量结论

工具覆盖足够支持内部协议验证，不足以支持外部市场判断。

## 过程日志

---
type: process_log
title: 研究工具覆盖和结果质量缺口
status: completed
updated_at: 2026-06-20
gate: passed
---



## 迭代 1

命令：

```bash
python3 scripts/signalproof.py init-case "研究工具覆盖和结果质量缺口"
```

结果：

- 生成完整案例文件。

自检：

- 模板文件齐全。

优化：

- 发现模板案例过于相似，需要按主题 seed 差异化内容。

## 迭代 2

命令：

```bash
python3 scripts/seed_cases.py
python3 scripts/signalproof.py check-all
```

结果：

- 进入差异化案例校验。

自检：

- `tool-ledger.md` 覆盖 last30days、Browser、Computer Use、Skill、Plugin、MCP。

优化：

新增按阶段预设的候选能力：研究、产物验收、发布、反馈、决策。
