---
type: research
status: researching
updated_at: 2026-06-20
---

# 研究

## 要回答的问题

- AI coding repo context loss 是否是真实痛点，还是我们从个人经验外推出来的伪需求？
- 官方和社区已有机制是什么？
- `AGENTS.md` / `CLAUDE.md` / repo instructions 的机会在哪里，风险在哪里？
- `last30days` 是否补到了真实讨论证据？
- 第一版最小验证应该是什么？

## 已确认事实

- Codex manual 说明 Skills 是可复用工作流的 authoring format，Plugins 是可安装分发单位；这支持 SignalProof 先做 Skill/协议，再考虑 Plugin。
- Codex manual 说明 Codex 会在工作前读取 `AGENTS.md`，按全局、项目、子目录层级合并指令，且有默认 32 KiB 限制。
- Codex manual 说明如果仍在迭代一个 repo 或个人工作流，应先从 local skill 开始；当要跨团队分享、绑定 app/MCP/hooks 或发布稳定包时再做 plugin。
- Codex manual 说明 subagents 适合复杂、并行任务，能由 Codex 编排、等待结果并汇总；这支持本次 fork 子线程协作。
- `last30days` 本轮输出显示 GitHub 5 条、Reddit 13 条，X 0、HN 0、YouTube 0、TikTok 0、Instagram 0、Perplexity 0；X 明确因 `CreditsDepleted` 失败，Reddit public 出现 403 但 fallback 部分成功。

## 一手来源

- Codex manual cache: `/var/folders/qf/j6djhy5x1ln2n2h7q5npwnd00000gn/T/openai-docs-cache/codex-manual.md`
- `last30days` raw: `/Users/rust/Documents/Codex/2026-06-19/new-chat-3/outputs/signalproof-rerun-2026-06-20/assets/research/ai-coding-repo-context-agents-md-claude-code-memory-codex-raw-signalproof-rerun.md`
- 旧 demo vault: `/Users/rust/Documents/Codex/2026-06-20/personal-opportunity-os-signalproof-codex-protocol-2/outputs/signalproof-vault`

## 工具覆盖

- 已使用：`personal-opportunity-os`、`user-working-profile`、`last30days`、OpenAI Codex manual、GitHub CLI 搜索、web search、Codex fork thread / send_message_to_thread。
- 未使用但相关：浏览器验收、Obsidian、NotebookLM、Lark。
- 跳过原因：当前阶段是研究与资产方案，不是网页交互验收或外部发布同步。
- 是否需要补跑：需要补更窄的真实讨论查询；本轮 `last30days` query 太宽，且 X/HN/YouTube/Perplexity 覆盖不足。

## 用户原话或真实讨论

- `last30days` 找到 r/ClaudeAI 的 “A Context Brain for you (and your AI Agent)” 和 r/PromptEngineering 的 “What real projects have you shipped using AI coding tools?”，但证据弱，不能证明“repo context audit”已被强烈需求。
- GitHub 搜到若干 AI code review / ECC bundle / agent config 相关 PR 评论，但多为 bot 输出，用户意图不强。
- 目前还没有直接用户原话说“我愿意使用 repo context audit checklist / 服务”。

## 替代品和已有方案

- Codex `AGENTS.md`。
- Claude Code `CLAUDE.md` / memory。
- agents.md 开放格式。
- AI code review bots，例如 CodeRabbit、Qodo、Codoki、SemanticDiff、Octopus Review 等。
- 各类项目 README、CONTRIBUTING、团队文档和 prompt 模板。

## 开源项目和相关工具

- agents.md / AGENTS.md 生态。
- `GunsNR/smart-skill-user` 一类 token-aware skill routing 小项目，说明围绕 agent instruction / skill routing 的工具还早期且零散。
- 旧 demo 中已有 `repo-ai-context-audit-demo`。

## 证据缺口

- 缺少 X 真实讨论，因为 `xurl` 额度耗尽。
- HN、YouTube、TikTok、Instagram、Perplexity 本轮都没有有效结果。
- `last30days` 出现明显泛 AI 噪音和 entity-miss demotion，说明查询策略需要更窄。
- 缺少真实用户 repo 的 before/after。
- 缺少发布后的 star、issue、评论、私聊、咨询等反馈。

## 当前判断

研究支持“收窄后继续”，但不支持大项目、不支持平台化、不支持立即插件化或服务化承诺。

最小有效机会仍然是：

```text
Repo AI Context Audit Checklist + 瘦身版 AGENTS.md / CLAUDE.md 模板 + before/after demo + 72 小时真实反馈验证
```

## 下一步还需要查什么

- 用更窄 query 补一次真实讨论，例如：`AGENTS.md repo instructions`, `Claude Code memory project instructions`, `AI coding agent ignores project conventions`。
- 私聊 5 个 AI coding 高频用户，收集真实写偏任务。
- 用一个真实任务跑 before/after，而不是继续完善 synthetic demo。
