---
type: validation
status: planned
updated_at: 2026-06-22
gate: passed
---

# 验证计划

## 验证对象

SignalProof 是否能把“报告里发现的缺口”升级成脚本、模板或文档中的可复用机制。

## 验证方式

1. 运行 `python3 -m py_compile scripts/signalproof.py`。
2. 运行 `python3 scripts/signalproof.py check-case 2026-06-22-signalproof-v0-2-两天收缩改造 --strict`。
3. 运行 `python3 scripts/signalproof.py check-assets`。
4. 运行 `python3 scripts/signalproof.py check-all`。
5. 运行 `python3 scripts/signalproof.py export-all`。
6. 运行 `python3 scripts/signalproof.py check-plugin-drift --no-codex`。
7. 运行 `git diff --check` 和 `git status --short`。

## 跳过项

- 真实外部反馈：本轮跳过。
- 发布渠道：本轮跳过。
- 浏览器/GUI 验收：本轮产物是 Markdown 和 Python 标准库脚本，没有页面或 GUI-only 流程。

## 成功标准

- 本 case strict 通过。
- `check-assets` 能输出 registered/reused/candidate/zero-reuse 统计。
- `check-all` 即使保留历史 warning，也必须显示 `Overall status: passed-with-warnings`。
- `check-plugin-drift --no-codex` 若仍失败，必须明确失败来自当天状态快照和锁定清单不一致，而不是把插件治理写成 ready。
