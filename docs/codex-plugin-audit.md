# Codex 插件全量审计

生成日期：2026-06-20

## 说明

这份文档按当前本机 Codex 插件市场和本机缓存重新整理插件清单。官方口径里，插件可以把技能、应用集成和 MCP 服务器打包成可复用工作流；安装插件只代表能力进入 Codex，外部账号、授权、MCP 设置和真实调用仍要单独验证。

本文件只记录“可见、已安装、可候选”的状态，不把它写成“已经用过”。每次真实调用仍要进入具体 SignalProof case 的 `tool-ledger.md`，记录候选、是否调用、失败原因、结果质量和下一步。

本轮数据来源：

- `codex plugin marketplace list`：确认插件市场来源。
- `codex plugin list`：确认插件市场插件安装状态。
- `/Users/rust/.codex/plugins/cache`：确认本机已缓存或运行时插件。
- 当前 Codex 会话暴露的 Skill/MCP 工具：确认哪些能力现在可被会话直接看到。

## 状态分层

| 层级 | 当前结果 | 判断 |
| --- | --- | --- |
| 插件市场可见 | 178 个 | 可以安装或评估，但多数还没有安装。 |
| 插件市场已安装启用 | 4 个 | `browser`、`chrome`、`computer-use`、`record-and-replay`。 |
| 本机运行时/缓存可见 | 11 个 | 含 Documents、PDF、Spreadsheets、Presentations、Data Visualization、HyperFrames、Superpowers 等。 |
| 当前已经记录过真实调用 | 2 类 | Browser 曾按真实流程调用但失败；Computer Use 已成功读取本机应用状态。 |
| 当前尚未真实调用的重点调研插件 | 多数 | Readwise、Zotero、Scite、Semrush、Similarweb、Brand24、Dovetail、PostHog、Mixpanel、Amplitude 等需要逐个实测。 |

## 数量总览

| 口径 | 数量 |
| --- | ---: |
| openai-bundled 插件市场 | 5 |
| openai-curated 插件市场 | 173 |
| 插件市场合计 | 178 |
| 已安装启用 | 4 |
| 未安装 | 174 |

| 等级 | 数量 |
| --- | ---: |
| A 重点候选 | 36 |
| B 可试点 | 69 |
| C 场景候选 | 31 |
| D 暂不适合 | 42 |

| 类别 | 数量 |
| --- | ---: |
| 其他 | 2 |
| 出行 | 2 |
| 创意内容 | 9 |
| 商业与运营 | 15 |
| 安全 | 1 |
| 工程 | 1 |
| 开发工具 | 41 |
| 教育与研究 | 11 |
| 数据与分析 | 12 |
| 沟通协作 | 12 |
| 生产力 | 46 |
| 金融 | 26 |

## 当前已安装启用的插件市场插件

| 插件 | 来源 | 主要阶段 | 当前调用状态 | 当前判断 |
| --- | --- | --- | --- | --- |
| `browser` | openai-bundled | 验证、发布、流程自检 | 已实测失败 | 控制 Codex 内置浏览器，适合验收报告页、公开页面和发布入口；本轮失败要作为能力缺口记录。 |
| `chrome` | openai-bundled | 调研、发布、反馈 | 未直接调用 | 使用本机 Chrome 登录态，适合读取授权页面、后台和真实反馈渠道。 |
| `computer-use` | openai-bundled | 验证、流程自检 | 已实测成功 | 控制本机图形界面，适合验证非网页流程和桌面应用状态。 |
| `record-and-replay` | openai-bundled | 流程录制、资产化 | 未实测 | 录制用户操作并沉淀成可复用技能，适合把稳定流程资产化。 |

## 本机运行时和缓存插件

| 插件 | 来源 | 当前状态 | 等级 | 主要阶段 | 中文判断 |
| --- | --- | --- | --- | --- | --- |
| `documents` | openai-primary-runtime | 本机运行时已缓存，当前会话有文档技能 | A 重点候选 | 产物、资产化、流程自检 | 创建、编辑和渲染 Word/Google Docs 类文档，适合把案例沉淀成正式资料。 |
| `pdf` | openai-primary-runtime | 本机运行时已缓存，当前会话未见独立技能入口 | A 重点候选 | 调研、产物、流程自检 | 读取、生成和渲染 PDF，适合研究材料处理和报告验收。 |
| `spreadsheets` | openai-primary-runtime | 本机运行时已缓存，当前会话有表格技能 | A 重点候选 | 调研、反馈、资产化 | 创建和分析表格，适合反馈台账、数据清洗和轻量统计。 |
| `presentations` | openai-primary-runtime | 本机运行时已缓存，当前会话有演示技能 | A 重点候选 | 产物、发布、资产化 | 创建和验收 PPT/Slides，适合把研究结论做成分享材料。 |
| `build-web-data-visualization` | openai-api-curated | 本机缓存存在，但插件市场当前显示未安装 | A 重点候选 | 调研、产物、资产化 | 把研究数据做成交互图表、报告页或可视化资产。 |
| `hyperframes` | openai-api-curated | 本机缓存存在，但插件市场当前显示未安装 | A 重点候选 | 产物、发布 | 把 HTML/网页内容视频化，适合把研究结论做成传播素材。 |
| `superpowers` | superpowers-dev | 本机缓存存在，但插件市场当前显示未安装 | A 重点候选 | 开发流程、复盘资产 | 规划、TDD、调试和交付流程，适合把开发流程固化。 |

