---
type: flow_review
status: completed
updated_at: {{created_at}}
case_stage: {{case_mode}}-loop
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
