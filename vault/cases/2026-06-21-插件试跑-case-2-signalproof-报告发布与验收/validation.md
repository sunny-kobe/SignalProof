---
type: validation
status: planned
updated_at: 2026-06-21
gate: passed
---

# 验证计划

## 验证对象

验证报告发布与验收阶段是否应默认启用 Browser、Computer Use、Record & Replay、GitHub。

## 验证方式

1. 查询 Record & Replay 状态。
2. 尝试读取 Codex App 状态，记录 Computer Use 失败。
3. 尝试 Browser setup，记录失败。
4. 检查报告索引和 HTML 产物文件是否存在。
5. 用 GitHub CLI 检查仓库公开入口和 issue 反馈状态。
6. 把失败能力写成 `failed/tool`，而不是让流程卡死。

## 执行结果

- Record & Replay：通过，可作为资产化入口。
- GitHub CLI：通过，可作为公开入口检查。
- Browser：失败，不作为默认硬 gate。
- Computer Use：失败，不作为默认硬 gate。
- HTML/报告文件级检查：通过，但不等于浏览器渲染验收。

## 成功标准

- 验证插件失败时有明确降级路线。
- 不把文件存在写成浏览器视觉验收通过。
- 不把 GitHub issue 为空写成没有需求。

## 本轮 gate

`weak-to-medium`。流程可继续，但 Browser/Computer Use 不能进入默认验收 gate。
