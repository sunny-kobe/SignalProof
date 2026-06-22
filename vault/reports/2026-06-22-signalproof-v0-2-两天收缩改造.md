# SignalProof 案例报告：2026-06-22-signalproof-v0-2-两天收缩改造

## 0. 决策先行

- case_mode：`full`
- 信号：SignalProof V0.2 两天收缩改造
- 决策：接受 V0.2 收缩改造：SignalProof 当前按个人证据协议执行，新外部机会默认 lite，full 只作为满足硬条件后的升级事件。
- 证据等级：当前证据等级：medium。内部脚本、模板、文档和 case 记录足以支持工作流机制改进；外部用户反馈仍为空，因此不能升级为市场验证结论。
Frontmatter 必须同步维护：
- `evidence_grade`: strong / medium / weak / blocked。
- `source_types_covered`: 已覆盖来源类型数量。
- 反馈状态：真实反馈为空。
Frontmatter 字段必须同步维护：
- 可复用资产：signalproof-v0-2-protocol-gates
- 下一步：- 完成本 case strict 和最终验证。
- 不重写历史 warning，只把它们作为历史债保留。
- 下一步可以开始 5 个 lite 外部信号实验，用 V0.2 模板检验真实使用成本。
- 边界：full case 只证明本轮已覆盖完整 SignalProof 记录；真实反馈为空时仍不能写成市场验证。

## 1. 详细记录

## 信号

---
type: signal
title: SignalProof V0.2 两天收缩改造
case_type: internal-audit
case_mode: full
protocol_scope: personal-evidence-protocol
status: captured
created_at: 2026-06-22
gate: passed
---



## 原始信号

SignalProof V0.2 两天收缩改造

## 为什么值得进入流程

- 这条信号用于检验 SignalProof 工作流本身是否能发现并修正流程缺口。
- 本 case 的价值来自本地文档、模板、脚本和 case 记录的可执行改进，而不是外部市场反馈。

## 初步用户

- SignalProof 维护者。
- 高频使用 Codex / Claude Code / MCP / 本地 AI coding 工作流，并希望把判断过程沉淀成可审计资产的人。

## 当前边界

- 不声称市场验证。
- 不默认产品化。
- 不做 SaaS、dashboard、workflow builder 或通用知识库。
- 内部流程反馈只能支持机制优化，不能支持外部需求成立。

## 研究

---
type: research
status: completed
updated_at: 2026-06-22
gate: weak
evidence_grade: medium
permission: continue-research
source_types_covered: 3
primary_source_count: 4
external_quote_count: 0
counterevidence_count: 3
independent_source_count: 3
---



## 要回答的问题

- V0.2 需要收缩哪些协议口径，才能避免 full 默认化和插件 ready 错觉？
- 哪些规则必须进入文档、模板、skill 和脚本 gate，而不是留在建议里？
- 哪些结果只能证明内部机制改进，不能证明外部机会成立？

## 已确认事实

- SignalProof V0.2 当前执行名是 `SignalProof 个人证据协议`，`Personal Opportunity OS` 只保留为长期背景。
- 本轮保持本地 Markdown vault + Python 标准库脚本路线，不引入 Web App、SaaS dashboard、workflow builder、通用知识库、自动雷达、n8n/Dify、Notion/Obsidian 集成。
- 新外部机会默认从 `case_mode: lite` 开始；full 变成有硬条件的升级事件。
- 插件治理降级为候选能力治理，安装数量、状态快照或 marketplace 可见性不等于工具可用或证据成立。
- 真实外部反馈为空，本 case 只能证明内部机制优化。

## 调研过程

