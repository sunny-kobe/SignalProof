---
type: flow_review
status: completed
updated_at: 2026-06-21
case_stage: full-internal-loop
gate: passed
---

# 流程自检

## 阶段完整性

| 阶段 | 状态 | 说明 |
| --- | --- | --- |
| signal | passed | 已把用户的“插件没有真实用起来”记录为流程改进信号。 |
| research | weak-to-medium | 插件安装、官方口径和公开只读试跑证据充分；真实账号类数据不足。 |
| debate | passed | 已明确反方：插件过多可能制造流程噪音。 |
| thesis | passed | 已收窄为“默认/条件/暂不用”三层策略。 |
| validation | passed | 已跑安装、调研、验证、产物、反馈五组测试。 |
| artifact | passed | 已生成工作簿、HTML、DOCX、PDF、PPTX、HyperFrames HTML 和原始证据目录。 |
| feedback | weak | 真实外部反馈仍为空；产品分析类插件无数据源。 |
| decision | passed | 未把安装成功写成插件有效。 |
| asset | passed | 插件评估矩阵可作为后续 case 的工具选择依据。 |

## 工具覆盖质量

- 强：GitHub、Record & Replay、Spreadsheets、Presentations。
- 中：Hugging Face 公开 API、last30days、Data Visualization、Documents、PDF、HyperFrames、OpenAI 官方手册、plugin manifest 分类。
- 中：重启后新线程探针确认 A 级推荐插件无缺失，安装后更多 Skills 可见，但 app connector 工具未自动暴露。
- 弱：Browser/GUI/视频导出和部分文件渲染依赖缺失，导致部分产物只能算文件级通过。
- 失败：Browser setup 报 `codex/sandbox-state-meta: missing field sandboxPolicy`。
- 条件可用：Computer Use 的 `list_apps` 可响应，但读取具体 App 状态曾在 Codex App 上报 `-1743`，使用前要先做目标 App 探针。
- 阻塞：Readwise、Scite、Semrush、Similarweb、Brand24、PostHog、Mixpanel、Amplitude、Datadog、Dovetail、Mem 等 app 类插件当前缺少授权或工具入口。

## 完成目标审计

本轮对 `docs/codex-plugin-audit.md` 中去重后的 40 个 A 级能力补了逐项矩阵：`evidence/a-level-plugin-completion-matrix.md`。

| 目标要求 | 当前证据 | 审计结论 |
| --- | --- | --- |
| 推荐插件全部下载/安装 | `codex plugin list`、`evidence/codex-plugin-list-current.txt` | marketplace A 级插件 36 个均已 installed/enabled；4 个 runtime 能力可用。 |
| 实际跑 case | 主 case + 3 个补跑 case | 已覆盖安装/官方口径、公开调研、验证 gate、产物资产化、反馈阻塞。 |
| 全部应用一次 | `evidence/a-level-plugin-completion-matrix.md`、`evidence/restart-thread-plugin-deepcheck-receipt.md` | 能安全调用或无副作用探针的能力已调用；不能调用的逐项标 `blocked` / `failed` / `condition-only`，未伪造成成功。 |
| 判断哪些带来提升 | `report.md`、`decision.md` | GitHub、Record & Replay、Spreadsheets、Presentations 为强增益；last30days 为调研默认候选但证据门要保留。 |
| 不行就不要用 | `decision.md`、本文件 | Browser 暂不默认；Computer Use 只在目标 App 权限确认后使用；app connector 类插件仅授权/有真实数据后启用。 |

审计后的 gate：`passed-with-blockers`。这表示本轮目标在当前机器、当前线程、当前授权状态下已跑完；外部账号类插件的真实数据读取仍需要单独授权 case，不能算本轮已验证有效。

## 这次暴露出的流程问题

- `docs/codex-plugin-audit.md` 的状态总览已修正为安装启用 36，但后续仍应自动刷新，避免再次过期。
- A 级推荐插件不能只写“推荐”，必须在每个 case 的 `tool-ledger.md` 里记录是否实际调用。
- Browser/Computer Use 这类验证插件如果失败或受权限限制，流程不能卡死；应允许用文件级检查、截图、runtime render 或人工复核降级。
- 新线程能提升 Skill 可见性，但不能解决 app connector 授权和工具暴露问题；这两层必须拆开。
- 产物类插件容易把流程做重；应把 Spreadsheets/Data Visualization 设为常用资产化能力，Documents/PDF/Presentations/HyperFrames 按交付场景启用。

## 下一轮优化

- 建一个“插件状态刷新”脚本：自动输出 installed/enabled、runtime、manifest capabilities 和当前线程可调用工具。
- 每个真实 case 开始时，先生成阶段插件候选清单，再选择最小必要插件。
- 对账号类插件单独做授权 case，不和普通研究 case 混在一起。
