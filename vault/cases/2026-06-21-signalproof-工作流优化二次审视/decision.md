---
type: decision
status: accepted-internal
decision: continue-internal-protocol-validation
updated_at: 2026-06-21
gate: passed
---

# 决策

## 决策

继续使用当前工作流，但把本轮发现的缺口落实为确定性检查和模板约束。

## 理由

- 本轮目标是验证 SignalProof 流程和自动化，而不是市场。
- 真实反馈为空，因此只能做内部继续/收窄判断。
- 原自审报告方向准确，但还留下了“internal-audit 模板”和“未完成占位 strict 检查”两个可落地缺口。
- 本轮已经把这两个缺口落到脚本、模板和文档，不只是继续写复盘。

## 下一步

- 提交前运行指定验证命令。
- 后续真实机会 case 继续用 `external-opportunity`，完成前必须清理占位标记。
- 后续内部审计和流程优化 case 使用 `--case-type internal-audit`。
- connector 可读性仍按具体 case 探针，不把插件安装写成授权成功。

## 边界

真实反馈为空，不能声称验证成功。