- 读取 `AGENTS.md`、`docs/signalproof-v0.2-two-day-refactor-plan.md`、repo skill、user-working-profile 和 session-handoff 规则。
- 运行初始 `git status --short`、`check-all`、`check-plugin-drift --no-codex`，记录 dirty files、warning 缺口和插件漂移失败。
- 对 `README.md`、`docs/protocol.md`、`docs/current-flow.md`、两个 skill、模板、资产账本和 `scripts/signalproof.py` 做增量修改。
- 用 `py_compile`、`check-assets`、`check-all` 和 `git diff --check` 做中间验证。

## 来源覆盖表

| 来源类型 | 候选能力 | 当前状态 | 结果质量 | 缺口 |
| --- | --- | --- | --- | --- |
| 当前用户要求 | 本轮 goal、硬边界和两天计划 | 已覆盖 | strong | 只能支持内部改造范围，不支持市场判断。 |
| 仓库事实 | `AGENTS.md`、`README.md`、`docs/`、`templates/`、`scripts/signalproof.py`、`vault/assets/registry.md` | 已覆盖 | strong | 足以判断本地机制是否改变。 |
| 运行证据 | 初始 `check-all`、`check-plugin-drift --no-codex`、中间 `py_compile`、`check-assets`、`check-all` | 已覆盖 | strong | 插件漂移仍失败，需要作为历史债记录。 |
| 反证和替代方案 | full case 过重、插件安装数误读、历史 warning 未清、zero-reuse 资产 | 已覆盖 | medium | 证明需要脚本 gate 和资产复用账本。 |

## 交叉验证

- 谁在说：用户要求按 V0.2 两天计划直接修改仓库，并明确硬边界。
- 说什么：SignalProof 必须从完整个人机会 OS 叙事收缩为个人证据协议；full 必须有升级条件；插件只作为候选能力；资产要看复用。
- 在哪里说：`docs/signalproof-v0.2-two-day-refactor-plan.md`、`AGENTS.md`、两份 SignalProof skill、当前脚本输出和资产账本。
- 有没有反证：有，历史 case 仍有结构化字段缺失和占位 warning；当天插件状态快照与锁定清单不一致；部分资产没有复用证据。
- 能支持什么结论：支持完成本地协议收缩和脚本 gate 增强；不支持外部市场验证、产品化或 SaaS 结论。

## 反证和替代方案

- 反证 1：历史 `check-all` 初始输出是 15 个 case、0 failure，但没有 warning 汇总，容易让历史债被误读成全绿。
- 反证 2：`check-plugin-drift --no-codex` 初始失败，说明插件锁定清单、安装脚本和当天状态快照不能被直接写成环境 ready。
- 反证 3：资产 registry 里 `repo-context-audit-kit`、`plugin-eval-multiformat-pack` 仍是 zero reuse，说明“已命名资产”不等于“已复用资产”。
- 替代方案：不引入数据库或 UI，先用 Markdown frontmatter + 标准库脚本把最关键的状态门槛跑起来。

## 证据等级

当前证据等级：medium。内部脚本、模板、文档和 case 记录足以支持工作流机制改进；外部用户反馈仍为空，因此不能升级为市场验证结论。

Frontmatter 必须同步维护：

- `evidence_grade`: strong / medium / weak / blocked。
- `source_types_covered`: 已覆盖来源类型数量。
- `primary_source_count`: 一手或官方来源数量。
- `external_quote_count`: 可复查外部原话数量。
- `counterevidence_count`: 反证或替代方案数量。
- `independent_source_count`: 独立来源数量。

## 结论许可

当前许可：继续本地流程优化，并把高价值缺口落到脚本、模板、文档或 skill。不得写成市场验证、插件全部授权成功或 SaaS 可行。

Frontmatter `permission` 只能是 `continue-research` / `low-cost-experiment` / `pause` / `abandon`。只有当来源覆盖和反证数量达到门槛时，才允许写 `low-cost-experiment`。

## 需要用户授权或开通

