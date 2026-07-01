---
name: signalproof
description: 用于本仓库的 SignalProof case：创建、推进、审计和导出从信号到资产的证明案例，并维护工具账本、过程日志和流程自检。触发词包括 SignalProof、证明案例、信号到资产、流程审计、工具覆盖、Codex 工作流验证。
---

# SignalProof Repo Skill

默认语言：中文。

把这个仓库作为 `SignalProof 个人证据协议` 的事实来源。`Personal Opportunity OS` 只是长期背景，不作为当前执行范围。

SignalProof 现在也是一个克制版 `AI Native Work Loop Protocol`：把高不确定性的个人工作压成证据、Spec、AI 执行、反馈、决策和资产。这个扩展只服务本地协议和 Codex 工作流，不允许扩成通用 workflow builder。

当前不做 Web App、SaaS dashboard、workflow builder、通用知识库、自动雷达、n8n/Dify、Notion/Obsidian 集成。保持本地 Markdown vault + Python 标准库脚本路线。

## 工作流

新外部机会默认使用 `case_mode: lite`。完整 proof case 使用 `case_mode: full`，而 full 是有硬条件的升级事件，维护这些文件：

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

轻量初筛 case 使用 `case_mode: lite`，只用于快速判断是否升级、收窄、暂停或放弃，至少维护：

- `signal.md`
- `research.md`
- `debate.md`
- `decision.md`
- `asset.md`

lite case 不代表完整 SignalProof proof，不能写成完整闭环。lite 资产被发布后，先在发布资产、发布台账、`asset.md` 或 `decision.md` 记录 URL 与状态；不要因为有发布 URL 就强行补 `feedback.md` 或升级 full。

外部机会升级为 full 前必须同时满足：

- `evidence_grade` 至少为 `medium`；
- 有明确外部动作：发布、访谈、私信测试、下载页、表单回收或真实目标人反馈；
- 至少有一个可登记资产候选；
- `decision.md` 写明为什么需要 full。

`internal-audit` / `plugin-test` / `external-opportunity` 必须在 `signal.md` frontmatter 或正文里清楚区分。

`case_type` 表示证据边界；`case_intent` 表示工作意图。允许的 `case_intent` 是：

- `external-opportunity`
- `product-iteration`
- `content-iteration`
- `workflow-improvement`
- `tool-evaluation`
- `learning-to-asset`

新 case 的 `signal.md` 必须维护 `loop_profile: ai-work-loop-v1` 和四个 loop 字段：`agentic_loop`、`developer_feedback_loop`、`external_feedback_loop`、`asset_loop`。当 `agentic_loop=required` 时，`validation.md` 必须包含 `Product Spec` 和 `Eval Set`。

只有当 case 明确基于假设反馈继续时，才使用 `assumed-feedback.md`。

## 命令

```bash
python3 scripts/signalproof.py init-case "<标题>" --case-type internal-audit
python3 scripts/signalproof.py init-case "<标题>" --case-type internal-audit --case-intent workflow-improvement
python3 scripts/signalproof.py init-case "<标题>" --case-mode lite
python3 scripts/signalproof.py diagnose
python3 scripts/signalproof.py capabilities
python3 scripts/signalproof.py plugin-status
python3 scripts/signalproof.py check-plugin-drift
python3 scripts/signalproof.py check-case <case-slug> --strict
python3 scripts/signalproof.py check-assets
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py export-all
```

## 规则

- 真实反馈为空时，不要声称市场验证。
- 阶段完成前，先记录候选 skill、plugin 和工具，但插件治理只作为候选能力治理。
- 判断工具结果质量，而不是只记录工具是否调用过。
- 产物本地优先，并且保持中文可读。
- Browser、Chrome、Computer Use、Record & Replay、Documents、PDF、Spreadsheets、Presentations 是候选能力，不是默认依赖。
- 每个 case 开始前可运行 `python3 scripts/signalproof.py capabilities`，查看阶段到 Codex 自带插件的能力矩阵。
- 需要判断插件是否真的安装、为什么 UI 里看不到、迁移时要带什么时，运行 `python3 scripts/signalproof.py plugin-status`，并参考 `docs/codex-plugin-status-and-migration.md`。
- 插件或流程更新后运行 `python3 scripts/signalproof.py check-plugin-drift`，比对锁定清单、安装脚本、当天状态快照和当前安装列表。
- 插件或阶段流程更新时，同步更新 `docs/codex-plugin-lock.md`、`scripts/install-codex-plugins.sh` 和 `docs/codex-plugin-status-and-migration.md`。
- 插件安装数量、状态快照或 marketplace 可见性不等于 connector 可用、账号已授权或证据成立。
- 内部流程审计、工作流优化和二次审视类 case 使用 `--case-type internal-audit`，避免套用外部机会验证口径。
- 内部工作流优化和插件试跑 case 是个人工作流测试样本，可以保留，但不能混同为外部机会验证。
- 真正可复用资产登记到 `vault/assets/registry.md`，并维护 `reuse_count`、`proof_of_reuse`、`last_used_by`；没有登记或没有后续引用时只算资产候选。
- full case 的 `research.md`、`feedback.md`、`asset.md` 结构化 frontmatter 字段必须维护；lite case 默认没有 `feedback.md`，但已有文件必须保持结构化字段。新 case strict 下字段缺失会失败。
- 新 case 完成前用 `check-case <case-slug> --strict`，未完成占位如 `TODO`、`待补`、`待定` 和未替换模板变量都不能保留。
- 只有当插件能改变判断、减少不确定性或验收产物时才调用；跳过或失败都要写入 `tool-ledger.md`。
