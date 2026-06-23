---
name: signalproof
description: 运行 SignalProof 信号到资产证明案例，维护工具账本、过程日志、流程自检，并导出报告。用于个人机会工作流验证和 Codex 协议审计。
---

# SignalProof Plugin Skill

SignalProof 是一套 Codex 优先的个人证据协议。`Personal Opportunity OS` 只是长期背景，不扩展当前仓库范围。

当前不做 Web App、SaaS dashboard、workflow builder、通用知识库、自动雷达、n8n/Dify、Notion/Obsidian 集成。保持本地 Markdown vault + Python 标准库脚本路线。

调用时，先判断 case mode：

- `lite`：新外部机会默认模式，用于外部信号初筛、快速反方判断和资产候选，只要求 `signal.md`、`research.md`、`debate.md`、`decision.md`、`asset.md`。
- `full`：有硬条件的升级事件，才要求覆盖所有阶段文件。

full case 覆盖：

- 信号捕捉；
- 研究；
- 反方审查；
- 判断；
- 验证计划；
- 产物；
- 反馈边界；
- 决策；
- 资产；
- 流程自检；
- 工具账本；
- 过程日志。

lite case 不代表完整闭环，不能写成市场验证或完整 proof。lite 资产被发布后，先在发布资产、发布台账、`asset.md` 或 `decision.md` 记录 URL 与状态；不要因为有发布 URL 就强行补 `feedback.md` 或升级 full。

外部机会升级为 full 前必须同时满足：`evidence_grade >= medium`、存在明确外部动作、至少有一个可登记资产候选，并且 `decision.md` 写明为什么需要 full。

内部工作流优化和插件试跑 case 是个人工作流测试样本，可以保留，但不能混同为外部机会验证。

真正可复用资产必须登记到 `vault/assets/registry.md`，并在后续 case 使用时更新 `reuse_count`、`proof_of_reuse` 和 `last_used_by`。

除非存在真实用户反馈，否则不要声称市场验证。

full case 的真实反馈可以为空，但 `feedback.md` 必须明确写出来。lite case 默认没有 `feedback.md`，发布后先维护发布资产和资产账本；只有满足 full 升级硬条件时才补齐 `feedback.md`。

每个阶段开始前，先用能力矩阵判断是否需要 Codex 自带插件：

```bash
python3 scripts/signalproof.py init-case "<标题>" --case-mode lite
python3 scripts/signalproof.py capabilities
python3 scripts/signalproof.py plugin-status
```

- Browser / Chrome：网页、登录态页面、发布页和报告预览；
- Computer Use：只能通过 GUI 操作或验收的流程；
- Record & Replay：用户演示的真实流程，需要沉淀成 Skill；
- Documents / PDF / Spreadsheets / Presentations：对应格式的资料包、报告、表格和演示文稿；
- Data Visualization / HyperFrames：研究数据可视化或传播型网页/视频表达。

不要默认全跑插件。插件治理只作为候选能力治理；只有它能改变判断、减少不确定性或验收产物时才调用，并把候选、使用、结果质量、是否改变判断、跳过原因写入 `tool-ledger.md`。

插件安装状态、界面不可见原因和可迁移性见 `docs/codex-plugin-status-and-migration.md`。插件锁定清单和换电脑重装脚本见 `docs/codex-plugin-lock.md` 和 `scripts/install-codex-plugins.sh`。不要把 `codex plugin list` 里的 `not installed` marketplace 项误读成当前流程缺插件。

插件安装数量、状态快照或 marketplace 可见性不等于 connector 可用、账号已授权或证据成立。

后续插件或阶段流程更新时，同步更新插件锁定清单、重装脚本和插件状态快照。
