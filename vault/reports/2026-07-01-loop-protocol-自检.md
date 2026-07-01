# SignalProof 案例报告：2026-07-01-loop-protocol-自检

## 0. 决策先行

- case_mode：`full`
- 信号：Loop Protocol 自检
- 决策：继续使用当前工作流，但把本轮发现的缺口落实为确定性检查和模板约束。
- 证据等级：当前证据等级：medium。内部脚本、模板和 case 记录足以支持工作流机制改进；外部用户反馈仍为 weak。
Frontmatter 必须同步维护：
- `evidence_grade`: strong / medium / weak / blocked。
- `source_types_covered`: 已覆盖来源类型数量。
- 反馈状态：真实反馈为空。
Frontmatter 字段必须同步维护：
- 可复用资产：Loop Protocol 自检 证明案例
- 下一步：- 如果本 case 暴露流程缺口，把缺口写入 `flow-review.md`。
- 如果缺口可脚本化，更新 `scripts/signalproof.py`、模板或协议文档。
- 如果下一步涉及真实机会，另开外部机会 case。
- 边界：full case 只证明本轮已覆盖完整 SignalProof 记录；真实反馈为空时仍不能写成市场验证。

## 1. 详细记录

## 信号

---
type: signal
title: Loop Protocol 自检
case_type: internal-audit
case_intent: workflow-improvement
case_mode: full
protocol_scope: personal-evidence-protocol
loop_profile: ai-work-loop-v1
agentic_loop: optional
developer_feedback_loop: required
external_feedback_loop: skipped-with-reason
asset_loop: required
status: captured
created_at: 2026-07-01
gate: passed
---



## 原始信号

Loop Protocol 自检

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

## Loop Profile

| Loop | 状态 | 说明 |
| --- | --- | --- |
| agentic coding | optional | 需要 Product Spec 和 Eval Set 时才启动 AI 构建循环。 |
| developer feedback | required | 用户用上下文优势修正方向、边界和下一轮 spec。 |
| external feedback | skipped-with-reason | 有真实发布、访谈、alpha、A/B、评论或指标时才写成外部反馈。 |
| asset/meta | required | 把本轮有效输出沉淀为模板、检查表、脚本、skill 或资产账本条目。 |

## 研究

---
type: research
status: completed
updated_at: 2026-07-01
gate: weak
evidence_grade: weak
permission: continue-research
source_types_covered: 0
primary_source_count: 0
external_quote_count: 0
counterevidence_count: 0
independent_source_count: 0
---



## 要回答的问题

- 这个信号背后最真实的问题是什么？
- 哪些证据足够支撑继续内部验证？
- 哪些证据缺口会阻止对外验证或产品化？
- 当前结论到底是 strong、medium、weak 还是 blocked？

## 已确认事实

- SignalProof 当前阶段是 Codex 协议 MVP。
- 真实外部反馈和发布渠道在本轮被用户明确暂时跳过。
- 研究阶段必须记录候选能力和结果质量。
- 研究准确性按 `docs/research-quality-gate.md` 判断，工具调用不等于证据合格。

## 调研过程

- 读取 `AGENTS.md`、repo skill、协议文档、研究质量门和插件流程文档。
- 复核最近自审 case 的报告、流程自检、工具账本和决策。
- 用 `git diff`、脚本输出和 case 内容判断哪些改进已经落地，哪些仍只是建议。

## 来源覆盖表

| 来源类型 | 候选能力 | 当前状态 | 结果质量 | 缺口 |
| --- | --- | --- | --- | --- |
| 公开讨论 | 当前用户任务和历史记忆中的 SignalProof 口径 | 部分覆盖 | weak | 只能支持本轮内部审计，不支持市场判断。 |
| 项目和数据 | 仓库文件、模板、脚本、case、报告索引、runs 快照 | 已覆盖 | strong | 足以判断本地工作流机制是否改变。 |
| 官方和一手资料 | `AGENTS.md`、`.agents/skills/signalproof/SKILL.md`、`docs/protocol.md`、`docs/research-quality-gate.md`、`docs/codex-plugin-flow.md` | 已覆盖 | strong | 本轮事实来源限定在仓库和用户要求。 |
| 反证和替代方案 | 最近自审 report、`check-all` warning、未完成占位标记、connector 授权缺口 | 已覆盖 | medium | 证明仍需脚本 gate，而不是只写复盘。 |

