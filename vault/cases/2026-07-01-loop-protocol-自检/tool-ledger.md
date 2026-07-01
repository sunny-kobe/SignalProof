---
type: tool_ledger
status: completed
updated_at: 2026-07-01
gate: passed
---

# 工具账本

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
