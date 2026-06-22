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

# 研究

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
