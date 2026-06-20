---
type: next_phase_plan
status: planned
updated_at: 2026-06-20
input: assumed-medium-feedback
---

# 下一阶段计划：SignalProof Protocol MVP

## 当前前提

真实反馈为空，但用户允许先采用“中等评价”继续推进。

因此下一阶段不是产品化，也不是商业化，而是把本轮跑出来的流程固化成更可复用的 Codex 工作流协议。

## 下一阶段目标

```text
把 SignalProof 从一次 case run，升级成可重复使用的 Codex Protocol MVP。
```

它应该让下一次机会验证可以更顺滑地完成：

- 自动建 case 目录；
- 自动生成阶段文件；
- 自动记录工具覆盖；
- 自动派发子线程；
- 自动验收子线程文件；
- 自动区分真实反馈和假设反馈；
- 自动生成 completion audit；
- 自动反补 skill 改进建议。

## 保持不做

- 不做 SaaS；
- 不做登录；
- 不做 Web dashboard；
- 不做多用户；
- 不做插件市场；
- 不做自动雷达全家桶；
- 不做 Dify / n8n 替代品；
- 不把中等假设评价包装成市场验证。

## MVP 组成

### 1. Codex Skill

已有：

- `/Users/rust/.codex/skills/personal-opportunity-os/SKILL.md`

下一步增强：

- 增加阶段文件清单；
- 增加 case 初始化规则；
- 增加假设反馈规则；
- 增加 Day 2 执行账本规则；
- 增加子线程文件验收规则。

### 2. 本地 Vault 模板

建议结构：

```text
signalproof-vault/
  cases/
    <date>-<slug>/
      signal.md
      research.md
      debate.md
      thesis.md
      validation.md
      artifact.md
      feedback.md
      assumed-feedback.md
      decision.md
      asset.md
      flow-review.md
      report.md
  assets/
    prompts/
    templates/
    sops/
    repos/
    real-cases/
  subtasks/
    index.md
  reports/
```

### 3. 可选脚本

不先做完整 CLI，只做能减少机械劳动的脚本：

- `init-case`：创建 case 目录和阶段文件；
- `check-case`：检查阶段文件是否存在；
- `audit-feedback`：检查真实反馈、假设反馈和指标是否混淆；
- `audit-subtasks`：检查子线程输出文件是否存在；
- `export-report`：把 case 汇总成报告。

### 4. 示例 Case

第一个示例 case：

```text
AI coding repo context loss
```

示例资产：

- `repo-ai-context-audit` GitHub repo；
- checklist；
- `AGENTS.md` 模板；
- `CLAUDE.md` 模板；
- synthetic before/after；
- Day 2 执行账本；
- 假设反馈记录；
- completion audit。

## 下一阶段成功标准

不是外部市场成功，而是内部协议成功。

成功标准：

- 新建一个 case 不再靠临场发挥；
- 每个阶段文件都有固定模板；
- 工具覆盖和证据强度默认会被记录；
- 子线程输出缺失会被自动发现；
- 真实反馈、假设反馈、synthetic demo 不会混在一起；
- 最终能导出一份可读报告；
- 后续可以打包成 Codex Plugin。

## 下一步实施顺序

1. 回填 `personal-opportunity-os` skill 的假设反馈规则。
2. 建立 `templates/` 参考模板。
3. 增加 case 初始化清单。
4. 写一个最小 `check-case` 脚本。
5. 用当前 case 跑一次自检。已完成，结果：`SignalProof case check: PASSED`。
6. 再选一个新信号跑第二个 case，验证协议是否可复用。已完成：`cases/2026-06-20-codex-subthread-output-missing/`。

## 已完成的第一步协议化

- 已新增 `assumed-feedback.md`，承接中等假设评价。
- 已更新 `decision.md`，状态为 `assumption-based-continuation`。
- 已新增 `scripts/check_case.py` 到 `personal-opportunity-os` skill。
- 已用当前 case 跑通自检，证明当前 case 没有把假设反馈包装成真实验证。
- 已用第二个内部流程 case 跑通自检，证明 SignalProof Protocol 不只适用于外部机会 case，也适用于流程质量改进 case。

## 下一步协议化重点

第二个 case 暴露出的下一步脚本方向：

- `audit_subtasks.py`：读取 `subtasks/index.md`，检查每个输出路径是否存在。
- `init_case.py`：根据 case 类型生成必需文件；外部机会 case 可包含 `assumed-feedback.md`，内部流程 case 默认不需要。
- `export_report.py`：把 case 汇总成最终报告。

## 当前结论

可以继续推进，但推进对象是：

```text
SignalProof Protocol MVP
```

不是：

```text
repo-ai-context-audit 产品化
```
