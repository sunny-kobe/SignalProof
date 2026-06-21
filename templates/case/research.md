---
type: research
status: completed
updated_at: {{created_at}}
gate: weak
---

# 研究

## 要回答的问题

- 这个信号背后最真实的问题是什么？
- 哪些证据足够支撑继续内部验证？
- 哪些证据缺口会阻止对外验证或产品化？
- 当前结论到底是 strong、medium、weak 还是 blocked？

## 已确认事实

- SignalProof 当前阶段是 Codex 协议 MVP。
- 真实外部反馈和发布渠道在本轮被用户明确暂时跳过。
- 研究阶段必须记录候选能力和结果质量。
- 研究准确性按 `docs/research-quality-gate.md` 判断，工具调用不等于证据合格。

## 调研过程

- 使用本地上下文、已有 SignalProof 产物、Codex 官方手册摘要和脚本自检。
- 如涉及最近趋势，`last30days` 是候选能力；若没有实际运行，必须在 `tool-ledger.md` 写原因。

## 来源覆盖表

| 来源类型 | 候选能力 | 当前状态 | 结果质量 | 缺口 |
| --- | --- | --- | --- | --- |
| 公开讨论 | last30days / Reddit / HN / X / YouTube / Browser / Chrome | 待补 | weak | 未确认目标用户原话。 |
| 项目和数据 | GitHub / Hugging Face / Similarweb / Semrush | 待补 | weak | 未确认可核验指标。 |
| 官方和一手资料 | 官方文档 / OpenAI Docs / PDF / Documents | 待补 | weak | 未确认直接来源。 |
| 反证和替代方案 | Scite / Readwise / Zotero / 竞品文档 / GitHub issues | 待补 | weak | 未确认强替代或失败风险。 |

## 交叉验证

- 谁在说：待补。
- 说什么：待补。
- 在哪里说：待补。
- 有没有反证：待补。
- 能支持什么结论：当前只能支持内部流程实验或继续补研究。

## 反证和替代方案

- 待补成熟替代方案。
- 待补失败案例或低意愿证据。
- 待补“用户现在怎么解决”的证据。

## 证据等级

当前为弱到中等证据：足够支持内部流程实验，不足以支持市场验证。

## 结论许可

当前许可：继续研究 / 低成本内部实验。不得写成已验证需求、市场已验证、可以产品化或可以做 SaaS。

## 需要用户授权或开通

- 若需要 X/Twitter 来源：先把 X API credits 记为暂缺但非阻断；只有 case 高度依赖 X 实时讨论、早期热度或 KOL 扩散时再提醒补 credits。
- 若需要浏览器 cookie：先运行 `python3 scripts/signalproof.py diagnose`，根据结果判断是否需要用户处理 Full Disk Access。
- 若需要 Readwise、Scite、Semrush、Similarweb、Brand24：按真实 case 做只读探针，不默认全开。

## 证据缺口

- 真实用户原话为空。
- 真实发布反馈为空。
- 真实 before/after 为空。

## 下一步补证

- 补 1 个公开讨论来源。
- 补 1 个项目或数据指标。
- 补 1 个官方或一手资料。
- 补 1 个反证或替代方案。

继续内部协议验证。