## 交叉验证

- 谁在说：用户要求二次审视并实际更新工作流；仓库规则要求本地优先和中文记录。
- 说什么：最近自审 case 已有部分脚本改进，但仍可能让未完成占位内容通过严格检查。
- 在哪里说：当前任务、`AGENTS.md`、repo skill、`docs/`、`scripts/signalproof.py`、`vault/cases/2026-06-21-signalproof-当前工作流自审/`。
- 有没有反证：有，原报告已落地 `check-plugin-drift` 和 `check-case --strict`，不能说它只是空报告；但它没有处理模板占位和内部审计 case 类型。
- 能支持什么结论：支持继续本地工作流优化；不支持市场验证。

## 反证和替代方案

- 原报告不是纯形式主义，因为已有脚本命令进入 `scripts/signalproof.py`。
- 但如果 `check-case --strict` 只看 TODO 和研究质量门术语，就可能漏掉 `待补`、`待定`、未替换模板变量等半成品痕迹。
- 普通 Markdown 复盘也能发现问题，但不能稳定阻止下一次误报完成。

## 证据等级

当前证据等级：medium。内部脚本、模板和 case 记录足以支持工作流机制改进；外部用户反馈仍为 weak。

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

- 对新增占位检查运行本次 case 严格检查。
- 更新模板和协议说明，避免内部审计默认套外部机会口径。
- 保留真实 feedback 为空的边界。

## 辩论

---
type: debate
status: completed
updated_at: 2026-07-01
gate: passed
---



## 强反方

- 这条信号可能只是噪声，不值得升级为 full。
- 当前证据可能只证明内部兴趣，不证明目标人群有痛点。
- 如果工具账本只记录“用了什么”，没有判断结果质量，价值会很低。

## 替代方案

- 继续补研究，而不是进入验证。
- 收窄到一个更小的人群或动作。
- 放弃这条信号，把资产候选留给下一次。

## Kill 条件

- 证据等级仍是 weak / blocked，且无法补到反证或一手来源。
- 没有明确外部动作，也没有可登记资产候选。
- 决策理由只是“流程完整”，而不是证据真的支持升级。

## 判断

---
type: thesis
status: accepted
updated_at: 2026-07-01
gate: passed
---



## 当前结论

必须在这里明确选择：继续 / 收窄 / 暂停 / 放弃。

默认不要写“继续内部验证”。只有当本 case 明确是内部流程测试或机制优化时，才允许写“继续内部验证”。

## 最小切口

把信号跑成完整证明案例，并记录工具覆盖和流程优化。

## 不做清单

- 不做真实发布。
- 不做真实用户反馈收集。
- 不做 SaaS。
- 不做 Web dashboard。

## 成功标准

- 决策和证据强度匹配。
- 如果是 lite case，能快速决定是否升级为 full case、收窄、暂停或放弃。
- 如果是 full case，必需阶段文件完整，工具覆盖账本完整，流程日志能复盘每轮优化，自检脚本通过。

## 放弃条件

- case 文件无法产生可复用规则。
- 自检发现反复过度声称。
- 工具账本无法帮助下一轮优化。

## 验证计划

---
type: validation
status: planned
updated_at: 2026-07-01
gate: passed
---



## 验证对象

SignalProof 是否能把 Andrew Ng 的 agentic coding、developer feedback、external feedback 三个 loop 嵌入本地协议，并保持 published != validated 的证据边界。

## Product Spec

