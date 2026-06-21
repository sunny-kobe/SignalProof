# SignalProof 案例报告：2026-06-21-signalproof-当前工作流自审

## 信号

---
type: signal
title: SignalProof 当前工作流自审
case_type: internal-workflow-audit
status: captured
created_at: 2026-06-21
gate: passed
---



## 原始信号

用户提出：“现在能反过头利用已经封装好的工作流去对当前工作流进行一个审视不？”

这条信号不是一个外部市场机会，而是一次内部协议自审：把当前 SignalProof / Codex 插件工作流本身当成 case，按已经固化的流程跑一遍，检验它是否能发现自己的缺口。

## 为什么值得进入流程

- SignalProof 当前已经有 repo skill、AGENTS.md、协议文档、插件流程文档、插件锁定清单、重装脚本和确定性检查脚本。
- 如果这套流程不能审视自身，就说明它还只是文档集合，不是可执行的工作流。
- 自审可以暴露三类问题：流程缺口、插件调用和证据质量之间的错位、迁移和授权边界是否被误判。

## 初步对象

- 当前仓库：`/Users/rust/Documents/SignalProof`
- 当前工作流：SignalProof case 生命周期、Codex 插件接入流程、研究质量门、插件迁移和状态快照。
- 当前使用者：用户本人和 Codex 执行线程。

## 当前边界

- 本 case 只证明内部流程是否可审计，不证明市场需求。
- 真实反馈可以为空，但必须明确写出。
- 不把插件已安装写成证据合格。
- 不把内部流程反馈写成外部用户验证。
- 不把 SignalProof 改成 Web App、SaaS dashboard、workflow builder 或通用知识库。

## 本轮要回答的问题

1. 当前工作流能否发现自己的缺漏？
2. `AGENTS.md`、repo skill、docs、templates、scripts 和 vault 是否一致？
3. 插件状态、插件使用流程和迁移说明是否能防止换机器后的漂移？
4. 哪些地方仍然依赖人工判断，应该进入下一轮自动检查？

## 研究

---
type: research
status: completed
updated_at: 2026-06-21
gate: medium
---



## 研究问题

本轮研究不是判断外部市场是否需要 SignalProof，而是判断当前封装好的 SignalProof 工作流能否对自己做一次有效审视。

核心问题：

- 现有流程是否已经从“文档说明”变成“可执行检查”？
- 插件安装、插件暴露、账号授权和证据质量是否被分层处理？
- 当前脚本能发现哪些缺口，发现不了哪些缺口？
- 自审结果允许什么结论，不允许什么结论？

## 已确认事实

- `AGENTS.md` 明确本仓库是本地优先 SignalProof 协议 MVP，事实来源是 `vault/` Markdown 和 `scripts/` 确定性检查。
- repo skill `.agents/skills/signalproof/SKILL.md` 要求每个 case 包含 13 个必需文件，并记录工具结果质量。
- `docs/protocol.md` 把 SignalProof 定位为 Codex 协议和未来插件包，不是独立 App。
- `docs/research-quality-gate.md` 已要求记录来源覆盖、交叉验证、反证和替代方案、证据等级、结论许可和用户授权缺口。
- `docs/codex-plugin-flow.md` 已明确插件不是默认全跑，而是按阶段目标选择。
- `docs/codex-plugin-status-and-migration.md` 已区分插件安装、界面可见、connector 授权和迁移边界。
- `python3 scripts/signalproof.py diagnose` 可生成本机能力诊断。
- `python3 scripts/signalproof.py capabilities` 可生成阶段到 Codex 插件的能力矩阵。
- `python3 scripts/signalproof.py plugin-status` 可生成当天插件状态快照。
- `python3 scripts/signalproof.py check-all` 当前检查 11 个旧 case，failures 为 0，但多个旧 case 有研究质量门 warning。
- `python3 scripts/signalproof.py check-goal --min-cases 5` 当前通过，报告索引存在。
- `python3.14 /Users/rust/.agents/skills/last30days/scripts/last30days.py --diagnose` 显示 GitHub、ScrapeCreators、OpenRouter 可用，`bird_authenticated` 为 false，X 后端是 `xurl`，仍应视为 X 侧来源缺口。

## 来源覆盖表

