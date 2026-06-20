---
type: validation
status: planned
updated_at: {{created_at}}
gate: passed
---

# 验证计划

## 验证对象

SignalProof 协议是否能把 `{{title}}` 跑成完整、可检查、可复用的 case。

## 验证方式

1. 生成完整阶段文件。
2. 补充工具账本。
3. 补充流程日志。
4. 运行 `python3 scripts/signalproof.py check-all`。
5. 运行 `python3 scripts/signalproof.py export-all`。
6. 记录优化空间。

## 跳过项

- 真实外部反馈：本轮跳过。
- 发布渠道：本轮跳过。

## 成功标准

自检通过，并且流程自检能指出至少一个下一轮优化点。
