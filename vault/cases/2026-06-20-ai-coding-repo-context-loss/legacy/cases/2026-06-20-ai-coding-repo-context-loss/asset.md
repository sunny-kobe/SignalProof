---
type: asset
status: published
asset_type: workflow-assets
created_at: 2026-06-20
path: /Users/rust/Documents/Codex/2026-06-19/new-chat-3/outputs/signalproof-rerun-2026-06-20/assets/repos/repo-ai-context-audit
url: https://github.com/Lan-Suny/repo-ai-context-audit
gate: published-not-validated-assumption-continued
---

# 复利资产

## 资产类型

当前可沉淀为：

- checklist。
- prompt。
- SOP。
- GitHub repo / gist。
- 案例文章。
- 方法论。
- SignalProof 流程质量门。

暂缓：

- Codex Plugin。
- Obsidian 插件。
- Web UI。
- 自动扫描器。
- SaaS。
- 服务页正式版。
- 付费资料包。

## 解决什么问题

帮助 AI coding 高频用户审计 repo-level instructions，减少 agent 在真实项目里写偏：

- 忽略现有组件；
- 改错 API 契约；
- 跨层改文件；
- 写出不像项目里的代码；
- 漏跑关键验证命令。

## 适合谁使用

- Codex / Claude Code 高频用户。
- 有真实 repo 和真实写偏任务的人。
- 想把个人 AI coding 工作流沉淀成可复用方法的人。

## 如何复用

1. 用 checklist 审计现有 `AGENTS.md` / `CLAUDE.md`。
2. 删除泛泛规则。
3. 只保留 agent 常写偏的高价值约束。
4. 选择一个真实写偏任务。
5. 跑 before/after。
6. 把结果写回 feedback 和 decision。

## 资产位置

本地可发布 repo/gist 包：

- `/Users/rust/Documents/Codex/2026-06-19/new-chat-3/outputs/signalproof-rerun-2026-06-20/assets/repos/repo-ai-context-audit`

旧 synthetic demo：

- `/Users/rust/Documents/Codex/2026-06-20/personal-opportunity-os-signalproof-codex-protocol-2/outputs/signalproof-vault/assets/repos/repo-ai-context-audit-demo/README.md`

本轮计划：

- `subtasks/artifact-plan.md`
- `assets/templates/`
- `assets/prompts/`
- `assets/sops/`
- `assets/repos/repo-ai-context-audit`

## 后续可继续验证什么

- 哪些 `AGENTS.md` 规则真的减少写偏。
- `AGENTS.md` 太长是否会降低质量。
- `CLAUDE.md` 和 `AGENTS.md` 是否应该分工。
- before/after 的改善是否来自上下文文件，还是来自更清晰的任务描述。
- 用户是否愿意为 repo context audit 服务付费。

## 当前资产状态

`repo-ai-context-audit` 已发布到 GitHub，但还没有真实用户反馈。资产状态是 `published-not-validated`，不是 `validated`。

用户已允许暂时跳过真实触达，并默认按中等评价继续推进。该假设只允许把资产继续沉淀为 SignalProof Protocol MVP 的示例 case，不能把它包装成真实成功案例。

## 可衍生方向

- 内容：《别把 AGENTS.md 写成第二份 README》。
- 服务：3 到 5 天 Repo AI Context Audit。
- 开源：`repo-ai-context-audit`。
- 产品：暂缓，除非多个真实 case 证明重复需求。
- 协议化：继续，把本 case 作为 SignalProof Protocol MVP 的第一个示例资产。
