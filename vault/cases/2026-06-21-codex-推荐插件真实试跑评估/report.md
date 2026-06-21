# 报告

## 摘要

本轮按 `docs/codex-plugin-audit.md` 的 A 级推荐清单安装并试跑插件。结果不是“所有插件都应该默认使用”，而是：

- 已安装启用：36 个 marketplace 插件。
- 运行时可用：4 个 primary-runtime 插件。
- 明显提升：GitHub、Record & Replay、Spreadsheets、Presentations。
- 趋势调研默认候选：last30days，有真实讨论增益，但必须带来源质量门。
- 资产化按场景启用：Data Visualization、Documents、PDF、HyperFrames 已有实际产物，但存在浏览器/渲染/视频依赖缺口。
- 条件有用：Hugging Face、Zotero、Sentry/PostHog/Mixpanel/Amplitude/Datadog、Semrush/Similarweb/Brand24/Readwise/Scite 等。
- 暂不默认：Browser；Computer Use 只作为条件候选，因为入口可响应但具体 App 状态读取仍可能受权限影响。
- 重启后新线程探针：A 级推荐 marketplace 插件无缺失，更多插件 Skills 可见，但 app connector 专用工具仍未暴露，账号类插件不能算已实际调用。

## 核心证据

- `evidence/codex-plugin-list-current.txt`：当前插件安装状态。
- `evidence/a-level-plugin-completion-matrix.md`：40 个 A 级能力逐项完成审计。
- `evidence/github-repo-view.json`：GitHub 公开仓库读取成功。
- `evidence/hf-model-openai-gpt-oss-20b.json`：Hugging Face 模型 API 成功。
- `evidence/zotero-status.json`：Zotero 本地 API 未运行。
- `vault/cases/2026-06-21-插件试跑-case-1-ai-coding-repo-context-loss-调研验证/evidence/ai-coding-repo-context-loss-raw-plugintrial.md`：last30days 原始调研输出。
- `vault/assets/plugin-test/workbook/outputs/plugin-eval-workbook.xlsx`：插件评估工作簿。
- `vault/assets/plugin-test/visual/plugin-eval-summary.html`：插件评估 HTML 汇总页。
- `vault/assets/plugin-test/document/outputs/plugin-eval-brief.docx`：DOCX 简报。
- `vault/assets/plugin-test/pdf/outputs/plugin-eval-brief.pdf`：PDF 简报。
- `vault/assets/plugin-test/presentation/outputs/plugin-eval-deck.pptx`：PPTX 演示稿。
- `vault/assets/plugin-test/hyperframes/index.html`：HyperFrames HTML 源文件。
- `evidence/plugin-manifest-capabilities.csv`：40 个推荐插件的 Skill/App/MCP manifest 形态。
- `evidence/plugin-app-only-blockers.md`：app-only 插件阻塞说明。
- `evidence/restart-thread-plugin-deepcheck-receipt.md`：重启后新线程只读深测回执。

## 给后续 SignalProof 的规则

- 调研阶段默认考虑 GitHub、last30days、OpenAI Docs；账号类调研插件只有授权后再用。
- 验证阶段默认优先文件级、自检脚本和 runtime render；Browser 修复前不做硬依赖，Computer Use 读取具体 App 前先做权限/状态探针。
- 产物阶段优先 Spreadsheets 和 Data Visualization；正式报告再引入 Documents/PDF/Presentations，传播素材再引入 HyperFrames。
- 反馈阶段只有真实数据源存在时才启用 PostHog/Mixpanel/Amplitude/Sentry/Datadog。
- 新线程只能证明 Skill 可见性改善，不能替代外部 app 授权或真实数据读取。

## 逐项完成结论

- 40 个 A 级能力均已进入完成矩阵：11 个 `called`，1 个 `failed/tool`，1 个 `failed/local-app`，4 个 `blocked/auth`，15 个 `blocked/auth-or-tool`，8 个 `condition-only`。
- 这不是“40 个都值得默认跑”的结论。真正值得默认进入流程的是少数强增益能力；其余按场景、授权和真实数据源启用。
- 本轮没有把未授权 connector、失败浏览器、失败 GUI 或未部署平台写成成功。

## 边界

本轮证明的是插件对内部工作流的增益，不证明市场需求。真实外部反馈仍为空。
