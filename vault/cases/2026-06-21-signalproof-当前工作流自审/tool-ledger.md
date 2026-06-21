---
type: tool_ledger
status: completed
updated_at: 2026-06-21
gate: passed-with-gaps
---

# 工具账本

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
