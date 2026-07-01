---
type: signal
title: Loop Protocol 自检
case_type: internal-audit
case_intent: workflow-improvement
case_mode: full
protocol_scope: personal-evidence-protocol
loop_profile: ai-work-loop-v1
agentic_loop: optional
developer_feedback_loop: required
external_feedback_loop: skipped-with-reason
asset_loop: required
status: captured
created_at: 2026-07-01
gate: passed
---

# 信号

## 原始信号

Loop Protocol 自检

## 为什么值得进入流程

- 这条信号用于检验 SignalProof 工作流本身是否能发现并修正流程缺口。
- 本 case 的价值来自本地文档、模板、脚本和 case 记录的可执行改进，而不是外部市场反馈。

## 初步用户

- SignalProof 维护者。
- 高频使用 Codex / Claude Code / MCP / 本地 AI coding 工作流，并希望把判断过程沉淀成可审计资产的人。

## 当前边界

- 不声称市场验证。
- 不默认产品化。
- 不做 SaaS、dashboard、workflow builder 或通用知识库。
- 内部流程反馈只能支持机制优化，不能支持外部需求成立。

## Loop Profile

| Loop | 状态 | 说明 |
| --- | --- | --- |
| agentic coding | optional | 需要 Product Spec 和 Eval Set 时才启动 AI 构建循环。 |
| developer feedback | required | 用户用上下文优势修正方向、边界和下一轮 spec。 |
| external feedback | skipped-with-reason | 有真实发布、访谈、alpha、A/B、评论或指标时才写成外部反馈。 |
| asset/meta | required | 把本轮有效输出沉淀为模板、检查表、脚本、skill 或资产账本条目。 |
