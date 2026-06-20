# 报告

## 摘要

`{{title}}` 已跑完 SignalProof 内部协议闭环。

## 边界

真实反馈和发布渠道本轮跳过，因此该 case 只能证明内部协议可运行，不能证明市场需求。

## 下一步

运行：

```bash
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py export-all
```
