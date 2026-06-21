# SignalProof 案例报告：2026-06-21-signalproof-工作流优化二次审视

## 信号

---
type: signal
title: SignalProof 工作流优化二次审视
case_type: internal-audit
status: captured
created_at: 2026-06-21
gate: passed
---



## 原始信号

复核最近 SignalProof 自审报告，判断哪些结论可靠、哪些只是建议，并把最高价值改进落地为本地脚本、模板和文档约束。

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
updated_at: 2026-06-21
gate: medium
---



## 要回答的问题

- 最近的自审报告是否准确，还是只是写得像完成？
- 哪些结论已经有脚本、模板或文档支撑？
- 哪些仍只是建议或待验证假设？
- 本轮最值得落地的机制改进是什么？

## 已确认事实

- SignalProof 当前阶段是 Codex 协议 MVP。
- 本轮是内部流程审计，不做真实外部反馈和发布渠道。
- 研究阶段必须记录候选能力和结果质量。
- 研究准确性按 `docs/research-quality-gate.md` 判断，工具调用不等于证据合格。
- 最近自审报告已经把 `check-plugin-drift` 和 `check-case <case-slug> --strict` 写入脚本、AGENTS、repo skill 和质量门文档；这不是纯复盘。
- 复核后发现新增 strict 仍有一个漏洞：如果 case 文件保留 `待补`、`待定` 或未替换模板变量，旧检查不一定把它视为未完成。
- 复核后发现另一个流程缺口：内部流程审计 case 默认套用外部机会验证模板，容易把内部审计写成市场研究。

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
- 原报告把“下一步优先做内部审计类模板优化”写成建议，但当时没有真正落入 `init-case` 或模板机制。
- 普通 Markdown 复盘也能发现问题，但不能稳定阻止下一次误报完成。

## 证据等级

当前证据等级：medium。

- strong：脚本 diff、模板 diff、AGENTS 和 repo skill 的规则变更，可以证明本地机制已经改变。
- medium：最近自审 case 的结论整体可靠，但它对模板占位、内部审计类型和 connector 探针仍只是建议。
- weak：外部用户反馈、真实市场反馈、外部 connector 可读性和 X 侧实时讨论。

## 结论许可

当前许可：继续本地流程优化，并把高价值缺口落到脚本、模板、文档或 skill。不得写成市场验证、插件全部授权成功或 SaaS 可行。

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

## 本轮研究判断

原报告基本准确，但不完整。

准确部分：

- `passed-with-gaps` 判断准确。
- 插件安装、工具暴露、账号授权、证据质量需要分层，这个判断准确。
- 真实反馈为空，不能写成市场验证，这个边界准确。
- `check-plugin-drift` 和 `check-case --strict` 已经进入脚本，不是只写在报告里。

不足部分：

- 原报告仍偏向“发现缺口后建议下一步”，没有把内部审计 case 类型落到 `init-case`。
- 原 strict 检查没有覆盖 `待补`、`待定` 和未替换模板变量，可能让新 case 看似完成。
- 原模板会让内部审计和外部机会验证共用一套默认话术，容易混淆证据许可。

本轮选择的高价值改进：

- 给 `check-case --strict` 增加未完成占位标记检查。
- 给 `init-case` 增加 `--case-type internal-audit`。
- 让模板按 case 类型渲染信号、研究、工具账本、验证、反馈、决策和报告边界。
- 把新规则写入 `AGENTS.md`、repo skill、`docs/protocol.md` 和 `docs/research-quality-gate.md`。

## 辩论

---
type: debate
status: completed
updated_at: 2026-06-21
gate: passed
---



## 正方

- 原自审报告不是空转，因为 `check-plugin-drift` 和 `check-case --strict` 已经进入脚本和文档。
- 本轮继续从脚本和模板下手，可以把“完成感”变成可执行 gate。
- 内部审计类 case 独立出来后，能减少把流程反馈误写成市场验证的风险。
- 占位标记检查能直接防止 `待补`、`待定`、未替换模板变量留在新 case 里。

## 反方

- 增加更多脚本规则可能造成历史 case warning 变多，让维护成本上升。
- 内部审计模板通过 strict，并不代表真实外部机会 case 的研究也会合格。
- 如果占位检查过严，可能误伤“解释占位风险”的文本。
- 新增 case 类型只是流程约束，不是 connector 授权或市场证据。

## 最强反对意见

本轮机制优化只能降低“内部 case 误报完成”的风险，不能替代真实外部反馈或 connector 探针。

## 收窄后的判断

继续落地，但把结论限定为内部工作流机制优化。对外部机会、插件 connector 和真实反馈仍必须按具体 case 重新验证。

## 判断

