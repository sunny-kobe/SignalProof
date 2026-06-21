# Codex 能力地图

这份地图基于 2026-06-21 当前本地 Codex 手册刷新结果、`codex plugin list` 和重启后只读深测线程结果。

## 稳定能力面

| 能力面 | SignalProof 里的角色 | 当前使用方式 |
| --- | --- | --- |
| Skill | 可复用工作流说明 | repo skill 位于 `.agents/skills/signalproof/` |
| Plugin | 可安装的分发包 | 草案包位于 `plugins/signalproof/` |
| MCP | 实时工具和外部上下文 | 候选能力，尚未打包绑定 |
| AGENTS.md | repo 本地持久规则 | 根目录 `AGENTS.md` |
| Hooks | 机械化生命周期约束 | 未来候选质量门 |
| Automations | 定时复查 | 可用于反馈复查 |
| In-app Browser | 本地预览和视觉验收 | 候选能力；历史 setup 失败，修复前不做硬 gate |
| Chrome | 依赖用户现有登录态、cookie 或打开标签页的网页验收 | 只在用户明确需要登录态或指定 Chrome 时使用 |
| Computer Use | 结构化工具不足时的 GUI 操作 | `list_apps` 可响应；读取具体 App 状态可能受 macOS 权限影响 |
| Record & Replay | 录制用户真实操作并沉淀成 skill | 适合把人工工作流转成可复用流程 |
| Documents | 生成和验收 DOCX/Google Docs 目标文档 | 适合资料包、服务说明、报告交付 |
| PDF | 读取、生成、渲染和验收 PDF | 适合需要版式确认的 PDF 资产 |
| Spreadsheets | 生成、分析和验收表格 | 适合反馈统计、数据台账、模板资产 |
| Presentations | 生成和验收 PPT/Slides | 适合分享 deck、案例发布材料 |
| Data Visualization | 数据可视化和图表 | 适合把研究或反馈数据变成图表 |
| HyperFrames | 网页视频和视觉叙事 | 适合把案例资产包装成可传播视频/网页表达 |
| last30days | 最近公开讨论和来源研究 | 研究阶段候选能力 |

## 推荐插件安装状态

| 口径 | 当前结果 |
| --- | --- |
| marketplace 插件总数 | 178 |
| installed/enabled | 36 |
| not installed | 142 |
| `~/.codex/config.toml` 启用项 | 40 |
| A 级推荐 marketplace 插件缺失 | 0 |
| primary-runtime 能力 | `documents`、`pdf`、`spreadsheets`、`presentations` |
| 重启后深测线程 | `019ee803-b71e-7b01-a7b6-1608b91e9916` |

深测结论：安装状态已经满足本轮推荐清单；但外部 SaaS / app connector 类插件仍需要 tool 入口、账号授权和真实数据源，不能因为已安装就写成已读取证据。`codex plugin list` 会同时展示已安装和未安装 marketplace 项，判断时只看 `STATUS = installed, enabled`。

## 个人工作流分层

| 层级 | 能力 | 默认动作 |
| --- | --- | --- |
| 基础默认 | SignalProof 本地脚本、Markdown vault、OpenAI Docs、GitHub、Spreadsheets、Data Visualization、Record & Replay | 每个相关 case 都优先考虑，除非没有阶段价值。 |
| 趋势调研 | last30days、GitHub、Hugging Face | 最近 30 天信号、AI 工具、开源项目或模型/数据集 case 默认候选；必须按 `docs/research-quality-gate.md` 判断来源覆盖和证据等级。 |
| 授权调研 | Readwise、Scite、Semrush、Similarweb、Brand24、Zotero、Notion、Google Drive、Airtable、Deepnote、Box | 有账号授权、目标资料库或真实对象时启用。 |
| 验证运行态 | Browser、Chrome、Computer Use、Sentry、PostHog、Mixpanel、Amplitude、Datadog、Codex Security | 有页面、登录态、GUI、产品事件、错误日志或安全扫描目标时启用。 |
| 产物表达 | Documents、PDF、Presentations、HyperFrames、Canva、Figma | 需要正式资料包、报告、演示、视频或视觉素材时启用。 |
| 暂不默认 | 未授权 app connector、无真实数据源的产品分析插件、无目标的部署插件 | 先写入 `tool-ledger.md` 作为候选或阻塞，不进入证据链。 |

## 本地能力快照

`last30days --diagnose` 当前报告这些来源可用：

```text
reddit, tiktok, instagram, x, youtube, hackernews, polymarket, github, perplexity, threads
```

已知状态：

```text
Full Disk Access 已通过 diagnose 复核，不再出现 Safari cookie permission denied。
X / xurl OAuth 已通过 xurl whoami 复核，但 xurl search 返回 CreditsDepleted；当前标记为暂缺但非阻断，只在真实 case 明确依赖 X 实时讨论或早期热度时提醒补 credits。
```

本机默认 `python3` 是 3.9.6，对 `last30days` 太旧；运行时使用 `python3.14`。

## 工具选择规则

不要每个 case 都强行使用所有能力。只有当某个能力能改变决策、减少不确定性或验收产物时，才使用它。

跳过相关能力时，必须在 `tool-ledger.md` 记录原因。

调用相关能力后，必须记录结果质量：强 / 中 / 弱 / 失败 / 阻塞。工具调用本身不等于证据合格。

研究准确性质量门见 [`docs/research-quality-gate.md`](research-quality-gate.md)。更细的阶段接入计划见 [`docs/codex-plugin-flow.md`](codex-plugin-flow.md)，全量插件清单和优先级审计见 [`docs/codex-plugin-audit.md`](codex-plugin-audit.md)，安装显示和迁移规则见 [`docs/codex-plugin-status-and-migration.md`](codex-plugin-status-and-migration.md)。也可以运行：

```bash
python3 scripts/signalproof.py capabilities
python3 scripts/signalproof.py plugin-status
```
