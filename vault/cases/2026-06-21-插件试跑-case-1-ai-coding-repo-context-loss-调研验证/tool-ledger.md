---
type: tool_ledger
status: completed
updated_at: 2026-06-21
gate: passed
---

# 工具账本

## 候选能力账本

| 能力 | 是否相关 | 是否使用 | 结果质量 | 说明 | 下次动作 |
| --- | --- | --- | --- | --- | --- |
| Skill: signalproof | 是 | 是 | 中 | repo 级 skill 提供本地流程规则。 | 保留。 |
| Skill: personal-opportunity-os | 是 | 是 | 中 | 提供长期方向和流程边界。 | 保留为上层方法论。 |
| Skill: last30days | 是 | 是 | 中 | 实际运行，得到 13 条证据，覆盖 GitHub/Reddit/YouTube；X/HN 缺失。 | 默认候选，但必须记录来源缺口。 |
| Browser | 低 | 否 | 未使用 | 本 case 是调研输出，不需要页面验收；主 case 已记录 Browser setup 失败。 | 有公开页面或报告预览时再用。 |
| Computer Use | 低 | 否 | 未使用 | 本 case 不需要 GUI；主 case 已记录 Codex App 状态读取失败。 | GUI-only 验证时再用。 |
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
| signal | Browser / Chrome / Record & Replay | 否 | not-needed | 信号来自用户要求和本地 case，不依赖网页或录制。 | 保留为候选。 |
| research | last30days / GitHub / Browser / Chrome | 是 | 中 | `last30days` 成功；X/HN/YouTube 评论有缺口。 | 更窄 query 补跑。 |
| debate | Browser / Chrome / Documents / PDF | 否 | not-needed | 本轮争论点来自调研输出，不需要长文档反证。 | 论文或长文档 case 再启用。 |
| validation | Browser / Computer Use / Spreadsheets | 部分 | weak | 以原始输出文件和脚本自检验收；未用 GUI。 | 总 case 继续记录 Browser/Computer Use 失败。 |
| artifact | Documents / PDF / Spreadsheets / Presentations / HyperFrames / Data Visualization | 否 | not-needed | 本 case 产物是 Markdown 和原始调研文件。 | 产物类见 case 3。 |
| publication | Browser / Chrome | 否 | not-needed | 未发布。 | 发布阶段再启用。 |
| feedback | Chrome / Browser / Spreadsheets / Record & Replay | 否 | not-needed | 真实反馈为空。 | 有反馈源再启用。 |
| asset | Record & Replay / Spreadsheets / Documents | 否 | not-needed | 本资产是调研记录，不需要录制或表格。 | 可汇入总插件矩阵。 |
| flow-review | Browser / Computer Use / Documents / PDF / Spreadsheets / Presentations | 部分 | 中 | 通过文件级检查和后续 `check-all` 验证。 | 保留降级验收路径。 |

## 能力结论

本 case 证明 `last30days` 对调研初筛有价值，但当前结果为弱到中证据，不能支持外部市场判断。
