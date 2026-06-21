---
type: validation
status: planned
updated_at: 2026-06-21
gate: passed
---

# 验证计划

## 验证对象

SignalProof 能否把 `研究准确性质量门与授权缺口` 固化到文档、模板和脚本检查中，并保持边界清晰。

## 验证方式

1. 生成完整阶段文件。
2. 补充工具账本。
3. 补充流程日志。
4. 运行 `python3 scripts/signalproof.py check-all`。
5. 运行 `python3 scripts/signalproof.py check-goal --min-cases 5`。
6. 运行 `python3 scripts/signalproof.py export-all`。
7. 记录优化空间。

## 跳过项

- 真实外部反馈：本轮跳过。
- 发布渠道：本轮跳过。
- 批量分发渠道：本轮跳过。

## 成功标准

自检通过，研究 gate 资产存在，并且流程自检能指出至少一个下一轮优化点。
