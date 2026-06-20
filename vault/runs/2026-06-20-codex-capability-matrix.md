# SignalProof Codex 能力矩阵

生成日期：2026-06-20

## Codex 自带插件可用性

| 插件 | 状态 | 本机路径 |
| --- | --- | --- |
| Browser | available | `/Users/rust/.codex/plugins/cache/openai-bundled/browser/26.616.41845/skills/control-in-app-browser/SKILL.md` |
| Chrome | available | `/Users/rust/.codex/plugins/cache/openai-bundled/chrome/latest/skills/control-chrome/SKILL.md` |
| Computer Use | available | `/Users/rust/.codex/plugins/cache/openai-bundled/computer-use/1.0.829/skills/computer-use/SKILL.md` |
| Record & Replay | available | `/Users/rust/.codex/plugins/cache/openai-bundled/record-and-replay/1.0.829/skills/record-and-replay/SKILL.md` |
| Documents | available | `/Users/rust/.codex/plugins/cache/openai-primary-runtime/documents/26.619.11828/skills/documents/SKILL.md` |
| PDF | available | `/Users/rust/.codex/plugins/cache/openai-primary-runtime/pdf/26.619.11828/skills/pdf/SKILL.md` |
| Spreadsheets | available | `/Users/rust/.codex/plugins/cache/openai-primary-runtime/spreadsheets/26.619.11828/skills/spreadsheets/SKILL.md` |
| Presentations | available | `/Users/rust/.codex/plugins/cache/openai-primary-runtime/presentations/26.619.11828/skills/presentations/SKILL.md` |
| Data Visualization | available | `/Users/rust/.codex/plugins/cache/openai-api-curated/build-web-data-visualization/43313cc9/.codex-plugin/plugin.json` |
| HyperFrames | available | `/Users/rust/.codex/plugins/cache/openai-api-curated/hyperframes/43313cc9/.codex-plugin/plugin.json` |

## 阶段能力计划

| 阶段 | 目标 | 默认能力 | Codex 自带插件候选 | 何时使用 | 写入位置 |
| --- | --- | --- | --- | --- | --- |
| signal | 捕捉信号，建立 case 边界。 | SignalProof skill、Codex 线程工具、本地文件系统。 | Browser 读取公开 URL；Chrome 读取用户已登录页面；Record & Replay 录制用户演示的真实工作流。 | 信号来自网页、已登录产品、用户演示或另一个 Codex 线程。 | signal.md、process-log.md、tool-ledger.md |
| research | 收集证据，区分事实、推断和缺口。 | last30days、Web/Search、GitHub/HN/RSS、官方文档。 | Browser 验证公开页面；Chrome 读取登录态页面；PDF/Documents/Spreadsheets 读取外部资料；Data Visualization 仅在需要看数据结构时使用。 | 信息时效性强、来源需要登录、资料是 PDF/DOCX/表格，或证据需要可视化判断。 | research.md、vault/assets/research/、tool-ledger.md |
| debate | 做正反方和反方审查，暴露风险。 | Codex 子线程、反方 prompt、本地证据包。 | Browser/Chrome 复核关键反证；PDF/Documents 读取长文档反证。 | 关键反对意见依赖外部页面、登录态页面或长文档证据。 | debate.md、subtasks/index.md、tool-ledger.md |
| thesis | 给出继续、收窄、暂停或放弃判断。 | 本地 case 文件、自检脚本、用户判断。 | 通常不需要；只在关键判断缺证据时回到 research/debate 阶段补用。 | 判断依赖未核验证据或需要补查事实。 | thesis.md、decision.md 草稿、flow-review.md |
| validation | 把机会压成可验证实验并验收产物。 | 本地脚本、case 自检、文件级检查。 | Browser 验收 HTML/本地 Web；Computer Use 验收只能 GUI 操作的流程；PDF/Documents/Spreadsheets/Presentations 验收对应文件产物。 | 产物有界面、GUI、文档、表格、演示文稿或 PDF 布局质量要求。 | validation.md、flow-review.md、tool-ledger.md |
| artifact | 生成公开产物或内部可复用产物。 | Codex 文件编辑、Git/GitHub CLI、本地脚本。 | Documents 做 DOCX/文档；PDF 做 PDF；Spreadsheets 做表格；Presentations 做 deck；HyperFrames 做网页视频/视觉叙事；Data Visualization 做数据图表。 | 产物格式不是纯 Markdown，或需要可视化、排版、演示、表格、视频化表达。 | artifact.md、asset.md、vault/assets/ |
| publication | 发布触达，但不伪造真实反馈。 | GitHub CLI、发布台账、本地文案。 | Browser 验证公开发布页；Chrome 在用户明确授权时使用登录态发布/查看数据。 | 需要确认公开 URL、截图、登录态后台或用户授权的渠道操作。 | feedback.md、day2-execution.md、tool-ledger.md |
| feedback | 回收真实反馈和指标，区分 published 与 validated。 | GitHub CLI、last30days、人工反馈输入。 | Chrome 查看登录态评论/私信/后台；Browser 验证公开评论；Spreadsheets 统计反馈；Record & Replay 沉淀用户示范流程。 | 反馈来自登录态渠道、公开页面、表格数据，或用户用操作演示真实任务。 | feedback.md、vault/assets/feedback/、tool-ledger.md |
| decision | 做继续、收窄、暂停、放弃或资产化决策。 | 本地 case 文件、check-all、check-goal。 | 通常不需要；缺少证据时回退到 research/feedback 补用插件。 | 决策依赖未核验反馈、指标或产物验收。 | decision.md、flow-review.md |
| asset | 把有效产物沉淀成可复用资产。 | Markdown 模板、脚本、GitHub repo、Codex skill/plugin。 | Documents/PDF/Spreadsheets/Presentations 做资料包；Record & Replay 把用户流程变成 Skill；Browser 验收发布后的资产页。 | 资产需要变成文档、PDF、表格、PPT、可录制流程或公开页面。 | asset.md、vault/assets/、plugins/、.agents/skills/ |
| flow-review | 审计阶段完整性、工具覆盖和下一轮优化。 | check-all、check-goal、capabilities、export-all。 | Browser 预览报告索引；Computer Use 复核 GUI-only 验收；PDF/Documents/Spreadsheets/Presentations 复核格式产物。 | 需要证明报告可读、界面可用、文件格式正确或 GUI 流程真实可跑。 | flow-review.md、tool-ledger.md、vault/runs/ |