| 来源类型 | 本轮来源 | 当前状态 | 结果质量 | 缺口 |
| --- | --- | --- | --- | --- |
| 公开讨论 | 用户当前问题、历史会话记忆中的插件审计口径 | 部分覆盖 | weak | 没有外部目标用户原话，不能支持市场判断。 |
| 项目和数据 | 仓库文件、case 数量、脚本检查结果、插件状态快照 | 已覆盖 | strong / medium | 能支持内部流程判断，但不能支持外部采用判断。 |
| 官方和一手资料 | AGENTS.md、repo skill、协议文档、Codex 插件流程文档、脚本输出 | 已覆盖 | strong | 官方 Codex 文档本轮没有重新联网复核，采用仓库内已记录的复核结论。 |
| 反证和替代方案 | `check-all` warnings、X 授权缺口、connector 未验证、插件安装不等于证据合格 | 已覆盖 | medium | 还缺一个自动 drift check 来强制 lock、安装脚本、状态快照三者一致。 |

## 交叉验证

- 谁在说：用户本人要求用已封装工作流反审当前工作流；仓库规则和脚本给出可执行约束。
- 说什么：当前流程需要从“能列插件”升级到“能按阶段判断插件是否有证据价值”。
- 在哪里说：当前 Codex 会话、`AGENTS.md`、`.agents/skills/signalproof/SKILL.md`、`docs/`、`scripts/signalproof.py`、`vault/runs/`。
- 有没有反证：有。旧 case 虽然通过结构检查，但仍有研究质量门 warning；这说明流程能发现历史缺口，但还没有把旧口径全部升级。
- 能支持什么结论：可以支持“继续使用当前流程，并把漂移检查作为下一轮优化”；不能支持“外部需求成立”或“流程已经无需人工判断”。

## 反证和替代方案

- 反证 1：`check-all` failures 为 0，但 warning 很多，说明结构完整不等于研究质量完全一致。
- 反证 2：`plugin-status` 能确认 36 个 marketplace 插件安装启用，但安装不等于外部账号授权，也不等于 connector 可以读取真实数据。
- 反证 3：`last30days` 诊断可用不等于所有来源可用，X / bird 侧仍有授权或额度缺口。
- 反证 4：本轮自审没有外部反馈，不能推出 SignalProof 对其他人有效。
- 替代方案：继续使用普通 Markdown 模板和人工复盘也能发现部分问题，但不如当前脚本和 case 结构稳定。

## 证据等级

当前证据等级：medium。

- strong：仓库内规则、必需文件、脚本输出、插件状态快照和目标检查，足以证明内部流程可执行。
- medium：插件迁移和能力矩阵已经形成闭环，但 connector 授权和真实数据源仍需按具体 case 探针。
- weak：外部市场反馈、目标用户原话、真实发布反馈和 X 侧实时讨论。
- blocked：本轮没有阻断项；X 侧不完整是来源缺口，不阻断内部自审。

## 结论许可

本轮允许的结论：

- 继续使用当前 SignalProof 工作流。
- 把当前状态标记为 `passed-with-gaps`。
- 下一轮补自动 drift check 和新 case 研究质量门硬约束。
- 对外部机会 case 仍必须重新做公开讨论、项目数据、官方资料和反证来源覆盖。

本轮不允许的结论：

- 已证明市场需求。
- 已证明插件 connector 都可读。
- 已证明所有旧 case 都满足新研究质量门。
- 可以产品化或 SaaS 化。

## 用户授权缺口

- X API credits 或 bird 授权仍不是完整状态。当前只标记为调研来源缺口，不作为本轮阻断。
- Readwise、Scite、Semrush、Similarweb、Brand24 等研究增强插件即使网页登录过，也仍需要在具体 case 中做只读探针。
- 浏览器、Chrome、Computer Use、Record & Replay 只有在网页、登录态、GUI 或流程录制会改变判断时才使用。

## 下一步补证

- 增加一个自动 drift check：比对 `docs/codex-plugin-lock.md`、`scripts/install-codex-plugins.sh`、`plugin-status` 快照和当前 `codex plugin list`。
- 对新 case 提高研究质量门：新建 case 不能只通过结构检查，还要减少关键 warning。
- 选择一个真实外部机会 case，补公开讨论、项目数据、官方资料和反证四类来源。
- 针对一个调研增强 connector 做只读探针，不一次性全跑所有插件。

## 辩论