- 若需要 X/Twitter 来源：先把 X API credits 记为暂缺但非阻断；只有 case 高度依赖 X 实时讨论、早期热度或 KOL 扩散时再提醒补 credits。
- 若需要浏览器 cookie：先运行 `python3 scripts/signalproof.py diagnose`，根据结果判断是否需要用户处理 Full Disk Access。
- 若需要 Readwise、Scite、Semrush、Similarweb、Brand24：按真实 case 做只读探针，不默认全开。

## 证据缺口

- 真实用户原话为空。
- 真实发布反馈为空。
- 真实 before/after 为空。

## 下一步补证

- 跑完本 case strict、`check-assets`、`check-all`、`export-all`、`check-plugin-drift --no-codex` 和 `git diff --check`。
- 把插件漂移失败和历史 structured frontmatter warning 作为后续债务，不强行重写历史 case。
- 下一步用 5 个 lite 外部信号实验验证 V0.2 模板和脚本 gate 是否真的降低判断成本。

## 辩论

---
type: debate
status: completed
updated_at: 2026-06-22
gate: passed
---



## 强反方

- V0.2 可能仍然太重：full case 保留 13 个文件，历史 warning 也明显增加。
- 结构化 frontmatter 只是更硬的表格；如果后续不跑真实 lite 外部信号，仍然无法证明它降低判断成本。
- 插件治理即使降级为候选能力，也可能继续占用注意力；下一步必须减少插件叙事，把重点放回证据和复用。

## 替代方案

- 更激进地删除 `thesis.md`、`report.md` 和 lite 的 `debate.md`，把 case 压到 4 个文件。
- 引入 SQLite 或一个小型 UI，直接把结构化字段放进数据模型。
- 暂停协议改造，先跑 5 个外部信号，再倒推模板。

## Kill 条件

- 后续 5 个 lite 外部信号实验如果仍然需要大量手写重复内容，说明模板没有真正收缩。
- 如果 `check-all` 的 warning 太多导致用户忽略输出，需要把历史 warning 分层或增加新旧 case 过滤。
- 如果 `check-assets` 只暴露 zero reuse 但不驱动后续复用，资产账本仍会退化成目录。

## 判断

---
type: thesis
status: accepted
updated_at: 2026-06-22
gate: passed
---



## 当前结论

继续，但只限于内部协议机制优化。V0.2 已把执行范围收缩为 `SignalProof 个人证据协议`，并把 full case 从默认动作降级为有硬条件的升级事件。

## 最小切口

不重写历史 case，不引入新依赖，只修改 docs、skills、templates、资产账本和 `scripts/signalproof.py`，让后续新 case 自动继承 V0.2 规则。

## 不做清单

- 不做真实发布。
- 不做真实用户反馈收集。
- 不做 SaaS。
- 不做 Web dashboard、workflow builder、通用知识库、自动雷达、n8n/Dify、Notion/Obsidian 集成。
- 不把插件安装数量写成工具可用或证据成立。

## 成功标准

- 文档和 skills 明确当前定位是 `SignalProof 个人证据协议`。
- 新模板包含 research / feedback / asset 的结构化 frontmatter。
- `check-all` 输出 failures、warnings 和 Overall status。
- `check-assets` 能暴露 zero-reuse 资产比例。
- 本 internal-audit full case 通过 strict 检查。

## 放弃条件

- 后续无法用 lite case 跑真实外部信号。
- 结构化字段只增加填写成本，没有减少判断成本。
- 用户仍需要靠记忆区分 published、observed feedback 和 validated。

## 验证计划

---
type: validation
status: planned
updated_at: 2026-06-22
gate: passed
---



## 验证对象

SignalProof 是否能把“报告里发现的缺口”升级成脚本、模板或文档中的可复用机制。

## 验证方式

