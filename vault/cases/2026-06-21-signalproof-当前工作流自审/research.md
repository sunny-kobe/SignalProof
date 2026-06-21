---
type: research
status: completed
updated_at: 2026-06-21
gate: medium
---

# 研究

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
