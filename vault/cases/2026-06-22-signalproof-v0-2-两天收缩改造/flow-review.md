---
type: flow_review
status: completed
updated_at: 2026-06-22
case_stage: full-loop
gate: passed
---

# 流程自检

## 阶段完整性

| 阶段 | 状态 | 说明 |
| --- | --- | --- |
| signal | passed | 已记录原始信号。 |
| research | medium | 内部仓库证据可用，真实外部证据为空。 |
| debate | passed | 已记录正反方。 |
| thesis | passed | 已明确继续内部机制优化。 |
| validation | passed | 已定义自检方式。 |
| artifact | passed | 已生成 case 产物。 |
| feedback | weak | 真实反馈为空。 |
| decision | passed | 未过度声称。 |
| asset | warning | 已登记资产候选，但还没有后续复用证明。 |

## 证据质量

- 强：文件级产物和脚本自检。
- 中：当前用户要求、仓库规则、脚本输出和资产账本。
- 弱：真实用户反馈、真实 before/after、发布渠道反馈。

## 研究准确性质量门

| 检查项 | 状态 | 说明 |
| --- | --- | --- |
| 来源覆盖 | medium | 本轮覆盖用户要求、仓库文件、脚本输出和反证风险。 |
| 交叉验证 | medium | 文档、模板、脚本和 case 互相约束。 |
| 结论许可 | medium | 只允许内部机制优化和下一步 lite 外部信号实验。 |
| 用户授权缺口 | weak / optional | 本轮不依赖外部账号；真实外部机会 case 再处理授权。 |

## 过度声称检查

没有把真实反馈为空写成验证成功。

## Full 升级检查

只有同时满足以下条件时，外部机会 case 才能从 lite 升级为 full：

- `research.md` 的 `evidence_grade` 至少为 `medium`。
- 有明确外部动作：发布、访谈、私信测试、下载页、表单回收或真实目标人反馈。
- 至少有一个可登记资产候选。
- `decision.md` 写明为什么需要 full，而不是为了完整而完整。

## 优化空间

- 历史 case 大量缺少结构化 frontmatter，`check-all` 会保留 warning；后续可以按需只迁移活跃 case。
- `check-plugin-drift --no-codex` 仍会因当天状态快照只显示少量已安装插件而失败；需要重新运行 `plugin-status` 或更新插件锁定策略。
- `check-assets` 暴露 zero-reuse 资产，下一步应用 5 个 lite 外部信号实验检验资产是否真的能复用。
