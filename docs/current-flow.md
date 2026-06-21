# 当前执行流程

这份文档记录 SignalProof 现在每个流程是怎么跑的，以及重启后推荐插件进入个人工作流的实际接入点。

## 1. 能力诊断

命令：

```bash
python3 scripts/signalproof.py diagnose
```

作用：

- 记录本机 Python 版本；
- 检查 `last30days` 脚本是否存在；
- 尝试运行 `last30days --diagnose`；
- 输出到 `vault/runs/<date>-capability-snapshot.json`。

当前边界：

- 这是环境诊断，不代表研究证据合格。
- 如果某个来源失败，只能写成能力缺口，不能写成反证。

## 2. Codex 能力矩阵

命令：

```bash
python3 scripts/signalproof.py capabilities
```

作用：

- 检测本机可用的 Codex 自带插件；
- 输出阶段到插件的能力矩阵；
- 写入 `vault/runs/<date>-codex-capability-matrix.md`。

当前插件候选分两层：

- Codex 自带和 runtime 能力：Browser、Chrome、Computer Use、Record & Replay、Documents、PDF、Spreadsheets、Presentations、Data Visualization、HyperFrames。
- 已安装的推荐 marketplace 插件：GitHub、Hugging Face、OpenAI Developers、Codex Security、Google Drive、Notion、Airtable、Deepnote、PostHog、Mixpanel、Amplitude、Sentry、Datadog、Brand24、Semrush、Similarweb、Scite、Readwise、Zotero、Canva、Figma、Vercel、Netlify、Cloudflare、Linear、Box、Superpowers 等。

使用原则：

- 不默认全跑；
- 只在能改变判断、减少不确定性或验收产物时调用；
- 使用、跳过、失败都写入 `tool-ledger.md`。

## 3. 插件实际调用循环

能力矩阵之后，不能直接假设插件可用。每个需要插件参与的案例，都按下面顺序跑：

1. 选择一个会改变判断、减少不确定性或验收产物的插件；
2. 读取对应插件 skill；
3. 按插件推荐入口实际调用；
4. 记录原始结果、错误信息和结果质量；
5. 如果失败，先写入 `tool-ledger.md`，再选择降级路径；
6. 在 `flow-review.md` 写明下次优化。

历史实测和当前复核：

- Browser 插件曾按真实接入流程调用失败，错误为 `codex/sandbox-state-meta: missing field sandboxPolicy`；该结果保留为历史风险，不再写成当前必然失败。后续有网页验收目标时重新做只读探针。
- Computer Use 插件入口可响应，重启后新线程 `list_apps` 成功；
- Computer Use 读取具体 App 状态仍可能失败，主线程 `get_app_state(Codex)` 返回 macOS 错误 `-1743`；
- Chrome 插件已做过只读复查：Codex Chrome 插件层能枚举到 GitHub 标签页；本机 Chrome 窗口能看到 X 和 Readwise 页面。Chrome/Browser 只在有登录态页面或网页验收目标时触发。

当前边界：

- 插件文件存在不等于真实可用；
- Computer Use 的 `list_apps` 成功不等于所有 GUI 状态都能读取；
- 插件失败是流程证据，不能被降级路径覆盖掉。

## 3.1 重启后推荐插件深测

探针线程：

```text
019ee803-b71e-7b01-a7b6-1608b91e9916
```

证据文件：

```text
vault/cases/2026-06-21-codex-推荐插件真实试跑评估/evidence/restart-thread-plugin-deepcheck-receipt.md
```

结论：

- marketplace 插件合计 178 个，已安装启用 36 个，未安装 142 个；
- `~/.codex/config.toml` 当前启用项合计 40 个，其中 3 个是 primary-runtime 配置启用项；本机缓存可见 Documents、PDF、Spreadsheets、Presentations 4 个 runtime 能力；
- A 级推荐 marketplace 插件无缺失；
- primary-runtime 的 Documents、PDF、Spreadsheets、Presentations 可见；
- Record & Replay 的 `event_stream_status` 可响应；
- Computer Use 的 `list_apps` 可响应；
- 多数外部 SaaS / app connector 插件已安装，但当前线程未暴露直连 tool 或尚未授权，不能写成已读取真实数据。

重启后执行规则：

1. 新 case 开始时可以先运行 `codex plugin list`、`python3 scripts/signalproof.py capabilities`。
2. 如果要判断“插件是否真实可用”，优先另开只读线程做无副作用探针。
3. 探针回执必须写入 case evidence，不只留在聊天记录里。
4. 外部 app connector 只有在 tool 入口、账号授权、真实数据源都成立时，才算可用于证据。

## 3.2 插件状态和迁移

命令：

```bash
python3 scripts/signalproof.py plugin-status
```

作用：

- 读取 `codex plugin list` 和 `codex plugin marketplace list`；
- 读取 `~/.codex/config.toml` 中的插件启用项；
- 生成 `vault/runs/<date>-codex-plugin-status.md`；
- 解释为什么界面里不一定直接看到已安装插件；
- 记录插件哪些部分能随仓库迁移，哪些需要在新机器重新安装或授权。

当前边界：

