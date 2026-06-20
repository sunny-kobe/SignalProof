# 别把 AGENTS.md 写成第二份 README

最近我在验证一个很窄的问题：

AI coding 工具不是不会写代码，而是经常在真实 repo 里写偏。

比如：

- 不知道项目的接口契约；
- 忽略已有组件和 formatter；
- 把 `0/1` 枚举改成 boolean；
- 跨层改文件；
- 没跑项目真正需要的验证命令。

Codex 有 `AGENTS.md`，Claude Code 有 `CLAUDE.md`，但问题不是“有没有上下文文件”，而是“这个文件有没有真的减少 AI 写偏”。

所以我做了一个很小的 Repo AI Context Audit checklist：

- 审计你的 `AGENTS.md` / `CLAUDE.md`；
- 删除泛泛规则；
- 只保留 AI 真正容易写偏的约束；
- 用一个 before/after 任务验证它有没有用。

目前只有 synthetic demo，不是成功案例。

我想找 5 个 Codex / Claude Code 高频用户一起验证：

你给我一个最近 AI 写偏的真实任务，我用这套 checklist 跑一次 before/after，看它到底有没有用。

如果你也遇到过“AI 写得很顺，但完全不像这个项目里的代码”，可以把任务丢给我。
