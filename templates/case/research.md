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

{{research_process}}

## 来源覆盖表

| 来源类型 | 候选能力 | 当前状态 | 结果质量 | 缺口 |
| --- | --- | --- | --- | --- |
{{source_coverage_rows}}

## 交叉验证

{{cross_validation}}

## 反证和替代方案

{{counterevidence}}

## 证据等级

{{evidence_grade}}

## 结论许可

{{decision_permission}}

## 需要用户授权或开通

- 若需要 X/Twitter 来源：先把 X API credits 记为暂缺但非阻断；只有 case 高度依赖 X 实时讨论、早期热度或 KOL 扩散时再提醒补 credits。
- 若需要浏览器 cookie：先运行 `python3 scripts/signalproof.py diagnose`，根据结果判断是否需要用户处理 Full Disk Access。
- 若需要 Readwise、Scite、Semrush、Similarweb、Brand24：按真实 case 做只读探针，不默认全开。

## 证据缺口

- 真实用户原话为空。
- 真实发布反馈为空。
- 真实 before/after 为空。

## 下一步补证

{{next_evidence_steps}}
