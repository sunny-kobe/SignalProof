# Repo AI Context Audit

> 一个正在验证中的 AI coding repo context checklist。当前只有 synthetic demo，不是真实成功案例。

## 这个解决什么问题

Codex / Claude Code / Cursor 等 coding agents 在真实 repo 中经常写偏：

- 不遵守目录边界；
- 忽略已有组件；
- 改错 API 契约；
- 漏跑验证命令；
- 把通用最佳实践套到你的项目里。

问题不是“有没有上下文文件”。Codex 有 `AGENTS.md`，Claude Code 有 `CLAUDE.md`。真正的问题是：

```text
这个上下文文件有没有真的减少 AI 写偏？
```

## 这不是做什么

- 不是 AI coding 平台。
- 不是自动 repo 扫描器。
- 不是让 AI 永远理解项目。
- 不是官方 `AGENTS.md` / `CLAUDE.md` 替代品。
- 不是真实成功案例。
- 当前不做 Web App、SaaS、dashboard 或插件市场。

## 快速使用

1. 打开 `checklist/repo-context-audit-checklist.md`。
2. 用它审计你的 `AGENTS.md` / `CLAUDE.md`。
3. 删除泛泛规则，只保留 agent 常写偏的关键约束。
4. 选一个最近真实写偏任务。
5. 跑一次 before/after。
6. 把结果反馈到 issue 或表单。

## 文件结构

```text
repo-ai-context-audit/
  README.md
  checklist/
    repo-context-audit-checklist.md
  templates/
    AGENTS.md
    CLAUDE.md
  demo/
    task.md
    before.md
    after.md
    comparison.md
  prompts/
    collect-failure-task.md
    run-before-after.md
  feedback/
    feedback-form-fields.md
  LICENSE
```

## Synthetic demo

`demo/` 目录是人为构造的演示，用来说明 before/after 的比较方式。它不是用户案例，也不代表市场已经验证。

## 参与验证

我想找 5 个 Codex / Claude Code 高频用户一起验证：

你给我一个最近 AI 写偏的真实任务，我用这套 checklist 跑一次 before/after，看它到底有没有用。

提交时请包含：

- 使用工具：Codex / Claude Code / Cursor / 其他；
- repo 类型：前端 / 后端 / 全栈 / CLI / 其他；
- 原任务描述；
- AI 写偏点；
- 当前是否已有 `AGENTS.md` / `CLAUDE.md`；
- 是否可以公开或脱敏公开；
- 你希望改善什么。

## 72 小时验证目标

- 至少 3 个 A/B 级反馈；
- 至少 1 个真实失败任务；
- 至少 1 个目标用户愿意看 before/after；
- 至少 1 条具体反对意见让 checklist 变窄。

如果只有点赞、收藏，没有任务提交，这个方向应暂停或收窄。
