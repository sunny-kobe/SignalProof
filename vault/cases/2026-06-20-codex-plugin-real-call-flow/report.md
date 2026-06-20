---
type: report
title: Codex 插件实际调用流程验证
status: completed
updated_at: 2026-06-20
gate: passed
---

# 报告

## 一句话结论

第一轮 Codex 插件实际调用流程已经跑通：Browser 插件真实调用失败，Computer Use 插件真实调用成功，二者都已进入工具账本和流程自检。

## 关键发现

- 能力矩阵有价值，但不足以证明插件可用。
- Browser 当前卡在 `sandboxPolicy` 字段问题。
- Computer Use 能读取本机应用和 Chrome 页面状态。
- SignalProof 需要把插件失败视为流程证据，而不是跳过。

## 决策

继续优化内部协议，下一步补 Browser 修复和报告索引页面验收。

## 边界

本案例只证明内部插件调用流程，不证明外部需求。
