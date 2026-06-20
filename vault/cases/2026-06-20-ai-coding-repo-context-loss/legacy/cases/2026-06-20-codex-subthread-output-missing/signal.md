---
type: signal
title: Codex 子线程完成但未落目标文件
status: captured
source_type: internal-workflow-failure
source_url:
captured_at: 2026-06-20
tags: [codex, signalproof, subthread, workflow-quality]
---

# 信号

## 这是什么

在 SignalProof Day 2 闭环审计中，主线程 fork 了一个同目录子线程，并要求它输出：

```text
outputs/signalproof-rerun-2026-06-20/subtasks/day2-loop-audit.md
```

子线程状态显示完成，但目标文件没有生成。源线程随后检查文件时发现缺失，并接管补齐。

## 为什么引起注意

这个问题直接影响 SignalProof 的核心承诺：Codex 不让用户当 prompt 搬运工，能跨会话派发、接收回执、验收结果并回写 vault。

如果子线程“看起来完成”但没有落文件，主线程又不做文件级验收，整个协作链路会产生假完成。

## 初步用户

- 高频使用 Codex 多线程/多会话协作的人；
- 想把 Codex 用成个人工作流系统的人；
- 需要把子任务结果沉淀到本地 vault 的人。

## 初步机会

把“子线程文件级验收”固化成 SignalProof Protocol 的强制质量门。

## 相关证据

- `subtasks/day2-loop-audit.md` 由源线程补齐，状态为 `source-thread-repaired`。
- `subtasks/index.md` 已记录该子线程未落文件。
- `completion-audit.md` 已记录新增流程教训。

## 进入研究的理由

这是刚刚真实发生的流程失败，不是外部市场假设。它能帮助验证 SignalProof Protocol 是否能自我修复和复利。

## 暂不研究的理由

不需要做大规模市场研究。这个 case 的目标不是商业验证，而是内部协议质量验证。