## SignalProof 阶段映射

| 阶段 | 优先插件 | 使用边界 |
| --- | --- | --- |
| 信号 | `browser`、`chrome`、`record-and-replay`、`github` | 信号来自网页、登录态页面、用户演示或开源仓库时使用。 |
| 调研 | `readwise`、`zotero`、`scite`、`semrush`、`similarweb`、`brand24`、`github`、`hugging-face`、`google-drive`、`notion` | 只在能补足真实讨论、论文、竞品、流量或历史资料时使用。 |
| 辩论 | `scite`、`browser`、`chrome`、`github`、`documents`、`pdf` | 用来找反证、替代方案和关键风险，不替代判断。 |
| 验证 | `browser`、`chrome`、`computer-use`、`posthog`、`mixpanel`、`amplitude`、`sentry`、`datadog`、`codex-security`、`linear` | 验证页面、运行状态、行为数据、错误、任务闭环和代码安全。 |
| 产物 | `documents`、`pdf`、`spreadsheets`、`presentations`、`build-web-data-visualization`、`hyperframes`、`canva`、`figma` | 只有产物不只是 Markdown，或需要视觉、文档、表格、PPT、视频时使用。 |
| 发布 | `browser`、`chrome`、`github`、`vercel`、`netlify`、`cloudflare`、`gmail`、`slack` | 确认公开入口、登录态后台、发布渠道和授权触达。 |
| 反馈 | `brand24`、`dovetail`、`posthog`、`mixpanel`、`amplitude`、`gmail`、`slack`、`github`、`jam`、`spreadsheets` | 回收真实讨论、用户原话、行为指标、issue、邮件和社群反馈。 |
| 决策 | 通常不直接用插件 | 如果决策缺证据，回退到调研、验证或反馈阶段补跑。 |
| 资产 | `record-and-replay`、`documents`、`pdf`、`spreadsheets`、`presentations`、`notion`、`mem`、`google-drive`、`airtable` | 把有效流程、报告、表格、演示和知识库沉淀为可复用资产。 |
| 流程自检 | `browser`、`computer-use`、`documents`、`pdf`、`spreadsheets`、`presentations`、`record-and-replay` | 验证文件、页面、应用和流程真实可跑。 |

## 第一批真实调用验证路线

| 批次 | 插件 | 目标 | 通过标准 |
| --- | --- | --- | --- |
| 1 调研证据 | `readwise`、`zotero`、`scite`、`semrush`、`similarweb`、`brand24` | 补足外部资料、论文、站点流量和真实讨论 | 能输出原始来源、覆盖范围、强/中/弱/失败评级。 |
| 2 反馈和行为 | `dovetail`、`posthog`、`mixpanel`、`amplitude`、`gmail`、`slack` | 回收用户原话、行为数据和授权反馈 | 能进入 `feedback.md`，且不把假设写成真实反馈。 |
| 3 验证工具 | `browser`、`chrome`、`computer-use`、`github`、`linear`、`sentry`、`datadog`、`codex-security` | 验收页面、代码、运行态和任务闭环 | 有截图、错误、issue、日志或扫描结果等可复核证据。 |
| 4 产物插件 | `documents`、`pdf`、`spreadsheets`、`presentations`、`build-web-data-visualization`、`hyperframes`、`figma`、`canva` | 生成非 Markdown 资产 | 能渲染或打开验收，文件进入 `vault/assets/`。 |
| 5 流程复利 | `record-and-replay`、`superpowers` | 把稳定操作沉淀成技能、检查清单或工程流程 | 能复用到下一个 case，并在 `flow-review.md` 记录效果。 |

## 当前最该优先验证的插件

