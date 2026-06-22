---
type: asset
status: reusable-internal
created_at: 2026-06-22
gate: passed
asset_status: registered
registry_required: true
reuse_count: 0
proof_of_reuse: none
---

# 资产

## 资产名称

signalproof-v0-2-protocol-gates

## 资产类型

protocol / template / script-gate

## 可复用内容

- `check-all` 顶层 failures / warnings / Overall status 输出。
- `check-case` 结构化 frontmatter 检查。
- `check-assets` 资产复用统计。
- lite 默认、full 硬条件升级、插件候选能力边界和资产复用账本规则。

## 可复用边界

只能证明内部流程能力，不能证明外部需求。

## Registry 更新

已登记到 `vault/assets/registry.md`，但 `reuse_count=0`，所以当前仍只是资产候选。只有后续 5 个 lite 外部信号实验实际复用后，才能回填 `proof_of_reuse`。
