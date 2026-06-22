# SignalProof 案例报告：2026-06-21-插件试跑-case-1-ai-coding-repo-context-loss-调研验证

## 0. 决策先行

- case_mode：`full`
- 信号：用调研类插件验证 AI coding repo context loss 是否仍是值得进入 SignalProof 的信号
- 决策：继续内部协议验证。
- 证据等级：| 维度 | 结论 |
| 来源覆盖 | 弱到中。GitHub/Reddit/YouTube 有结果，但 X/HN 缺失。 |
| 相关性 | 中。部分命中 repo context 和 memory，部分为泛 AI coding 噪音。 |
| 用户原话 | 中。Reddit 有原话，但样本少。 |
- 反馈状态：真实反馈为空。
- 可复用资产：`last30days` 调研插件试跑样本：AI coding repo context loss
- 下一步：- 如果本 case 暴露流程缺口，把缺口写入 `flow-review.md`。
- 如果缺口可脚本化，更新 `scripts/signalproof.py`。
- 边界：full case 只证明本轮已覆盖完整 SignalProof 记录；真实反馈为空时仍不能写成市场验证。

## 1. 详细记录

## 信号

---
type: signal
title: 插件试跑 case 1：AI coding repo context loss 调研验证
case_type: plugin-trial
status: captured
created_at: 2026-06-21
gate: passed
---



## 原始信号

用调研类插件验证 AI coding repo context loss 是否仍是值得进入 SignalProof 的信号

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

- `last30days` 作为调研类能力，能否给 AI coding repo context loss 这类信号补到最近 30 天的真实讨论？
- 这些讨论来自哪些渠道，强度够不够改变 SignalProof 对该方向的判断？
- 调研类插件失败、额度和来源缺口应该如何进入工具账本？

## 实际调研命令

```bash
python3.14 /Users/rust/.agents/skills/last30days/scripts/last30days.py "AI coding repo context loss" --emit=compact --auto-resolve --save-dir="/Users/rust/Documents/SignalProof/vault/cases/2026-06-21-插件试跑-case-1-ai-coding-repo-context-loss-调研验证/evidence" --save-suffix=plugintrial
```

输出文件：

`evidence/ai-coding-repo-context-loss-raw-plugintrial.md`

## 已确认事实

- `last30days` 成功运行，耗时约 67 秒。
- 共得到 13 条证据，覆盖 3 类来源：Reddit 6 条、YouTube 3 条、GitHub 4 条。
- 相关方向包括：AI coding agent 的阶段 gate、repo context/memory、Claude Code memory/knowledge graph、重复解释项目结构、上下文成本等。
- 工具也明确暴露了来源缺口：X 为 0，Hacker News 为 0，TikTok/Instagram/Threads/Perplexity 为 0。
- 运行过程中出现降级：X `CreditsDepleted`、Reddit public API 403 后 fallback、YouTube comments HTTP 402、LLM planning/reranking 402 fallback。

## 有价值命中

- Reddit `r/ClaudeWorkflows` 出现“verifiable phases and gates”相关讨论，和 SignalProof 的证据门、阶段门高度相关。
- Reddit `r/PromptEngineering` 出现 second brain / MCP / context memory 讨论，说明“AI coding 上下文需要结构化外部记忆”不是凭空想象。
- YouTube 出现 Claude Code repo knowledge graph / memory problem 内容，说明 repo context 仍是传播热点。
- Reddit `r/buildinpublic` 出现“每次会话重复解释项目结构”的痛点，和 repo context loss 更贴近。

## 证据质量

| 维度 | 结论 |
| --- | --- |
| 来源覆盖 | 弱到中。GitHub/Reddit/YouTube 有结果，但 X/HN 缺失。 |
| 相关性 | 中。部分命中 repo context 和 memory，部分为泛 AI coding 噪音。 |
| 用户原话 | 中。Reddit 有原话，但样本少。 |
| 决策影响 | 中。支持继续内部验证，不支持对外声称需求成立。 |

## 证据缺口