- 目标用户：SignalProof 维护者和高频使用 Codex/Claude Code 的个人工作流实践者。
- 目标任务：把高不确定性的个人工作压成证据、Spec、AI 执行、反馈、决策和资产。
- 非目标：不做 Web App、SaaS dashboard、workflow builder、通用知识库或自动雷达。
- 成功标准：新 case 能声明 case_intent 与 loop_profile；validation.md 能承接 Product Spec 和 Eval Set；flow-review.md 能审计 loop 是否转动。

## Eval Set

- 通过样例：`init-case --case-intent workflow-improvement` 生成 signal.md loop frontmatter、validation.md Product Spec/Eval Set、flow-review.md loop review。
- 失败样例：只生成旧线性 case 文件，没有 loop_profile，或把 external_feedback_loop=skipped-with-reason 写成验证成功。
- 回归检查：`check-case --strict`、`check-all`、`check-assets`、`export-all`、`check-plugin-drift`。

## Agentic Build Acceptance

- agentic loop 本轮为 optional，因为产物是协议、模板和脚本，而不是独立产品功能。
- 如果后续 case 选择 `case_intent=product-iteration`，agentic_loop 必须为 required，并要求 Product Spec 与 Eval Set 同时存在。

## 验证方式

1. 复核最近自审 case 和报告。
2. 修改 `scripts/signalproof.py`、模板、协议或 skill。
3. 新建或更新本次内部审计 case。
4. 运行 `python3 scripts/signalproof.py check-plugin-drift`。
5. 运行 `python3 scripts/signalproof.py check-case <case-slug> --strict`。
6. 运行 `python3 scripts/signalproof.py export-all`、`check-all`、`check-goal --min-cases 5` 和 `git diff --check`。

## 跳过项

- 真实外部反馈：本轮跳过。
- 发布渠道：本轮跳过。

## 成功标准

自检通过，并且流程自检能指出至少一个下一轮优化点。

## 产物

---
type: artifact
status: created
updated_at: 2026-07-01
gate: passed
---



## 产物

本 case 的产物是一次 SignalProof 工作流机制优化：脚本能识别未完成占位标记，模板能区分内部流程审计与外部机会验证。

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

## 产物边界

这是内部协议产物，不是市场验证产物。

## 反馈

---
type: feedback
status: skipped-real-feedback
updated_at: 2026-07-01
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

- 通过 case 自检判断协议是否可运行。
- 通过流程自检记录优化空间。

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
updated_at: 2026-07-01
gate: passed
---



## 决策

继续使用当前工作流，但把本轮发现的缺口落实为确定性检查和模板约束。

## 理由

- 本轮目标是优化个人工作流和 SignalProof 机制，不是外部机会验证。
- 内部流程反馈只能证明机制是否更好用，不能证明市场需求。

## 下一步

- 如果本 case 暴露流程缺口，把缺口写入 `flow-review.md`。
- 如果缺口可脚本化，更新 `scripts/signalproof.py`、模板或协议文档。
- 如果下一步涉及真实机会，另开外部机会 case。

## 下一轮 Loop 决策

- 改 spec：当 Product Spec 或 Eval Set 不能指导 AI 执行。
- 改产物：当产物和用户任务、内容目标或工作流目标不匹配。
- 改反馈渠道：当外部反馈为空或不命中真实目标人。
- 停止：当证据不足、反证强或继续成本高于潜在资产价值。

## 边界

真实反馈为空，内部流程测试不能写成市场验证、产品化或 SaaS 结论。

## 资产

---
type: asset
status: reusable-internal
created_at: 2026-07-01
gate: passed
asset_status: candidate
registry_required: true
reuse_count: 0
proof_of_reuse: none
---



## 资产名称

Loop Protocol 自检 证明案例

## 资产类型

内部流程审计和机制优化案例。

## 可复用内容

- 严格检查未完成占位标记的脚本规则。
- `internal-audit` case 类型。
- 中文 case 记录模板。
- 复核原报告时区分“已落地机制”和“仍是建议”的判断口径。