| 插件 | slug | 阶段 | 第一种真实调用验证 |
| --- | --- | --- | --- |
| Readwise | `readwise` | 调研/资产 | 搜索一个 AI 工作流主题的 Reader/高亮，判断能否补旧资料。 |
| Zotero | `zotero` | 调研/证据 | 检索本地论文库并导出引用，补强研究证据。 |
| Scite | `scite` | 调研/反方验证 | 检查一个 AI coding 论断的支持与反驳论文。 |
| Semrush | `semrush` | 市场调研 | 查询关键词或站点，判断公开需求和内容机会。 |
| Similarweb | `similarweb` | 市场调研 | 查询候选产品官网流量，作为热度侧证。 |
| Brand24 | `brand24` | 外部讨论/反馈 | 查询关键词提及，观察真实讨论来源和情绪。 |
| Dovetail | `dovetail` | 用户研究/反馈 | 读取访谈或反馈主题，把原话转成决策证据。 |
| PostHog | `posthog` | 行为验证 | 读取事件/漏斗/实验，验证真实使用。 |
| Mixpanel | `mixpanel` | 行为验证 | 读取事件/留存/漏斗，验证使用质量。 |
| Amplitude | `amplitude` | 行为验证 | 读取行为分析，验证产品反馈。 |
| GitHub | `github` | 开源反馈/发布 | 搜索 issue、repo、PR、star/fork 反馈。 |
| Browser | `browser` | 页面验收 | 打开报告索引或公开页面做可视化验收。 |
| Chrome | `chrome` | 登录态验收 | 读取授权页面或后台反馈，不用公共搜索代替。 |
| Computer Use | `computer-use` | 桌面流程验收 | 读取本机应用状态或复现图形界面流程。 |
| Record & Replay | `record-and-replay` | 流程资产化 | 录制一个稳定流程，沉淀成技能草稿。 |
| Documents | `documents` | 文档产物 | 把一个 case 导出成可审阅文档并渲染验收。 |
| PDF | `pdf` | 资料/报告验收 | 读取 PDF 资料或把报告导出 PDF 后检查。 |
| Spreadsheets | `spreadsheets` | 数据/反馈台账 | 把反馈或证据整理成表格并统计。 |
| Presentations | `presentations` | 分享产物 | 把研究结论做成 PPT/Slides。 |
| Data Visualization | `build-web-data-visualization` | 研究可视化 | 把证据数据做成交互图表或报告页。 |
| HyperFrames | `hyperframes` | 视频化产物 | 把研究结论做成 HTML 视频片段。 |

## 全量插件市场插件清单

下面是当前两个插件市场可见的 178 个插件。`安装状态` 来自 `codex plugin list`，不是主观推断。

### 其他

| 插件 | 来源 | 安装状态 | 调用状态 | 等级 | 主要阶段 | 中文判断 |
| --- | --- | --- | --- | --- | --- | --- |
| `cogedim` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 暂不纳入 | 垂直场景插件，当前不进入个人 SignalProof 主线。 |
| `myregistry-com` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 暂不纳入 | 垂直场景插件，当前不进入个人 SignalProof 主线。 |

### 出行

| 插件 | 来源 | 安装状态 | 调用状态 | 等级 | 主要阶段 | 中文判断 |
| --- | --- | --- | --- | --- | --- | --- |
| `finn` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 暂不纳入 | 垂直场景插件，当前不进入个人 SignalProof 主线。 |
| `weatherpromise` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 暂不纳入 | 垂直场景插件，当前不进入个人 SignalProof 主线。 |

### 创意内容

| 插件 | 来源 | 安装状态 | 调用状态 | 等级 | 主要阶段 | 中文判断 |
| --- | --- | --- | --- | --- | --- | --- |
| `biorender` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 产物 | 创意素材或媒体生成插件，可用于内容产物，但不是默认研究能力。 |
| `canva` | openai-curated | 未安装 | 未实测 | A 重点候选 | 内容产物 | 生成或编辑设计，适合中文内容卡片。 |
| `fal` | openai-curated | 未安装 | 未实测 | B 可试点 | 产物 | 创意素材或媒体生成插件，可用于内容产物，但不是默认研究能力。 |
| `figma` | openai-curated | 未安装 | 未实测 | A 重点候选 | 设计产物、视觉验证 | 读取设计或辅助设计到代码，适合视觉产物验证。 |
| `heygen` | openai-curated | 未安装 | 未实测 | B 可试点 | 产物 | 创意素材或媒体生成插件，可用于内容产物，但不是默认研究能力。 |
| `hyperframes` | openai-curated | 未安装 | 未实测 | A 重点候选 | 产物、发布 | 把 HTML/网页内容视频化，适合把研究结论做成传播素材。 |
| `picsart` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 产物 | 创意素材或媒体生成插件，可用于内容产物，但不是默认研究能力。 |
| `remotion` | openai-curated | 未安装 | 未实测 | B 可试点 | 产物 | 创意素材或媒体生成插件，可用于内容产物，但不是默认研究能力。 |
| `shutterstock` | openai-curated | 未安装 | 未实测 | B 可试点 | 产物 | 创意素材或媒体生成插件，可用于内容产物，但不是默认研究能力。 |

### 商业与运营

