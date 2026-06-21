---
type: asset
status: reusable-internal
created_at: 2026-06-21
gate: passed
---

# 资产

## 资产名称

研究准确性质量门与授权缺口

## 资产类型

内部协议验证案例、研究 gate 文档、case 模板和脚本检查规则。

## 可复用内容

- `docs/research-quality-gate.md`：研究准确性规则。
- `templates/case/research.md`：新 case 的来源覆盖和交叉验证模板。
- `templates/case/tool-ledger.md`：研究准确性账本模板。
- `templates/case/flow-review.md`：流程自检中的研究 gate 检查。
- `scripts/signalproof.py`：研究 gate 资产存在性检查和 case warning。
- 当前授权缺口清单。
- `docs/codex-plugin-status-and-migration.md`：插件安装显示、界面不可见原因和可迁移性说明。
- `python3 scripts/signalproof.py plugin-status`：生成本机插件状态快照。

## 可复用边界

只能证明内部流程能力和研究 gate 固化，不能证明外部需求。真实反馈为空，外部市场验证仍未开始。

插件迁移只覆盖 repo 内 Skill、插件源码、marketplace 入口、模板、文档和 vault；不迁移外部账号授权、浏览器登录态、API key 或 Codex 本机缓存。
