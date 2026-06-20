---
type: thesis
status: proposed
updated_at: 2026-06-20
gate: passed
---

# 机会判断

## 当前判断

继续，但只继续优化 SignalProof 的“真实插件调用和工具账本”流程，不扩大成独立应用或全插件自动化系统。

## 是否继续

- 继续 / 收窄 / 暂停 / 放弃：继续，范围收窄到案例级插件调用闭环。

## 第一批用户

- 当前用户本人。
- 需要把 Codex 工作流沉淀为本地协议、模板和可审计案例的高阶使用者。

## 最小切口

每个需要插件验证的案例增加一个固定动作：

1. 运行能力矩阵。
2. 选择一个真正影响判断或验收的插件。
3. 实际调用。
4. 把成功、失败、结果质量和降级动作写入 `tool-ledger.md`。
5. 在 `flow-review.md` 写下次优化。

## 不做清单

- 不自动调用所有 Codex 插件。
- 不把 Browser、Chrome、Computer Use 混成同一种能力。
- 不把工具调用成功等同于证据有效。
- 不把内部插件流程写成市场反馈。

## 成功标准

- 至少一个插件真实调用成功，并写入案例。
- 至少一个插件失败被保留为流程证据，而不是被忽略。
- 文档能指导下一次按同样步骤补跑插件。
- `check-all` 和 `check-goal --min-cases 6` 通过。

## 放弃条件

- 如果后续所有 Codex 自带插件都只能停留在文件检测，不能实际调用，则先暂停插件化叙事，只保留脚本和 Markdown 协议。

## 下一步验证动作

- 修复或复查 Browser 插件运行时字段问题。
- 用 Browser 或 Computer Use 对 `vault/reports/index.html` 做一次页面级验收。
- 在后续真实产物里分别验证 Documents、PDF、Spreadsheets、Presentations。
