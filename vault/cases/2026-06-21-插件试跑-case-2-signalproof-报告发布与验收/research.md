---
type: research
status: completed
updated_at: 2026-06-21
gate: weak
---

# 研究

## 要回答的问题

- 验证类插件是否能让 SignalProof 报告、HTML 索引和本地页面验收更可靠？
- Browser、Computer Use、Record & Replay 在当前环境下是否能作为默认验收 gate？
- 如果 GUI/浏览器插件失败，SignalProof 是否有降级验收路线？

## 已确认事实

- Record & Replay 的 `event_stream_status` 可见，返回 `isRecording=false`，最大录制 1800 秒。
- Computer Use 调用 `get_app_state(app="Codex")` 失败，返回 macOS 错误 `-1743`。
- Browser 插件 setup 失败，错误为 `codex/sandbox-state-meta: missing field sandboxPolicy`。
- `vault/reports/index.html` 和插件评估 HTML 文件存在，可以走文件级检查，但不能写成 Browser 视觉验收通过。
- GitHub CLI 可读取仓库公开状态，适合验证发布入口；当前 GitHub issues 为空，不能作为外部反馈。

## 证据强度

| 能力 | 结果质量 | 说明 |
| --- | --- | --- |
| Record & Replay | 强 | 工具状态可读，适合后续把用户演示转为 Skill。 |
| GitHub CLI | 强 | 能读取公开仓库，适合发布入口和开源反馈检查。 |
| Browser | 失败 | 当前环境 setup 失败，不能作为硬性验收 gate。 |
| Computer Use | 失败 | 当前 macOS 权限或目标 App 状态读取失败，不能作为默认 gate。 |
| 文件级检查 | 中 | 能证明 HTML/报告文件存在，但不能证明浏览器渲染正常。 |

## 当前判断

验证类插件有价值，但当前默认策略应是：Record & Replay 默认候选；GitHub CLI 默认检查公开入口；Browser/Computer Use 先保持条件候选并提供降级路线。
