# AGENTS.md

## 项目形态

- 这是一个面向 Codex 的本地优先 SignalProof 协议 MVP。
- 事实来源是 `vault/` 里的 Markdown，以及 `scripts/` 里的确定性检查。
- 除非用户明确要求，不要把它改成 Web App、SaaS dashboard、workflow builder 或通用知识库。

## 必需 Case 文件

每个 `vault/cases/<case-slug>/` 下的 case 都必须包含：

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

只有当 case 基于明确的假设反馈继续推进时，才使用 `assumed-feedback.md`。

## 验证

声称 case 完成前，先运行：

```bash
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py export-all
```

检查工具可用性时运行：

```bash
python3 scripts/signalproof.py diagnose
python3 scripts/signalproof.py capabilities
python3 scripts/signalproof.py plugin-status
```

运行 `last30days` 时使用较新的 Python：

```bash
python3.14 /Users/rust/.agents/skills/last30days/scripts/last30days.py --diagnose
```

## 边界

- 真实反馈可以为空，但 `feedback.md` 必须明确写出来。
- synthetic demo、假设反馈和内部流程反馈不能写成市场验证。
- 弱证据只能支持低成本内部实验，不能支持产品化或 SaaS 结论。
- 调用了工具不等于证据合格，`tool-ledger.md` 必须判断工具结果是否真的有用。
- Codex 自带插件接入按 `docs/codex-plugin-flow.md` 执行；不要默认全跑插件。
- 插件安装显示、界面不可见原因和可迁移性按 `docs/codex-plugin-status-and-migration.md` 执行；不要把 `not installed` marketplace 项误判成已安装插件缺失。
- 插件锁定清单和换电脑重装脚本按 `docs/codex-plugin-lock.md` 与 `scripts/install-codex-plugins.sh` 执行；后续新增/移除插件或调整阶段流程时，必须同步更新这两个文件、`docs/codex-plugin-status-and-migration.md` 和当天 `plugin-status` 快照。
