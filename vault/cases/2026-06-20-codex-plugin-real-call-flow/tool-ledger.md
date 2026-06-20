---
type: tool_ledger
title: Codex 插件实际调用流程验证
status: completed
updated_at: 2026-06-20
gate: passed
---

# 工具账本

## 候选能力账本

| 能力 | 是否相关 | 是否使用 | 结果质量 | 说明 | 下次动作 |
| --- | --- | --- | --- | --- | --- |
| Skill: personal-opportunity-os | 是 | 是 | 强 | 约束本案例不能扩大成独立应用，必须写工具覆盖和流程自检。 | 保留。 |
| Skill: user-working-profile | 是 | 是 | 中 | 对齐用户偏好：中文、证据边界、执行到结果。 | 保留。 |
| Skill: signalproof | 是 | 是 | 强 | 明确必需文件、真实反馈为空边界、工具账本规则。 | 保留。 |
| Plugin: Browser | 是 | 是 | 失败 | 按 Browser skill 接入步骤调用失败，缺 `sandboxPolicy` 字段。 | 修复或复查 Browser 运行时。 |
| Plugin: Computer Use | 是 | 是 | 强 | `list_apps` 和 `get_app_state Google Chrome` 成功。 | 作为图形界面验收降级路径。 |
| Plugin: Chrome | 中 | 否 | 弱 | Chrome 页面被 Computer Use 读取，但 Chrome 插件未直接调用。 | 登录态页面场景再补跑。 |
| Plugin: Record & Replay | 低 | 否 | 弱 | 本案例没有用户演示录制需求。 | 用户演示流程时再用。 |
| Plugin: Documents | 低 | 否 | 弱 | 本案例没有 DOCX 或长文档产物。 | 文档产物案例再用。 |
| Plugin: PDF | 低 | 否 | 弱 | 本案例没有 PDF 产物。 | PDF 导出或验收时再用。 |
| Plugin: Spreadsheets | 低 | 否 | 弱 | 本案例没有表格数据产物。 | 反馈统计或数据分析时再用。 |
| Plugin: Presentations | 低 | 否 | 弱 | 本案例没有演示文稿产物。 | 做 deck 时再用。 |
| MCP: Node REPL | 是 | 是 | 失败 | Browser 插件必须通过 Node REPL 调用，但当前 Browser 连接失败。 | 记录错误并修复环境。 |
| MCP: Computer Use | 是 | 是 | 强 | 本机应用和 Chrome 窗口状态可读。 | 保留为验证工具。 |
| last30days | 低 | 否 | 弱 | 本案例不判断最近 30 天市场讨论。 | 进入外部需求判断时再用。 |
| Git / GitHub CLI | 中 | 待补 | 弱 | Computer Use 只能看到页面，提交级状态应由 Git 确认。 | 提交前用 Git 校验。 |

## 阶段能力计划

| 阶段 | 候选 Codex 插件 | 是否使用 | 结果质量 | 跳过或失败原因 | 下一步 |
| --- | --- | --- | --- | --- | --- |
| signal | Browser / Chrome / Record & Replay | 使用 Browser 作为候选 | 失败 | Browser 连接缺 `sandboxPolicy` | 记录为信号：能力矩阵不等于真实可用 |
| research | Browser / Chrome / Documents / PDF / Spreadsheets / Data Visualization | 使用 Browser、Computer Use | 中 | Browser 失败，Computer Use 成功 | 形成插件调用证据 |
| debate | Browser / Chrome / Documents / PDF | 未额外调用 | 中 | 反方基于已取得的一手工具输出足够 | 后续补 Browser 成功路径 |
| validation | Browser / Computer Use / Documents / PDF / Spreadsheets / Presentations | 使用 Browser、Computer Use | 中 | Browser blocked，Computer Use 降级路径可用 | 补报告索引页面验收 |
| artifact | Documents / PDF / Spreadsheets / Presentations / HyperFrames / Data Visualization | 未使用 | 弱 | 本轮产物是 Markdown 和文档更新 | 对非 Markdown 产物再接入 |
| publication | Browser / Chrome | Computer Use 读取 Chrome 页面 | 中 | 没有执行发布动作 | 用 Git/GitHub CLI 确认远程状态 |
| feedback | Chrome / Browser / Spreadsheets / Record & Replay | 未使用 | 弱 | 真实反馈为空 | 等外部反馈出现后再用 |
| asset | Documents / PDF / Spreadsheets / Presentations / Record & Replay / Browser | 未使用 | 中 | 资产是流程模板，不需要格式插件 | 后续做资料包时再接入 |
| flow-review | Browser / Computer Use / Documents / PDF / Spreadsheets / Presentations | 使用 Computer Use | 中 | Browser blocked | 下次优先修复 Browser |

## 工具结果质量结论

- 强：Computer Use 读取本机应用和 Chrome 状态。
- 中：能力矩阵和 Chrome 可见页面。
- 弱：未直接调用 Chrome 插件、Documents、PDF、Spreadsheets、Presentations。
- 失败：Browser 插件真实调用。

本账本足够支持内部流程优化，不足以支持外部需求判断。
