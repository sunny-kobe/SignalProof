# Day 2 最小发布包

## 结论

不要做 Web App，不要做 SaaS，不要做 dashboard。Day 2 只做一个可公开、可复用、可验证的最小发布包：

```text
Repo AI Context Audit Checklist + AGENTS.md / CLAUDE.md 模板 + synthetic before/after demo + 真实失败任务反馈入口
```

## GitHub repo / gist 结构

```text
repo-ai-context-audit/
  README.md
  checklist.md
  templates/
    AGENTS.md
    CLAUDE.md
  demo/
    task.md
    project-conventions.md
    before.md
    after.md
    comparison.md
  feedback.md
```

## README 大纲

- 这个 repo 解决什么问题。
- 不解决什么问题。
- 适合谁。
- 5 分钟使用方式。
- Synthetic demo 的边界。
- 如何提交真实 AI 写偏任务。
- 72 小时验证目标。

## 中文发布文案

我在验证一个很小的 AI coding 工作流问题：很多时候不是模型不会写代码，而是它没读懂真实 repo 的上下文。

我做了一个最小版 Repo AI Context Audit：一份 checklist、一个瘦身版 `AGENTS.md` / `CLAUDE.md` 模板、一个 synthetic before/after demo。

这不是成功案例，也不是 SaaS。我想找真实 AI coding 高频用户，用你最近“AI 写偏了”的任务来挑战这份 checklist。

我想验证的不是“上下文文件越多越好”，而是哪些 repo 规则真的会改变 AI 输出。

## 私聊脚本

最近我在验证一个小工作流：Repo AI Context Audit。

我想找 5 个真实 AI coding 高频用户，收集一个你最近遇到的“AI 写偏了”的任务。你只要给我任务描述、AI 写偏的地方、项目里它没遵守的关键约定，以及可以公开或脱敏到什么程度。

我会用 checklist 做一次 before/after，并把结果回给你。现在还没有真实反馈，所以我不想包装成成功案例，只想验证它到底有没有用。

## 反馈表字段

- 角色。
- 使用工具。
- 任务类型。
- AI 写偏的地方。
- 项目上下文入口。
- 是否愿意提交脱敏任务。
- 期望 checklist 帮你解决什么。
- 是否愿意继续私聊。

## 72 小时动作

1. 整理 GitHub repo 或 gist。
2. 发布中文短文。
3. 私聊 5 个 AI coding 高频用户。
4. 收集真实失败任务。
5. 把反馈更新回 `feedback.md`。
6. 72 小时后更新 `decision.md`。

## 成功标准

- 至少 3 个具体使用信号。
- 至少 1 个真实失败任务进入 before/after。
- 至少 1 条高质量反对意见让 checklist 变窄。

## Kill 条件

- 只有泛点赞。
- 没人提交真实失败任务。
- 真实 before/after 无明显改善。
- 用户认为官方文档已足够。

## 可以沉淀的资产

- checklist。
- `AGENTS.md` / `CLAUDE.md` 模板。
- 发布文案。
- 私聊脚本。
- 反馈表字段。
- 72 小时验证 SOP。

## 暂缓的资产

- Obsidian 插件。
- GitHub/HN/RSS 自动适配器。
- n8n / Dify 集成。
- Web dashboard。
- SaaS。
- Codex Plugin 正式分发。

## Completion Receipt

委派任务名称：SignalProof rerun - publishable artifact plan

状态：completed / ready-for-source-review

新增文件：

- `/Users/rust/Documents/Codex/2026-06-19/new-chat-3/outputs/signalproof-rerun-2026-06-20/subtasks/artifact-plan.md`

关键结论：Day 2 只发布最小验证包，不做应用、不做平台、不做 dashboard。核心动作是拿真实 AI 写偏任务挑战 checklist。

明确边界：synthetic demo 只能作为演示，不能包装成真实反馈或成功案例。

下一步：整理实际 repo/gist 文件并发布，私聊 5 个目标用户。
