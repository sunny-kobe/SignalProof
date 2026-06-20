---
type: decision
status: accepted
decision: 沉淀为 SignalProof 子线程文件验收门
decided_at: 2026-06-20
gate: passed
---

# 决策

## 最终决策

```text
继续，沉淀为 SignalProof Protocol 的强制质量门
```

## 理由

- 失败真实发生；
- 对跨线程协作可靠性影响大；
- 修复成本低；
- 已经产生可复用规则；
- 可继续脚本化。

## 不做什么

- 不做线程管理产品；
- 不做 UI；
- 不做商业化。

## 下一步

1. 保留 skill 中的子线程文件验收规则。
2. 把本 case 作为第二个 SignalProof 示例 case。
3. 后续新增 `audit_subtasks.py`。