---
type: debate
status: completed
updated_at: 2026-06-21
gate: passed
---



## 正方：当前工作流已经能自审

- case 必需文件已经固定，避免只写一个总结就结束。
- `diagnose`、`capabilities`、`plugin-status`、`check-all`、`check-goal` 和 `export-all` 能把能力、插件、结构、报告产物串起来。
- 插件流程文档明确区分“候选能力”和“实际证据”，避免默认全跑插件。
- 研究质量门已经把来源覆盖、交叉验证、反证、证据等级、结论许可和用户授权缺口写成明文规则。
- 本轮自审确实发现了旧 case warning、X 侧缺口和 connector 未验证问题。

## 反方：当前工作流还不能完全相信自己

- `check-all` 现在对研究质量门多数是 warning，不是 failure；旧 case 通过不代表质量完全达标。
- `check-goal` 更偏资产存在性检查，不等同于语义质量检查。
- 插件状态快照能说明安装层，但不能说明外部 app connector 已授权、可读、可产出证据。
- 自审主要基于本地文件和脚本，没有外部用户反馈。
- 如果后续流程更新时只改文档，不同步 lock、install 脚本和状态快照，仍会漂移。

## 反方最强问题

“如果一个 case 文档都写得很完整，但来源其实很弱，SignalProof 会不会仍然让它通过？”

当前答案：会有 warning 和流程自检提醒，但还不够硬。它能暴露问题，但不一定自动阻止低质量 case 被视为完成。

## 综合判断

当前流程已经能完成自审，但还处在 `passed-with-gaps` 状态。

最重要的下一步不是扩展更多插件，而是把已经发现的漂移和质量门问题进一步自动化：

- 对新 case 强化研究质量门；
- 增加插件锁定清单和安装脚本的一致性检查；
- 保留真实反馈为空的边界；
- 对账号类 connector 只在具体问题中做只读探针。

## 判断

---
type: thesis
status: completed
updated_at: 2026-06-21
gate: passed-with-gaps
---



## 暂定结论

可以反过来使用已经封装好的 SignalProof 工作流审视当前工作流本身。

本轮结论是：当前工作流已经形成可执行闭环，能够发现自己的主要缺口，但仍需要把部分“人工记得做”的规则升级成自动 drift check。

## 支撑理由

- case 骨架由 `init-case` 生成，必需文件完整。
- 能力和插件状态由脚本生成，不只靠口头判断。
- 研究质量门已经进入协议、插件流程、模板和脚本检查。
- 自审发现了具体缺口：旧 case warning、X 侧调研缺口、connector 授权未验证、安装状态不等于证据质量。
- `check-goal` 已把插件状态快照、插件锁定清单、重装脚本和 AGENTS 同步规则纳入目标检查。

## 限制

- 本轮自审不是外部市场研究。
- 真实反馈为空。
- 没有证明所有 app connector 都能读取真实数据。
- 没有证明所有历史 case 都满足新版研究质量门。

## 判断标签

`passed-with-gaps`

含义：

- 继续使用当前工作流；
- 不扩大成产品；
- 下一步补自动化检查；
- 对外部机会 case 仍重新做证据链。

## 验证计划

---
type: validation
status: completed
updated_at: 2026-06-21
gate: passed
---



## 验证目标

验证当前 SignalProof 工作流是否能用自己的规则完成一次工作流自审。

通过标准：

- 生成一个完整 case。
- 13 个必需文件都存在且不是占位。
- `tool-ledger.md` 记录候选能力、实际使用、结果质量和跳过原因。
- `research.md` 覆盖来源覆盖、交叉验证、反证、证据等级、结论许可和用户授权缺口。
- `feedback.md` 明确真实反馈为空。
- `check-all`、`export-all` 和 `check-goal` 最终通过。

## 已执行验证

