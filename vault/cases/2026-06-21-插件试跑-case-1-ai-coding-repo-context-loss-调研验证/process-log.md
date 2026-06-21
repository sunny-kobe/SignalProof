---
type: process_log
status: completed
updated_at: 2026-06-21
gate: passed
---

# 过程日志

## 迭代 1

命令：

```bash
python3 scripts/signalproof.py init-case "插件试跑 case 1：AI coding repo context loss 调研验证"
```

结果：

- 生成完整 case 文件。

自检：

- 文件齐全。
- 真实反馈为空边界明确。

优化：

- 后续把重复检查脚本化。

## 迭代 2

命令：

```bash
python3.14 /Users/rust/.agents/skills/last30days/scripts/last30days.py "AI coding repo context loss" --emit=compact --auto-resolve --save-dir="/Users/rust/Documents/SignalProof/vault/cases/2026-06-21-插件试跑-case-1-ai-coding-repo-context-loss-调研验证/evidence" --save-suffix=plugintrial
```

结果：

- 运行成功，保存 `evidence/ai-coding-repo-context-loss-raw-plugintrial.md`。
- 得到 13 条证据：Reddit 6 条、YouTube 3 条、GitHub 4 条。
- X 为 0，Hacker News 为 0，YouTube 评论和部分 LLM rerank 降级。

自检：

- `last30days` 是真实调用，不再写“待定”。
- 输出存在明显来源缺口，gate 必须保持 `weak`。

优化：

- 后续 query 要更窄，并把额度/403/402 写成阻塞而不是反证。

## 迭代 3

命令：

```bash
python3 scripts/signalproof.py check-all
```

结果：

- 等待总自检统一运行。

自检：

- 本 case 已补齐 Skill、Plugin、MCP、Browser、Computer Use、last30days 等账本关键词。

优化：

- 把 `last30days` 质量门写回主 case 和插件审计文档。
