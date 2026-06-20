---
type: process_log
title: 假设反馈的决策边界
status: completed
updated_at: 2026-06-20
gate: passed
---

# 过程日志

## 迭代 1

命令：

```bash
python3 scripts/signalproof.py init-case "假设反馈的决策边界"
```

结果：

- 生成完整案例文件。

自检：

- 模板文件齐全。

优化：

- 发现模板案例过于相似，需要按主题 seed 差异化内容。

## 迭代 2

命令：

```bash
python3 scripts/seed_cases.py
python3 scripts/signalproof.py check-all
```

结果：

- 进入差异化案例校验。

自检：

- `tool-ledger.md` 覆盖 last30days、Browser、Computer Use、Skill、Plugin、MCP。

优化：

随着更多案例出现边缘写法，继续把危险短语加入过度声称检测。
