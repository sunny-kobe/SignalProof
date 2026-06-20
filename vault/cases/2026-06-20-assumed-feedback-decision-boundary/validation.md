---
type: validation
title: 假设反馈的决策边界
status: planned
updated_at: 2026-06-20
gate: passed
---

# 验证计划

## 验证方式

当案例引用假设时要求存在 `assumed-feedback.md`，并检查 decision 里的过度声称语言。

## 命令

```bash
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py export-all
python3 scripts/signalproof.py check-goal --min-cases 5
```
