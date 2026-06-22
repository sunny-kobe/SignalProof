---
type: artifact
status: created
updated_at: 2026-06-22
gate: passed
---

# 产物

## 产物

本 case 的产物是一次 SignalProof V0.2 收缩改造：文档、skills、模板、资产账本和脚本 gate 都改为服务 `SignalProof 个人证据协议`。

## 文件

- `signal.md`
- `research.md`
- `debate.md`
- `thesis.md`
- `validation.md`
- `artifact.md`
- `feedback.md`
- `decision.md`
- `asset.md`
- `flow-review.md`
- `tool-ledger.md`
- `process-log.md`
- `report.md`

## 本轮改动清单

- `README.md`、`docs/protocol.md`、`docs/current-flow.md`、`AGENTS.md`、两份 SignalProof skill：统一定位、lite 默认、full 升级硬条件和插件候选能力边界。
- `templates/case/`：给 signal / research / feedback / asset 等模板加入结构化 frontmatter，压缩 lite debate，减少 report 重复。
- `vault/assets/registry.md`：升级为资产复用账本，新增 reuse_count、proof_of_reuse、reuse_cost_minutes、preconditions、public_or_private、supersedes、owner_scope。
- `scripts/signalproof.py`：新增 frontmatter 检查、`check-all` 顶层状态和 `check-assets`。
- `vault/cases/2026-06-22-signalproof-v0-2-两天收缩改造/`：记录本轮 internal-audit full case。

## 产物边界

这是内部协议产物，不是市场验证产物。
