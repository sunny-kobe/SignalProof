# 报告

## 决策先行

- case mode：`full`
- 当前决策：接受 V0.2 收缩改造；新外部机会默认 lite，full 只作为满足硬条件后的升级事件。
- 证据边界：本报告只证明内部工作流机制完成一次优化，不证明外部用户需求、市场采用或产品化可行性。

## 摘要

`SignalProof V0.2 两天收缩改造` 已完成当前 case mode 对应的 SignalProof 记录，并把规则落到文档、模板、资产账本和脚本 gate。

lite case 只用于快速判断和资产候选，不代表完整 proof；full case 只有在满足升级硬条件后才进入完整验证、产物、反馈、流程自检和报告。

## 边界

本报告只证明内部工作流机制完成一次优化，不证明外部用户需求、市场采用或产品化可行性。

## 下一步

运行：

```bash
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py check-assets
python3 scripts/signalproof.py export-all
```
