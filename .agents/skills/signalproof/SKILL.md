---
name: signalproof
description: 用于本仓库的 SignalProof case：创建、推进、审计和导出从信号到资产的证明案例，并维护工具账本、过程日志和流程自检。触发词包括 SignalProof、证明案例、信号到资产、流程审计、工具覆盖、Codex 工作流验证。
---

# SignalProof Repo Skill

默认语言：中文。

把这个仓库作为 SignalProof 协议 MVP 的事实来源。

## 工作流

每个 case 都维护这些文件：

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

只有当 case 明确基于假设反馈继续时，才使用 `assumed-feedback.md`。

## 命令

```bash
python3 scripts/signalproof.py diagnose
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py export-all
```

## 规则

- 真实反馈为空时，不要声称市场验证。
- 阶段完成前，先记录候选 skill、plugin 和工具。
- 判断工具结果质量，而不是只记录工具是否调用过。
- 产物本地优先，并且保持中文可读。
- Browser、Chrome、Computer Use、Record & Replay、Documents、PDF、Spreadsheets、Presentations 是候选能力，不是默认依赖。
- 每个 case 开始前可运行 `python3 scripts/signalproof.py capabilities`，查看阶段到 Codex 自带插件的能力矩阵。
- 只有当插件能改变判断、减少不确定性或验收产物时才调用；跳过或失败都要写入 `tool-ledger.md`。
