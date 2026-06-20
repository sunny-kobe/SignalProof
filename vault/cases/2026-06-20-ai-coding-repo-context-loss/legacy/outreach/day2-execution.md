---
type: day2_execution
status: ready-for-human-channel
updated_at: 2026-06-20
gate: collecting
---

# Day 2 执行账本

## 当前目标

把 `repo-ai-context-audit` 从公开产物推进到真实反馈。

本阶段不继续加功能，不做 dashboard，不做插件化，不做 SaaS。唯一目标是拿到真实 AI coding 写偏任务，验证 checklist 是否能减少同类错误。

## 已完成

- GitHub repo 已发布：`https://github.com/Lan-Suny/repo-ai-context-audit`
- 真实任务征集 issue 已创建：`https://github.com/Lan-Suny/repo-ai-context-audit/issues/1`
- 中文发布文案已准备：`assets/articles/day2-cn-post.md`
- 私聊文案已准备：`assets/prompts/collect-failure-task.md`
- 72 小时验证 SOP 已准备：`assets/sops/72-hour-validation-sop.md`
- 反馈字段已准备：`assets/repos/repo-ai-context-audit/feedback/feedback-form-fields.md`
- 72 小时反馈复查 heartbeat 已创建：`signalproof-72h`

## 当前外部指标

核验时间：2026-06-20

| 指标 | 当前值 |
| --- | ---: |
| star | 0 |
| fork | 0 |
| issue | 1 |
| issue comments | 0 |
| 真实失败任务 | 0 |
| 真实 before/after | 0 |
| A/B 级反馈 | 0 |

## 触达渠道

| 渠道 | 状态 | 下一步 |
| --- | --- | --- |
| GitHub issue | 已创建 | 等待外部提交或手动邀请目标用户提交 |
| 中文朋友圈/社群/帖子 | 未发送 | 使用 `assets/articles/day2-cn-post.md` |
| 5 个目标用户私聊 | 未发送 | 使用 `assets/prompts/collect-failure-task.md` |
| GitHub repo README | 已发布 | 观察 star/fork/issue/comment |

## 5 个目标用户槽位

这一步需要真实触达渠道。Codex 可以准备、跟踪和整理，但不能伪造外部反馈。

| 编号 | 人群类型 | 候选人/渠道 | 是否已发送 | 是否回复 | 反馈等级 | 是否提交真实任务 | 下一步 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Codex 高频用户 | 待补 | no | no |  | no |  |
| 2 | Claude Code 高频用户 | 待补 | no | no |  | no |  |
| 3 | Cursor / AI coding 高频用户 | 待补 | no | no |  | no |  |
| 4 | 小团队工程负责人 | 待补 | no | no |  | no |  |
| 5 | 熟悉 repo context 的工程师 | 待补 | no | no |  | no |  |

## 发送文案

```text
我最近在验证一个很窄的 AI coding 工作流：

不是教人写 AGENTS.md，而是审计 repo context 能不能减少 Codex / Claude Code 在真实项目里写偏。

我想找 5 个高频 AI coding 用户做一个小测试：
你给我一个最近 AI 写偏的任务，我用 checklist 帮你脱敏跑一次 before/after。

GitHub repo 在这里：
https://github.com/Lan-Suny/repo-ai-context-audit

目前只有 synthetic demo，不是成功案例。
我不会公开你的 repo，也不会把它包装成成功案例。

你最近有没有一个 AI 明显写偏的任务？
```

## 回复处理规则

- A：提交真实任务 + 具体写偏点 + 愿意看 before/after。立即进入真实 before/after。
- B：没有任务，但给出具体反对意见或改进建议。更新 checklist 或反方记录。
- C：收藏、点赞、泛泛支持。记录，但不算有效验证。
- D：无关讨论。忽略。

只有 A/B 算有效验证信号。

## 收到真实任务后的 Codex 操作

1. 把原任务和写偏点写入 `feedback.md`。
2. 建立脱敏任务目录：`assets/real-cases/<date>-<short-name>/`。
3. 运行 `assets/prompts/run-before-after.md`。
4. 生成 `before.md`、`after.md`、`comparison.md`。
5. 判断改善来源：来自 checklist / 来自更清晰任务描述 / 没改善。
6. 更新 `decision.md`、`asset.md`、`flow-review.md` 和总报告。

## 72 小时决策门

继续条件：满足任意 3 条。

- 至少 3 个 A/B 级反馈。
- 至少 1 个真实失败任务。
- 至少 1 个目标用户愿意看 before/after。
- 至少 1 条具体反对意见让 checklist 变窄。
- GitHub repo 出现 issue、fork、PR、明确改进建议或高质量 star。

暂停或收窄条件：

- 只有点赞、收藏，没有任务提交。
- 5 个目标用户都没有兴趣。
- 用户觉得官方文档足够。
- 真实 before/after 没改善。
- 改善来自更清晰的任务描述，而不是 checklist。
- 为了讲清价值必须做 dashboard、自动扫描器或 SaaS。

## 当前结论

当前 Day 2 尚未完成。公开入口已经存在，但真实触达和真实反馈还没发生。

下一步需要真实渠道输入：5 个目标用户或可发布的中文渠道。Codex 可以代写、代跟踪、代分析、代回填，但不能把未发生的触达写成已发生。
