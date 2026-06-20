# Before / After 验证 Prompt

## Before

请在不新增 repo context audit 规则的情况下执行这个任务：

```text
<task>
```

要求：

- 记录你会改哪些文件。
- 记录你依据了哪些项目上下文。
- 不要读取新的 checklist 或模板。
- 输出结果保存为 `before.md`。

## Context Audit

使用 `repo-context-audit-checklist.md` 审计当前 `AGENTS.md` / `CLAUDE.md`，只补充能改变 agent 行为的关键规则：

- 失败模式。
- 目录边界。
- API / 后端契约。
- 已有组件和工具复用。
- 验证命令。

删除泛泛规则。

## After

请在更新后的 repo context 下执行同一个任务：

```text
<task>
```

要求：

- 输出结果保存为 `after.md`。
- 对比 before/after 是否更符合项目约定。
- 如果没有改善，明确写为反证。

## Comparison

请输出 `comparison.md`：

- 是否更少写偏。
- 哪条 context 规则产生了作用。
- 哪些问题仍然没有解决。
- 改善是否可能只是因为任务描述更清楚。
- 结论：有效 / 弱有效 / 无效 / 反向变差。
