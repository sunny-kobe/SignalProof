---
type: signal
title: AI coding repo context loss
status: captured
source_type: internal_signal
source_url:
captured_at: 2026-06-20
tags: [ai-coding, codex, claude-code, agents-md, workflow]
---

# 信号

## 这是什么

AI coding 用户在真实 repo 里使用 Codex / Claude Code / Cursor / 其他 coding agents 时，经常遇到 agent 不理解项目上下文、接口契约、目录边界、验证命令和团队约定，导致输出代码看似能运行但不符合项目实际规范。

## 为什么引起注意

这和用户个人优势高度贴合：用户长期使用 Codex、Claude Code、MCP、本地工具链和复杂前端项目，已经能识别“AI 写代码”之外更高层的问题：如何让 AI 稳定理解项目边界、如何验证输出、如何把工作流沉淀为可复用资产。

## 初步用户

- Codex / Claude Code 高频用户。
- 在真实业务 repo 中使用 AI coding 的前端或全栈工程师。
- 小团队里推动 AI coding 工作流的人。
- 对 `AGENTS.md`、`CLAUDE.md`、repo instructions 有兴趣但不知道怎么维护的人。

## 初步机会

不是做“AI coding 上下文平台”，而是做一套可公开验证的 repo context audit 工作流：

- 识别 agent 常写偏的真实任务；
- 审计 repo 指令文件和上下文入口；
- 输出瘦身版 `AGENTS.md` / `CLAUDE.md` 模板；
- 做 before/after 对比；
- 形成 checklist、prompt、SOP 和服务验证素材。

## 相关证据

- Codex 官方 manual 说明 Codex 会读取 `AGENTS.md`，并支持全局、项目、子目录层级。
- Codex 官方 manual 说明 Skills 是 reusable workflow 的 authoring format，Plugins 是可安装分发单位。
- `last30days` 已运行，但本轮结果源覆盖不足且噪音较高，不能直接当强市场证据。
- 旧 demo 已有 synthetic before/after 资产，但没有真实用户反馈。

## 进入研究的理由

- 痛点和用户个人能力匹配；
- 官方机制已经存在，说明方向不是空想；
- 旧 demo 证明可以做出可解释演示；
- 但真实需求、真实讨论和可服务化证据不足，需要重跑完整链路。

## 暂不研究的理由

- 如果只做模板，容易被官方文档或通用博客替代；
- 如果做平台，范围会膨胀；
- 如果缺少真实 before/after，价值容易变成泛泛工程规范。
