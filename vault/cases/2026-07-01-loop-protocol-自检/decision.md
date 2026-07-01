---
type: decision
status: accepted-internal
decision: continue-internal-protocol-validation
updated_at: 2026-07-01
gate: passed
---

# 决策

## 决策

继续使用当前工作流，但把本轮发现的缺口落实为确定性检查和模板约束。

## 理由

- 本轮目标是优化个人工作流和 SignalProof 机制，不是外部机会验证。
- 内部流程反馈只能证明机制是否更好用，不能证明市场需求。

## 下一步

- 如果本 case 暴露流程缺口，把缺口写入 `flow-review.md`。
- 如果缺口可脚本化，更新 `scripts/signalproof.py`、模板或协议文档。
- 如果下一步涉及真实机会，另开外部机会 case。

## 下一轮 Loop 决策

- 改 spec：当 Product Spec 或 Eval Set 不能指导 AI 执行。
- 改产物：当产物和用户任务、内容目标或工作流目标不匹配。
- 改反馈渠道：当外部反馈为空或不命中真实目标人。
- 停止：当证据不足、反证强或继续成本高于潜在资产价值。

## 边界

真实反馈为空，内部流程测试不能写成市场验证、产品化或 SaaS 结论。