| 验证项 | 命令或动作 | 结果 | 判断 |
| --- | --- | --- | --- |
| 仓库规则读取 | 读取 `AGENTS.md`、repo skill、工作偏好 skill | 已完成 | passed |
| 能力诊断 | `python3 scripts/signalproof.py diagnose` | 成功，生成本机能力信息 | passed |
| 插件能力矩阵 | `python3 scripts/signalproof.py capabilities` | 成功，生成阶段能力计划 | passed |
| 插件状态快照 | `python3 scripts/signalproof.py plugin-status` | 成功，记录 36 个已安装启用 marketplace 插件 | passed |
| 研究能力诊断 | `python3.14 /Users/rust/.agents/skills/last30days/scripts/last30days.py --diagnose` | 成功，但 X / bird 侧不是完整授权态 | passed-with-gap |
| 全量 case 检查 | `python3 scripts/signalproof.py check-all` | 旧 case failures 为 0，但有研究质量门 warning | passed-with-warning |
| 插件漂移检查 | `python3 scripts/signalproof.py check-plugin-drift` | 锁定清单 36、安装脚本 36、状态快照脚本 36、状态快照已安装 36、当前安装 36，全量一致 | passed |
| 新 case 严格检查 | `python3 scripts/signalproof.py check-case 2026-06-21-signalproof-当前工作流自审 --strict` | 自审 case 通过，warning 未触发失败 | passed |
| 目标检查 | `python3 scripts/signalproof.py check-goal --min-cases 5` | 通过 | passed |

## 验证发现

- 结构层已经可验证。
- 插件安装层已经可验证。
- 插件迁移说明已经可验证。
- 研究质量层对新 case 已可用 strict 模式收紧；旧 case warning 说明历史口径需要后续处理。
- connector 授权和真实数据读取仍必须按具体 case 探针。

## 本轮不验证

- 不验证外部市场需求。
- 不验证所有网页登录网站。
- 不验证所有 app connector。
- 不做 Browser、Chrome、Computer Use 或 Record & Replay 的全量试跑，因为本 case 没有 UI 或用户演示验收目标。

## 验证结论

当前工作流可以完成自审，结论为 `passed-with-gaps`。

## 产物

---
type: artifact
status: completed
updated_at: 2026-06-21
gate: passed
---



## 本轮产物

本轮产物是一个完整的 SignalProof 自审 case：

```text
vault/cases/2026-06-21-signalproof-当前工作流自审/
```

包含 13 个必需文件：

- `signal.md`
- `research.md`
- `debate.md`
- `thesis.md`
- `validation.md`
- `artifact.md`
- `feedback.md`
- `decision.md`
- `asset.md`
- `flow-review.md`
- `tool-ledger.md`
- `process-log.md`
- `report.md`

## 产物内容

- 一个内部流程自审记录。
- 一个插件和工具结果质量账本。
- 一个真实反馈为空的边界声明。
- 一个下一轮优化清单。
- 一个可导出的报告。

## 产物边界

- 产物是 Markdown case，不是网页应用。
- 不包含外部市场验证。
- 不包含假设反馈推进。
- 不需要 DOCX、PDF、Spreadsheets 或 Presentations 交付格式。

## 反馈

---
type: feedback
status: completed
updated_at: 2026-06-21
gate: weak
---



## 真实反馈

真实反馈为空。

本轮没有外部发布、没有公开评论、没有用户访谈、没有产品指标，也没有第三方采用反馈。

## 内部流程反馈

内部流程反馈如下：

- 当前工作流可以通过 case 结构反审自身。
- 脚本能发现结构完整性、报告导出、插件状态和目标资产是否存在。
- `check-all` 的旧 case warning 说明流程能暴露历史质量门缺口。
- `plugin-status` 能避免把 `not installed` marketplace 项误判为已安装缺失。
- `last30days` 诊断能提示 X / bird 侧来源缺口。

## 不能写成什么

- 不能写成市场反馈。
- 不能写成外部用户认可。
- 不能写成 connector 已全部可用。
- 不能写成旧 case 已全部满足新版研究质量门。

## 假设反馈

不需要假设反馈。

本 case 不基于假设反馈继续推进，因此不创建 `assumed-feedback.md`。

## 决策

---
type: decision
status: completed
updated_at: 2026-06-21
gate: passed-with-gaps
---



## 决策

继续使用当前 SignalProof 工作流，并把它标记为 `passed-with-gaps`。

二次验收后补充判断：原报告方向正确，但它当时只完成了“发现问题”，还没有完成“改进工作流”。因此本轮把两项最关键缺口落地为确定性检查：

- 新增 `python3 scripts/signalproof.py check-plugin-drift`，用于检查插件锁定清单、安装脚本、当天状态快照和当前安装列表是否漂移。
- 新增 `python3 scripts/signalproof.py check-case <case-slug> --strict`，用于让新 case 的 warning 直接失败，避免研究质量门只停留在人工提醒。

