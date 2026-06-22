---
type: thesis
status: accepted
updated_at: 2026-06-22
gate: passed
---

# 判断

## 当前结论

继续，但只限于内部协议机制优化。V0.2 已把执行范围收缩为 `SignalProof 个人证据协议`，并把 full case 从默认动作降级为有硬条件的升级事件。

## 最小切口

不重写历史 case，不引入新依赖，只修改 docs、skills、templates、资产账本和 `scripts/signalproof.py`，让后续新 case 自动继承 V0.2 规则。

## 不做清单

- 不做真实发布。
- 不做真实用户反馈收集。
- 不做 SaaS。
- 不做 Web dashboard、workflow builder、通用知识库、自动雷达、n8n/Dify、Notion/Obsidian 集成。
- 不把插件安装数量写成工具可用或证据成立。

## 成功标准

- 文档和 skills 明确当前定位是 `SignalProof 个人证据协议`。
- 新模板包含 research / feedback / asset 的结构化 frontmatter。
- `check-all` 输出 failures、warnings 和 Overall status。
- `check-assets` 能暴露 zero-reuse 资产比例。
- 本 internal-audit full case 通过 strict 检查。

## 放弃条件

- 后续无法用 lite case 跑真实外部信号。
- 结构化字段只增加填写成本，没有减少判断成本。
- 用户仍需要靠记忆区分 published、observed feedback 和 validated。
