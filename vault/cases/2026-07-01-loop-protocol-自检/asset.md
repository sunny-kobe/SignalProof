---
type: asset
status: reusable-internal
created_at: 2026-07-01
gate: passed
asset_status: candidate
registry_required: true
reuse_count: 0
proof_of_reuse: none
---

# 资产

## 资产名称

Loop Protocol 自检 证明案例

## 资产类型

内部流程审计和机制优化案例。

## 可复用内容

- 严格检查未完成占位标记的脚本规则。
- `internal-audit` case 类型。
- 中文 case 记录模板。
- 复核原报告时区分“已落地机制”和“仍是建议”的判断口径。

## 可复用边界

只能证明内部流程能力，不能证明外部需求。

## Registry 更新

如果本资产真的值得复用，必须同步登记到 `vault/assets/registry.md`，并在下一次使用时补 `reuse_count`、`proof_of_reuse` 和 `last_used_by`。没有登记或没有后续引用时，只能算资产候选。