## 依据

- 真实反馈为空，因此本轮不做市场判断。
- 内部流程证据足以说明：当前工作流能生成 case、记录证据质量、导出报告并通过目标检查。
- 旧 case warning 说明流程已经能发现历史缺口，但还没有完全自动修复或阻止旧口径漂移。
- 插件状态和迁移说明已经基本闭环，但 connector 授权和真实数据读取仍需在具体 case 中验证。

## 下一步优先级

1. 选择一个真实机会 case，跑外部来源覆盖，而不是继续只做内部流程完善。
2. 对一个调研增强 connector 做只读探针，确认它是否能进入证据链。
3. 后续考虑给 `init-case` 增加内部审计类默认模板。

## 明确不做

- 不立刻做 Web App。
- 不立刻做 SaaS。
- 不把所有插件默认全跑。
- 不把 X API credits 当作当前必付项。
- 不把内部流程反馈写成外部验证。

## 资产

---
type: asset
status: completed
updated_at: 2026-06-21
gate: passed
---



## 可复用资产

本 case 沉淀出一套“工作流自审”模式：

```text
把当前流程本身作为 signal
读取规则和能力矩阵
运行诊断和目标检查
记录插件和工具结果质量
区分内部流程证据与外部市场证据
给出 passed-with-gaps 决策
导出报告并复核
```

## 可复用检查清单

- 是否读取了 repo skill 和 AGENTS.md？
- 是否运行了 `diagnose`、`capabilities`、`plugin-status`？
- 是否运行了 `check-plugin-drift`？
- 新 case 是否运行了 `check-case <case-slug> --strict`？
- 是否运行了 `check-all`、`export-all`、`check-goal`？
- 是否记录了工具结果质量，而不是只记录调用？
- 是否把真实反馈为空写清楚？
- 是否区分插件安装、工具暴露、账号授权和证据质量？
- 是否记录下一轮自动化缺口？

## 已沉淀为脚本的资产

- `check-plugin-drift`：比对插件锁定清单、安装脚本、状态快照和当前安装列表。
- `check-case <case-slug> --strict`：对新 case 提高研究质量门，而不是让所有历史 case warning 立刻变成 failure。

## 可沉淀为后续脚本的候选项

- `workflow-audit`：一键生成自审 case 草稿和检查清单。
- 内部审计类模板：避免 `init-case` 默认把内部审计 case 标成外部机会。

## 当前资产边界

这些资产只适用于 SignalProof 内部流程审计，不等于外部机会验证模板。

## 流程自检

---
type: flow_review
status: completed
updated_at: 2026-06-21
case_stage: full-internal-loop
gate: passed-with-gaps
---



## 阶段完整性

| 阶段 | 状态 | 说明 |
| --- | --- | --- |
| signal | passed | 已把“用工作流审视工作流”记录为内部审计信号。 |
| research | passed-with-gaps | 已覆盖来源覆盖、交叉验证、反证、证据等级、结论许可和用户授权缺口；外部市场来源仍弱。 |
| debate | passed | 已记录正反两方和最强反方问题。 |
| thesis | passed | 已给出 `passed-with-gaps` 判断。 |
| validation | passed | 已运行诊断、能力、插件状态和目标检查。 |
| artifact | passed | 已生成完整 Markdown case。 |
| feedback | weak | 真实反馈为空，只记录内部流程反馈。 |
| decision | passed | 已明确继续使用并补自动化检查。 |
| asset | passed | 已沉淀工作流自审清单。 |

## 证据质量

- 强：本地文件、脚本输出、case 必填结构、插件状态快照、报告导出。
- 中：插件迁移说明、阶段能力矩阵、历史会话记忆中的插件审计口径。
- 弱：外部用户反馈、真实市场反馈、X 侧实时讨论、账号类 connector 读取能力。

## 过度声称风险

- 风险：把 `check-all` 通过理解成所有 case 研究质量都达标。
- 处理：记录旧 case warning，下一轮考虑对新 case 提高质量门。
- 风险：把插件安装理解成 connector 可读。
- 处理：按安装、工具暴露、账号授权、证据质量四层记录。
- 风险：把内部流程反馈理解成市场反馈。
- 处理：`feedback.md` 明确真实反馈为空。