---
type: thesis
status: accepted
updated_at: 2026-06-21
gate: passed
---



## 当前结论

继续使用当前 SignalProof 工作流，但把本轮发现的两个缺口升级为机制：

- 新 case strict 检查必须识别未完成占位标记。
- 内部流程审计必须使用独立 case 类型，避免套用外部机会验证口径。

## 最小切口

只改本地优先的协议资产：`scripts/`、`templates/`、`docs/`、`AGENTS.md`、repo skill 和本次 case 记录。

## 不做清单

- 不做真实发布。
- 不做真实用户反馈收集。
- 不做 SaaS。
- 不做 Web dashboard。

## 成功标准

- 必需阶段文件完整。
- 工具覆盖账本完整。
- 流程日志能复盘每轮优化。
- 指定验证命令全部通过。
- 新 case strict 检查能阻止 `TODO`、`待补`、`待定` 和未替换模板变量。
- 本次 case 明确真实反馈为空，不写成市场验证。

## 放弃条件

- case 文件无法产生可复用规则。
- 自检发现反复过度声称。
- 工具账本无法帮助下一轮优化。

## 验证计划

---
type: validation
status: completed
updated_at: 2026-06-21
gate: passed
---



## 验证对象

SignalProof 是否能把“报告里发现的缺口”升级成脚本、模板或文档中的可复用机制。

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
- Browser / Chrome / Computer Use / Record & Replay：本轮没有网页、登录态、GUI 或录制验收目标。
- Documents / PDF / Spreadsheets / Presentations：本轮交付物是 Markdown、模板和 Python 脚本，不需要格式插件验收。

## 成功标准

自检通过，并且流程自检能指出至少一个下一轮优化点。

## 已完成验证

| 验证项 | 结果 | 判断 |
| --- | --- | --- |
| Python 语法检查 | `python3 -m py_compile scripts/signalproof.py` 通过 | passed |
| 新 case 类型生成 | `init-case ... --case-type internal-audit --force` 生成完整 case | passed |
| 占位 strict 检查 | 第一次 strict 抓到 `待定` 残留，修正模板后通过 | passed |
| 原报告复核 | 确认原报告部分准确，但内部审计模板和占位检查仍未落地 | passed-with-gaps |
| 插件调用质量 | 本轮未调用外部 connector；原因是不会改变内部脚本判断，不能写成插件证据 | passed |

## 最终验证命令

最终验证以本 case 完成后的命令输出为准：

```bash
python3 scripts/signalproof.py check-plugin-drift
python3 scripts/signalproof.py check-case 2026-06-21-signalproof-工作流优化二次审视 --strict
python3 scripts/signalproof.py export-all
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py check-goal --min-cases 5
git diff --check
```

## 最终验证结果

| 命令 | 结果 | 说明 |
| --- | --- | --- |
| `python3 scripts/signalproof.py check-plugin-drift` | passed | 锁定清单 36、安装脚本 36、当天状态快照脚本 36、当天状态快照已安装 36、当前 `codex plugin list` 已安装 36，全部一致。 |
| `python3 scripts/signalproof.py check-case 2026-06-21-signalproof-工作流优化二次审视 --strict` | passed | 本次 case 无 warning，无未完成占位标记。 |
| `python3 scripts/signalproof.py export-all` | passed | 导出 13 份报告并更新报告索引。 |
| `python3 scripts/signalproof.py check-all` | passed-with-warnings | 13 个 case，failures 0；旧 case 暴露历史占位和研究质量门 warning。 |
| `python3 scripts/signalproof.py check-goal --min-cases 5` | passed | cases: 13；报告索引存在。 |
| `git diff --check` | passed | 无空白错误。 |

## 验证解释

这些命令证明本轮内部工作流机制已落地并通过本地检查；它们不证明外部账号授权成功，也不证明 connector 可读取真实数据，更不证明市场需求成立。

## 产物

---
type: artifact
status: completed
updated_at: 2026-06-21
gate: passed
---



## 产物

本 case 的产物是一次 SignalProof 工作流机制优化：脚本能识别未完成占位标记，模板能区分内部流程审计与外部机会验证。

## 文件

- `scripts/signalproof.py`：新增 `check-case` 的未完成占位标记检查、`CASE_TYPE_PRESETS` 和 `--case-type internal-audit`。
- `templates/case/`：按 case 类型渲染关键块，内部审计 case 不再默认带外部机会验证话术。
- `AGENTS.md`：补充 internal-audit 创建命令和 strict 占位检查边界。
- `.agents/skills/signalproof/SKILL.md`：补充 internal-audit 和 strict 使用规则。
- `docs/protocol.md`：新增 Case 类型说明和 strict 占位检查说明。
- `docs/research-quality-gate.md`：新增新 case 严格检查说明。
- `vault/cases/2026-06-21-signalproof-工作流优化二次审视/`：记录本次优化闭环。

