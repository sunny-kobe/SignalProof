---
type: signal
title: Codex 推荐插件真实试跑评估
case_type: external-opportunity
status: captured
created_at: 2026-06-21
gate: passed
---

# 信号

## 原始信号

用户指出当前 SignalProof 流程里“好多插件都没用”，特别是调研类、验证类、产物类插件。要求按 `docs/codex-plugin-audit.md` 的推荐插件清单，把推荐插件全部安装，并实际跑多个 case，判断哪些插件能让个人工作流明显提升，哪些不值得默认使用。

## 为什么值得进入流程

- 这是对 SignalProof 自身流程的反向压力测试：如果工具账本只写“候选能力”，但真实执行时没有调用插件，就会变成形式主义。
- Codex 官方插件不是单一能力，可能包含 Skill、App connector、MCP server 和 runtime 文件产物能力，必须拆开验证。
- 用户需要的是个人可复利工作流，不是插件越多越好；最终要沉淀“默认用、条件用、暂不用”的实际判断。

## 本轮验证对象

- A 级推荐插件源表：`docs/codex-plugin-audit.md` 中 40 个推荐条目。
- 已安装 marketplace 插件：36 个 `installed, enabled`。
- 运行时插件：`documents`、`pdf`、`spreadsheets`、`presentations`。
- 实际调用证据：GitHub、Hugging Face 公开 API、Zotero 本地 API 状态、last30days、Record & Replay 状态、Computer Use、Browser、Spreadsheets、Data Visualization、Documents、PDF、Presentations、HyperFrames。

## 当前边界

- 已安装不等于当前线程已暴露工具。
- App connector 类插件如果没有账号授权或当前线程没有工具入口，只能写 `blocked/auth-or-tool`，不能写成“0 结果”。
- 本轮仍不声称市场验证；它验证的是 Codex 插件是否能改善 SignalProof 的内部研究、验证和资产化流程。