- X 缺失不是反证，而是额度阻塞。
- YouTube 评论缺失，无法判断真实观众反馈质量。
- Hacker News 为 0，不能证明开发者社区完全没有讨论。
- 结果里大量 `entity-miss demotion`，说明 query 还不够窄。
- 没有真实目标用户愿意提交 repo 或失败任务。

## 当前判断

`last30days` 对调研阶段有明显提升，适合作为 SignalProof 真实趋势 case 的默认候选能力。但本次结果只能支撑“继续低成本验证/收窄 query”，不能支撑产品化、SaaS 化或市场验证成功。

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

验证 `last30days` 能否作为 SignalProof 调研阶段的默认候选插件能力。

## 验证方式

1. 用 `python3.14` 实际运行 `last30days`，并保存原始输出。
2. 统计来源覆盖、命中数量、失败来源和降级路径。
3. 判断工具结果是强、中、弱还是失败。
4. 把结论写入 `research.md`、`tool-ledger.md` 和 `flow-review.md`。
5. 运行 `python3 scripts/signalproof.py check-all` 与 `export-all`。

## 执行结果

- 已生成原始证据文件：`evidence/ai-coding-repo-context-loss-raw-plugintrial.md`。
- 覆盖 13 条证据，来源为 GitHub、Reddit、YouTube。
- X、HN、短视频等关键来源缺失或为 0。
- 结论为“调研初筛有用，但证据强度不足以验证市场”。

## 成功标准

- 有真实工具输出，而不是只写“候选”。
- 明确记录来源缺口和失败原因。
- 不把弱证据写成市场验证。

## 本轮 gate

`weak`。可以继续内部验证和更窄 query 补跑，不能进入产品化判断。

## 产物

---
type: artifact
status: created
updated_at: 2026-06-21
gate: passed
---



## 产物

本 case 的核心产物是一次真实 `last30days` 调研试跑记录，以及对应的 SignalProof 工具质量判断。

## 文件

| 文件 | 用途 |
| --- | --- |
| `evidence/ai-coding-repo-context-loss-raw-plugintrial.md` | `last30days` 原始调研输出 |
| `research.md` | 来源覆盖、证据强度和缺口判断 |
| `tool-ledger.md` | 调研类插件实际调用账本 |
| `flow-review.md` | 记录该工具是否应默认进入调研阶段 |
| `report.md` | 给用户看的 case 摘要 |

## 产物边界

这是调研插件试跑产物，不是市场验证产物。它证明 `last30days` 可以增强调研初筛，也证明来源缺口必须被显式记录。

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

`last30days` 调研插件试跑样本：AI coding repo context loss

## 资产类型

调研工具质量样本 + 来源缺口记录。

## 可复用内容

- 真实运行命令和保存目录。
- 来源覆盖统计：GitHub、Reddit、YouTube 有结果，X/HN 等缺失。
- 工具失败口径：额度、403、402、fallback 不能当作 0 结果。
- 决策边界：弱到中证据只能支持继续验证，不能支持产品化。

## 可复用边界

可复用于后续“最近 30 天真实讨论”类 case 的调研账本；不可复用为市场需求已验证的证据。

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
| research | weak | `last30days` 有真实外部来源，但覆盖缺口明显。 |
| debate | passed | 已记录正反方。 |
| thesis | passed | 已明确继续内部验证。 |
| validation | passed | 已定义自检方式。 |
| artifact | passed | 已保存 `last30days` 原始输出和中文判断。 |
| feedback | weak | 真实反馈为空。 |
| decision | passed | 未过度声称。 |
| asset | passed | 已沉淀内部资产。 |

## 证据质量

- 中：Reddit/YouTube/GitHub 有真实命中，能提示方向和痛点。
- 弱：X/HN/短视频缺失，且多条结果是泛 AI coding 噪音。
- 失败/阻塞：X 额度耗尽、YouTube 评论 402、Reddit public API 403 fallback。

## 过度声称检查

没有把真实反馈为空写成验证成功。

## 插件结论

`last30days` 应进入 SignalProof 调研阶段默认候选，但必须加质量门：来源不足、query 跑偏或关键渠道失败时，只能写 `weak`，不能推进到“已验证需求”。

