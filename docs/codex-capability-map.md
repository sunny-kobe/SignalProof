# Codex 能力地图

这份地图基于 2026-06-20 当前本地 Codex 手册刷新结果，以及本地 plugin/skill 检查结果。

## 稳定能力面

| 能力面 | SignalProof 里的角色 | 当前使用方式 |
| --- | --- | --- |
| Skill | 可复用工作流说明 | repo skill 位于 `.agents/skills/signalproof/` |
| Plugin | 可安装的分发包 | 草案包位于 `plugins/signalproof/` |
| MCP | 实时工具和外部上下文 | 候选能力，尚未打包绑定 |
| AGENTS.md | repo 本地持久规则 | 根目录 `AGENTS.md` |
| Hooks | 机械化生命周期约束 | 未来候选质量门 |
| Automations | 定时复查 | 可用于反馈复查 |
| In-app Browser | 本地预览和视觉验收 | 可用于报告预览检查 |
| Computer Use | 结构化工具不足时的 GUI 操作 | 仅作为候选；本轮没有直接工具暴露 |
| last30days | 最近公开讨论和来源研究 | 研究阶段候选能力 |

## 本地能力快照

`last30days --diagnose` 当前报告这些来源可用：

```text
reddit, tiktok, instagram, x, youtube, hackernews, polymarket, github, perplexity, threads
```

已知缺口：

```text
Safari cookie read permission denied。如果需要浏览器 cookie 抽取，需要开启 Full Disk Access。
```

本机默认 `python3` 是 3.9.6，对 `last30days` 太旧；运行时使用 `python3.14`。

## 工具选择规则

不要每个 case 都强行使用所有能力。只有当某个能力能改变决策、减少不确定性或验收产物时，才使用它。

跳过相关能力时，必须在 `tool-ledger.md` 记录原因。
