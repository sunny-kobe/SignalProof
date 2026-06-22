---
type: debate
status: completed
updated_at: 2026-06-22
gate: passed
---

# 辩论

## 强反方

- V0.2 可能仍然太重：full case 保留 13 个文件，历史 warning 也明显增加。
- 结构化 frontmatter 只是更硬的表格；如果后续不跑真实 lite 外部信号，仍然无法证明它降低判断成本。
- 插件治理即使降级为候选能力，也可能继续占用注意力；下一步必须减少插件叙事，把重点放回证据和复用。

## 替代方案

- 更激进地删除 `thesis.md`、`report.md` 和 lite 的 `debate.md`，把 case 压到 4 个文件。
- 引入 SQLite 或一个小型 UI，直接把结构化字段放进数据模型。
- 暂停协议改造，先跑 5 个外部信号，再倒推模板。

## Kill 条件

- 后续 5 个 lite 外部信号实验如果仍然需要大量手写重复内容，说明模板没有真正收缩。
- 如果 `check-all` 的 warning 太多导致用户忽略输出，需要把历史 warning 分层或增加新旧 case 过滤。
- 如果 `check-assets` 只暴露 zero reuse 但不驱动后续复用，资产账本仍会退化成目录。
