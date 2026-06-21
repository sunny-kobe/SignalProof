---
type: research
status: completed
updated_at: 2026-06-21
gate: weak
---

# 研究

## 要回答的问题

- `last30days` 作为调研类能力，能否给 AI coding repo context loss 这类信号补到最近 30 天的真实讨论？
- 这些讨论来自哪些渠道，强度够不够改变 SignalProof 对该方向的判断？
- 调研类插件失败、额度和来源缺口应该如何进入工具账本？

## 实际调研命令

```bash
python3.14 /Users/rust/.agents/skills/last30days/scripts/last30days.py "AI coding repo context loss" --emit=compact --auto-resolve --save-dir="/Users/rust/Documents/SignalProof/vault/cases/2026-06-21-插件试跑-case-1-ai-coding-repo-context-loss-调研验证/evidence" --save-suffix=plugintrial
```

输出文件：

`evidence/ai-coding-repo-context-loss-raw-plugintrial.md`

## 已确认事实

- `last30days` 成功运行，耗时约 67 秒。
- 共得到 13 条证据，覆盖 3 类来源：Reddit 6 条、YouTube 3 条、GitHub 4 条。
- 相关方向包括：AI coding agent 的阶段 gate、repo context/memory、Claude Code memory/knowledge graph、重复解释项目结构、上下文成本等。
- 工具也明确暴露了来源缺口：X 为 0，Hacker News 为 0，TikTok/Instagram/Threads/Perplexity 为 0。
- 运行过程中出现降级：X `CreditsDepleted`、Reddit public API 403 后 fallback、YouTube comments HTTP 402、LLM planning/reranking 402 fallback。

## 有价值命中

- Reddit `r/ClaudeWorkflows` 出现“verifiable phases and gates”相关讨论，和 SignalProof 的证据门、阶段门高度相关。
- Reddit `r/PromptEngineering` 出现 second brain / MCP / context memory 讨论，说明“AI coding 上下文需要结构化外部记忆”不是凭空想象。
- YouTube 出现 Claude Code repo knowledge graph / memory problem 内容，说明 repo context 仍是传播热点。
- Reddit `r/buildinpublic` 出现“每次会话重复解释项目结构”的痛点，和 repo context loss 更贴近。

## 证据质量

| 维度 | 结论 |
| --- | --- |
| 来源覆盖 | 弱到中。GitHub/Reddit/YouTube 有结果，但 X/HN 缺失。 |
| 相关性 | 中。部分命中 repo context 和 memory，部分为泛 AI coding 噪音。 |
| 用户原话 | 中。Reddit 有原话，但样本少。 |
| 决策影响 | 中。支持继续内部验证，不支持对外声称需求成立。 |

## 证据缺口

- X 缺失不是反证，而是额度阻塞。
- YouTube 评论缺失，无法判断真实观众反馈质量。
- Hacker News 为 0，不能证明开发者社区完全没有讨论。
- 结果里大量 `entity-miss demotion`，说明 query 还不够窄。
- 没有真实目标用户愿意提交 repo 或失败任务。

## 当前判断

`last30days` 对调研阶段有明显提升，适合作为 SignalProof 真实趋势 case 的默认候选能力。但本次结果只能支撑“继续低成本验证/收窄 query”，不能支撑产品化、SaaS 化或市场验证成功。
