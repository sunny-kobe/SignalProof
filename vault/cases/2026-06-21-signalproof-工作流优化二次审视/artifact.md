---
type: artifact
status: completed
updated_at: 2026-06-21
gate: passed
---

# 产物

## 产物

本 case 的产物是一次 SignalProof 工作流机制优化：脚本能识别未完成占位标记，模板能区分内部流程审计与外部机会验证。

## 文件

- `scripts/signalproof.py`：新增 `check-case` 的未完成占位标记检查、`CASE_TYPE_PRESETS` 和 `--case-type internal-audit`。
- `templates/case/`：按 case 类型渲染关键块，内部审计 case 不再默认带外部机会验证话术。
- `AGENTS.md`：补充 internal-audit 创建命令和 strict 占位检查边界。
- `.agents/skills/signalproof/SKILL.md`：补充 internal-audit 和 strict 使用规则。
- `docs/protocol.md`：新增 Case 类型说明和 strict 占位检查说明。
- `docs/research-quality-gate.md`：新增新 case 严格检查说明。
- `vault/cases/2026-06-21-signalproof-工作流优化二次审视/`：记录本次优化闭环。

## 原报告处理

本轮没有顺着原报告说满分，也没有把它否定成空报告。判断是：

- 原报告对 `passed-with-gaps`、插件分层、真实反馈为空、不能市场验证的结论准确。
- 原报告已经落地 `check-plugin-drift` 和 `check-case --strict`，所以不是“写得像完成”。
- 原报告仍留下可落地缺口：strict 未识别半成品占位，内部审计 case 没有独立类型。

## 产物边界

这是内部协议产物，不是市场验证产物。