## 优化空间

- 下一轮用更窄 query 补跑，例如 `AI coding agent ignores repo instructions`、`Claude Code project context stale`。
- 对 X/HN 缺失单独走 GitHub/HN/RSS 或浏览器补查，而不是把缺失当作没人讨论。
- 如果出现具体候选项目，再用 GitHub、Hugging Face 或官方文档做项目级验证。

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
| Skill: last30days | 是 | 是 | 中 | 实际运行，得到 13 条证据，覆盖 GitHub/Reddit/YouTube；X/HN 缺失。 | 默认候选，但必须记录来源缺口。 |
| Browser | 低 | 否 | 未使用 | 本 case 是调研输出，不需要页面验收；主 case 已记录 Browser setup 失败。 | 有公开页面或报告预览时再用。 |
| Computer Use | 低 | 否 | 未使用 | 本 case 不需要 GUI；主 case 已记录 Codex App 状态读取失败。 | GUI-only 验证时再用。 |
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
| signal | Browser / Chrome / Record & Replay | 否 | not-needed | 信号来自用户要求和本地 case，不依赖网页或录制。 | 保留为候选。 |
| research | last30days / GitHub / Browser / Chrome | 是 | 中 | `last30days` 成功；X/HN/YouTube 评论有缺口。 | 更窄 query 补跑。 |
| debate | Browser / Chrome / Documents / PDF | 否 | not-needed | 本轮争论点来自调研输出，不需要长文档反证。 | 论文或长文档 case 再启用。 |
| validation | Browser / Computer Use / Spreadsheets | 部分 | weak | 以原始输出文件和脚本自检验收；未用 GUI。 | 总 case 继续记录 Browser/Computer Use 失败。 |
| artifact | Documents / PDF / Spreadsheets / Presentations / HyperFrames / Data Visualization | 否 | not-needed | 本 case 产物是 Markdown 和原始调研文件。 | 产物类见 case 3。 |
| publication | Browser / Chrome | 否 | not-needed | 未发布。 | 发布阶段再启用。 |
| feedback | Chrome / Browser / Spreadsheets / Record & Replay | 否 | not-needed | 真实反馈为空。 | 有反馈源再启用。 |
| asset | Record & Replay / Spreadsheets / Documents | 否 | not-needed | 本资产是调研记录，不需要录制或表格。 | 可汇入总插件矩阵。 |
| flow-review | Browser / Computer Use / Documents / PDF / Spreadsheets / Presentations | 部分 | 中 | 通过文件级检查和后续 `check-all` 验证。 | 保留降级验收路径。 |

## 能力结论

本 case 证明 `last30days` 对调研初筛有价值，但当前结果为弱到中证据，不能支持外部市场判断。

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
python3 scripts/signalproof.py init-case "插件试跑 case 1：AI coding repo context loss 调研验证"
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
python3.14 /Users/rust/.agents/skills/last30days/scripts/last30days.py "AI coding repo context loss" --emit=compact --auto-resolve --save-dir="/Users/rust/Documents/SignalProof/vault/cases/2026-06-21-插件试跑-case-1-ai-coding-repo-context-loss-调研验证/evidence" --save-suffix=plugintrial
```

结果：

- 运行成功，保存 `evidence/ai-coding-repo-context-loss-raw-plugintrial.md`。
- 得到 13 条证据：Reddit 6 条、YouTube 3 条、GitHub 4 条。
- X 为 0，Hacker News 为 0，YouTube 评论和部分 LLM rerank 降级。

自检：

- `last30days` 是真实调用，不再写“待定”。
- 输出存在明显来源缺口，gate 必须保持 `weak`。

优化：

- 后续 query 要更窄，并把额度/403/402 写成阻塞而不是反证。

## 迭代 3

命令：

```bash
python3 scripts/signalproof.py check-all
```

结果：

- 等待总自检统一运行。

自检：

- 本 case 已补齐 Skill、Plugin、MCP、Browser、Computer Use、last30days 等账本关键词。

优化：

- 把 `last30days` 质量门写回主 case 和插件审计文档。