| 插件 | 来源 | 安装状态 | 调用状态 | 等级 | 主要阶段 | 中文判断 |
| --- | --- | --- | --- | --- | --- | --- |
| `actively` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 线索调研 | 销售、CRM 或线索数据插件，只有做 B2B 服务验证时再启用。 |
| `apollo` | openai-curated | 未安装 | 未实测 | B 可试点 | 线索调研 | 销售、CRM 或线索数据插件，只有做 B2B 服务验证时再启用。 |
| `attio` | openai-curated | 未安装 | 未实测 | B 可试点 | 线索调研 | 销售、CRM 或线索数据插件，只有做 B2B 服务验证时再启用。 |
| `carta-crm` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 线索调研 | 销售、CRM 或线索数据插件，只有做 B2B 服务验证时再启用。 |
| `clay` | openai-curated | 未安装 | 未实测 | B 可试点 | 线索调研 | 销售、CRM 或线索数据插件，只有做 B2B 服务验证时再启用。 |
| `close` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 线索调研 | 销售、CRM 或线索数据插件，只有做 B2B 服务验证时再启用。 |
| `demandbase` | openai-curated | 未安装 | 未实测 | C 场景候选 | 线索调研 | 销售、CRM 或线索数据插件，只有做 B2B 服务验证时再启用。 |
| `hebbia` | openai-curated | 未安装 | 未实测 | B 可试点 | 线索调研 | 销售、CRM 或线索数据插件，只有做 B2B 服务验证时再启用。 |
| `hubspot` | openai-curated | 未安装 | 未实测 | B 可试点 | 线索调研 | 销售、CRM 或线索数据插件，只有做 B2B 服务验证时再启用。 |
| `intercom` | openai-curated | 未安装 | 未实测 | B 可试点 | 线索调研 | 销售、CRM 或线索数据插件，只有做 B2B 服务验证时再启用。 |
| `outreach` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 线索调研 | 销售、CRM 或线索数据插件，只有做 B2B 服务验证时再启用。 |
| `pipedrive` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 线索调研 | 销售、CRM 或线索数据插件，只有做 B2B 服务验证时再启用。 |
| `streak` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 线索调研 | 销售、CRM 或线索数据插件，只有做 B2B 服务验证时再启用。 |
| `zoho` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 线索调研 | 销售、CRM 或线索数据插件，只有做 B2B 服务验证时再启用。 |
| `zoominfo` | openai-curated | 未安装 | 未实测 | B 可试点 | 线索调研 | 销售、CRM 或线索数据插件，只有做 B2B 服务验证时再启用。 |

### 安全

| 插件 | 来源 | 安装状态 | 调用状态 | 等级 | 主要阶段 | 中文判断 |
| --- | --- | --- | --- | --- | --- | --- |
| `codex-security` | openai-curated | 未安装 | 未实测 | A 重点候选 | 代码验证、安全审计 | 扫描授权代码，适合作为代码验证和安全审计补充。 |

### 工程

| 插件 | 来源 | 安装状态 | 调用状态 | 等级 | 主要阶段 | 中文判断 |
| --- | --- | --- | --- | --- | --- | --- |
| `browser` | openai-bundled | 已安装启用 | 已实测失败 | A 重点候选 | 验证、发布、流程自检 | 控制 Codex 内置浏览器，适合验收报告页、公开页面和发布入口；本轮失败要作为能力缺口记录。 |

### 开发工具

