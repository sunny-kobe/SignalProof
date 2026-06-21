---
type: report
status: completed
updated_at: 2026-06-21
gate: passed-with-gaps
---

# 报告：SignalProof 当前工作流自审

## 结论

可以使用已经封装好的 SignalProof 工作流反过来审视当前工作流。

本轮自审结论是 `passed-with-gaps`：当前流程已经能生成 case、调用诊断、记录插件状态、导出报告、发现旧 case warning 和授权缺口。

二次验收结论：原报告的判断基本正确，但当时还停留在“发现缺口”。现在已经把两项最关键改进落到工作流：

- `check-plugin-drift`：检查插件锁定清单、安装脚本、当天状态快照和当前安装列表是否漂移。
- `check-case <case-slug> --strict`：让新 case 的 warning 可以直接失败，避免研究质量门只停留在提醒。

## 关键证据

- `diagnose`、`capabilities`、`plugin-status` 都能运行。
- `check-all` 当前 failures 为 0，但旧 case 仍有研究质量门 warning。
- `check-goal --min-cases 5` 通过。
- 插件状态快照显示已安装启用 marketplace 插件 36 个，未安装 marketplace 项 142 个，primary-runtime 能力可见。
- `last30days --diagnose` 成功，但 X / bird 侧不是完整授权态。

## 关键缺口

- 研究质量门对旧 case 主要是 warning；新 case 已可用 strict 模式收紧。
- 插件锁定清单、安装脚本、状态快照和当前安装列表已新增自动漂移比对。
- app connector 是否可读仍要按具体 case 探针。
- 真实反馈为空，不能写成外部验证。

## 决策

继续使用当前工作流，不扩大成产品，不默认全跑插件。

下一步优先做：

1. 一个真实外部机会 case 的证据链。
2. 一个调研增强 connector 的只读探针。
3. 内部审计类 case 模板优化。

## 边界声明

本报告只证明内部流程自审完成，不证明市场需求、用户采用或产品化可行性。
