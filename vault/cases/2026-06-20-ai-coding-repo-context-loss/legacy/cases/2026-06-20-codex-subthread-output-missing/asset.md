---
type: asset
status: reusable
asset_type: protocol-quality-gate
created_at: 2026-06-20
gate: internal-validated
---

# 复用资产

## 资产名称

子线程文件级验收门。

## 资产内容

规则：

```text
子线程状态 completed 不等于产物完成。源线程必须检查 completion receipt 中列出的 files 是否真实存在并满足验收标准。
```

## 复用场景

- 子线程调研；
- 子线程反方辩论；
- 子线程实现；
- 子线程验收；
- 跨会话协作。

## 已沉淀位置

- `/Users/rust/.codex/skills/personal-opportunity-os/SKILL.md`
- `subtasks/index.md`
- `subtasks/day2-loop-audit.md`

## 后续资产化

扩展为 `audit_subtasks.py`，成为 SignalProof Protocol MVP 的脚本质量门。
