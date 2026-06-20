---
type: validation
title: Codex 子线程完成但输出文件缺失
status: planned
updated_at: 2026-06-20
gate: passed
---

# 验证计划

## 验证方式

通过强制 `process-log.md`、`tool-ledger.md` 和脚本检查来验证，而不是相信线程 UI 状态。

## 命令

```bash
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py export-all
python3 scripts/signalproof.py check-goal --min-cases 5
```
