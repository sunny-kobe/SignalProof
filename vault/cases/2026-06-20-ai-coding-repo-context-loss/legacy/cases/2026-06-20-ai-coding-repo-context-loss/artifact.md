---
type: artifact
status: published
artifact_type: github-repo-or-gist
url: https://github.com/Lan-Suny/repo-ai-context-audit
path: /Users/rust/Documents/Codex/2026-06-19/new-chat-3/outputs/signalproof-rerun-2026-06-20/assets/repos/repo-ai-context-audit
published_at: 2026-06-20
gate: published-awaiting-feedback
---

# 公开产物

## 产物类型

Day 2 最小发布包：

```text
repo-ai-context-audit
```

形态：GitHub repo 或 gist。

不做 Web App，不做 SaaS，不做 dashboard，不做自动扫描器。

## 核心承诺

不是“让 AI 永远理解你的项目”，而是：

```text
用一份轻量 checklist 审计 AGENTS.md / CLAUDE.md，验证它能否减少 AI coding 在真实 repo 中写偏。
```

## 面向谁

- Codex / Claude Code 高频用户。
- 经常遇到 AI 写偏、跨层改文件、忽略接口契约、漏用已有组件的人。
- 愿意提交真实失败任务做 before/after 的 AI coding power user。

## 建议 repo 结构

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

## README 必须写清楚

- 当前是验证中的 checklist。
- 当前只有 synthetic demo，不是真实成功案例。
- 不替代官方 `AGENTS.md` / `CLAUDE.md` 文档。
- 不承诺自动理解 repo。
- 最需要的是用户提交真实 AI 写偏任务。

## 中文发布文案

标题：

```text
别把 AGENTS.md 写成第二份 README：我做了一个 AI coding repo context 审计 checklist
```

正文：

```text
最近我在验证一个很窄的问题：

AI coding 工具不是不会写代码，而是经常在真实 repo 里写偏。

比如：
- 不知道项目的接口契约；
- 忽略已有组件和 formatter；
- 把 0/1 枚举改成 boolean；
- 跨层改文件；
- 没跑项目真正需要的验证命令。

Codex 有 AGENTS.md，Claude Code 有 CLAUDE.md，但问题不是“有没有上下文文件”，而是“这个文件有没有真的减少 AI 写偏”。

所以我做了一个很小的 Repo AI Context Audit checklist：
- 审计你的 AGENTS.md / CLAUDE.md；
- 删除泛泛规则；
- 只保留 AI 真正容易写偏的约束；
- 用一个 before/after 任务验证它有没有用。

目前只有 synthetic demo，不是成功案例。

我想找 5 个 Codex / Claude Code 高频用户一起验证：
你给我一个最近 AI 写偏的真实任务，我用这套 checklist 跑一次 before/after，看它到底有没有用。

如果你也遇到过“AI 写得很顺，但完全不像这个项目里的代码”，可以把任务丢给我。
```

## 私聊脚本

```text
我最近在验证一个很窄的 AI coding 工作流：

不是教人写 AGENTS.md，而是审计 repo context 能不能减少 Codex / Claude Code 在真实项目里写偏。

我想找 5 个高频 AI coding 用户做一个小测试：
你给我一个最近 AI 写偏的任务，我用 checklist 帮你脱敏跑一次 before/after。

我不会把它包装成成功案例，也不会公开你的 repo。
我只想验证这件事到底有没有用：
一份更瘦、更贴近失败模式的 AGENTS.md / CLAUDE.md，是否能让 agent 少犯同类错。

你最近有没有一个 AI 明显写偏的任务？
```

## 当前状态

- 草稿 / 可发布 / 已发布 / 已更新 / 已归档：已发布。
- 已有旧 synthetic demo：`/Users/rust/Documents/Codex/2026-06-20/personal-opportunity-os-signalproof-codex-protocol-2/outputs/signalproof-vault/assets/repos/repo-ai-context-audit-demo/README.md`
- 当前新 run 已生成本地可发布 repo/gist 包：`/Users/rust/Documents/Codex/2026-06-19/new-chat-3/outputs/signalproof-rerun-2026-06-20/assets/repos/repo-ai-context-audit`
- GitHub 发布链接：`https://github.com/Lan-Suny/repo-ai-context-audit`

## 复用价值

- checklist。
- `AGENTS.md` 模板。
- `CLAUDE.md` 对照模板。
- 私聊 prompt。
- before/after prompt。
- 反馈表字段。
- 72 小时验证 SOP。

## 发布前必须保留的边界

- 当前只有 synthetic demo。
- 真实反馈为空。
- 不能写市场已验证。
- 不能写成功案例。
- 不能包装成平台、插件、SaaS 或自动扫描器。

## 后续可扩展为

- 模板：立即可做。
- checklist：立即可做。
- repo：Day 2 可做。
- SOP：Day 2 可做。
- 服务页：至少 1 个真实 before/after 后再做。
- Codex skill / plugin：至少 2 到 3 个不同 case 跑完后再做。
- 资料包：至少有真实反馈和案例后再做。
