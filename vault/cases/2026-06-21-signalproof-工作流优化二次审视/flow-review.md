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
| research | passed-with-gaps | 已复核原报告、脚本 diff、模板和文档；外部市场证据为空。 |
| debate | passed | 已记录“原报告不是空转”与“仍不能替代真实反馈”的两侧论点。 |
| thesis | passed | 已明确只做本地工作流机制优化。 |
| validation | passed | 已用 strict 检查验证新模板，并准备最终命令验收。 |
| artifact | passed | 已更新脚本、模板、文档和本 case。 |
| feedback | weak | 真实反馈为空。 |
| decision | passed | 决策限定为继续内部机制优化。 |
| asset | passed | 已沉淀为 strict 占位检查和 internal-audit case 类型。 |

## 证据质量

- 强：文件级产物和脚本自检。
- 中：最近自审 case、历史记忆中的插件审计口径、插件流程文档。
- 弱：真实用户反馈、真实 before/after、发布渠道反馈。

## 研究准确性质量门

| 检查项 | 状态 | 说明 |
| --- | --- | --- |
| 来源覆盖 | medium | 内部审计覆盖仓库文件、脚本、模板、文档和 case；公开讨论只覆盖当前用户任务。 |
| 交叉验证 | medium | 已用原报告、diff、strict 失败再修正、模板生成结果互相验证。 |
| 结论许可 | medium | 当前只能支持内部机制优化，不能支持市场验证。 |
| 用户授权缺口 | weak / optional | Full Disk Access 已是诊断项；X API credits 默认记为暂缺但非阻断；Readwise、Scite、Semrush、Similarweb、Brand24 按具体 case 做只读探针。 |

## 过度声称检查

没有把真实反馈为空写成验证成功。

## 本轮已落地优化

- `scripts/signalproof.py` 新增未完成占位标记检查，覆盖 `TODO`、`TBD`、`待补`、`待定` 和未替换模板变量。
- `scripts/signalproof.py` 新增 `CASE_TYPE_PRESETS`，`init-case` 支持 `--case-type internal-audit`。
- `templates/case/` 改为按 case 类型渲染关键内容，内部审计 case 不再默认套外部机会验证口径。
- `AGENTS.md`、`.agents/skills/signalproof/SKILL.md`、`docs/protocol.md`、`docs/research-quality-gate.md` 补充 strict 和 internal-audit 规则。
- 本次 case 用新模板生成，并通过 strict 检查。

## 仍未解决

- 旧 case 中仍有历史 `待定` 或研究质量门 warning；本轮不批量改旧材料，避免改写历史证据。
- Readwise、Scite、Semrush、Similarweb、Brand24 等 connector 仍未在具体 case 中证明可读。
- 真实外部反馈为空，不能证明 SignalProof 对其他用户有效。

## 下一轮优化空间

- 对一个真实外部机会 case 跑完整研究质量门。
- 对一个调研增强 connector 做只读探针。
- 需要视觉验收的报告再用 Browser 预览，不默认加入本轮 gate。
