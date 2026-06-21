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
| Computer Use | 视 GUI 而定 | 待定 | 中 / conditional | 适合只能通过 GUI 操作的验证；具体 App 状态可能受系统权限影响。 | 有 GUI 验收目标时再用。 |
| Plugin | 是 | 是 | 中 | 先运行 `codex plugin list` 和 `python3 scripts/signalproof.py plugin-status` 复核安装状态。 | 按 case 选择，不默认全跑。 |
| MCP | 中 | 否 | 弱 | 可接 OpenAI Docs、Context7、GitHub 等，但本轮先记录映射。 | 后续按阶段接入。 |
| Hooks | 中 | 否 | 弱 | 可用于强制 check-case。 | 后续加入。 |
| Automation | 中 | 否 | 弱 | 可用于 72h 反馈复查。 | 等发布渠道恢复后启用。 |

## 研究准确性账本

按 `docs/research-quality-gate.md` 记录研究阶段是否真的能支持结论，必须覆盖来源覆盖、交叉验证、反证、证据等级、结论许可和用户授权缺口：

| 检查项 | 是否覆盖 | 证据等级 | 说明 | 下一步 |
| --- | --- | --- | --- | --- |
| 公开讨论 | 待定 | weak | 需要目标用户原话、抱怨、采用或反对意见；X API credits 默认暂缺但非阻断。 | 优先补 last30days / HN / Reddit / YouTube / GitHub；必要时再提醒补 X。 |
| 项目和数据 | 待定 | weak | 需要 GitHub、下载、访问、流量或产品指标。 | 补 GitHub / Hugging Face / Similarweb / Semrush。 |
| 官方和一手资料 | 待定 | weak | 需要官方文档、API、价格、论文或一手说明。 | 补官方文档 / OpenAI Docs / PDF。 |
| 反证和替代方案 | 待定 | weak | 需要成熟替代、失败案例或低意愿证据。 | 补 Scite / Readwise / Zotero / 竞品文档。 |
| 结论许可 | 待定 | weak | weak 只能支持继续研究或低成本内部实验。 | 证据未升到 medium/strong 前不写产品化。 |

## 阶段能力计划

运行：

```bash
python3 scripts/signalproof.py capabilities
```

然后把本 case 各阶段真正考虑过的 Codex 自带插件记录到这里：

| 阶段 | 候选 Codex 插件 | 是否使用 | 结果质量 | 跳过或失败原因 | 下一步 |
| --- | --- | --- | --- | --- | --- |
| signal | Browser / Chrome / Record & Replay | 待定 | 待定 | 待定 | 待定 |
| research | GitHub / last30days / OpenAI Docs / Hugging Face / Readwise / Scite / Semrush / Similarweb / Brand24 / Zotero / Browser / Chrome / Documents / PDF / Spreadsheets / Data Visualization | 待定 | 待定 | 待定 | 待定 |
| debate | Browser / Chrome / Documents / PDF | 待定 | 待定 | 待定 | 待定 |
| validation | Browser / Computer Use / Documents / PDF / Spreadsheets / Presentations | 待定 | 待定 | 待定 | 待定 |
| artifact | Documents / PDF / Spreadsheets / Presentations / HyperFrames / Data Visualization | 待定 | 待定 | 待定 | 待定 |
| publication | Browser / Chrome | 待定 | 待定 | 待定 | 待定 |
| feedback | Chrome / Browser / Spreadsheets / Record & Replay | 待定 | 待定 | 待定 | 待定 |
| asset | Documents / PDF / Spreadsheets / Presentations / Record & Replay / Browser | 待定 | 待定 | 待定 | 待定 |
| flow-review | Browser / Computer Use / Documents / PDF / Spreadsheets / Presentations | 待定 | 待定 | 待定 | 待定 |

## 能力结论

本 case 的工具使用足够支持内部协议验证，但不能支持外部市场判断。