## 本轮发现的流程缺口

- 已补自动 drift check：新增 `check-plugin-drift`，并接入 `check-goal`。
- 已补新 case 严格模式：新增 `check-case <case-slug> --strict`，新 case 可把 warning 当成失败。
- 缺 connector 探针闭环：Readwise、Scite、Semrush、Similarweb、Brand24 等需要具体问题触发，不应该全量空跑。
- 缺外部机会 case：当前工作流已经偏内部成熟，下一步应该回到真实外部来源。

## 下一轮优化

1. 给 `init-case` 增加内部审计类 case 类型，避免默认 `external-opportunity`。
2. 选择一个真实机会 case，补外部来源覆盖。
3. 对一个调研增强 connector 做只读探针。

## 结论

当前工作流可以自审，但不是满分闭环。二次验收后，最关键的两项“发现缺口”已经升级成脚本 gate；剩余重点应从内部打磨转向真实外部来源和 connector 探针。

## 工具账本

---
type: tool_ledger
status: completed
updated_at: 2026-06-21
gate: passed-with-gaps
---



## result quality / 结果质量口径

本 case 使用 `强 / 中 / 弱 / 失败 / 阻塞` 记录工具结果质量。工具调用只代表执行过，不自动代表证据合格。

## 候选能力账本

| 能力 | 是否相关 | 是否使用 | 结果质量 | 是否改变判断 | 说明 | 下一步 |
| --- | --- | --- | --- | --- | --- | --- |
| Skill: signalproof | 是 | 是 | 强 | 是 | 提供 repo 级 case 文件、工具账本、流程自检和插件使用规则。 | 保留为默认入口。 |
| Skill: user-working-profile | 是 | 是 | 强 | 是 | 确认用户偏好：中文、证据、边界、少追问多执行。 | 保留。 |
| Plugin: SignalProof repo plugin | 是 | 间接使用 | 中 | 是 | 通过 repo skill、docs、scripts 体现；没有单独调用 plugin UI。 | 后续迁移时复核 repo marketplace。 |
| `diagnose` | 是 | 是 | 强 | 是 | 输出 Python、last30days、provider 和本机诊断信息。 | 每次大流程前运行。 |
| `capabilities` | 是 | 是 | 强 | 是 | 生成阶段到 Codex 自带插件的能力矩阵。 | 每个 case 开始时运行。 |
| `plugin-status` | 是 | 是 | 强 | 是 | 确认 36 个 marketplace 插件 installed enabled，142 个 not installed，primary-runtime 能力可见。 | 后续加入 drift check。 |
| `check-plugin-drift` | 是 | 是 | 强 | 是 | 确认锁定清单、安装脚本、当天状态快照和当前安装列表 36 项一致。 | 后续插件更新后作为硬 gate。 |
| `check-case --strict` | 是 | 是 | 强 | 是 | 自审 case 在严格模式下通过；新 case 可让 warning 直接失败。 | 新 case 完成前运行。 |
| `check-all` | 是 | 是 | 中 | 是 | failures 为 0，但旧 case 有研究质量门 warning。 | 对新 case 提高质量门。 |
| `check-goal` | 是 | 是 | 强 | 是 | 目标检查通过，报告索引存在。 | 保留为完成前 gate。 |
| `export-all` | 是 | 是 | 强 | 是 | 用于生成报告产物和索引。 | 写完 case 后运行。 |
| last30days | 是 | 是，诊断模式 | 中 | 是 | `python3.14 ... --diagnose` 成功；GitHub、ScrapeCreators、OpenRouter 可用；X / bird 侧不是完整授权态。 | 真实趋势 case 再跑查询，X 只在高依赖时提醒补。 |
| Browser / 浏览器 | 条件相关 | 否 | 弱 | 否 | 本 case 没有网页验收目标；历史 Browser 风险已由流程文档记录。 | 报告预览或公开页面验收时启用。 |
| Chrome | 条件相关 | 否 | 弱 | 否 | 本 case 不需要登录态页面读取。 | 需要用户登录态来源时做只读探针。 |
| Computer Use | 条件相关 | 否 | 弱 | 否 | 本 case 没有 GUI-only 验收目标。 | GUI 流程或本地 App 状态验收时启用。 |
| Record & Replay / 录制 | 条件相关 | 否 | 弱 | 否 | 本 case 没有用户操作演示要沉淀。 | 流程稳定后录制成 skill 候选。 |
| Documents / 文档 / DOCX | 条件相关 | 否 | 弱 | 否 | 本轮产物是 Markdown，不需要 DOCX。 | 正式资料包再启用。 |
| PDF | 条件相关 | 否 | 弱 | 否 | 本轮不交付 PDF。 | 需要排版或阅读件时启用。 |
| Spreadsheets / Sheets / 表格 | 条件相关 | 否 | 弱 | 否 | 本轮没有结构化表格数据要计算。 | 反馈或指标统计时启用。 |
| Presentations / Slides / 演示文稿 | 条件相关 | 否 | 弱 | 否 | 本轮不做 deck。 | 对外汇报需要时启用。 |
| GitHub | 低相关 | 否 | 弱 | 否 | 本轮没有提交和远程发布要求；上一轮已确认仓库远程和账号。 | 用户要求保存时再用。 |
| MCP | 条件相关 | 否 | 弱 | 否 | 本轮不需要新增 MCP server 或外部 API 绑定。 | 具体 connector 或文档查询需要时使用。 |
| Memory | 相关 | 是 | 中 | 是 | 用于复核历史插件审计口径：安装、暴露、授权、证据分层。 | 只作上下文，不替代当前脚本输出。 |

