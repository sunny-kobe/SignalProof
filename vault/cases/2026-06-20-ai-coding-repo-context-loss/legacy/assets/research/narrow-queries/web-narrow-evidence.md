# 窄查询 Web 证据留档

查询时间：2026-06-20

## 查询组

| 查询层 | query | 目标问题 | 结论 |
| --- | --- | --- | --- |
| 上下文文件 | `AGENTS.md coding agents repo instructions Codex` | 官方和社区是否已有入口 | 有，OpenAI Codex 官方支持 `AGENTS.md`，agents.md 也是开放格式。 |
| Claude 对照 | `Claude Code CLAUDE.md project memory repo instructions` | Claude Code 是否有类似机制 | 有，Claude Code 有 memory / `CLAUDE.md` / `.claude` 目录体系。 |
| 失败模式 | `AI coding agent ignores project conventions repo context` | 是否有真实抱怨 | 有弱到中等证据，例如 GitHub Community 讨论提到 Copilot 不可靠读取项目规则。 |
| 反证 | `long repository instructions coding agents context files performance` | 上下文文件是否可能有害 | 有强反证，论文与相关文章指出 repo context files 可能降低成功率并增加成本。 |

## 强相关证据

- OpenAI Codex 官方文档：`https://developers.openai.com/codex/guides/agents-md`  
  支撑：Codex 会在工作前读取 `AGENTS.md`。这证明 repo instruction 是真实机制入口。

- arXiv 论文：`https://arxiv.org/html/2602.11988v1`  
  支撑：研究发现 context files 可能降低 coding agent 任务成功率，并提高成本。  
  用途：这是反证，说明方向必须是“审计和瘦身”，不是“写更多上下文”。

- GitHub Community 讨论：`https://github.com/orgs/community/discussions/184411`  
  支撑：有用户反馈 AI agent 不稳定读取完整 repo structure 或 custom instructions。  
  用途：这是具体失败模式证据，但不是付费或使用意图证据。

- Reddit / r/codex：`https://www.reddit.com/r/codex/comments/1t248sh/managing_your_agentsmd/`  
  支撑：用户在讨论如何管理 `AGENTS.md` 和文档，担心增加 context usage。  
  用途：这是目标人群问题线索，但仍需真实任务验证。

## 中相关证据

- agents.md 官网：`https://agents.md/`  
  支撑：AGENTS.md 是面向 coding agents 的开放格式，推荐包含项目概览、构建测试命令、代码风格、测试说明等。  
  用途：证明已有方案存在，SignalProof 不能只做模板。

- Claude Code Docs memory：`https://code.claude.com/docs/en/memory`  
  支撑：Claude Code 有 memory 机制。  
  用途：对照 `CLAUDE.md` / memory 生态。

- Packmind：`https://packmind.com/evaluate-context-ai-coding-agent/`  
  支撑：AI coding agent context files 容易写，难点是持续保持准确。  
  用途：支持“审计/维护/验证”比“初始模板”更有价值。

- Augment Code：`https://www.augmentcode.com/blog/your-agents-context-is-a-junk-drawer`  
  支撑：引用 AGENTS.md 研究，强调上下文可能变成杂物抽屉。  
  用途：支持瘦身和质量门。

## 弱相关或仅作背景

- 多篇 `CLAUDE.md` / AGENTS.md 教程、Medium/Substack/YouTube 说明类内容。  
  用途：说明内容生态已经拥挤，单纯写教程不稀缺。

## GitHub CLI 精确搜索结果

已保存：

- `github-repos-agents-md.json`
- `github-issues-repo-context.json`
- `github-issues-agent-ignores-conventions.json`

三个文件都是 `[]`，说明精确 GitHub repo/issue 查询没有找到强命中。这不是“无人需要”的结论，只能说明公开 GitHub issue 证据薄，下一步应转向真实用户私聊和 before/after。

## 研究质量门结论

- 官方机制证据：strong。
- 反证证据：strong。
- 用户痛点证据：weak to medium。
- 使用/付费/采用意图：missing。
- 是否足以产品化：no。
- 是否足以做 Day 2 公开验证：yes。

## 对机会判断的影响

继续坚持“收窄后继续验证”。  
不要做平台、插件、SaaS、自动扫描器。  
最小发布包必须强调：不是写更多上下文，而是验证 repo instructions 是否真的减少 AI 写偏。
