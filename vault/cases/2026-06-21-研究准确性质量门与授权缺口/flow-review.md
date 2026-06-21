---
type: flow_review
status: completed
updated_at: 2026-06-21
case_stage: full-internal-loop
gate: passed
---

# 流程自检

## 阶段完整性

| 阶段 | 状态 | 说明 |
| --- | --- | --- |
| signal | passed | 已记录原始信号。 |
| research | passed | 已把来源覆盖、交叉验证、反证、证据等级、结论许可和用户授权缺口写入规则与模板；外部市场证据仍为 weak。 |
| debate | passed | 已记录正反方。 |
| thesis | passed | 已明确继续研究 gate 固化和内部验证。 |
| validation | passed | 已定义自检方式。 |
| artifact | passed | 已生成 case 产物。 |
| feedback | weak | 真实反馈为空。 |
| decision | passed | 未过度声称。 |
| asset | passed | 已沉淀内部资产。 |

## 证据质量

- 强：文件级产物和脚本自检。
- 中：研究 gate 文档、模板、插件流程和能力矩阵。
- 弱：真实用户反馈、真实 before/after、发布渠道反馈、外部目标用户原话。

## 研究准确性质量门

| 检查项 | 状态 | 说明 |
| --- | --- | --- |
| 来源覆盖 | passed-in-template / weak-in-market | 规则已要求公开讨论、项目和数据、官方和一手资料、反证和替代方案；本 case 不声称外部市场覆盖。 |
| 交叉验证 | passed-in-template / weak-in-market | 模板已要求谁在说、说什么、在哪里说、有没有反证；具体机会 case 仍需补真实来源。 |
| 结论许可 | passed | 已限制为继续研究、低成本内部实验、暂停或放弃。 |
| 用户授权缺口 | partial | Full Disk Access 和 X OAuth 已通过；X search 因 credits 暂缺但非阻断；Readwise、Scite、Semrush、Similarweb、Brand24 已网页登录但 connector 未验证；Chrome 标签页复查只证明 GitHub、X、Readwise 页面可见，未证明研究增强 connector 可读。 |

## 过度声称检查

没有把真实反馈为空写成验证成功。

## 优化空间

- 下一轮可增加更窄的 `last30days --days=3` 或 `--days=7` 调研分支。
- 对需要视觉验证的产物，可使用 Browser 预览导出报告。
- 对只能用 GUI 操作的流程，可考虑 Computer Use，但本轮没有直接工具暴露。
- 可以进一步把 `check-all` 的研究 gate warning 变成仅对新 case 的强规则，避免旧 case 噪音过多。
- X API credits 暂不建议单独付费；后续只有当真实趋势 case 高度依赖 X 实时讨论时，再提醒用户补 credits。
- 对 Readwise / Scite / Semrush / Similarweb / Brand24 选择一个具体问题做只读 connector 探针，成功后再写成可用证据源。
- 下一步不要泛泛重登所有网站；先选一个真实研究问题，再按该问题打开目标页面或 connector 做只读探针。
- 插件迁移已新增独立说明和 `plugin-status` 快照；后续迁移时仍需在新机器重新安装官方插件并重新授权外部 app。