## 研究准确性账本

| 检查项 | 是否覆盖 | 证据等级 | 说明 | 用户授权或缺口 | 下一步 |
| --- | --- | --- | --- | --- | --- |
| 来源覆盖 | 覆盖内部来源，外部来源弱 | medium / weak | 使用仓库文档、脚本输出、插件状态和历史记忆；没有外部用户原话。 | X / bird 侧不是完整授权态。 | 真实机会 case 补公开讨论。 |
| 交叉验证 | 已覆盖 | medium | 用 AGENTS、repo skill、docs、scripts、runs 相互核对。 | 官方 Codex 文档本轮未重新联网复核。 | 需要官方事实时再用 openai-docs。 |
| 反证和替代方案 | 已覆盖 | medium | 旧 case warning、connector 未验证、插件安装不等于证据质量都是反证。 | 账号类 connector 仍需具体探针。 | 做单个 connector 只读验证。 |
| 证据等级 | 已覆盖 | medium | 内部流程 medium，结构检查 strong，外部反馈 weak。 | 无阻断项。 | 新 case 提升质量门。 |
| 结论许可 | 已覆盖 | medium | 只允许继续使用、低成本内部优化、补 drift check。 | 不允许市场判断。 | 下一轮进入真实机会验证。 |
| 用户授权 | 已覆盖 | partial | last30days 可诊断，X 侧不完整；外部 app 登录和 Codex connector 不是一回事。 | 不补 X API credits，除非具体 case 高度依赖 X。 | 按 case 触发授权提醒。 |

## 阶段能力计划复盘

| 阶段 | 候选 Codex 插件 | 是否使用 | 结果质量 | 跳过或失败原因 | 下一步 |
| --- | --- | --- | --- | --- | --- |
| signal | Browser / Chrome / Record & Replay | 否 | 弱 | 信号来自当前会话和本地仓库，不需要网页或录制。 | 保留为条件候选。 |
| research | GitHub / last30days / OpenAI Docs / Hugging Face / Readwise / Scite / Semrush / Similarweb / Brand24 / Zotero / Browser / Chrome / Documents / PDF / Spreadsheets / Data Visualization | 部分 | 中 | 使用本地 docs、脚本和 last30days 诊断；没有真实外部研究问题。 | 真实 case 按质量门补证。 |
| debate | Browser / Chrome / Documents / PDF / Scite / Readwise / Zotero | 否 | 中 | 反证来自本地脚本结果和插件状态，不依赖外部长文档。 | 外部机会 case 补外部反证。 |
| thesis | 通常不需要插件 | 否 | 中 | 判断基于本地证据。 | 缺证据时回退 research。 |
| validation | Browser / Computer Use / Documents / PDF / Spreadsheets / Presentations | 否 | 中 | 本轮用脚本验收，不需要 UI 或文件格式验收。 | 导出报告后可视需要 Browser 预览。 |
| artifact | Documents / PDF / Spreadsheets / Presentations / HyperFrames / Data Visualization | 否 | 弱 | 产物是 Markdown case。 | 正式资料包时再启用。 |
| feedback | Chrome / Browser / Spreadsheets / Record & Replay | 否 | 弱 | 真实反馈为空。 | 恢复外部发布后再启用。 |
| decision | 通常不需要插件 | 否 | 中 | 决策依赖当前 case 证据。 | 保留。 |
| asset | Documents / PDF / Spreadsheets / Presentations / Record & Replay / Browser | 否 | 中 | 资产是流程清单和 Markdown。 | 稳定后可录制流程。 |
| flow-review | Browser / Computer Use / Documents / PDF / Spreadsheets / Presentations | 否 | 中 | 脚本和文件级检查足够。 | 需要可视化报告验收时再用。 |

