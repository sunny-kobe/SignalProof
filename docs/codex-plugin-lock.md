# Codex 插件锁定清单

这份清单用于换电脑、重装 Codex 或后续插件更新时恢复 SignalProof 的工作流能力。

## 保存原则

- 保存“应该安装哪些插件”和“为什么需要它们”；
- 保存 SignalProof 自己的 repo skill、repo plugin、repo marketplace；
- 不保存官方插件缓存；
- 不保存 OAuth、浏览器 cookie、API key 或外部账号登录态；
- 插件更新或流程更新后，同步更新本文件、`scripts/install-codex-plugins.sh` 和 `docs/codex-plugin-status-and-migration.md`。

## 研究质量门边界

这份锁定清单只证明“迁移时应该恢复哪些 Codex 能力”，不证明某个机会已经被验证。每个真实 case 仍必须按 `docs/research-quality-gate.md` 单独记录：

- 来源覆盖：公开讨论、项目和数据、官方和一手资料、反证和替代方案；
- 交叉验证：谁在说、说什么、在哪里说、有没有反证；
- 证据等级：strong / medium / weak / blocked；
- 结论许可：继续研究、低成本实验、暂停或放弃；
- 用户授权缺口：外部 app connector、OAuth、cookie、API key、付费额度是否真实可用。

因此，插件已安装只能支持“可执行流程恢复”，不能直接支持市场验证、产品化或 SaaS 化判断。

## 官方插件安装清单

下面是当前本机已启用并进入 SignalProof 候选流程的插件。换电脑时优先用安装脚本重装，而不是复制 `~/.codex/plugins/cache`。

| 插件 | 来源 | SignalProof 角色 | 迁移处理 |
| --- | --- | --- | --- |
| `browser` | `openai-bundled` | 网页验收和公开页面复核 | 重装后新线程探针 |
| `chrome` | `openai-bundled` | 使用用户 Chrome 登录态做只读复查 | 重装后重新授权/确认扩展 |
| `computer-use` | `openai-bundled` | GUI-only 验收和本地应用检查 | 重装后重新授予系统权限 |
| `record-and-replay` | `openai-bundled` | 把用户演示沉淀成 skill | 重装后重新检查 macOS 权限 |
| `build-web-data-visualization` | `openai-curated` | 把研究或反馈数据转成可视化资产 | 重装 |
| `hyperframes` | `openai-curated` | 视觉叙事和视频化表达 | 重装 |
| `github` | `openai-curated` | 开源信号、issue、PR、发布反馈 | 重装后确认 `gh` 账号 |
| `hugging-face` | `openai-curated` | 模型、数据集和 AI 项目信号 | 重装，必要时另装 CLI |
| `openai-developers` | `openai-curated` | OpenAI / Codex 官方文档和 API 事实 | 重装 |
| `codex-security` | `openai-curated` | 安全扫描和安全审查 | 重装 |
| `google-drive` | `openai-curated` | 外部文档资料和授权资料库 | 重装后重新授权 |
| `notion` | `openai-curated` | 授权知识库和规格资料 | 重装后重新授权 |
| `airtable` | `openai-curated` | 表格化资料和反馈台账 | 重装后重新授权 |
| `deepnote` | `openai-curated` | 数据分析 notebook | 重装后重新授权 |
| `posthog` | `openai-curated` | 产品行为反馈 | 有真实项目后授权 |
| `mixpanel` | `openai-curated` | 产品行为反馈 | 有真实项目后授权 |
| `amplitude` | `openai-curated` | 产品行为反馈 | 有真实项目后授权 |
| `sentry` | `openai-curated` | 运行错误和异常反馈 | 有线上项目后授权 |
| `datadog` | `openai-curated` | 运行态指标和日志 | 有线上项目后授权 |
| `brand24` | `openai-curated` | 品牌/关键词公开提及 | 具体 case 后授权探针 |
| `semrush` | `openai-curated` | SEO、关键词和竞品研究 | 具体 case 后授权探针 |
| `similarweb` | `openai-curated` | 竞品流量和来源分析 | 具体 case 后授权探针 |
| `readwise` | `openai-curated` | 阅读库和高亮资料 | 具体 case 后授权探针 |
| `scite` | `openai-curated` | 论文支持和反证 | 具体 case 后授权探针 |
| `zotero` | `openai-curated` | 本地论文资料库 | 有资料库后启用 |
| `canva` | `openai-curated` | 设计物料 | 有视觉素材目标时授权 |
| `figma` | `openai-curated` | 设计稿和图表 | 有设计目标时授权 |
| `vercel` | `openai-curated` | Web 发布和部署验收 | 有部署目标时授权 |
| `netlify` | `openai-curated` | Web 发布和部署验收 | 有部署目标时授权 |
| `cloudflare` | `openai-curated` | Workers / DNS / 部署 | 有部署目标时授权 |
| `linear` | `openai-curated` | issue/project 工作流 | 有项目管理目标时授权 |
| `box` | `openai-curated` | 外部文件库 | 有资料源时授权 |
| `dovetail` | `openai-curated` | 访谈/研究反馈库 | 有真实访谈资料时授权 |
| `jam` | `openai-curated` | bug/页面反馈材料 | 有页面反馈目标时授权 |
| `mem` | `openai-curated` | 外部知识沉淀 | 有知识库目标时授权 |
| `superpowers` | `openai-curated` | 规划、验证和分工工作流 | 重装 |

