---
type: validation
status: planned
updated_at: 2026-06-21
gate: passed
---

# 验证计划

## 验证对象

验证 `last30days` 能否作为 SignalProof 调研阶段的默认候选插件能力。

## 验证方式

1. 用 `python3.14` 实际运行 `last30days`，并保存原始输出。
2. 统计来源覆盖、命中数量、失败来源和降级路径。
3. 判断工具结果是强、中、弱还是失败。
4. 把结论写入 `research.md`、`tool-ledger.md` 和 `flow-review.md`。
5. 运行 `python3 scripts/signalproof.py check-all` 与 `export-all`。

## 执行结果

- 已生成原始证据文件：`evidence/ai-coding-repo-context-loss-raw-plugintrial.md`。
- 覆盖 13 条证据，来源为 GitHub、Reddit、YouTube。
- X、HN、短视频等关键来源缺失或为 0。
- 结论为“调研初筛有用，但证据强度不足以验证市场”。

## 成功标准

- 有真实工具输出，而不是只写“候选”。
- 明确记录来源缺口和失败原因。
- 不把弱证据写成市场验证。

## 本轮 gate

`weak`。可以继续内部验证和更窄 query 补跑，不能进入产品化判断。
