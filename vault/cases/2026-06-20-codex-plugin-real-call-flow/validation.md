---
type: validation
status: validated-internally
updated_at: 2026-06-20
gate: passed
---

# 验证计划

## 验证目标

验证 SignalProof 是否能按插件实际调用流程完整跑一轮，并把真实结果写回案例。

## 验证步骤

1. 运行 `python3 scripts/signalproof.py capabilities`，确认 Codex 自带插件候选。
2. 按 Browser 插件 skill 的接入路径尝试连接 in-app Browser。
3. 调用 Computer Use 的 `list_apps`，确认本机应用可读。
4. 调用 Computer Use 的 `get_app_state` 读取 Google Chrome。
5. 把 Browser 失败、Computer Use 成功、Chrome 可见页面写入研究和工具账本。
6. 更新流程文档，形成后续可复用的插件调用循环。

## 成功标准

- 能明确区分“插件文件可发现”和“插件真实调用可用”。
- Browser 失败有错误类型、影响和补救动作。
- Computer Use 成功有可核对的目标应用、窗口标题和 URL。
- 工具结果质量被分级为强、中、弱或失败。
- 自检命令通过。

## 实际结果

- 能力矩阵：通过，插件候选可发现。
- Browser 插件：失败，错误为 `codex/sandbox-state-meta: missing field sandboxPolicy`。
- Computer Use `list_apps`：通过，能读取本机应用列表。
- Computer Use `get_app_state Google Chrome`：通过，能读取 GitHub 仓库页面。

## 验证边界

- 这不是外部用户反馈。
- 这不是登录态 Chrome 插件直接调用。
- 这不是 Browser 页面级验收完成。
- 这只能证明第一轮插件实际调用流程已经跑通，并暴露了下一步缺口。
