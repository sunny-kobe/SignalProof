---
type: validation
title: AI 编码仓库上下文丢失
status: planned
updated_at: 2026-06-20
gate: passed
---

# 验证计划

## 验证方式

通过迁移 legacy run、保留仓库上下文审计资产、检查报告导出，并把弱 last30days 结果保存为研究证据来验证。

## 命令

```bash
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py export-all
python3 scripts/signalproof.py check-goal --min-cases 5
```
