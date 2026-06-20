---
type: validation
title: Codex 插件和 Skill 编排边界
status: planned
updated_at: 2026-06-20
gate: passed
---

# 验证计划

## 验证方式

通过创建 `.agents/skills/signalproof/`、`plugins/signalproof/.codex-plugin/plugin.json` 和 repo marketplace 入口来验证。

## 命令

```bash
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py export-all
python3 scripts/signalproof.py check-goal --min-cases 5
```