## 原报告处理

本轮没有顺着原报告说满分，也没有把它否定成空报告。判断是：

- 原报告对 `passed-with-gaps`、插件分层、真实反馈为空、不能市场验证的结论准确。
- 原报告已经落地 `check-plugin-drift` 和 `check-case --strict`，所以不是“写得像完成”。
- 原报告仍留下可落地缺口：strict 未识别半成品占位，内部审计 case 没有独立类型。

## 产物边界

这是内部协议产物，不是市场验证产物。

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

本 case 是内部流程优化，没有发布、访谈、公开评论或产品指标；真实反馈为空。

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

继续使用当前工作流，但把本轮发现的缺口落实为确定性检查和模板约束。

## 理由

- 本轮目标是验证 SignalProof 流程和自动化，而不是市场。
- 真实反馈为空，因此只能做内部继续/收窄判断。
- 原自审报告方向准确，但还留下了“internal-audit 模板”和“未完成占位 strict 检查”两个可落地缺口。
- 本轮已经把这两个缺口落到脚本、模板和文档，不只是继续写复盘。

## 下一步

- 提交前运行指定验证命令。
- 后续真实机会 case 继续用 `external-opportunity`，完成前必须清理占位标记。
- 后续内部审计和流程优化 case 使用 `--case-type internal-audit`。
- connector 可读性仍按具体 case 探针，不把插件安装写成授权成功。

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

SignalProof 工作流优化二次审视 证明案例

## 资产类型

内部流程审计和机制优化案例。

## 可复用内容

- 严格检查未完成占位标记的脚本规则。
- `internal-audit` case 类型。
- 中文 case 记录模板。
- 复核原报告时区分“已落地机制”和“仍是建议”的判断口径。

## 可复用边界

只能证明内部流程能力，不能证明外部需求。

## 使用方式

内部审计或流程优化 case：

```bash
python3 scripts/signalproof.py init-case "<标题>" --case-type internal-audit
python3 scripts/signalproof.py check-case <case-slug> --strict
```

外部机会 case：

```bash
python3 scripts/signalproof.py init-case "<标题>" --case-type external-opportunity
```

外部机会 case 可以在创建初期保留研究缺口，但声称完成前必须清理占位标记，并把缺口改写成真实来源、明确跳过原因或证据等级。

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
| research | passed-with-gaps | 已复核原报告、脚本 diff、模板和文档；外部市场证据为空。 |
| debate | passed | 已记录“原报告不是空转”与“仍不能替代真实反馈”的两侧论点。 |
| thesis | passed | 已明确只做本地工作流机制优化。 |
| validation | passed | 已用 strict 检查验证新模板，并准备最终命令验收。 |
| artifact | passed | 已更新脚本、模板、文档和本 case。 |
| feedback | weak | 真实反馈为空。 |
| decision | passed | 决策限定为继续内部机制优化。 |
| asset | passed | 已沉淀为 strict 占位检查和 internal-audit case 类型。 |

## 证据质量

- 强：文件级产物和脚本自检。
- 中：最近自审 case、历史记忆中的插件审计口径、插件流程文档。
- 弱：真实用户反馈、真实 before/after、发布渠道反馈。

## 研究准确性质量门

| 检查项 | 状态 | 说明 |
| --- | --- | --- |
| 来源覆盖 | medium | 内部审计覆盖仓库文件、脚本、模板、文档和 case；公开讨论只覆盖当前用户任务。 |
| 交叉验证 | medium | 已用原报告、diff、strict 失败再修正、模板生成结果互相验证。 |
| 结论许可 | medium | 当前只能支持内部机制优化，不能支持市场验证。 |
| 用户授权缺口 | weak / optional | Full Disk Access 已是诊断项；X API credits 默认记为暂缺但非阻断；Readwise、Scite、Semrush、Similarweb、Brand24 按具体 case 做只读探针。 |

## 过度声称检查

没有把真实反馈为空写成验证成功。

## 本轮已落地优化

- `scripts/signalproof.py` 新增未完成占位标记检查，覆盖 `TODO`、`TBD`、`待补`、`待定` 和未替换模板变量。
- `scripts/signalproof.py` 新增 `CASE_TYPE_PRESETS`，`init-case` 支持 `--case-type internal-audit`。
- `templates/case/` 改为按 case 类型渲染关键内容，内部审计 case 不再默认套外部机会验证口径。
- `AGENTS.md`、`.agents/skills/signalproof/SKILL.md`、`docs/protocol.md`、`docs/research-quality-gate.md` 补充 strict 和 internal-audit 规则。
- 本次 case 用新模板生成，并通过 strict 检查。