| 插件 | 来源 | 安装状态 | 调用状态 | 等级 | 主要阶段 | 中文判断 |
| --- | --- | --- | --- | --- | --- | --- |
| `base44` | openai-curated | 未安装 | 未实测 | C 场景候选 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `build-ios-apps` | openai-curated | 未安装 | 未实测 | C 场景候选 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `build-macos-apps` | openai-curated | 未安装 | 未实测 | C 场景候选 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `build-web-apps` | openai-curated | 未安装 | 未实测 | B 可试点 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `build-web-data-visualization` | openai-curated | 未安装 | 未实测 | A 重点候选 | 调研、产物、资产化 | 把研究数据做成交互图表、报告页或可视化资产。 |
| `catalyst-by-zoho` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `circleci` | openai-curated | 未安装 | 未实测 | B 可试点 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `cloudflare` | openai-curated | 未安装 | 未实测 | A 重点候选 | 发布、运行验证 | 管理 Cloudflare 平台能力，适合部署和运行验证。 |
| `cloudinary` | openai-curated | 未安装 | 未实测 | B 可试点 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `coderabbit` | openai-curated | 未安装 | 未实测 | B 可试点 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `convex` | openai-curated | 未安装 | 未实测 | B 可试点 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `datadog` | openai-curated | 未安装 | 未实测 | A 重点候选 | 运行反馈、验证 | 读取日志、指标和链路，适合验证运行态问题。 |
| `expo` | openai-curated | 未安装 | 未实测 | C 场景候选 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `game-studio` | openai-curated | 未安装 | 未实测 | C 场景候选 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `github` | openai-curated | 未安装 | 未实测 | A 重点候选 | 开源证据、发布反馈 | 读取仓库、issue、PR、CI 和发布反馈，适合开源案例。 |
| `hostinger` | openai-curated | 未安装 | 未实测 | C 场景候选 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `hugging-face` | openai-curated | 未安装 | 未实测 | A 重点候选 | 模型/数据集调研 | 检索模型、数据集和 Space，适合 AI 技术调研。 |
| `lovable` | openai-curated | 未安装 | 未实测 | C 场景候选 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `magicpath` | openai-curated | 未安装 | 未实测 | B 可试点 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `marcopolo` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `neon-postgres` | openai-curated | 未安装 | 未实测 | B 可试点 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `netlify` | openai-curated | 未安装 | 未实测 | A 重点候选 | 发布、运行验证 | 部署和管理发布，适合公开验证入口。 |
| `nvidia` | openai-curated | 未安装 | 未实测 | C 场景候选 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `openai-developers` | openai-curated | 未安装 | 未实测 | A 重点候选 | 技术调研、实现验证 | 查询 OpenAI 开发文档和实现建议，适合技术方案验证。 |
| `plugin-eval` | openai-curated | 未安装 | 未实测 | C 场景候选 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `quicknode` | openai-curated | 未安装 | 未实测 | C 场景候选 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `render` | openai-curated | 未安装 | 未实测 | B 可试点 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `replit` | openai-curated | 未安装 | 未实测 | C 场景候选 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `sendgrid` | openai-curated | 未安装 | 未实测 | C 场景候选 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `sentry` | openai-curated | 未安装 | 未实测 | A 重点候选 | 错误反馈、验证 | 读取线上错误和事件，适合把运行问题纳入反馈。 |
| `shopify` | openai-curated | 未安装 | 未实测 | C 场景候选 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `statsig` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `supabase` | openai-curated | 未安装 | 未实测 | B 可试点 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `superpowers` | openai-curated | 未安装 | 未实测 | A 重点候选 | 开发流程、复盘资产 | 规划、TDD、调试和交付流程，适合把开发流程固化。 |
| `temporal` | openai-curated | 未安装 | 未实测 | B 可试点 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `test-android-apps` | openai-curated | 未安装 | 未实测 | B 可试点 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `twilio-developer-kit` | openai-curated | 未安装 | 未实测 | C 场景候选 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `vantage` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `vercel` | openai-curated | 未安装 | 未实测 | A 重点候选 | 发布、运行验证 | 部署和检查 Web 产物，适合公开验证入口。 |
| `wix` | openai-curated | 未安装 | 未实测 | C 场景候选 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |
| `yepcode` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 实现、验证 | 开发、部署或调试插件，适合产物落地后的工程验证。 |

### 教育与研究

| 插件 | 来源 | 安装状态 | 调用状态 | 等级 | 主要阶段 | 中文判断 |
| --- | --- | --- | --- | --- | --- | --- |
| `dow-jones-factiva` | openai-curated | 未安装 | 未实测 | B 可试点 | 调研 | 专业研究插件，适合对应领域调研，需看账号和资料覆盖。 |
| `govtribe` | openai-curated | 未安装 | 未实测 | C 场景候选 | 调研 | 专业研究插件，适合对应领域调研，需看账号和资料覆盖。 |
| `latex` | openai-bundled | 未安装 | 未实测 | C 场景候选 | 调研 | 专业研究插件，适合对应领域调研，需看账号和资料覆盖。 |
| `life-science-research` | openai-curated | 未安装 | 未实测 | B 可试点 | 调研 | 专业研究插件，适合对应领域调研，需看账号和资料覆盖。 |
| `midpage` | openai-curated | 未安装 | 未实测 | B 可试点 | 调研 | 专业研究插件，适合对应领域调研，需看账号和资料覆盖。 |
| `ngs-analysis` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 调研 | 专业研究插件，适合对应领域调研，需看账号和资料覆盖。 |
| `particl-market-research` | openai-curated | 未安装 | 未实测 | B 可试点 | 调研 | 专业研究插件，适合对应领域调研，需看账号和资料覆盖。 |
| `policynote` | openai-curated | 未安装 | 未实测 | B 可试点 | 调研 | 专业研究插件，适合对应领域调研，需看账号和资料覆盖。 |
| `readwise` | openai-curated | 未安装 | 未实测 | A 重点候选 | 调研、资产化 | 读取 Reader/高亮信息，适合补充旧资料和长期阅读资产。 |
| `scite` | openai-curated | 未安装 | 未实测 | A 重点候选 | 调研、反方验证 | 检查论文支持和反驳关系，适合验证关键论断。 |
| `zotero` | openai-curated | 未安装 | 未实测 | A 重点候选 | 调研、证据管理 | 检索论文库和引用，适合做严肃研究证据补强。 |