## 可复用边界

只能证明内部流程能力，不能证明外部需求。

## Registry 更新

如果本资产真的值得复用，必须同步登记到 `vault/assets/registry.md`，并在下一次使用时补 `reuse_count`、`proof_of_reuse` 和 `last_used_by`。没有登记或没有后续引用时，只能算资产候选。

## 流程自检

---
type: flow_review
status: completed
updated_at: 2026-07-01
case_stage: full-loop
gate: passed
---



## 阶段完整性

| 阶段 | 状态 | 说明 |
| --- | --- | --- |
| signal | passed | 已记录原始信号。 |
| research | weak | 内部证据可用，真实外部证据为空。 |
| debate | passed | 已记录正反方。 |
| thesis | passed | 已明确继续内部验证。 |
| validation | passed | 已定义自检方式。 |
| artifact | passed | 已生成 case 产物。 |
| feedback | weak | 真实反馈为空。 |
| decision | passed | 未过度声称。 |
| asset | passed | 已沉淀内部资产。 |

## 证据质量

- 强：文件级产物和脚本自检。
- 中：已有 SignalProof 经验和 Codex 手册能力映射。
- 弱：真实用户反馈、真实 before/after、发布渠道反馈。

## 研究准确性质量门

| 检查项 | 状态 | 说明 |
| --- | --- | --- |
| 来源覆盖 | weak | 需要覆盖公开讨论、项目和数据、官方和一手资料、反证和替代方案。 |
| 交叉验证 | weak | 需要确认谁在说、说什么、在哪里说、有没有反证。 |
| 结论许可 | weak | 当前只能支持继续研究或低成本内部实验。 |
| 用户授权缺口 | weak / optional | Full Disk Access 已是诊断项；X API credits 默认记为暂缺但非阻断；Readwise、Scite、Semrush、Similarweb、Brand24 按具体 case 做只读探针。 |

## 过度声称检查

没有把真实反馈为空写成验证成功。

## AI Native Work Loop Review

| Loop | 预期状态 | 本轮检查 | 结论 |
| --- | --- | --- | --- |
| agentic coding | optional | `validation.md` 是否给出 Product Spec、Eval Set 和 Agentic Build Acceptance。 | 只有 spec 和 eval 可执行时，才让 AI 长时间构建或测试。 |
| developer feedback | required | `debate.md`、`decision.md` 和本轮人工判断是否修正方向。 | 人类上下文优势必须进入决策，不能只依赖 agent 输出。 |
| external feedback | skipped-with-reason | `feedback.md` 是否有真实发布、访谈、评论、issue、指标或明确跳过原因。 | `published` 不能自动写成 `externally-observed` 或 validated。 |
| asset/meta | required | `asset.md` 和 `vault/assets/registry.md` 是否能承接复用。 | 没有后续引用时只能算资产候选。 |

## 下一轮 Loop 决策

- 改 spec：当 agentic loop 卡住、产物不符合目标用户任务或 Eval Set 不可检查。
- 改产物：当 developer feedback 发现 UI、内容、用户流或交付形态偏离目标。
- 改反馈渠道：当 external feedback 缺少真实目标人、真实任务或可复查指标。
- 停止：当证据保持 weak / blocked，且没有低成本补证路径。

## Full 升级检查

只有同时满足以下条件时，外部机会 case 才能从 lite 升级为 full：

- `research.md` 的 `evidence_grade` 至少为 `medium`。
- 有明确外部动作：发布、访谈、私信测试、下载页、表单回收或真实目标人反馈。
- 至少有一个可登记资产候选。
- `decision.md` 写明为什么需要 full，而不是为了完整而完整。

## 优化空间

- 下一轮可增加更窄的 `last30days --days=3` 或 `--days=7` 调研分支。
- 对需要视觉验证的产物，可使用 Browser 预览导出报告。
- 对只能用 GUI 操作的流程，可考虑 Computer Use，但本轮没有直接工具暴露。

