---
type: tool_ledger
status: completed
updated_at: 2026-06-22
gate: passed
---

# 工具账本

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
