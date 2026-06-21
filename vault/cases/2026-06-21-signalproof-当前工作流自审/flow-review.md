---
type: flow_review
status: completed
updated_at: 2026-06-21
case_stage: full-internal-loop
gate: passed-with-gaps
---

# 流程自检

## 阶段完整性

| 阶段 | 状态 | 说明 |
| --- | --- | --- |
| signal | passed | 已把“用工作流审视工作流”记录为内部审计信号。 |
| research | passed-with-gaps | 已覆盖来源覆盖、交叉验证、反证、证据等级、结论许可和用户授权缺口；外部市场来源仍弱。 |
| debate | passed | 已记录正反两方和最强反方问题。 |
| thesis | passed | 已给出 `passed-with-gaps` 判断。 |
| validation | passed | 已运行诊断、能力、插件状态和目标检查。 |
| artifact | passed | 已生成完整 Markdown case。 |
| feedback | weak | 真实反馈为空，只记录内部流程反馈。 |
| decision | passed | 已明确继续使用并补自动化检查。 |
| asset | passed | 已沉淀工作流自审清单。 |

## 证据质量

- 强：本地文件、脚本输出、case 必填结构、插件状态快照、报告导出。
- 中：插件迁移说明、阶段能力矩阵、历史会话记忆中的插件审计口径。
- 弱：外部用户反馈、真实市场反馈、X 侧实时讨论、账号类 connector 读取能力。

## 过度声称风险

- 风险：把 `check-all` 通过理解成所有 case 研究质量都达标。
- 处理：记录旧 case warning，下一轮考虑对新 case 提高质量门。
- 风险：把插件安装理解成 connector 可读。
- 处理：按安装、工具暴露、账号授权、证据质量四层记录。
- 风险：把内部流程反馈理解成市场反馈。
- 处理：`feedback.md` 明确真实反馈为空。

## 本轮发现的流程缺口

- 已补自动 drift check：新增 `check-plugin-drift`，并接入 `check-goal`。
- 已补新 case 严格模式：新增 `check-case <case-slug> --strict`，新 case 可把 warning 当成失败。
- 缺 connector 探针闭环：Readwise、Scite、Semrush、Similarweb、Brand24 等需要具体问题触发，不应该全量空跑。
- 缺外部机会 case：当前工作流已经偏内部成熟，下一步应该回到真实外部来源。

## 下一轮优化

1. 给 `init-case` 增加内部审计类 case 类型，避免默认 `external-opportunity`。
2. 选择一个真实机会 case，补外部来源覆盖。
3. 对一个调研增强 connector 做只读探针。

## 结论

当前工作流可以自审，但不是满分闭环。二次验收后，最关键的两项“发现缺口”已经升级成脚本 gate；剩余重点应从内部打磨转向真实外部来源和 connector 探针。