### 数据与分析

| 插件 | 来源 | 安装状态 | 调用状态 | 等级 | 主要阶段 | 中文判断 |
| --- | --- | --- | --- | --- | --- | --- |
| `alation` | openai-curated | 未安装 | 未实测 | B 可试点 | 调研、验证 | 数据分析插件，适合已有产品、营销或业务数据时使用。 |
| `amplitude` | openai-curated | 未安装 | 未实测 | A 重点候选 | 行为反馈、验证 | 查询行为分析和漏斗，适合产品验证阶段。 |
| `coupler-io` | openai-curated | 未安装 | 未实测 | B 可试点 | 调研、验证 | 数据分析插件，适合已有产品、营销或业务数据时使用。 |
| `deepnote` | openai-curated | 未安装 | 未实测 | A 重点候选 | 数据分析、研究实验 | 做数据探索和分析实验，适合研究型数据处理。 |
| `mixpanel` | openai-curated | 未安装 | 未实测 | A 重点候选 | 行为反馈、验证 | 查询产品行为数据，适合看真实使用和留存。 |
| `mixpanel-headless` | openai-curated | 未安装 | 未实测 | B 可试点 | 调研、验证 | 数据分析插件，适合已有产品、营销或业务数据时使用。 |
| `motherduck` | openai-curated | 未安装 | 未实测 | B 可试点 | 调研、验证 | 数据分析插件，适合已有产品、营销或业务数据时使用。 |
| `omni-analytics` | openai-curated | 未安装 | 未实测 | B 可试点 | 调研、验证 | 数据分析插件，适合已有产品、营销或业务数据时使用。 |
| `posthog` | openai-curated | 未安装 | 未实测 | A 重点候选 | 行为反馈、验证 | 查询事件、漏斗、实验和错误，适合验证产品行为反馈。 |
| `similarweb` | openai-curated | 未安装 | 未实测 | A 重点候选 | 市场调研 | 查询网站流量和来源，适合竞品热度和市场侧证。 |
| `thoughtspot` | openai-curated | 未安装 | 未实测 | B 可试点 | 调研、验证 | 数据分析插件，适合已有产品、营销或业务数据时使用。 |
| `windsor-ai` | openai-curated | 未安装 | 未实测 | B 可试点 | 调研、验证 | 数据分析插件，适合已有产品、营销或业务数据时使用。 |

### 沟通协作

| 插件 | 来源 | 安装状态 | 调用状态 | 等级 | 主要阶段 | 中文判断 |
| --- | --- | --- | --- | --- | --- | --- |
| `circleback` | openai-curated | 未安装 | 未实测 | B 可试点 | 反馈、触达 | 会议、邮件或协作记录插件，可在授权后作为反馈来源。 |
| `fireflies` | openai-curated | 未安装 | 未实测 | B 可试点 | 反馈、触达 | 会议、邮件或协作记录插件，可在授权后作为反馈来源。 |
| `fyxer` | openai-curated | 未安装 | 未实测 | B 可试点 | 反馈、触达 | 会议、邮件或协作记录插件，可在授权后作为反馈来源。 |
| `gmail` | openai-curated | 未安装 | 未实测 | B 可试点 | 邮件反馈、发布触达 | 读取和整理邮件反馈，适合授权后做发布触达和反馈回收。 |
| `granola` | openai-curated | 未安装 | 未实测 | B 可试点 | 反馈、触达 | 会议、邮件或协作记录插件，可在授权后作为反馈来源。 |
| `otter-ai` | openai-curated | 未安装 | 未实测 | B 可试点 | 反馈、触达 | 会议、邮件或协作记录插件，可在授权后作为反馈来源。 |
| `outlook-email` | openai-curated | 未安装 | 未实测 | C 场景候选 | 反馈、触达 | 会议、邮件或协作记录插件，可在授权后作为反馈来源。 |
| `read-ai` | openai-curated | 未安装 | 未实测 | B 可试点 | 反馈、触达 | 会议、邮件或协作记录插件，可在授权后作为反馈来源。 |
| `slack` | openai-curated | 未安装 | 未实测 | B 可试点 | 社群反馈、协作触达 | 读取和总结频道信息，适合授权社群或团队反馈。 |
| `superhuman` | openai-curated | 未安装 | 未实测 | B 可试点 | 反馈、触达 | 会议、邮件或协作记录插件，可在授权后作为反馈来源。 |
| `teams` | openai-curated | 未安装 | 未实测 | C 场景候选 | 反馈、触达 | 会议、邮件或协作记录插件，可在授权后作为反馈来源。 |
| `zoom` | openai-curated | 未安装 | 未实测 | B 可试点 | 反馈、触达 | 会议、邮件或协作记录插件，可在授权后作为反馈来源。 |

