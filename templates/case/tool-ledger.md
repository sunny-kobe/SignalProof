---
type: tool_ledger
status: completed
updated_at: {{created_at}}
gate: passed
---

# 工具账本

## 候选能力账本

| 能力 | 是否相关 | 是否使用 | 结果质量 | 说明 | 下次动作 |
| --- | --- | --- | --- | --- | --- |
| Skill: signalproof | 是 | 是 | 中 | repo 级 skill 提供本地流程规则。 | 保留。 |
| Skill: personal-opportunity-os | 是 | 是 | 中 | 提供长期方向和流程边界。 | 保留为上层方法论。 |
| Skill: last30days | 视研究主题而定 | 待定 | 弱 | 本轮批量内部 case 不强制跑完整外部研究；能力已诊断可用。 | 对真实趋势 case 用 `python3.14` 跑 `--days=3` 或 `--days=7`。 |
| Browser | 视产物而定 | 待定 | 中 | 适合验证本地报告页面或文件预览。 | 对 HTML 报告预览使用。 |
| Computer Use | 低 | 否 | 失败 | 插件文件存在，但本轮没有直接暴露 UI 控制工具。 | 后续若工具可用，再用于只能通过 GUI 操作的验证。 |
| Plugin | 是 | 是 | 中 | 已建立插件草案骨架。 | 后续安装测试。 |
| MCP | 中 | 否 | 弱 | 可接 OpenAI Docs、Context7、GitHub 等，但本轮先记录映射。 | 后续按阶段接入。 |
| Hooks | 中 | 否 | 弱 | 可用于强制 check-case。 | 后续加入。 |
| Automation | 中 | 否 | 弱 | 可用于 72h 反馈复查。 | 等发布渠道恢复后启用。 |

## 阶段能力计划

运行：

```bash
python3 scripts/signalproof.py capabilities
```

然后把本 case 各阶段真正考虑过的 Codex 自带插件记录到这里：

| 阶段 | 候选 Codex 插件 | 是否使用 | 结果质量 | 跳过或失败原因 | 下一步 |
| --- | --- | --- | --- | --- | --- |
| signal | Browser / Chrome / Record & Replay | 待定 | 待定 | 待定 | 待定 |
| research | Browser / Chrome / Documents / PDF / Spreadsheets / Data Visualization | 待定 | 待定 | 待定 | 待定 |
| debate | Browser / Chrome / Documents / PDF | 待定 | 待定 | 待定 | 待定 |
| validation | Browser / Computer Use / Documents / PDF / Spreadsheets / Presentations | 待定 | 待定 | 待定 | 待定 |
| artifact | Documents / PDF / Spreadsheets / Presentations / HyperFrames / Data Visualization | 待定 | 待定 | 待定 | 待定 |
| publication | Browser / Chrome | 待定 | 待定 | 待定 | 待定 |
| feedback | Chrome / Browser / Spreadsheets / Record & Replay | 待定 | 待定 | 待定 | 待定 |
| asset | Documents / PDF / Spreadsheets / Presentations / Record & Replay / Browser | 待定 | 待定 | 待定 | 待定 |
| flow-review | Browser / Computer Use / Documents / PDF / Spreadsheets / Presentations | 待定 | 待定 | 待定 | 待定 |

## 能力结论

本 case 的工具使用足够支持内部协议验证，但不能支持外部市场判断。
