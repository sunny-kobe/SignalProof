---
type: signal
title: Codex 插件实际调用流程验证
status: captured
source_type: internal-workflow
source_url:
captured_at: 2026-06-20
tags:
  - SignalProof
  - Codex 插件
  - 流程自检
---

# 信号

## 这是什么

当前 SignalProof 已经有 Codex 自带插件能力矩阵，但能力矩阵只能说明插件文件和入口存在，不能证明真实调用路径可用。

这次信号是：按“插件实际调用”的方式跑一遍流程，把成功、失败、降级和下一步都写入案例，而不是只停留在文档设计。

## 为什么引起注意

SignalProof 的价值不只是生成案例文件，还要让 Codex 在每个阶段判断该用什么能力、实际调用、记录结果质量，并把流程缺口沉淀成下次优化。

如果 Browser、Computer Use、Chrome 等插件只是列在能力矩阵里，却没有真实调用记录，后续流程会高估自动化能力。

## 初步用户

- 当前用户本人：希望把个人 Codex 工作流从“会写文档”推进到“能调用插件并审计流程”。
- 未来使用 SignalProof 的 Codex 高阶用户：需要知道哪个阶段该用哪个插件，以及插件失败时怎么记录和降级。

## 初步机会

把“能力矩阵 -> 实际调用 -> 工具账本 -> 流程自检 -> 下一轮优化”固化成 SignalProof 的标准验证环节。

## 相关证据

- `python3 scripts/signalproof.py capabilities` 可生成 Codex 自带插件能力矩阵。
- Browser 插件按自身 skill 的接入方式调用时失败，错误为 `codex/sandbox-state-meta: missing field sandboxPolicy`。
- Computer Use 插件 `list_apps` 调用成功，能读取本机正在运行的应用列表。
- Computer Use 插件 `get_app_state` 读取 Google Chrome 成功，确认 Chrome 打开的是 `github.com/sunny-kobe/SignalProof`。

## 进入研究的理由

这是 SignalProof 插件化流程的关键内部验证。它能证明当前流程是否已经从“文档规划”进入“真实工具调用和失败记录”阶段。

## 暂不研究的理由

本案例不做外部市场研究，也不需要 `last30days`。它验证的是本地 Codex 插件调用链，不是用户需求热度。