### 生产力

| 插件 | 来源 | 安装状态 | 调用状态 | 等级 | 主要阶段 | 中文判断 |
| --- | --- | --- | --- | --- | --- | --- |
| `airtable` | openai-curated | 未安装 | 未实测 | A 重点候选 | 反馈台账、线索台账 | 维护结构化表，适合反馈台账、线索台账和候选池。 |
| `asana` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `atlassian-rovo` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `box` | openai-curated | 未安装 | 未实测 | A 重点候选 | 文档资料、资产化 | 搜索文档库，适合资料型研究。 |
| `brand24` | openai-curated | 未安装 | 未实测 | A 重点候选 | 外部讨论、反馈 | 查询品牌和关键词提及，适合捕捉真实讨论与反馈。 |
| `brighthire` | openai-curated | 未安装 | 未实测 | B 可试点 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `calendly` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `channel99` | openai-curated | 未安装 | 未实测 | B 可试点 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `chrome` | openai-bundled | 已安装启用 | 未直接调用 | A 重点候选 | 调研、发布、反馈 | 使用本机 Chrome 登录态，适合读取授权页面、后台和真实反馈渠道。 |
| `clickup` | openai-curated | 未安装 | 未实测 | C 场景候选 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `common-room` | openai-curated | 未安装 | 未实测 | B 可试点 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `computer-use` | openai-bundled | 已安装启用 | 已实测成功 | A 重点候选 | 验证、流程自检 | 控制本机图形界面，适合验证非网页流程和桌面应用状态。 |
| `conductor` | openai-curated | 未安装 | 未实测 | B 可试点 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `coveo` | openai-curated | 未安装 | 未实测 | B 可试点 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `datasite` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `docket` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `docusign` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `domotz-preview` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `dovetail` | openai-curated | 未安装 | 未实测 | A 重点候选 | 用户研究、反馈 | 读取访谈和用户研究资料，适合把反馈转成决策证据。 |
| `egnyte` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `google-calendar` | openai-curated | 未安装 | 未实测 | B 可试点 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `google-drive` | openai-curated | 未安装 | 未实测 | A 重点候选 | 资料调研、资产沉淀 | 访问 Drive/Docs/Sheets/Slides，适合沉淀研究资料和资产。 |
| `happenstance` | openai-curated | 未安装 | 未实测 | B 可试点 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `help-scout` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `hg-insights` | openai-curated | 未安装 | 未实测 | B 可试点 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `highlevel` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `jam` | openai-curated | 未安装 | 未实测 | A 重点候选 | 问题录制、验证反馈 | 录制问题上下文，适合反馈复现。 |
| `linear` | openai-curated | 未安装 | 未实测 | A 重点候选 | 任务反馈、决策跟踪 | 读取或创建任务，适合把验证结论进入任务闭环。 |
| `mem` | openai-curated | 未安装 | 未实测 | A 重点候选 | 个人知识库、资产化 | 连接个人第二大脑，适合长期资产复用。 |
| `meticulate` | openai-curated | 未安装 | 未实测 | C 场景候选 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `monday-com` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `network-solutions` | openai-curated | 未安装 | 未实测 | B 可试点 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `notion` | openai-curated | 未安装 | 未实测 | A 重点候选 | 资料沉淀、资产化 | 读取或维护 Notion 资料，适合知识库和研究记录。 |
| `outlook-calendar` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `pylon` | openai-curated | 未安装 | 未实测 | B 可试点 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `ranked-ai` | openai-curated | 未安装 | 未实测 | B 可试点 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `record-and-replay` | openai-bundled | 已安装启用 | 未实测 | A 重点候选 | 流程录制、资产化 | 录制用户操作并沉淀成可复用技能，适合把稳定流程资产化。 |
| `responsive` | openai-curated | 未安装 | 未实测 | B 可试点 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `rox` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `semrush` | openai-curated | 未安装 | 未实测 | A 重点候选 | 市场调研、发布反馈 | 查询关键词、站点和 SEO 数据，适合内容机会和公开需求判断。 |
| `sharepoint` | openai-curated | 未安装 | 未实测 | B 可试点 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `signnow` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `skywatch` | openai-curated | 未安装 | 未实测 | B 可试点 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `teamwork-com` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `united-rentals` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |
| `waldo` | openai-curated | 未安装 | 未实测 | B 可试点 | 资料、反馈、资产 | 知识库、项目管理或协作插件，适合授权资料和反馈沉淀。 |

### 金融