1. 运行 `python3 -m py_compile scripts/signalproof.py`。
2. 运行 `python3 scripts/signalproof.py check-case 2026-06-22-signalproof-v0-2-两天收缩改造 --strict`。
3. 运行 `python3 scripts/signalproof.py check-assets`。
4. 运行 `python3 scripts/signalproof.py check-all`。
5. 运行 `python3 scripts/signalproof.py export-all`。
6. 运行 `python3 scripts/signalproof.py check-plugin-drift --no-codex`。
7. 运行 `git diff --check` 和 `git status --short`。

## 跳过项

- 真实外部反馈：本轮跳过。
- 发布渠道：本轮跳过。
- 浏览器/GUI 验收：本轮产物是 Markdown 和 Python 标准库脚本，没有页面或 GUI-only 流程。

## 成功标准

- 本 case strict 通过。
- `check-assets` 能输出 registered/reused/candidate/zero-reuse 统计。
- `check-all` 即使保留历史 warning，也必须显示 `Overall status: passed-with-warnings`。
- `check-plugin-drift --no-codex` 若仍失败，必须明确失败来自当天状态快照和锁定清单不一致，而不是把插件治理写成 ready。

## 产物

---
type: artifact
status: created
updated_at: 2026-06-22
gate: passed
---



## 产物

本 case 的产物是一次 SignalProof V0.2 收缩改造：文档、skills、模板、资产账本和脚本 gate 都改为服务 `SignalProof 个人证据协议`。

## 文件

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

## 本轮改动清单

- `README.md`、`docs/protocol.md`、`docs/current-flow.md`、`AGENTS.md`、两份 SignalProof skill：统一定位、lite 默认、full 升级硬条件和插件候选能力边界。
- `templates/case/`：给 signal / research / feedback / asset 等模板加入结构化 frontmatter，压缩 lite debate，减少 report 重复。
- `vault/assets/registry.md`：升级为资产复用账本，新增 reuse_count、proof_of_reuse、reuse_cost_minutes、preconditions、public_or_private、supersedes、owner_scope。
- `scripts/signalproof.py`：新增 frontmatter 检查、`check-all` 顶层状态和 `check-assets`。
- `vault/cases/2026-06-22-signalproof-v0-2-两天收缩改造/`：记录本轮 internal-audit full case。

## 产物边界

这是内部协议产物，不是市场验证产物。

## 反馈

---
type: feedback
status: skipped-real-feedback
updated_at: 2026-06-22
gate: weak
feedback_status: none
validation_status: none
real_feedback_count: 0
paid_signal_count: 0
published_url_count: 0
---



## 当前反馈状态

真实反馈为空。

Frontmatter 字段必须同步维护：

- `feedback_status`: none / internal / synthetic-demo / assumed / published-no-feedback / qualitative-real / quantitative-real / paid-signal。
- `validation_status`: none / artifact-built / published / externally-observed / repeated。
- `real_feedback_count`: 真实目标人反馈数量。
- `paid_signal_count`: 付费、预付、购买、打赏或明确预算信号数量。
- `published_url_count`: 已发布 URL 数量。

## 为什么为空

本 case 是内部流程优化，没有发布、访谈、公开评论或产品指标；真实反馈为空。

## 内部反馈

- 中间验证显示 `python3 -m py_compile scripts/signalproof.py` 通过。
- 中间验证显示 `check-assets` 可输出复用统计，并标出 2 个 zero-reuse 资产。
- 中间验证显示 `check-all` 可输出 failures、warnings 和 `Overall status: passed-with-warnings`。
- 初始 `check-plugin-drift --no-codex` 失败，原因是当天状态快照已安装插件数与锁定清单不一致；这证明插件治理不能写成 ready。

## 不能得出的结论

- 不能把 `published` 写成 `externally-observed`。
- 不能写验证成功。
- 不能声称市场已验证。
- 不能声称用户需要这个产品。
- 不能进入 SaaS 化结论。

## 决策

---
type: decision
status: accepted-internal
decision: continue-internal-protocol-validation
updated_at: 2026-06-22
gate: passed
---



## 决策

