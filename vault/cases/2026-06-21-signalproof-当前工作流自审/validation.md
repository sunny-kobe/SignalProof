---
type: validation
status: completed
updated_at: 2026-06-21
gate: passed
---

# 验证计划

## 验证目标

验证当前 SignalProof 工作流是否能用自己的规则完成一次工作流自审。

通过标准：

- 生成一个完整 case。
- 13 个必需文件都存在且不是占位。
- `tool-ledger.md` 记录候选能力、实际使用、结果质量和跳过原因。
- `research.md` 覆盖来源覆盖、交叉验证、反证、证据等级、结论许可和用户授权缺口。
- `feedback.md` 明确真实反馈为空。
- `check-all`、`export-all` 和 `check-goal` 最终通过。

## 已执行验证

| 验证项 | 命令或动作 | 结果 | 判断 |
| --- | --- | --- | --- |
| 仓库规则读取 | 读取 `AGENTS.md`、repo skill、工作偏好 skill | 已完成 | passed |
| 能力诊断 | `python3 scripts/signalproof.py diagnose` | 成功，生成本机能力信息 | passed |
| 插件能力矩阵 | `python3 scripts/signalproof.py capabilities` | 成功，生成阶段能力计划 | passed |
| 插件状态快照 | `python3 scripts/signalproof.py plugin-status` | 成功，记录 36 个已安装启用 marketplace 插件 | passed |
| 研究能力诊断 | `python3.14 /Users/rust/.agents/skills/last30days/scripts/last30days.py --diagnose` | 成功，但 X / bird 侧不是完整授权态 | passed-with-gap |
| 全量 case 检查 | `python3 scripts/signalproof.py check-all` | 旧 case failures 为 0，但有研究质量门 warning | passed-with-warning |
| 插件漂移检查 | `python3 scripts/signalproof.py check-plugin-drift` | 锁定清单 36、安装脚本 36、状态快照脚本 36、状态快照已安装 36、当前安装 36，全量一致 | passed |
| 新 case 严格检查 | `python3 scripts/signalproof.py check-case 2026-06-21-signalproof-当前工作流自审 --strict` | 自审 case 通过，warning 未触发失败 | passed |
| 目标检查 | `python3 scripts/signalproof.py check-goal --min-cases 5` | 通过 | passed |

## 验证发现

- 结构层已经可验证。
- 插件安装层已经可验证。
- 插件迁移说明已经可验证。
- 研究质量层对新 case 已可用 strict 模式收紧；旧 case warning 说明历史口径需要后续处理。
- connector 授权和真实数据读取仍必须按具体 case 探针。

## 本轮不验证

- 不验证外部市场需求。
- 不验证所有网页登录网站。
- 不验证所有 app connector。
- 不做 Browser、Chrome、Computer Use 或 Record & Replay 的全量试跑，因为本 case 没有 UI 或用户演示验收目标。

## 验证结论

当前工作流可以完成自审，结论为 `passed-with-gaps`。
