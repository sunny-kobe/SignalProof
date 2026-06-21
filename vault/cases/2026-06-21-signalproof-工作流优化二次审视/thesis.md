---
type: thesis
status: accepted
updated_at: 2026-06-21
gate: passed
---

# 判断

## 当前结论

继续使用当前 SignalProof 工作流，但把本轮发现的两个缺口升级为机制：

- 新 case strict 检查必须识别未完成占位标记。
- 内部流程审计必须使用独立 case 类型，避免套用外部机会验证口径。

## 最小切口

只改本地优先的协议资产：`scripts/`、`templates/`、`docs/`、`AGENTS.md`、repo skill 和本次 case 记录。

## 不做清单

- 不做真实发布。
- 不做真实用户反馈收集。
- 不做 SaaS。
- 不做 Web dashboard。

## 成功标准

- 必需阶段文件完整。
- 工具覆盖账本完整。
- 流程日志能复盘每轮优化。
- 指定验证命令全部通过。
- 新 case strict 检查能阻止 `TODO`、`待补`、`待定` 和未替换模板变量。
- 本次 case 明确真实反馈为空，不写成市场验证。

## 放弃条件

- case 文件无法产生可复用规则。
- 自检发现反复过度声称。
- 工具账本无法帮助下一轮优化。
