# SignalProof Case Report: AI coding repo context loss

## 1. Signal Brief

AI coding 高频用户在真实 repo 中经常遇到 agent 不理解项目上下文、接口契约、目录边界、验证命令和团队约定，导致代码看似顺畅但不符合项目实际。机会不在做上下文平台，而在做 repo context audit 工作流。

## 2. Research Pack

Codex 官方机制支持 `AGENTS.md`，Skill / Plugin / Subagents 也支持 SignalProof 先作为 Codex 协议和 Skill 运行。本轮 `last30days` 已使用，但有效来源只有 GitHub + Reddit，且大量结果弱相关，不能作为强市场证据。

## 3. Debate Memo

严格反方裁决为“收窄后继续”。不做平台、插件、SaaS、dashboard 或服务承诺。保留最小切口：Repo AI Context Audit Checklist + 瘦身版 `AGENTS.md` / `CLAUDE.md` 模板 + synthetic demo + 72 小时真实失败任务验证。

## 4. Opportunity Thesis

当前结论是预验证阶段的“收窄后继续”。第一批用户是 Codex / Claude Code 高频用户。成功标准不是泛点赞，而是真实失败任务、A/B 级反馈和 before/after 改善。

## 5. Validation Plan

Day 2 已发布 GitHub repo，公开 checklist、模板、synthetic demo、私聊脚本和反馈字段。下一步是私聊 5 个目标用户，征集真实失败任务。

## 6. Artifact

已生成本地可发布 repo/gist 包：

- `assets/repos/repo-ai-context-audit`
- `https://github.com/Lan-Suny/repo-ai-context-audit`

同时生成草稿资产：

- `assets/templates/repo-context-audit-checklist.md`
- `assets/templates/AGENTS.md.template.md`
- `assets/templates/CLAUDE.md.template.md`
- `assets/prompts/collect-failure-task.md`
- `assets/prompts/run-before-after.md`
- `assets/sops/72-hour-validation-sop.md`
- `assets/articles/day2-cn-post.md`
- `assets/services/repo-context-audit-service-draft.md`

## 7. Feedback Evidence

GitHub repo 和真实任务征集 issue 已发布，但真实反馈为空。不能写验证成功。

## 8. Decision Memo

预验证决策：收窄后继续验证。暂不产品化，暂不插件化，暂不服务化承诺。

## 9. Reusable Asset

当前可复用资产是 checklist、模板、prompt、SOP、case report、Flow Review 质量门和已发布 GitHub repo。状态是 published-not-validated，不是 validated。

## 10. Flow Review

本次最重要的流程发现：工具调用不等于证据有效。`last30days` 已使用，但 query 太宽、来源覆盖弱、结果相关性不足，因此必须引入 last30days 质量门、研究分层查询、工具失败记录门、子任务台账和 completion receipt 增补字段。
