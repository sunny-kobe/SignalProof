# 报告

## 决策先行

- case mode：`{{case_mode}}`
- 当前决策：{{decision_default}}
- 证据边界：{{report_boundary}}

## 摘要

`{{title}}` 已完成当前 case mode 对应的 SignalProof 记录。

lite case 只用于快速判断和资产候选，不代表完整 proof；full case 只有在满足升级硬条件后才进入完整验证、产物、反馈、流程自检和报告。

## 边界

{{report_boundary}}

## 下一步

运行：

```bash
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py export-all
```
