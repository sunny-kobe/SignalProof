---
type: process_log
title: Codex 插件实际调用流程验证
status: completed
updated_at: 2026-06-20
gate: passed
---

# 过程日志

## 迭代 1：确认能力矩阵

命令 / Command：

```bash
python3 scripts/signalproof.py capabilities
```

结果：

- 发现 Browser、Chrome、Computer Use、Record & Replay、Documents、PDF、Spreadsheets、Presentations、Data Visualization、HyperFrames 等候选插件。
- 生成 `vault/runs/2026-06-20-codex-capability-matrix.md`。

自检 / Self-check：

- 能力矩阵只能证明插件可发现，不能证明真实调用可用。

优化 / Optimization：

- 下一步必须至少选一个插件做实际调用，并把失败也写入账本。

## 迭代 2：尝试 Browser 插件真实调用

命令 / Command：

```js
const { setupBrowserRuntime } = await import('/Users/rust/.codex/plugins/cache/openai-bundled/browser/26.616.41845/scripts/browser-client.mjs');
await setupBrowserRuntime({ globals: globalThis });
globalThis.browser = await agent.browsers.get('iab');
nodeRepl.write(await browser.documentation());
```

结果：

```text
Mcp error: -32602: js: codex/sandbox-state-meta: missing field `sandboxPolicy`
```

自检 / Self-check：

- Browser 插件已经实际调用，但当前环境接入失败。
- 失败不能被隐藏，也不能用 Computer Use 成功覆盖掉。

优化 / Optimization：

- 在 `tool-ledger.md` 标为失败，并把 Browser 修复列为下一步。

## 迭代 3：调用 Computer Use 插件

命令 / Command：

```text
mcp__computer_use.list_apps({})
mcp__computer_use.get_app_state({"app":"Google Chrome"})
```

结果：

- `list_apps` 成功，返回本机运行应用列表。
- `get_app_state` 成功，读取到 Google Chrome 当前窗口。
- Chrome 窗口标题为 `sunny-kobe/SignalProof: SignalProof：Codex 优先的个人信号到资产证明协议`。
- 地址栏值为 `github.com/sunny-kobe/SignalProof`。

自检 / Self-check：

- Computer Use 可作为本机图形界面验收的降级路径。
- 这不是 Chrome 插件直接调用，也不是 DOM 级 Browser 验收。

优化 / Optimization：

- 在流程文档中补充“先记录失败，再选择降级路径”的规则。

## 迭代 4：写入案例和文档

命令 / Command：

```bash
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py export-all
python3 scripts/signalproof.py check-goal --min-cases 6
```

结果：

- `check-all` 通过，6 个案例全部通过。
- `export-all` 重新生成 6 份报告和报告索引。
- `check-goal --min-cases 6` 通过，报告索引路径为 `vault/reports/index.html`。

自检 / Self-check：

- 新案例必须包含 13 个必需文件。
- `feedback.md` 必须写明真实反馈为空。
- `tool-ledger.md` 必须包含 Skill、Plugin、MCP、Browser、Computer Use、Chrome、Documents、PDF、Spreadsheets、Presentations 和结果质量。
- 本轮上述条件已满足。

优化 / Optimization：

- 如果校验失败，优先修正案例结构和边界语言，不扩大功能范围。