接受 V0.2 收缩改造：SignalProof 当前按个人证据协议执行，新外部机会默认 lite，full 只作为满足硬条件后的升级事件。

## 理由

- 本轮目标是优化个人工作流和 SignalProof 机制，不是外部机会验证。
- 内部流程反馈只能证明机制是否更好用，不能证明市场需求。

## 下一步

- 完成本 case strict 和最终验证。
- 不重写历史 warning，只把它们作为历史债保留。
- 下一步可以开始 5 个 lite 外部信号实验，用 V0.2 模板检验真实使用成本。

## 边界

真实反馈为空，内部流程测试不能写成市场验证、产品化或 SaaS 结论。

## 资产

---
type: asset
status: reusable-internal
created_at: 2026-06-22
gate: passed
asset_status: registered
registry_required: true
reuse_count: 0
proof_of_reuse: none
---



## 资产名称

signalproof-v0-2-protocol-gates

## 资产类型

protocol / template / script-gate

## 可复用内容

- `check-all` 顶层 failures / warnings / Overall status 输出。
- `check-case` 结构化 frontmatter 检查。
- `check-assets` 资产复用统计。
- lite 默认、full 硬条件升级、插件候选能力边界和资产复用账本规则。

## 可复用边界

只能证明内部流程能力，不能证明外部需求。

## Registry 更新

已登记到 `vault/assets/registry.md`，但 `reuse_count=0`，所以当前仍只是资产候选。只有后续 5 个 lite 外部信号实验实际复用后，才能回填 `proof_of_reuse`。

## 流程自检

---
type: flow_review
status: completed
updated_at: 2026-06-22
case_stage: full-loop
gate: passed
---



## 阶段完整性

| 阶段 | 状态 | 说明 |
| --- | --- | --- |
| signal | passed | 已记录原始信号。 |
| research | medium | 内部仓库证据可用，真实外部证据为空。 |
| debate | passed | 已记录正反方。 |
| thesis | passed | 已明确继续内部机制优化。 |
| validation | passed | 已定义自检方式。 |
| artifact | passed | 已生成 case 产物。 |
| feedback | weak | 真实反馈为空。 |
| decision | passed | 未过度声称。 |
| asset | warning | 已登记资产候选，但还没有后续复用证明。 |

## 证据质量

- 强：文件级产物和脚本自检。
- 中：当前用户要求、仓库规则、脚本输出和资产账本。
- 弱：真实用户反馈、真实 before/after、发布渠道反馈。

## 研究准确性质量门

| 检查项 | 状态 | 说明 |
| --- | --- | --- |
| 来源覆盖 | medium | 本轮覆盖用户要求、仓库文件、脚本输出和反证风险。 |
| 交叉验证 | medium | 文档、模板、脚本和 case 互相约束。 |
| 结论许可 | medium | 只允许内部机制优化和下一步 lite 外部信号实验。 |
| 用户授权缺口 | weak / optional | 本轮不依赖外部账号；真实外部机会 case 再处理授权。 |

## 过度声称检查

没有把真实反馈为空写成验证成功。

## Full 升级检查

只有同时满足以下条件时，外部机会 case 才能从 lite 升级为 full：

- `research.md` 的 `evidence_grade` 至少为 `medium`。
- 有明确外部动作：发布、访谈、私信测试、下载页、表单回收或真实目标人反馈。
- 至少有一个可登记资产候选。
- `decision.md` 写明为什么需要 full，而不是为了完整而完整。

## 优化空间

- 历史 case 大量缺少结构化 frontmatter，`check-all` 会保留 warning；后续可以按需只迁移活跃 case。
- `check-plugin-drift --no-codex` 仍会因当天状态快照只显示少量已安装插件而失败；需要重新运行 `plugin-status` 或更新插件锁定策略。
- `check-assets` 暴露 zero-reuse 资产，下一步应用 5 个 lite 外部信号实验检验资产是否真的能复用。

## 工具账本

