---
type: validation
status: planned
updated_at: 2026-07-01
gate: passed
---

# 验证计划

## 验证对象

SignalProof 是否能把 Andrew Ng 的 agentic coding、developer feedback、external feedback 三个 loop 嵌入本地协议，并保持 published != validated 的证据边界。

## Product Spec

- 目标用户：SignalProof 维护者和高频使用 Codex/Claude Code 的个人工作流实践者。
- 目标任务：把高不确定性的个人工作压成证据、Spec、AI 执行、反馈、决策和资产。
- 非目标：不做 Web App、SaaS dashboard、workflow builder、通用知识库或自动雷达。
- 成功标准：新 case 能声明 case_intent 与 loop_profile；validation.md 能承接 Product Spec 和 Eval Set；flow-review.md 能审计 loop 是否转动。

## Eval Set

- 通过样例：`init-case --case-intent workflow-improvement` 生成 signal.md loop frontmatter、validation.md Product Spec/Eval Set、flow-review.md loop review。
- 失败样例：只生成旧线性 case 文件，没有 loop_profile，或把 external_feedback_loop=skipped-with-reason 写成验证成功。
- 回归检查：`check-case --strict`、`check-all`、`check-assets`、`export-all`、`check-plugin-drift`。

## Agentic Build Acceptance

- agentic loop 本轮为 optional，因为产物是协议、模板和脚本，而不是独立产品功能。
- 如果后续 case 选择 `case_intent=product-iteration`，agentic_loop 必须为 required，并要求 Product Spec 与 Eval Set 同时存在。

## 验证方式

1. 复核最近自审 case 和报告。
2. 修改 `scripts/signalproof.py`、模板、协议或 skill。
3. 新建或更新本次内部审计 case。
4. 运行 `python3 scripts/signalproof.py check-plugin-drift`。
5. 运行 `python3 scripts/signalproof.py check-case <case-slug> --strict`。
6. 运行 `python3 scripts/signalproof.py export-all`、`check-all`、`check-goal --min-cases 5` 和 `git diff --check`。

## 跳过项

- 真实外部反馈：本轮跳过。
- 发布渠道：本轮跳过。

## 成功标准

自检通过，并且流程自检能指出至少一个下一轮优化点。
