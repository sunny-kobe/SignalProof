---
type: decision
status: completed
updated_at: 2026-06-21
gate: passed-with-gaps
---

# 决策

## 决策

继续使用当前 SignalProof 工作流，并把它标记为 `passed-with-gaps`。

二次验收后补充判断：原报告方向正确，但它当时只完成了“发现问题”，还没有完成“改进工作流”。因此本轮把两项最关键缺口落地为确定性检查：

- 新增 `python3 scripts/signalproof.py check-plugin-drift`，用于检查插件锁定清单、安装脚本、当天状态快照和当前安装列表是否漂移。
- 新增 `python3 scripts/signalproof.py check-case <case-slug> --strict`，用于让新 case 的 warning 直接失败，避免研究质量门只停留在人工提醒。

## 依据

- 真实反馈为空，因此本轮不做市场判断。
- 内部流程证据足以说明：当前工作流能生成 case、记录证据质量、导出报告并通过目标检查。
- 旧 case warning 说明流程已经能发现历史缺口，但还没有完全自动修复或阻止旧口径漂移。
- 插件状态和迁移说明已经基本闭环，但 connector 授权和真实数据读取仍需在具体 case 中验证。

## 下一步优先级

1. 选择一个真实机会 case，跑外部来源覆盖，而不是继续只做内部流程完善。
2. 对一个调研增强 connector 做只读探针，确认它是否能进入证据链。
3. 后续考虑给 `init-case` 增加内部审计类默认模板。

## 明确不做

- 不立刻做 Web App。
- 不立刻做 SaaS。
- 不把所有插件默认全跑。
- 不把 X API credits 当作当前必付项。
- 不把内部流程反馈写成外部验证。