## 工具结论

本轮工具使用足够支持内部工作流自审，并且已经把漂移检查和新 case 严格检查落成脚本 gate；但仍不足以支持外部市场结论。下一轮最有价值的增强不是全量跑插件，而是做一个真实 connector 只读探针和一个真实外部机会 case。

## 过程日志

---
type: process_log
status: completed
updated_at: 2026-06-21
gate: passed
---



## Iteration / 迭代 1：确认规则

Command / 命令：

```bash
sed -n '1,240p' .agents/skills/signalproof/SKILL.md
sed -n '1,220p' /Users/rust/.codex/skills/user-working-profile/SKILL.md
sed -n '1,220p' AGENTS.md
```

结果：

- 确认本仓库事实来源是 `vault/` Markdown 和 `scripts/` 确定性检查。
- 确认每个 case 需要 13 个必需文件。
- 确认文档默认中文，真实反馈为空也必须写清楚。

## Iteration / 迭代 2：读取流程文档

Command / 命令：

```bash
sed -n '1,260p' docs/protocol.md
sed -n '1,260p' docs/research-quality-gate.md
sed -n '1,260p' docs/codex-plugin-flow.md
sed -n '1,260p' docs/codex-plugin-status-and-migration.md
```

结果：

- 确认插件不是默认全跑。
- 确认研究质量门要求来源覆盖、交叉验证、反证、证据等级、结论许可和用户授权缺口。
- 确认插件迁移要区分 repo 资产、本机配置、缓存和外部凭据。

## Iteration / 迭代 3：运行诊断

Command / 命令：

```bash
python3 scripts/signalproof.py diagnose
python3 scripts/signalproof.py capabilities
python3 scripts/signalproof.py plugin-status
python3.14 /Users/rust/.agents/skills/last30days/scripts/last30days.py --diagnose
```

结果：

- `diagnose` 成功。
- `capabilities` 成功生成阶段能力矩阵。
- `plugin-status` 成功生成插件状态快照。
- `last30days --diagnose` 成功，但 X / bird 侧不是完整授权态。

## Iteration / 迭代 4：运行当前目标检查

Command / 命令：

```bash
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py check-goal --min-cases 5
```

结果：

- `check-all` 对 11 个旧 case 返回 failures 0。
- 多个旧 case 出现研究质量门 warning。
- `check-goal` 通过，报告索引存在。

## Iteration / 迭代 5：创建自审 case

Command / 命令：

```bash
python3 scripts/signalproof.py init-case "SignalProof 当前工作流自审"
```

结果：

```text
vault/cases/2026-06-21-signalproof-当前工作流自审/
```

## Self-check / 自检

本轮自检问题：

- 是否把内部流程反馈写成外部反馈？没有。
- 是否把插件安装写成 connector 可读？没有。
- 是否把 X 侧缺口写成“没有需求”？没有。
- 是否把 `check-all` 通过写成所有 case 质量满分？没有。
- 是否默认全跑插件？没有。

## Optimization / 优化记录

第一轮没有立刻修改脚本新增命令，因为先要证明现有工作流能完成自审。

二次验收后已经完成两项优化：

- 增加 `check-plugin-drift`，把插件锁定清单、安装脚本、当天状态快照和当前安装列表的漂移检查脚本化。
- 增加 `check-case <case-slug> --strict`，让新 case 可以把 warning 当成失败，减少研究质量门只靠人工记忆的问题。

剩余优化候选：

- 给内部审计类 case 增加更合适的默认模板。
- 对一个真实 connector 做只读探针。
- 选择一个真实外部机会 case，补完整来源覆盖。