| 插件 | 来源 | 安装状态 | 调用状态 | 等级 | 主要阶段 | 中文判断 |
| --- | --- | --- | --- | --- | --- | --- |
| `aiera` | openai-curated | 未安装 | 未实测 | C 场景候选 | 专项调研 | 金融、公司或市场数据插件，只在金融/公司研究案例中启用。 |
| `alpaca` | openai-curated | 未安装 | 未实测 | C 场景候选 | 专项调研 | 金融、公司或市场数据插件，只在金融/公司研究案例中启用。 |
| `binance` | openai-curated | 未安装 | 未实测 | C 场景候选 | 专项调研 | 金融、公司或市场数据插件，只在金融/公司研究案例中启用。 |
| `brex` | openai-curated | 未安装 | 未实测 | C 场景候选 | 专项调研 | 金融、公司或市场数据插件，只在金融/公司研究案例中启用。 |
| `cb-insights` | openai-curated | 未安装 | 未实测 | B 可试点 | 专项调研 | 金融、公司或市场数据插件，只在金融/公司研究案例中启用。 |
| `chronograph` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 专项调研 | 金融、公司或市场数据插件，只在金融/公司研究案例中启用。 |
| `cube` | openai-curated | 未安装 | 未实测 | C 场景候选 | 专项调研 | 金融、公司或市场数据插件，只在金融/公司研究案例中启用。 |
| `daloopa` | openai-curated | 未安装 | 未实测 | C 场景候选 | 专项调研 | 金融、公司或市场数据插件，只在金融/公司研究案例中启用。 |
| `dnb-finance-analytics` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 专项调研 | 金融、公司或市场数据插件，只在金融/公司研究案例中启用。 |
| `factset` | openai-curated | 未安装 | 未实测 | B 可试点 | 专项调研 | 金融、公司或市场数据插件，只在金融/公司研究案例中启用。 |
| `fiscal-ai` | openai-curated | 未安装 | 未实测 | B 可试点 | 专项调研 | 金融、公司或市场数据插件，只在金融/公司研究案例中启用。 |
| `keybid-puls` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 专项调研 | 金融、公司或市场数据插件，只在金融/公司研究案例中启用。 |
| `lseg` | openai-curated | 未安装 | 未实测 | B 可试点 | 专项调研 | 金融、公司或市场数据插件，只在金融/公司研究案例中启用。 |
| `moody-s` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 专项调研 | 金融、公司或市场数据插件，只在金融/公司研究案例中启用。 |
| `morningstar` | openai-curated | 未安装 | 未实测 | B 可试点 | 专项调研 | 金融、公司或市场数据插件，只在金融/公司研究案例中启用。 |
| `mt-newswires` | openai-curated | 未安装 | 未实测 | B 可试点 | 专项调研 | 金融、公司或市场数据插件，只在金融/公司研究案例中启用。 |
| `pitchbook` | openai-curated | 未安装 | 未实测 | B 可试点 | 专项调研 | 金融、公司或市场数据插件，只在金融/公司研究案例中启用。 |
| `quartr` | openai-curated | 未安装 | 未实测 | B 可试点 | 专项调研 | 金融、公司或市场数据插件，只在金融/公司研究案例中启用。 |
| `quickbooks` | openai-curated | 未安装 | 未实测 | C 场景候选 | 专项调研 | 金融、公司或市场数据插件，只在金融/公司研究案例中启用。 |
| `razorpay` | openai-curated | 未安装 | 未实测 | C 场景候选 | 专项调研 | 金融、公司或市场数据插件，只在金融/公司研究案例中启用。 |
| `s-p` | openai-curated | 未安装 | 未实测 | B 可试点 | 专项调研 | 金融、公司或市场数据插件，只在金融/公司研究案例中启用。 |
| `setu-bharat-connect-billpay` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 专项调研 | 金融、公司或市场数据插件，只在金融/公司研究案例中启用。 |
| `stripe` | openai-curated | 未安装 | 未实测 | C 场景候选 | 专项调研 | 金融、公司或市场数据插件，只在金融/公司研究案例中启用。 |
| `taxdown` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 专项调研 | 金融、公司或市场数据插件，只在金融/公司研究案例中启用。 |
| `third-bridge` | openai-curated | 未安装 | 未实测 | B 可试点 | 专项调研 | 金融、公司或市场数据插件，只在金融/公司研究案例中启用。 |
| `tinman-ai` | openai-curated | 未安装 | 未实测 | D 暂不适合 | 专项调研 | 金融、公司或市场数据插件，只在金融/公司研究案例中启用。 |

## 使用原则

1. 先按阶段选候选插件，不按插件清单机械全跑。
2. 调研类插件优先回答“谁在说、在哪里说、痛点是什么、有没有反证”。
3. 验证类插件优先回答“页面是否能打开、行为是否发生、错误是否真实、任务是否闭环”。
4. 应用集成或 MCP 型插件如果没有授权，就记录为 `blocked/auth`，不能把未授权当成 0 结果。
5. 只要真实调用过，就把原始查询、失败信息、结果质量和下一步写入对应 case 的 `tool-ledger.md`。
