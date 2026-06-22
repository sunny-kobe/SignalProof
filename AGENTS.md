# AGENTS.md

## 项目形态

- 这是一个面向 Codex 的本地优先 SignalProof 个人证据协议 MVP。
- `Personal Opportunity OS` 只是长期背景叙事，不作为当前执行口号。
- 事实来源是 `vault/` 里的 Markdown，以及 `scripts/` 里的确定性检查。
- 除非用户明确要求，不要把它改成 Web App、SaaS dashboard、workflow builder、通用知识库、自动雷达、n8n/Dify、Notion/Obsidian 集成或插件平台。

## 必需 Case 文件

新外部机会默认从 `case_mode: lite` 开始。完整 proof case 使用 `case_mode: full`，而 full 是有硬条件的升级事件。每个 `vault/cases/<case-slug>/` 下的 full case 都必须包含：

- `signal.md`
- `research.md`
- `debate.md`
- `thesis.md`
- `validation.md`
- `artifact.md`
- `feedback.md`
- `decision.md`
- `asset.md`
- `flow-review.md`
- `tool-ledger.md`
- `process-log.md`
- `report.md`

轻量初筛 case 使用 `case_mode: lite`，只用于快速判断是否升级、收窄、暂停或放弃。lite case 至少包含：

- `signal.md`
- `research.md`
- `debate.md`
- `decision.md`
- `asset.md`

lite case 不代表完整 SignalProof proof，不能写成完整闭环；只有升级为 full case 后才补齐验证、产物、反馈、流程自检、工具账本、过程日志和报告。

外部机会升级为 full 前必须同时满足：

- `evidence_grade` 至少为 `medium`；
- 有明确外部动作：发布、访谈、私信测试、下载页、表单回收或真实目标人反馈；
- 至少有一个可登记资产候选；
- `decision.md` 写明为什么需要 full，而不是为了完整而完整。

`internal-audit` / `plugin-test` / `external-opportunity` 必须在 `signal.md` frontmatter 或正文里清楚区分。

只有当 case 基于明确的假设反馈继续推进时，才使用 `assumed-feedback.md`。

## 验证

创建内部流程审计或工作流优化 case 时，优先使用：

```bash
python3 scripts/signalproof.py init-case "<标题>" --case-type internal-audit
```

声称 case 完成前，先运行：

```bash
python3 scripts/signalproof.py check-case <case-slug> --strict
python3 scripts/signalproof.py check-assets
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py export-all
```

检查工具可用性时运行：

```bash
python3 scripts/signalproof.py diagnose
python3 scripts/signalproof.py capabilities
python3 scripts/signalproof.py plugin-status
python3 scripts/signalproof.py check-plugin-drift
```

运行 `last30days` 时使用较新的 Python：

```bash
python3.14 /Users/rust/.agents/skills/last30days/scripts/last30days.py --diagnose
```

## 边界

- 真实反馈可以为空，但 `feedback.md` 必须明确写出来。
- synthetic demo、假设反馈和内部流程反馈不能写成市场验证。
- 内部工作流优化和插件试跑 case 可以作为个人工作流测试样本保留，但不得混同为外部机会验证。
- 弱证据只能支持低成本内部实验，不能支持产品化或 SaaS 结论。
- 调用了工具不等于证据合格，`tool-ledger.md` 必须判断工具结果是否真的有用。
- 可复用资产必须优先登记到 `vault/assets/registry.md`；没有后续引用的 asset 只能算资产候选。
- 插件治理是候选能力治理；插件安装数量、状态快照或 marketplace 可见性不等于工具可用或证据成立。
- `feedback_status`、`validation_status`、`asset_status`、`reuse_count` 等结构化字段必须维护；新 case strict 下字段缺失会失败。
- 新 case 的 strict 检查会把 `TODO`、`待补`、`待定` 和未替换模板变量视为未完成；历史 case warning 可以保留为后续补齐清单。
- Codex 自带插件接入按 `docs/codex-plugin-flow.md` 执行；不要默认全跑插件。
- 插件安装显示、界面不可见原因和可迁移性按 `docs/codex-plugin-status-and-migration.md` 执行；不要把 `not installed` marketplace 项误判成已安装插件缺失。
- 插件锁定清单和换电脑重装脚本按 `docs/codex-plugin-lock.md` 与 `scripts/install-codex-plugins.sh` 执行；后续新增/移除插件或调整阶段流程时，必须同步更新这两个文件、`docs/codex-plugin-status-and-migration.md` 和当天 `plugin-status` 快照。
- 插件或流程更新后运行 `python3 scripts/signalproof.py check-plugin-drift`，确保锁定清单、安装脚本、当天状态快照和当前安装列表没有漂移。