## 工具账本

---
type: tool_ledger
status: completed
updated_at: 2026-07-01
gate: passed
---



## 候选能力账本

| 能力 | 候选原因 | 是否使用 | 结果质量 | 是否改变判断 | 下次动作 |
| --- | --- | --- | --- | --- | --- |
| Skill: signalproof | 是 | 是 | 强 | 已读取 repo skill，确认必需 case 文件、插件记录、真实反馈和验证命令规则。 | 保留为默认入口。 |
| Skill: user-working-profile | 是 | 是 | 强 | 已读取用户偏好，确认中文、边界、证据和少追问多执行。 | 保留。 |
| Memory | 是 | 是 | 中 | 用于复核历史 SignalProof 方向和插件审计口径；只作上下文，不替代当前仓库证据。 | 需要历史口径时轻量使用。 |
| last30days | 条件相关 | 未使用 | 中 | 本 case 是内部工作流机制审计，外部趋势不会改变脚本和模板判断。 | 真实外部机会 case 再运行。 |
| Browser / Chrome | 条件相关 | 未使用 | 中 | 本轮没有网页、登录态或报告预览验收目标。 | 有页面验收时再用。 |
| Computer Use | 条件相关 | 未使用 | 中 | 本轮没有 GUI-only 验收目标。 | 有本地 App 操作验收时再用。 |
| Record & Replay | 条件相关 | 未使用 | 中 | 本轮没有用户演示录制目标。 | 需要沉淀操作流程时再用。 |
| Documents / PDF / Spreadsheets / Presentations | 条件相关 | 未使用 | 中 | 本轮产物是 Markdown、模板和 Python 脚本。 | 正式资料包或格式产物再用。 |
| Plugin / MCP | 是 | 使用本地脚本和已读插件流程文档 | 中 | 记录安装、暴露、授权、证据质量分层；没有默认全跑外部 connector。 | 具体 case 再做只读探针。 |

## 研究准确性账本

按 `docs/research-quality-gate.md` 记录研究阶段是否真的能支持结论，必须覆盖来源覆盖、交叉验证、反证、证据等级、结论许可和用户授权缺口：

| 检查项 | 是否覆盖 | 证据等级 | 说明 | 下一步 |
| --- | --- | --- | --- | --- |
| 公开讨论 | 覆盖当前用户任务，未做外部扩散扫描 | weak | 本轮是内部流程审计，公开讨论不构成市场证据。 | 真实机会 case 再补。 |
| 项目和数据 | 已覆盖仓库文件、脚本、模板、case 和 runs | strong | 可判断本地机制是否真实改变。 | 继续用脚本验证。 |
| 官方和一手资料 | 已覆盖 AGENTS、repo skill、协议和质量门文档 | strong | 本轮按用户指定文档执行。 | 官方联网事实变更时再查。 |
| 反证和替代方案 | 已覆盖原报告缺口、strict 漏检占位风险、connector 授权缺口 | medium | 反证足以支持新增脚本 gate。 | 后续 connector case 再探针。 |
| 结论许可 | 已覆盖 | medium | 只允许内部机制优化和低成本实验。 | 不写市场验证。 |

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
updated_at: 2026-07-01
gate: passed
---



## 迭代 1

命令：

```bash
python3 scripts/signalproof.py init-case "Loop Protocol 自检"
```

结果：

- 生成当前 `case_mode` 对应的 case 文件。

自检：

- 文件齐全。
- 真实反馈为空边界明确。

优化：

- 后续把重复检查脚本化。

## 迭代 2

命令：

```bash
python3 scripts/signalproof.py check-all
```

结果：

- 等待本轮自检结果。

自检：

- 检查 `tool-ledger.md` 是否记录 Skill / Plugin / MCP / Browser / Computer Use / last30days。
- 检查 `research.md`、`feedback.md`、`asset.md` 是否维护结构化 frontmatter 字段。

优化：

- 根据 warnings 更新模板或脚本。
