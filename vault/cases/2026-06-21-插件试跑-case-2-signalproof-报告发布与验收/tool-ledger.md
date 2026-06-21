---
type: tool_ledger
status: completed
updated_at: 2026-06-21
gate: passed
---

# 工具账本

## 候选能力账本

| 能力 | 是否相关 | 是否使用 | 结果质量 | 说明 | 下次动作 |
| --- | --- | --- | --- | --- | --- |
| Skill: signalproof | 是 | 是 | 中 | repo 级 skill 提供本地流程规则。 | 保留。 |
| Skill: personal-opportunity-os | 是 | 是 | 中 | 提供长期方向和流程边界。 | 保留为上层方法论。 |
| Skill: last30days | 否 | 否 | not-needed | 本 case 不是趋势调研。 | 调研 case 1 已实际运行。 |
| Browser | 是 | 是 | 失败 | setup 报 `codex/sandbox-state-meta: missing field sandboxPolicy`，不能做浏览器级验收。 | 修复后补验收截图。 |
| Computer Use | 是 | 是 | 失败 | `get_app_state(app="Codex")` 返回 macOS 错误 `-1743`。 | 修权限或换目标 App 后再跑。 |
| Record & Replay | 是 | 是 | 强 | `event_stream_status` 可读，适合录制用户演示。 | 默认作为资产化候选。 |
| GitHub CLI | 是 | 是 | 强 | 可读取 `sunny-kobe/SignalProof` 和 issues；issues 当前为空。 | 默认用于公开入口和开源反馈检查。 |
| Plugin | 是 | 是 | 中 | 已建立插件草案骨架。 | 后续安装测试。 |
| MCP | 中 | 否 | 弱 | 可接 OpenAI Docs、Context7、GitHub 等，但本轮先记录映射。 | 后续按阶段接入。 |
| Hooks | 中 | 否 | 弱 | 可用于强制 check-case。 | 后续加入。 |
| Automation | 中 | 否 | 弱 | 可用于 72h 反馈复查。 | 等发布渠道恢复后启用。 |

## 阶段能力计划

运行：

```bash
python3 scripts/signalproof.py capabilities
```

然后把本 case 各阶段真正考虑过的 Codex 自带插件记录到这里：

| 阶段 | 候选 Codex 插件 | 是否使用 | 结果质量 | 跳过或失败原因 | 下一步 |
| --- | --- | --- | --- | --- | --- |
| signal | Browser / Chrome / Record & Replay | 部分 | 强 | Record & Replay 状态可读；未启动录制。 | 用户演示时再录。 |
| research | GitHub / Browser / Chrome | 部分 | 强 | GitHub CLI 可读公开仓库；Browser 失败。 | Browser 修复后补网页级检查。 |
| debate | Browser / Chrome / Documents / PDF | 否 | not-needed | 本 case 不依赖外部长文档。 | 保留为候选。 |
| validation | Browser / Computer Use / GitHub / 文件级检查 | 是 | weak-to-medium | GitHub/文件级通过；Browser/Computer Use 失败。 | 拆分文件级与浏览器级 gate。 |
| artifact | Data Visualization / Reports / Presentations | 部分 | 中 | HTML 文件存在，但未完成 Browser 渲染验收；演示类产物在 case 3 通过 Presentations 试跑。 | 产物类详见 case 3。 |
| publication | Browser / Chrome / GitHub | 部分 | 中 | GitHub 仓库可读；无真实发布操作。 | 发布时再启用。 |
| feedback | Chrome / Browser / GitHub / Spreadsheets | 部分 | 弱 | GitHub issues 为空；不能代表无需求。 | 有反馈后再统计。 |
| asset | Record & Replay / Browser | 部分 | 强 | Record & Replay 可作为演示录制资产入口。 | 后续录一次真实发布/反馈流程。 |
| flow-review | Browser / Computer Use / 文件级检查 | 是 | weak-to-medium | 失败能力已记录并提供降级路线。 | 修复后补跑。 |

## 能力结论

本 case 证明验证插件需要分层：Record & Replay/GitHub 可默认候选，Browser/Computer Use 当前只能条件启用并保留降级路线。