- repo 内的 `.agents/skills/signalproof/`、`plugins/signalproof/`、`.agents/plugins/marketplace.json` 可以迁移；
- 官方/curated 插件缓存不建议直接迁移，应在新机器用 `codex plugin add` 或插件市场重新安装；
- 外部账号 OAuth、浏览器 cookie、API key 不随仓库迁移。
- skills / plugins 的界面可见性受新线程加载和初始 skills 列表上下文预算影响；看不到全量列表不等于未安装，应以 `plugin-status`、`codex plugin list` 的 `STATUS`、以及只读探针为准。

## 3.3 个人工作流分层

| 层级 | 默认进入的能力 | 使用方式 |
| --- | --- | --- |
| 基础默认 | SignalProof 本地脚本、Markdown vault、`check-all`、`export-all`、`capabilities` | 每个 case 都保留。 |
| 调研默认候选 | GitHub、last30days、OpenAI Docs | 有公开信号、AI 工具趋势、技术事实时优先考虑。 |
| 验证默认候选 | 本地脚本、Spreadsheets、Record & Replay | 用于结构检查、证据表、用户演示流程。 |
| 产物默认候选 | Spreadsheets、Data Visualization | 把工具账本和结果变成可检查资产。 |
| 条件触发 | Browser、Chrome、Computer Use、Documents、PDF、Presentations、HyperFrames、Canva、Figma、Codex Security | 有网页、登录态、GUI、正式交付件、传播素材或安全扫描目标时启用。 |
| 授权后触发 | PostHog、Mixpanel、Amplitude、Sentry、Datadog、Brand24、Semrush、Similarweb、Scite、Readwise、Zotero、Notion、Google Drive、Airtable、Deepnote、Linear、Box | 有账号、tool 入口和真实数据源时启用。 |

任何插件调用后都要写结果质量：强 / 中 / 弱 / 失败 / 阻塞。工具被调用过，不等于证据合格。

## 4. 创建 Case

命令：

```bash
python3 scripts/signalproof.py init-case "<title>"
```

作用：

- 从 `templates/case/` 创建完整案例文件；
- 必需文件包括 `signal.md`、`research.md`、`debate.md`、`thesis.md`、`validation.md`、`artifact.md`、`feedback.md`、`decision.md`、`asset.md`、`flow-review.md`、`tool-ledger.md`、`process-log.md`、`report.md`。

当前边界：

- `init-case` 只生成结构，不自动判断证据；
- 是否调用插件由阶段能力计划决定。

## 5. Seed 示例案例

命令：

```bash
python3 scripts/seed_cases.py
```

作用：

- 生成 5 个差异化内部案例；
- 每个案例都带工具账本、流程自检和过程日志；
- 真实反馈和发布渠道保持为空。

当前边界：

- seed 只证明内部协议闭环，不证明市场需求。
- seed 内容会覆盖对应案例的顶层文件，不覆盖 legacy 目录。

## 6. Case 自检

命令：

```bash
python3 scripts/signalproof.py check-all
```

作用：

- 检查必需文件是否存在；
- 检查真实反馈为空时是否过度声称；
- 检查 `tool-ledger.md` 是否覆盖关键能力和结果质量；
- 检查 `process-log.md` 是否包含迭代、命令、自检和优化。

当前边界：

- 它是结构和风险语言检查；
- 不替代真实市场验证。

## 7. 导出报告

命令：

```bash
python3 scripts/signalproof.py export-all
```

作用：

- 把每个案例导出到 `vault/reports/*.md`；
- 生成 `vault/reports/index.md` 和 `vault/reports/index.html`。

当前边界：

- HTML 报告索引可以用 Browser 验收；
- 当前脚本只做文件级导出，不做视觉渲染判断。

## 8. MVP 目标检查

命令：

```bash
python3 scripts/signalproof.py check-goal --min-cases 5
```

作用：

- 检查至少 5 个案例；
- 检查报告索引；
- 检查能力快照；
- 检查 Codex 能力矩阵；
- 检查 legacy 迁移；
- 检查插件 marketplace；
- 检查每个案例的反馈边界、工具账本和优化记录。

当前边界：

- 通过表示内部协议 MVP 成立；
- 不表示真实反馈、真实发布或市场验证成立。

## 下一步增量

下一步不应该一次性接入所有插件，而是按阶段增加：

1. 调研 case：默认考虑 GitHub + last30days + OpenAI Docs，并按 `docs/research-quality-gate.md` 检查来源覆盖、交叉验证、反证和结论许可；账号类调研插件只有授权后再加。
2. 验证 case：优先脚本自检 + 文件级检查 + Spreadsheets；Browser 修复后、Computer Use 目标 App 权限确认后再作为硬验收。
3. 产物 case：默认用 Spreadsheets / Data Visualization；正式交付件再加 Documents / PDF / Presentations。
4. 反馈 case：只有真实产品数据或公开触达反馈存在时，才启用 PostHog / Mixpanel / Amplitude / Sentry / Datadog / Brand24。

当前最重要的流程缺口是研究准确性门，而不是继续安装更多插件。研究证据弱时，SignalProof 只能推进到补研究或低成本内部实验，不能把内部流程闭环写成市场验证。

用户本人需要处理的授权/API 见 [`docs/user-auth-and-api-checklist.md`](user-auth-and-api-checklist.md)。当前没有必须立刻付费处理的 X API 项；GitHub 已是 `sunny-kobe` 活跃账号，Full Disk Access 已通过，研究增强类账号按 case 做只读探针。
