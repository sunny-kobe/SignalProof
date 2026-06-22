---
type: asset
status: reusable-internal
created_at: {{created_at}}
gate: passed
asset_status: candidate
registry_required: true
reuse_count: 0
proof_of_reuse: none
---

# 资产

## 资产名称

{{title}} 证明案例

## 资产类型

{{asset_type}}

## 可复用内容

{{asset_reusable_content}}

## 可复用边界

只能证明内部流程能力，不能证明外部需求。

## Registry 更新

如果本资产真的值得复用，必须同步登记到 `vault/assets/registry.md`，并在下一次使用时补 `reuse_count`、`proof_of_reuse` 和 `last_used_by`。没有登记或没有后续引用时，只能算资产候选。