---
type: tool_ledger
status: completed
updated_at: 2026-06-22
gate: passed
---



## 候选能力账本

| 能力 | 候选原因 | 是否使用 | 结果质量 | 是否改变判断 | 下次动作 |
| --- | --- | --- | --- | --- | --- |
| Skill: signalproof | repo 规则是本轮事实来源 | 是 | 强 | 是，确认 full/lite、strict、插件和资产边界 | 保留为默认入口。 |
| Skill: user-working-profile | 需要遵守用户执行和证据偏好 | 是 | 强 | 是，确认中文、窄范围、证据优先和少追问多执行 | 保留。 |
| Skill: session-handoff | 本任务面广，需可交接记录 | 是 | 中 | 是，最终说明按状态、证据、风险组织 | 长任务继续使用。 |
| Memory | 需要复核历史 SignalProof 口径 | 是 | 中 | 是，确认个人证据协议和插件 exposure 分层 | 只作上下文，不替代当前仓库证据。 |
| last30days | 外部趋势不会改变本地脚本和模板判断 | 未使用 | 中 | 否 | 真实外部机会 case 再运行。 |
| Browser / Chrome | 本轮没有网页、登录态或报告预览目标 | 未使用 | 中 | 否 | 有页面验收时再用。 |
| Computer Use | 本轮没有 GUI-only 验收目标 | 未使用 | 中 | 否 | 有本地 App 操作验收时再用。 |
| Record & Replay | 本轮没有用户演示录制目标 | 未使用 | 中 | 否 | 需要沉淀操作流程时再用。 |
| Documents / PDF / Spreadsheets / Presentations | 本轮产物是 Markdown 和 Python 脚本 | 未使用 | 中 | 否 | 正式资料包或格式产物再用。 |
| Plugin / MCP | 需要记录安装、暴露、授权、证据质量分层 | 使用本地脚本和已读插件流程文档 | 中 | 是，插件治理降级为候选能力 | 具体 case 再做只读探针。 |

## 研究准确性账本

按 `docs/research-quality-gate.md` 记录研究阶段是否真的能支持结论，必须覆盖来源覆盖、交叉验证、反证、证据等级、结论许可和用户授权缺口：

| 检查项 | 是否覆盖 | 证据等级 | 说明 | 下一步 |
| --- | --- | --- | --- | --- |
| 来源覆盖 | 已覆盖用户要求、仓库文件、脚本输出和历史口径 | medium | 本轮是内部流程审计，不构成市场证据。 | 真实机会 case 再补外部来源。 |
| 交叉验证 | 已用 docs、templates、skills、scripts 和 case 互相验证 | medium | 可判断本地机制是否真实改变。 | 继续用脚本验证。 |
| 反证 | 已覆盖 full 过重、插件 ready 错觉、历史 warning、zero-reuse 资产 | medium | 反证足以支持新增脚本 gate。 | 下一轮观察 lite 实验成本。 |
| 证据等级 | medium | medium | 只支持内部机制优化。 | 不写市场验证。 |
| 结论许可 | continue-research | medium | 允许继续本地优化和低成本 lite 外部实验。 | 不写产品化。 |
| 用户授权缺口 | 不依赖外部账号 | weak | 本轮无需用户授权；真实外部机会 case 再探针。 | 保留为后续条件。 |

## 阶段能力计划

运行：

```bash
python3 scripts/signalproof.py capabilities
```

然后把本 case 各阶段真正考虑过的 Codex 自带插件记录到这里：

