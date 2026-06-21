---
type: process_log
status: completed
updated_at: 2026-06-21
gate: passed
---

# 过程日志

## Iteration / 迭代 1：读取规则和用户约束

命令：

```bash
sed -n '1,220p' AGENTS.md
sed -n '1,260p' .agents/skills/signalproof/SKILL.md
sed -n '1,260p' docs/protocol.md
sed -n '1,260p' docs/research-quality-gate.md
sed -n '1,300p' docs/codex-plugin-flow.md
```

结果：

- 确认本仓库保持本地优先，不做 Web App、SaaS dashboard、workflow builder 或通用知识库。
- 确认每个 case 必须包含 13 个必需文件。
- 确认插件安装、工具暴露、账号授权和证据质量必须分层。

Self-check / 自检：

- 本轮只做内部流程优化，不做市场验证。

Optimization / 优化：

- 优先寻找能落到脚本或模板的机制缺口。

## Iteration / 迭代 2：复核最近自审 case

命令：

```bash
sed -n '1,260p' vault/cases/2026-06-21-signalproof-当前工作流自审/report.md
sed -n '1,260p' vault/cases/2026-06-21-signalproof-当前工作流自审/flow-review.md
sed -n '1,260p' vault/cases/2026-06-21-signalproof-当前工作流自审/tool-ledger.md
sed -n '1,240p' vault/cases/2026-06-21-signalproof-当前工作流自审/decision.md
git diff -- AGENTS.md .agents/skills/signalproof/SKILL.md docs/protocol.md docs/research-quality-gate.md scripts/signalproof.py
```

结果：

- 原报告 `passed-with-gaps` 判断基本准确。
- `check-plugin-drift` 和 `check-case --strict` 已经进入脚本，不是只写报告。
- 仍有可落地缺口：内部审计 case 类型未进入 `init-case`，strict 未识别 `待补`、`待定` 和未替换模板变量。

Self-check / 自检：

- 没有把原报告一概否定；区分已落地机制和仍是建议。

Optimization / 优化：

- 选择“未完成占位检查”和“internal-audit case 类型”作为本轮高价值改进。

## Iteration / 迭代 3：修改脚本和模板

命令：

```bash
python3 -m py_compile scripts/signalproof.py
```

结果：

- `scripts/signalproof.py` 新增未完成占位标记检查。
- `scripts/signalproof.py` 新增 `CASE_TYPE_PRESETS` 和 `--case-type internal-audit`。
- `templates/case/` 改为按 case 类型渲染 signal、research、tool-ledger、validation、feedback、decision、asset、artifact、report。
- `AGENTS.md`、repo skill、`docs/protocol.md`、`docs/research-quality-gate.md` 已补规则。
- Python 语法检查通过。

Self-check / 自检：

- 没有修改成 Web App 或 SaaS。
- 没有把插件调用写成证据合格。

Optimization / 优化：

- 新 strict 检查会把未完成占位变成 warning；配合 `--strict` 后新 case 会失败。

## Iteration / 迭代 4：创建并校验本次 case

命令：

```bash
python3 scripts/signalproof.py init-case "SignalProof 工作流优化二次审视" --case-type internal-audit --signal "复核最近 SignalProof 自审报告，判断哪些结论可靠、哪些只是建议，并把最高价值改进落地为本地脚本、模板和文档约束。" --force
python3 scripts/signalproof.py check-case 2026-06-21-signalproof-工作流优化二次审视 --strict
```

结果：

- 第一次 strict 抓到了模板里的 `待定` 残留。
- 修正模板候选能力行后，本 case strict 通过。

Self-check / 自检：

- 这证明新增 gate 有实际价值：它抓到的不是抽象问题，而是本轮新模板里的真实残留。

Optimization / 优化：

- 本 case 作为 `internal-audit` 样例保留，后续内部审计可复用。