## primary-runtime 能力

这些能力当前通过 `~/.codex/config.toml` 和本机缓存可见，但不建议直接复制缓存目录：

- `documents@openai-primary-runtime`
- `spreadsheets@openai-primary-runtime`
- `presentations@openai-primary-runtime`
- 本机缓存还可见 `pdf`

换电脑后用 `python3 scripts/signalproof.py capabilities` 复核。

## SignalProof 本地插件

这些文件应随仓库迁移：

- `.agents/skills/signalproof/SKILL.md`
- `.agents/plugins/marketplace.json`
- `plugins/signalproof/.codex-plugin/plugin.json`
- `plugins/signalproof/skills/signalproof/SKILL.md`

如果未来要把它同步到 CcSwitch，优先同步 repo skill；官方插件安装状态仍以本文件和安装脚本为准。

## 换电脑恢复步骤

1. 克隆 SignalProof 仓库。
2. 运行：

```bash
bash scripts/install-codex-plugins.sh
```

3. 打开新 Codex 线程。
4. 运行：

```bash
python3 scripts/signalproof.py capabilities
python3 scripts/signalproof.py plugin-status
python3 scripts/signalproof.py check-plugin-drift
python3 scripts/signalproof.py check-goal --min-cases 5
```

5. 对需要真实数据的 app connector 重新登录授权。

## 漂移检查

每次插件或流程更新后，先运行：

```bash
python3 scripts/signalproof.py plugin-status
python3 scripts/signalproof.py check-plugin-drift
```

`check-plugin-drift` 会比对四层：

- `docs/codex-plugin-lock.md` 中的官方插件锁定清单；
- `scripts/install-codex-plugins.sh` 中的安装清单；
- 当天 `vault/runs/<date>-codex-plugin-status.md` 状态快照；
- 当前 `codex plugin list` 的已安装启用项。

如果只想检查 repo 文件和当天快照，不实时调用 Codex CLI，可以运行：

```bash
python3 scripts/signalproof.py check-plugin-drift --no-codex
```

这个检查只证明安装和记录没有漂移，不证明外部账号已授权，也不证明 connector 能读取真实数据。

## 更新规则

后续只要发生下面任一变化，就同步更新本文件和安装脚本：

- 新增或移除 Codex 插件；
- 某个插件从“条件触发”变成“默认候选”；
- SignalProof 阶段流程改变；
- 换电脑或重装 Codex 后发现恢复步骤缺漏；
- CcSwitch 增加官方 Codex 插件管理能力。
