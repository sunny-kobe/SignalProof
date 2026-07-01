---
type: signal
title: {{title}}
case_type: {{case_type}}
case_intent: {{case_intent}}
case_mode: {{case_mode}}
protocol_scope: personal-evidence-protocol
loop_profile: {{loop_profile}}
agentic_loop: {{agentic_loop}}
developer_feedback_loop: {{developer_feedback_loop}}
external_feedback_loop: {{external_feedback_loop}}
asset_loop: {{asset_loop}}
status: captured
created_at: {{created_at}}
gate: passed
---

# 信号

## 原始信号

{{signal}}

## 为什么值得进入流程

{{why_enter_flow}}

## 初步用户

{{initial_users}}

## 当前边界

{{current_boundary}}

## Loop Profile

| Loop | 状态 | 说明 |
| --- | --- | --- |
| agentic coding | {{agentic_loop}} | 需要 Product Spec 和 Eval Set 时才启动 AI 构建循环。 |
| developer feedback | {{developer_feedback_loop}} | 用户用上下文优势修正方向、边界和下一轮 spec。 |
| external feedback | {{external_feedback_loop}} | 有真实发布、访谈、alpha、A/B、评论或指标时才写成外部反馈。 |
| asset/meta | {{asset_loop}} | 把本轮有效输出沉淀为模板、检查表、脚本、skill 或资产账本条目。 |