| 阶段 | 候选 Codex 插件 | 实际使用 | 结果质量 | 是否改变判断 | 跳过或失败原因 |
| --- | --- | --- | --- | --- | --- |
| signal | Browser / Chrome / Record & Replay | 未使用 | 中 | 信号来自当前会话和本地仓库，不需要网页、登录态或录制。 | 保留为条件候选。 |
| research | GitHub / last30days / OpenAI Docs / Browser / Documents / PDF / Spreadsheets | 部分使用本地文件和记忆；未调用外部插件 | 中 | 本轮按用户指定本地文档复核，外部趋势不会改变内部脚本判断。 | 真实外部机会 case 再跑。 |
| debate | Browser / Chrome / Documents / PDF | 未使用 | 中 | 反证来自本地 case、diff 和脚本行为。 | 外部反证依赖页面时再用。 |
| validation | 本地脚本 / Browser / Computer Use / Documents / PDF / Spreadsheets / Presentations | 使用本地脚本 | 强 | 本轮产物是 Markdown 和 Python 脚本，不需要 GUI 或格式插件。 | 按最终命令验证。 |
| artifact | Documents / PDF / Spreadsheets / Presentations / HyperFrames / Data Visualization | 未使用 | 中 | 产物是本地 Markdown、模板和脚本。 | 正式资料包再启用。 |
| publication | Browser / Chrome | 未使用 | 弱 | 未发布。 | 有公开 URL 时再验收。 |
| feedback | Chrome / Browser / Spreadsheets / Record & Replay | 未使用 | 弱 | 真实反馈为空。 | 外部反馈恢复后再用。 |
| asset | Documents / PDF / Spreadsheets / Presentations / Record & Replay / Browser | 未使用 | 中 | 资产沉淀为本地规则和 case。 | 需要演示或资料包时再用。 |
| flow-review | 本地脚本 / Browser / Computer Use / Documents / PDF / Spreadsheets / Presentations | 使用本地脚本 | 强 | 指定验证命令足以验收本轮机制。 | 保留脚本 gate。 |

## 能力结论

只有工具结果改变判断、减少不确定性或验收产物时，才算对本 case 有实质贡献。插件安装数量、候选数量或调用次数不能写成证据合格。

## 过程日志

---
type: process_log
status: completed
updated_at: 2026-06-22
gate: passed
---



## 迭代 1

命令：

```bash
git status --short
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py check-plugin-drift --no-codex
```

结果：

- `git status --short` 显示仓库已有多项 dirty changes，包含本次目标文件、历史 reports、新增 assets/cases/runs。
- 初始 `check-all`：15 个 case，0 failure，但旧输出没有 warning 汇总。
- 初始 `check-plugin-drift --no-codex`：failed；锁定清单和安装脚本为 36 个，状态快照已安装插件仅 3 个。

自检：

- 不能回滚用户已有 dirty changes。
- 插件漂移失败不能写成工具 ready。

优化：

- 本轮需要增强 `check-all`、`check-case` 和新增 `check-assets`。

## 迭代 2

命令：

```bash
python3 -m py_compile scripts/signalproof.py
python3 scripts/signalproof.py check-assets
python3 scripts/signalproof.py check-all
```

结果：

- Python 编译通过。
- `check-assets` 输出 10 个登记资产、3 个 zero-reuse warning。
- `check-all` 输出 failures、warnings 和 `Overall status: passed-with-warnings`。

自检：

- 检查 `tool-ledger.md` 是否记录 Skill / Plugin / MCP / Browser / Computer Use / last30days。
- 检查 `research.md`、`feedback.md`、`asset.md` 是否维护结构化 frontmatter 字段。

优化：

- 根据 warnings 更新模板或脚本。

## 迭代 3

命令：

```bash
python3 scripts/signalproof.py init-case "SignalProof V0.2 两天收缩改造" --case-type internal-audit --case-mode full
```

结果：

- 创建 `vault/cases/2026-06-22-signalproof-v0-2-两天收缩改造/`。
- 填写采纳、改写采纳、不采纳、真实反馈为空、插件漂移失败和后续风险。

自检：

- 本 case 必须通过 strict，作为 V0.2 新规则样本。

优化：

- 若 strict 报 warning，优先改本 case，不迁移全部历史 case。