## 仍未解决

- 旧 case 中仍有历史 `待定` 或研究质量门 warning；本轮不批量改旧材料，避免改写历史证据。
- Readwise、Scite、Semrush、Similarweb、Brand24 等 connector 仍未在具体 case 中证明可读。
- 真实外部反馈为空，不能证明 SignalProof 对其他用户有效。

## 下一轮优化空间

- 对一个真实外部机会 case 跑完整研究质量门。
- 对一个调研增强 connector 做只读探针。
- 需要视觉验收的报告再用 Browser 预览，不默认加入本轮 gate。

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

| 阶段 | 候选 Codex 插件 | 是否使用 | 结果质量 | 跳过或失败原因 | 下一步 |
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

本 case 的工具使用足够支持内部协议验证，但不能支持外部市场判断。

## 过程日志

---
type: process_log
status: completed
updated_at: 2026-06-21
gate: passed
---



## Iteration / 迭代 1：读取规则和用户约束

命令：

```bash
sed -n '1,220p' AGENTS.md
sed -n '1,260p' .agents/skills/signalproof/SKILL.md
sed -n '1,260p' docs/protocol.md
sed -n '1,260p' docs/research-quality-gate.md
sed -n '1,300p' docs/codex-plugin-flow.md
```

结果：

- 确认本仓库保持本地优先，不做 Web App、SaaS dashboard、workflow builder 或通用知识库。
- 确认每个 case 必须包含 13 个必需文件。
- 确认插件安装、工具暴露、账号授权和证据质量必须分层。

Self-check / 自检：

- 本轮只做内部流程优化，不做市场验证。

Optimization / 优化：

- 优先寻找能落到脚本或模板的机制缺口。

## Iteration / 迭代 2：复核最近自审 case

命令：

```bash
sed -n '1,260p' vault/cases/2026-06-21-signalproof-当前工作流自审/report.md
sed -n '1,260p' vault/cases/2026-06-21-signalproof-当前工作流自审/flow-review.md
sed -n '1,260p' vault/cases/2026-06-21-signalproof-当前工作流自审/tool-ledger.md
sed -n '1,240p' vault/cases/2026-06-21-signalproof-当前工作流自审/decision.md
git diff -- AGENTS.md .agents/skills/signalproof/SKILL.md docs/protocol.md docs/research-quality-gate.md scripts/signalproof.py
```

结果：

- 原报告 `passed-with-gaps` 判断基本准确。
- `check-plugin-drift` 和 `check-case --strict` 已经进入脚本，不是只写报告。
- 仍有可落地缺口：内部审计 case 类型未进入 `init-case`，strict 未识别 `待补`、`待定` 和未替换模板变量。

Self-check / 自检：

- 没有把原报告一概否定；区分已落地机制和仍是建议。

Optimization / 优化：

- 选择“未完成占位检查”和“internal-audit case 类型”作为本轮高价值改进。

## Iteration / 迭代 3：修改脚本和模板

命令：

```bash
python3 -m py_compile scripts/signalproof.py
```

结果：

- `scripts/signalproof.py` 新增未完成占位标记检查。
- `scripts/signalproof.py` 新增 `CASE_TYPE_PRESETS` 和 `--case-type internal-audit`。
- `templates/case/` 改为按 case 类型渲染 signal、research、tool-ledger、validation、feedback、decision、asset、artifact、report。
- `AGENTS.md`、repo skill、`docs/protocol.md`、`docs/research-quality-gate.md` 已补规则。
- Python 语法检查通过。

Self-check / 自检：

- 没有修改成 Web App 或 SaaS。
- 没有把插件调用写成证据合格。

Optimization / 优化：

- 新 strict 检查会把未完成占位变成 warning；配合 `--strict` 后新 case 会失败。

## Iteration / 迭代 4：创建并校验本次 case

命令：

```bash
python3 scripts/signalproof.py init-case "SignalProof 工作流优化二次审视" --case-type internal-audit --signal "复核最近 SignalProof 自审报告，判断哪些结论可靠、哪些只是建议，并把最高价值改进落地为本地脚本、模板和文档约束。" --force
python3 scripts/signalproof.py check-case 2026-06-21-signalproof-工作流优化二次审视 --strict
```

结果：

- 第一次 strict 抓到了模板里的 `待定` 残留。
- 修正模板候选能力行后，本 case strict 通过。

Self-check / 自检：

- 这证明新增 gate 有实际价值：它抓到的不是抽象问题，而是本轮新模板里的真实残留。

Optimization / 优化：

- 本 case 作为 `internal-audit` 样例保留，后续内部审计可复用。
