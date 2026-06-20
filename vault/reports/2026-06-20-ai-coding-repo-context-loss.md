# SignalProof 案例报告：2026-06-20-ai-coding-repo-context-loss

## 信号

---
type: signal
title: AI 编码仓库上下文丢失
status: captured
updated_at: 2026-06-20
gate: passed
---



## 原始信号

AI 编码用户经常丢失仓库局部约定，导致 agent 写出看起来合理、但违反本地契约的代码。

## 为什么值得进入流程

- 这是一个真实 SignalProof 工作流问题。
- 它能检验协议是否能从信号推进到资产。

## 当前边界

- 真实外部反馈和发布渠道本轮跳过。
- 本 case 只能证明内部协议能力。

## 研究

---
type: research
title: AI 编码仓库上下文丢失
status: completed
updated_at: 2026-06-20
gate: weak
---



## 研究结论

一次真实的 `last30days --days=3 --quick --auto-resolve` 只找到 2 条 Reddit 讨论，X、YouTube、HN、GitHub、Polymarket 都没有有效命中。这个结果可以作为弱证据和工具质量样本，不能作为市场证明。

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
title: AI 编码仓库上下文丢失
status: completed
updated_at: 2026-06-20
gate: passed
---



## 正反方结论

这是一个很贴合用户个人 AI 编码经验的工作流切口。最强反对意见是：公开讨论证据很薄，可能只是小圈层工作流话题，不代表广泛买方意图。

## 最强反对意见

内部协议跑通不等于外部需求成立。

## 收窄后判断

继续内部验证，不进入市场验证结论。

## 判断

---
type: thesis
title: AI 编码仓库上下文丢失
status: accepted
updated_at: 2026-06-20
gate: passed
---



## 当前判断

继续作为内部证明案例和可复用检查清单方向推进。没有真实前后对比任务前，不声称需求成立、不产品化、不销售。

## 成功标准

- 全部阶段文件存在。
- 工具账本记录结果质量。
- 流程日志记录迭代和优化。
- 自检脚本通过。

## 验证计划

---
type: validation
title: AI 编码仓库上下文丢失
status: planned
updated_at: 2026-06-20
gate: passed
---



## 验证方式

通过迁移 legacy run、保留仓库上下文审计资产、检查报告导出，并把弱 last30days 结果保存为研究证据来验证。

## 命令

```bash
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py export-all
python3 scripts/signalproof.py check-goal --min-cases 5
```

## 产物

---
type: artifact
title: AI 编码仓库上下文丢失
status: created
updated_at: 2026-06-20
gate: passed
---



## 产物内容

legacy 跑法已迁移到 `legacy/`；新的正式 case 已沉淀在 `vault/cases/2026-06-20-ai-coding-repo-context-loss/`。

## 产物边界

该产物是内部协议验证，不是外部市场验证。

## 反馈

---
type: feedback
title: AI 编码仓库上下文丢失
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
title: AI 编码仓库上下文丢失
status: accepted-internal
updated_at: 2026-06-20
gate: passed
---



## 决策

继续内部协议验证。

## 理由

继续作为内部证明案例和可复用检查清单方向推进。没有真实前后对比任务前，不声称需求成立、不产品化、不销售。

## 边界

真实反馈为空，不能声称验证成功。

## 资产

---
type: asset
title: AI 编码仓库上下文丢失
status: reusable-internal
updated_at: 2026-06-20
gate: passed
---



## 复用资产

可复用资产：仓库上下文审计检查清单、AGENTS 模板、CLAUDE 模板、72 小时验证 SOP，以及一个弱证据研究样例。

## 如何复用

- 作为后续 SignalProof 案例的模板或规则来源。
- 作为脚本、skill、plugin 迭代的证据。

## 边界

不能替代真实外部反馈。

## 流程自检

---
type: flow_review
title: AI 编码仓库上下文丢失
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

下一轮应使用更窄查询，例如 `repo AGENTS.md context drift`、`Claude Code project instructions`、`AI coding agent verifiable workflow`，并把窗口扩到 `--days=7`。

## 过度声称检查

未把 synthetic demo、假设反馈或内部流程反馈写成市场验证。

## 工具账本

---
type: tool_ledger
title: AI 编码仓库上下文丢失
status: completed
updated_at: 2026-06-20
gate: passed
---



## 候选能力账本

| 能力 | 是否相关 | 是否使用 | 结果质量 | 说明 | 下次动作 |
| --- | --- | --- | --- | --- | --- |
| Skill: signalproof | 是 | 是 | 中 | repo 级 skill 约束本地案例。 | 保留。 |
| Skill: personal-opportunity-os | 是 | 是 | 中 | 上层个人机会 OS 方法论。 | 保留。 |
| Skill: last30days | 视主题而定 | 视主题而定 | 弱 | `last30days`：弱但有用；Codex 官方手册：中；本地脚本：强；Browser：待验证报告预览；Computer Use：当前没有直接工具暴露。 | 真实趋势判断时补跑更窄查询。 |
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
title: AI 编码仓库上下文丢失
status: completed
updated_at: 2026-06-20
gate: passed
---



## 迭代 1

命令：

```bash
python3 scripts/signalproof.py init-case "AI 编码仓库上下文丢失"
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

下一轮应使用更窄查询，例如 `repo AGENTS.md context drift`、`Claude Code project instructions`、`AI coding agent verifiable workflow`，并把窗口扩到 `--days=7`。
