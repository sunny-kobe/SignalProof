---
type: asset
status: completed
updated_at: 2026-06-21
gate: passed
---

# 资产

## 可复用资产

本 case 沉淀出一套“工作流自审”模式：

```text
把当前流程本身作为 signal
读取规则和能力矩阵
运行诊断和目标检查
记录插件和工具结果质量
区分内部流程证据与外部市场证据
给出 passed-with-gaps 决策
导出报告并复核
```

## 可复用检查清单

- 是否读取了 repo skill 和 AGENTS.md？
- 是否运行了 `diagnose`、`capabilities`、`plugin-status`？
- 是否运行了 `check-plugin-drift`？
- 新 case 是否运行了 `check-case <case-slug> --strict`？
- 是否运行了 `check-all`、`export-all`、`check-goal`？
- 是否记录了工具结果质量，而不是只记录调用？
- 是否把真实反馈为空写清楚？
- 是否区分插件安装、工具暴露、账号授权和证据质量？
- 是否记录下一轮自动化缺口？

## 已沉淀为脚本的资产

- `check-plugin-drift`：比对插件锁定清单、安装脚本、状态快照和当前安装列表。
- `check-case <case-slug> --strict`：对新 case 提高研究质量门，而不是让所有历史 case warning 立刻变成 failure。

## 可沉淀为后续脚本的候选项

- `workflow-audit`：一键生成自审 case 草稿和检查清单。
- 内部审计类模板：避免 `init-case` 默认把内部审计 case 标成外部机会。

## 当前资产边界

这些资产只适用于 SignalProof 内部流程审计，不等于外部机会验证模板。
