---
type: validation
title: 研究工具覆盖和结果质量缺口
status: planned
updated_at: 2026-06-20
gate: passed
---

# 验证计划

## 验证方式

把 `tool-ledger.md` 设为必需文件，并检查它覆盖 last30days、Browser、Computer Use、Skill、Plugin、MCP 和工具结果质量。

## 命令

```bash
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py export-all
python3 scripts/signalproof.py check-goal --min-cases 5
```
