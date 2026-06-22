---
type: tool_ledger
status: completed
updated_at: 2026-06-22
gate: passed
---

# 工具账本

## 候选能力账本

| 能力 | 是否相关 | 是否使用 | 结果质量 | 说明 | 下次动作 |
| --- | --- | --- | --- | --- | --- |
| Skill: signalproof | 是 | 是 | strong | 提供 full case 文件要求、质量门、strict 检查和边界规则。 | 保留为每个 case 默认入口。 |
| Skill: ai-content-commerce | 是 | 是 | strong | 提供内容商业化边界、账号验证、平台策略、变现路径和不做项。 | 后续内容实验继续使用。 |
| Skill: personal-opportunity-os | 是 | 是 | strong | 提供 SignalProof 从信号到资产的长期工作流框架。 | 用于跨 case 复利和资产化。 |
| Skill: last30days | 是 | 是 | medium | 运行两条近 30 天 query，命中 Reddit/GitHub/YouTube，但 X credits depleted，YouTube 评论 402，短视频源无有效命中。 | 方向收窄后对 5 个具体信号再跑。 |
| Web search | 是 | 是 | medium | 补充 QuestMobile、CMI、IAB、Stack Overflow、a16z、网信办等来源。 | 具体发布前补平台规则。 |
| Browser | 条件相关 | 未使用 | medium | 本轮没有网页交互验收目标，web 工具足够读公开来源。 | 发布页或报告预览时使用。 |
| Chrome | 条件相关 | 未使用 | medium | 本轮未授权读取登录态账号后台、评论或私信。 | 用户授权发布/查看后台后使用。 |
| Computer Use | 否 | 未使用 | medium | 本轮没有 GUI-only 操作流程。 | 需要平台后台操作时再评估。 |
| Documents / PDF / Spreadsheets / Presentations | 条件相关 | 未使用 | medium | 本轮产物为 Markdown 方向实验包，不需要格式文件。 | 做正式资料包时再使用。 |
| HyperFrames | 条件相关 | 未使用 | medium | 本轮判断方向，不制作视频。HyperFrames 是后续内容表达引擎。 | 7 天实验生成视频脚本/网页视频时使用。 |
| MCP / connector 插件 | 条件相关 | 未使用 | medium | Semrush、Similarweb、Brand24 等未暴露直接工具，且本轮不需要品牌监测。 | 进入分发/反馈阶段再做只读探针。 |

## 研究准确性账本

按 `docs/research-quality-gate.md` 记录研究阶段是否真的能支持结论，必须覆盖来源覆盖、交叉验证、反证、证据等级、结论许可和用户授权缺口：

| 检查项 | 是否覆盖 | 证据等级 | 说明 | 下一步 |
| --- | --- | --- | --- | --- |
| 公开讨论 | 是 | medium | last30days 覆盖 Reddit、GitHub、YouTube；X failed by CreditsDepleted；YouTube 评论 HTTP 402；TikTok/Instagram/Threads 结果少。 | 具体信号再跑；如依赖 X 扩散，补 credits 或降级。 |
| 项目和数据 | 是 | medium | QuestMobile、IAB、CMI、Stack Overflow、a16z 提供趋势和人群证据；GitHub 有 issues/PR 信号。 | 下一轮补具体账号/平台数据。 |
| 官方和一手资料 | 是 | medium | 网信办 AIGC 标识办法已覆盖，能证明合规边界。 | 发布前逐平台复核小红书、公众号、抖音、B站、视频号。 |
| 反证和替代方案 | 是 | medium | 已覆盖 AI slop、GEO hype、泛工具测评拥挤、AI coding 过窄、AI 视频合规和成本风险。 | 7 天实验中记录真实低意愿反馈。 |
| 证据等级 | 是 | medium | 允许低成本实验，不允许产品化或市场验证成功。 | 真实反馈后再升级或降级。 |
| 结论许可 | 是 | passed | 当前结论许可为低成本实验。 | 不能跳到 SaaS。 |
| 用户授权缺口 | 是 | medium | X credits、YouTube 评论 402、平台发布授权、Chrome 登录态均已记录。 | 发布前由用户决定账号和渠道。 |

## 阶段能力计划

运行过：

```bash
python3 scripts/signalproof.py capabilities
```

| 阶段 | 候选 Codex 插件 | 是否使用 | 结果质量 | 跳过或失败原因 | 下一步 |
| --- | --- | --- | --- | --- | --- |
| signal | Browser / Chrome / Record & Replay | 未使用 | medium | 信号来自用户文本，不需要网页或录制。 | 用户演示账号流程时再用 Record & Replay。 |
| research | last30days / Web / GitHub / Browser / Chrome / Documents / PDF / Spreadsheets / Data Visualization | 使用 last30days、Web、GitHub | medium | X credits depleted；YouTube 评论 402；未授权 Chrome 登录态；不需要 PDF/表格。 | 具体信号再补 last30days 和平台规则。 |
| debate | Browser / Chrome / Documents / PDF | 未使用 | medium | 反方基于已有研究足够。 | 若某个反证依赖长文档，再用 Documents/PDF。 |
| validation | Browser / Computer Use / Documents / PDF / Spreadsheets / Presentations | 未使用 | medium | 本轮只制定验证计划，没有 UI 或格式产物验收。 | 发布内容和资料包后再用。 |
| artifact | Documents / PDF / Spreadsheets / Presentations / HyperFrames / Data Visualization | 生成 Markdown asset | medium | 未制作正式 PDF/PPT/视频。 | 7 天实验可用 HyperFrames 和 Presentations。 |
| publication | Browser / Chrome | 未使用 | weak | 未获用户发布授权。 | 用户授权后验证公开 URL 和后台指标。 |
| feedback | Chrome / Browser / Spreadsheets / Record & Replay | 未使用 | weak | 真实反馈为空。 | 发布后用表格记录反馈。 |
| asset | Documents / PDF / Spreadsheets / Presentations / Record & Replay / Browser | 使用 Markdown registry | medium | 当前资产是方向实验包，未做资料包格式化。 | 被实验使用后更新 `last_used_by`。 |
| flow-review | Browser / Computer Use / Documents / PDF / Spreadsheets / Presentations | 未使用 | medium | 本轮报告为 Markdown，脚本检查足够。 | 正式报告展示时再预览。 |

## 能力结论

工具使用足够支持方向选择和低成本实验决策。

工具使用不足以支持市场验证、产品化或 SaaS 结论。
