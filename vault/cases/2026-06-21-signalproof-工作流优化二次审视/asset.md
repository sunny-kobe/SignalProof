---
type: asset
status: reusable-internal
created_at: 2026-06-21
gate: passed
---

# 资产

## 资产名称

SignalProof 工作流优化二次审视 证明案例

## 资产类型

内部流程审计和机制优化案例。

## 可复用内容

- 严格检查未完成占位标记的脚本规则。
- `internal-audit` case 类型。
- 中文 case 记录模板。
- 复核原报告时区分“已落地机制”和“仍是建议”的判断口径。

## 可复用边界

只能证明内部流程能力，不能证明外部需求。

## 使用方式

内部审计或流程优化 case：

```bash
python3 scripts/signalproof.py init-case "<标题>" --case-type internal-audit
python3 scripts/signalproof.py check-case <case-slug> --strict
```

外部机会 case：

```bash
python3 scripts/signalproof.py init-case "<标题>" --case-type external-opportunity
```

外部机会 case 可以在创建初期保留研究缺口，但声称完成前必须清理占位标记，并把缺口改写成真实来源、明确跳过原因或证据等级。
