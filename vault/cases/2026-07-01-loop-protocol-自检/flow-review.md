---
type: flow_review
status: completed
updated_at: 2026-07-01
case_stage: full-loop
gate: passed
---

# 流程自检

## 阶段完整性

| 阶段 | 状态 | 说明 |
| --- | --- | --- |
| signal | passed | 已记录原始信号。 |
| research | weak | 内部证据可用，真实外部证据为空。 |
| debate | passed | 已记录正反方。 |
| thesis | passed | 已明确继续内部验证。 |
| validation | passed | 已定义自检方式。 |
| artifact | passed | 已生成 case 产物。 |
| feedback | weak | 真实反馈为空。 |
| decision | passed | 未过度声称。 |
| asset | passed | 已沉淀内部资产。 |

## 证据质量

- 强：文件级产物和脚本自检。
- 中：已有 SignalProof 经验和 Codex 手册能力映射。
- 弱：真实用户反馈、真实 before/after、发布渠道反馈。

## 研究准确性质量门

| 检查项 | 状态 | 说明 |
| --- | --- | --- |
| 来源覆盖 | weak | 需要覆盖公开讨论、项目和数据、官方和一手资料、反证和替代方案。 |
| 交叉验证 | weak | 需要确认谁在说、说什么、在哪里说、有没有反证。 |
| 结论许可 | weak | 当前只能支持继续研究或低成本内部实验。 |
| 用户授权缺口 | weak / optional | Full Disk Access 已是诊断项；X API credits 默认记为暂缺但非阻断；Readwise、Scite、Semrush、Similarweb、Brand24 按具体 case 做只读探针。 |

## 过度声称检查

没有把真实反馈为空写成验证成功。

## AI Native Work Loop Review

| Loop | 预期状态 | 本轮检查 | 结论 |
| --- | --- | --- | --- |
| agentic coding | optional | `validation.md` 是否给出 Product Spec、Eval Set 和 Agentic Build Acceptance。 | 只有 spec 和 eval 可执行时，才让 AI 长时间构建或测试。 |
| developer feedback | required | `debate.md`、`decision.md` 和本轮人工判断是否修正方向。 | 人类上下文优势必须进入决策，不能只依赖 agent 输出。 |
| external feedback | skipped-with-reason | `feedback.md` 是否有真实发布、访谈、评论、issue、指标或明确跳过原因。 | `published` 不能自动写成 `externally-observed` 或 validated。 |
| asset/meta | required | `asset.md` 和 `vault/assets/registry.md` 是否能承接复用。 | 没有后续引用时只能算资产候选。 |

## 下一轮 Loop 决策

- 改 spec：当 agentic loop 卡住、产物不符合目标用户任务或 Eval Set 不可检查。
- 改产物：当 developer feedback 发现 UI、内容、用户流或交付形态偏离目标。
- 改反馈渠道：当 external feedback 缺少真实目标人、真实任务或可复查指标。
- 停止：当证据保持 weak / blocked，且没有低成本补证路径。

## Full 升级检查

只有同时满足以下条件时，外部机会 case 才能从 lite 升级为 full：

- `research.md` 的 `evidence_grade` 至少为 `medium`。
- 有明确外部动作：发布、访谈、私信测试、下载页、表单回收或真实目标人反馈。
- 至少有一个可登记资产候选。
- `decision.md` 写明为什么需要 full，而不是为了完整而完整。

## 优化空间

- 下一轮可增加更窄的 `last30days --days=3` 或 `--days=7` 调研分支。
- 对需要视觉验证的产物，可使用 Browser 预览导出报告。
- 对只能用 GUI 操作的流程，可考虑 Computer Use，但本轮没有直接工具暴露。
