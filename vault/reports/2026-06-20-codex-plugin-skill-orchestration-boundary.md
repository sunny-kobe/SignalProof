# SignalProof 案例报告：2026-06-20-codex-plugin-skill-orchestration-boundary

## 信号

---
type: signal
title: Codex 插件和 Skill 编排边界
status: captured
updated_at: 2026-06-20
gate: passed
---



## 原始信号

SignalProof 应该成为一个 Codex skill/plugin 包，用来协调其他能力，但不能假装自己能像代码 API 一样直接调用所有插件。

## 为什么值得进入流程

- 这是一个真实 SignalProof 工作流问题。
- 它能检验协议是否能从信号推进到资产。

## 当前边界

- 真实外部反馈和发布渠道本轮跳过。
- 本 case 只能证明内部协议能力。

## 研究

---
type: research
title: Codex 插件和 Skill 编排边界
status: completed
updated_at: 2026-06-20
gate: weak
---



## 研究结论

刷新后的 Codex 手册确认：Skill 是可复用工作流，Plugin 是分发单元，MCP 把模型连接到工具和上下文。Browser 和 Computer Use 是用于视觉或 GUI 验收的独立能力面。

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
title: Codex 插件和 Skill 编排边界
status: completed
updated_at: 2026-06-20
gate: passed
---



## 正反方结论

这支持 SignalProof 作为协议包存在。反对意见是过度自动化：太早把所有集成打包进去，会把项目拖成通用 agent 平台。

## 最强反对意见

内部协议跑通不等于外部需求成立。

## 收窄后判断

继续内部验证，不进入市场验证结论。

## 判断

---
type: thesis
title: Codex 插件和 Skill 编排边界
status: accepted
updated_at: 2026-06-20
gate: passed
---



## 当前判断

继续维护 repo 级 skill 和插件草案。MCP、hooks、automations 等先延后，等重复案例证明必要性再接入。

## 成功标准

- 全部阶段文件存在。
- 工具账本记录结果质量。
- 流程日志记录迭代和优化。
- 自检脚本通过。

## 验证计划

---
type: validation
title: Codex 插件和 Skill 编排边界
status: planned
updated_at: 2026-06-20
gate: passed
---



## 验证方式

通过创建 `.agents/skills/signalproof/`、`plugins/signalproof/.codex-plugin/plugin.json` 和 repo marketplace 入口来验证。

## 命令

```bash
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py export-all
python3 scripts/signalproof.py check-goal --min-cases 5
```

## 产物

---
type: artifact
title: Codex 插件和 Skill 编排边界
status: created
updated_at: 2026-06-20
gate: passed
---



## 产物内容

repo 级 skill 和本地插件草案包。

## 产物边界

该产物是内部协议验证，不是外部市场验证。

## 反馈

---
type: feedback
title: Codex 插件和 Skill 编排边界
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
title: Codex 插件和 Skill 编排边界
status: accepted-internal
updated_at: 2026-06-20
gate: passed
---



## 决策

继续内部协议验证。

## 理由

继续维护 repo 级 skill 和插件草案。MCP、hooks、automations 等先延后，等重复案例证明必要性再接入。

## 边界

真实反馈为空，不能声称验证成功。

## 资产

---
type: asset
title: Codex 插件和 Skill 编排边界
status: reusable-internal
updated_at: 2026-06-20
gate: passed
---



## 复用资产

可复用资产：Codex 能力地图和插件骨架。

## 如何复用

- 作为后续 SignalProof 案例的模板或规则来源。
- 作为脚本、skill、plugin 迭代的证据。

## 边界

不能替代真实外部反馈。

## 流程自检

---
type: flow_review
title: Codex 插件和 Skill 编排边界
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

下一版应测试本地插件安装，并判断是否用 hooks 在案例完成前强制 `check-all`。

## 过度声称检查

未把 synthetic demo、假设反馈或内部流程反馈写成市场验证。

## 工具账本

---
type: tool_ledger
title: Codex 插件和 Skill 编排边界
status: completed
updated_at: 2026-06-20
gate: passed
---



## 候选能力账本

| 能力 | 是否相关 | 是否使用 | 结果质量 | 说明 | 下次动作 |
| --- | --- | --- | --- | --- | --- |
| Skill: signalproof | 是 | 是 | 中 | repo 级 skill 约束本地案例。 | 保留。 |
| Skill: personal-opportunity-os | 是 | 是 | 中 | 上层个人机会 OS 方法论。 | 保留。 |
| Skill: last30days | 视主题而定 | 视主题而定 | 弱 | OpenAI Codex manual：强；本地插件骨架：中；MCP：已映射但未集成；Browser：候选；Computer Use：候选但当前没有直接工具暴露。 | 真实趋势判断时补跑更窄查询。 |
| Browser | 视产物而定 | 待验证 | 中 | 适合验证报告索引或本地预览。 | 用文件预览检查报告页。 |
| Computer Use | 低到中 | 否 | 失败 | 插件文件存在，但当前没有直接控制工具暴露。 | 工具可用后再接入只能通过 GUI 操作的流程。 |
| Plugin | 是 | 是 | 中 | 已创建插件草案骨架。 | 后续安装测试。 |
| MCP | 中 | 否 | 弱 | 已映射能力，未绑定服务器。 | 按阶段接 OpenAI Docs / Context7 / GitHub。 |
| Hooks | 中 | 否 | 弱 | 可强制 case check。 | 后续加 pre-finish hook。 |
| Automation | 中 | 否 | 弱 | 可做 72 小时反馈复查。 | 等发布渠道恢复后启用。 |

## 阶段能力计划

运行：

```bash
python3 scripts/signalproof.py capabilities
```

然后把本 case 各阶段真正考虑过的 Codex 自带插件记录到这里：

| 阶段 | 候选 Codex 插件 | 是否使用 | 结果质量 | 跳过或失败原因 | 下一步 |
| --- | --- | --- | --- | --- | --- |
| signal | Browser / Chrome / Record & Replay | 待定 | 待定 | 待定 | 待定 |
| research | Browser / Chrome / Documents / PDF / Spreadsheets / Data Visualization | 待定 | 待定 | 待定 | 待定 |
| debate | Browser / Chrome / Documents / PDF | 待定 | 待定 | 待定 | 待定 |
| validation | Browser / Computer Use / Documents / PDF / Spreadsheets / Presentations | 待定 | 待定 | 待定 | 待定 |
| artifact | Documents / PDF / Spreadsheets / Presentations / HyperFrames / Data Visualization | 待定 | 待定 | 待定 | 待定 |
| publication | Browser / Chrome | 待定 | 待定 | 待定 | 待定 |
| feedback | Chrome / Browser / Spreadsheets / Record & Replay | 待定 | 待定 | 待定 | 待定 |
| asset | Documents / PDF / Spreadsheets / Presentations / Record & Replay / Browser | 待定 | 待定 | 待定 | 待定 |
| flow-review | Browser / Computer Use / Documents / PDF / Spreadsheets / Presentations | 待定 | 待定 | 待定 | 待定 |

## 工具结果质量结论

工具覆盖足够支持内部协议验证，不足以支持外部市场判断。

## 过程日志

---
type: process_log
title: Codex 插件和 Skill 编排边界
status: completed
updated_at: 2026-06-20
gate: passed
---



## 迭代 1

命令：

```bash
python3 scripts/signalproof.py init-case "Codex 插件和 Skill 编排边界"
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

下一版应测试本地插件安装，并判断是否用 hooks 在案例完成前强制 `check-all`。
