---
type: validation
status: planned
started_at: 2026-06-20
deadline: 2026-06-23
gate: ready-for-day-2
---

# 验证计划

## 目标用户

- Codex / Claude Code 高频用户。
- 已经在真实业务 repo 中使用 AI coding 的前端或全栈工程师。
- 小团队里推动 AI coding 工作流的人。
- 对 `AGENTS.md`、`CLAUDE.md`、repo instructions 有兴趣但没有稳定维护方法的人。

## 核心假设

AI coding 高频用户不是缺“更多上下文”，而是缺一套能把 repo 指令变短、变准、可验证的审计流程。

最小可验证问题：

```text
目标用户是否愿意提交一个真实 AI 写偏任务，并用 checklist 观察 before/after 是否改善？
```

## 最小公开产物

- GitHub repo 或 gist：`repo-ai-context-audit`。
- `repo-context-audit-checklist.md`。
- 瘦身版 `AGENTS.md` 模板。
- 可选 `CLAUDE.md` 对照模板。
- synthetic before/after demo。
- 私聊脚本。
- 反馈字段。
- 72 小时验证记录。

## 发布渠道

- GitHub repo：`https://github.com/Lan-Suny/repo-ai-context-audit`
- 中文短文：朋友圈、即刻、小红书、公众号或技术社群任选一个轻发布渠道。
- 私聊 5 个目标用户。

## 行动引导

不要引导用户“夸一夸这个想法”，只引导具体动作：

- 复制 checklist 审计自己的 `AGENTS.md` / `CLAUDE.md`。
- 提交一个最近 AI 写偏的真实任务。
- 指出 checklist 哪条没用、哪条缺失。
- 如果 repo 不能公开，可以脱敏描述任务、目录边界和写偏点。

## 反馈来源

- GitHub star / fork / issue / PR。
- 真实任务征集 issue：`https://github.com/Lan-Suny/repo-ai-context-audit/issues/1`
- repo/gist 评论。
- 社媒评论、收藏、私信。
- 私聊目标用户的任务提交。
- before/after 结果。
- 强反对意见。

## 反馈质量分级

- A：提交真实任务 + 具体写偏点 + 愿意看 before/after。
- B：没有任务，但给出具体反对意见或改进建议。
- C：收藏、点赞、泛泛支持。
- D：无关讨论或泛 AI 情绪。

只有 A/B 算有效验证信号。

## 最小成功标准

72 小时内满足以下任意 3 条，才算继续：

- 至少 3 个 A/B 级反馈。
- 至少 1 个真实失败任务。
- 至少 1 个目标用户愿意看 before/after。
- 至少 1 条具体反对意见让 checklist 变窄。
- GitHub repo/gist 出现 issue、fork、PR、明确改进建议或高质量 star。

更强继续信号：

- 有人主动问能不能帮他审计 repo context。
- 有人愿意公开脱敏案例。
- 有人愿意为 3 到 5 天诊断服务付费或交换资源。

## 放弃条件

- 只有点赞、收藏，没有任务提交。
- 5 个目标用户都没有兴趣。
- 用户觉得官方文档足够。
- 真实 before/after 没改善。
- 改善来自更清晰的任务描述，而不是 checklist。
- 为了讲清价值必须做工具、dashboard 或自动扫描器。

## 时间限制

```text
Day 2: 发布最小 repo/gist + 私聊 5 人
Day 3: 收集反馈 + 选择 1 个真实任务
Day 4: 跑 before/after + 更新决策
```

## 当前边界

当前已有真实发布链接和公开任务征集 issue，但没有真实用户反馈。因此本 case 不能写“验证成功”，只能写“进入公开验证并等待反馈”。
