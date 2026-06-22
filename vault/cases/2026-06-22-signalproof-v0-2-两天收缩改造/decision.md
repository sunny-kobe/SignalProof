---
type: decision
status: accepted-internal
decision: continue-internal-protocol-validation
updated_at: 2026-06-22
gate: passed
---

# 决策

## 决策

接受 V0.2 收缩改造：SignalProof 当前按个人证据协议执行，新外部机会默认 lite，full 只作为满足硬条件后的升级事件。

## 理由

- 本轮目标是优化个人工作流和 SignalProof 机制，不是外部机会验证。
- 内部流程反馈只能证明机制是否更好用，不能证明市场需求。

## 下一步

- 完成本 case strict 和最终验证。
- 不重写历史 warning，只把它们作为历史债保留。
- 下一步可以开始 5 个 lite 外部信号实验，用 V0.2 模板检验真实使用成本。

## 边界

真实反馈为空，内部流程测试不能写成市场验证、产品化或 SaaS 结论。
