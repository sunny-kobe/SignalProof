# SignalProof Rerun Case Report

> Case: AI coding repo context loss
> Date: 2026-06-20
> Run: `/Users/rust/Documents/Codex/2026-06-19/new-chat-3/outputs/signalproof-rerun-2026-06-20`
> Status: ready-for-day-2-validation
> Decision: 收窄后继续验证

## 0. 总判断

这个机会仍然值得继续，但只能继续到 Day 2 最小公开验证，不能扩成产品、平台、插件、SaaS 或服务承诺。

当前最小切口是：

```text
Repo AI Context Audit Checklist
+ 瘦身版 AGENTS.md / CLAUDE.md 模板
+ synthetic before/after demo
+ 72 小时真实失败任务征集
```

关键判断：机会不在“再造一个上下文文件”，而在“审计、瘦身和验证上下文是否真的减少 AI 写偏”。

## 1. Signal

AI coding 用户在真实 repo 中使用 Codex / Claude Code / Cursor 等工具时，经常遇到 agent 不理解项目上下文、接口契约、目录边界、验证命令和团队约定，导致输出代码看似能运行但不符合项目实际规范。

这个信号和用户个人能力匹配：用户熟悉 Codex、Claude Code、MCP、本地工具链和真实复杂前端项目，能把 AI coding 中的隐性流程问题转成可复用资产。

## 2. Evidence

已确认事实：

- Codex 官方 manual 说明 Skills 是可复用工作流的 authoring format，Plugins 是可安装分发单位。
- Codex 官方 manual 说明 Codex 会在工作前读取 `AGENTS.md`，支持全局、项目和子目录层级。
- Codex 官方 manual 说明 `project_doc_max_bytes` 默认约 32 KiB，说明指令文件不能无限膨胀。
- Codex 官方 manual 说明 Subagents 可以用于并行任务。
- 旧 demo 已有 synthetic before/after，但没有真实反馈。

本轮 `last30days`：

- 日期范围：2026-05-21 到 2026-06-20。
- 活跃来源：GitHub 5 条、Reddit 13 条。
- X：0，原因是 `CreditsDepleted`。
- HN / YouTube / TikTok / Instagram / Perplexity / Threads / Polymarket：0。
- 多数结果弱相关，出现 `fallback-local-score` 和 `entity-miss demotion`。

结论：`last30days` 已使用，但只能算弱证据和流程优化样本，不能算市场验证。

## 3. Debate

正方：

- 痛点和用户个人能力匹配。
- 官方机制真实存在。
- 低成本可验证。
- 资产化路径清楚。

反方：

- 官方已经有 `AGENTS.md` / `CLAUDE.md`。
- 模板很容易被替代。
- 公开市场证据弱。
- synthetic demo 不能证明需求。
- 上下文可能越写越长，反而降低质量。

严格裁决：收窄后继续。

## 4. Thesis

不要做“AI coding 上下文平台”。真正要验证的是：

```text
AI coding 高频用户是否愿意用一套轻量审计流程，改善真实 repo 中 agent 写偏的问题。
```

第一批用户：

- Codex / Claude Code 高频用户。
- 在真实业务 repo 中使用 AI coding 的前端或全栈工程师。
- 小团队中推动 AI coding 工作流的人。

## 5. Validation

72 小时验证动作：

- Day 2：发布 GitHub repo 或 gist，私聊 5 个 AI coding 高频用户。
- Day 3：收集反馈，选择 1 个真实失败任务。
- Day 4：做真实 before/after，更新决策。

成功标准：

- 至少 3 个 A/B 级反馈。
- 至少 1 个真实失败任务。
- 至少 1 个目标用户愿意看 before/after。
- 至少 1 条具体反对意见让 checklist 变窄。

Kill 条件：

- 只有点赞收藏，没有任务提交。
- 真实 before/after 没有改善。
- 用户认为官方文档已经足够。

## 6. Artifact

Day 2 最小发布包结构：

```text
repo-ai-context-audit/
  README.md
  checklist/repo-context-audit-checklist.md
  templates/AGENTS.md
  templates/CLAUDE.md
  demo/task.md
  demo/before.md
  demo/after.md
  demo/comparison.md
  prompts/collect-failure-task.md
  prompts/run-before-after.md
  feedback/feedback-form-fields.md
```

必须在 README 顶部写清楚：当前只有 synthetic demo，不是真实成功案例。

## 7. Feedback

真实反馈为空。

当前不能写：

- 市场已验证；
- 用户已需要；
- 可以开始做插件或 SaaS；
- synthetic demo 是成功案例。

## 8. Decision

当前决策：

```text
收窄后继续验证
```

下一步不是继续完善 demo，而是公开发布最小包、私聊目标用户、收集真实失败任务。

## 9. Asset

可沉淀资产：

- checklist。
- `AGENTS.md` 模板。
- `CLAUDE.md` 对照模板。
- 私聊脚本。
- 反馈字段。
- 72 小时验证 SOP。
- SignalProof 流程质量门。

暂缓资产：

- Codex Plugin。
- Obsidian 插件。
- Web UI。
- 自动扫描器。
- SaaS。
- 服务页正式版。

## 10. Flow Review

流程自检结论：

- 这次 rerun 使用了 `last30days`，但结果弱相关，不能当强证据。
- 旧 Day 1 synthetic demo 没有使用 `last30days`，进入市场判断前补跑是必要的。
- Codex Pro / 插件系统里的搜索、调研、last30days、官方文档、GitHub/HN/Web 都应该作为候选能力，但必须审计结果质量。
- 后续 skill 必须加入工具质量门、last30days 质量门、子任务台账、真实反馈门。

当前可以进入 Day 2，但只能带着明确缺口推进。
