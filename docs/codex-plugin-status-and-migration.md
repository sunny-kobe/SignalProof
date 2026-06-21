# Codex 插件状态和迁移说明

这份文档回答三个问题：

- 插件到底有没有装好；
- 为什么 Codex 界面里不一定看得到；
- SignalProof 想做成可迁移工作流时，插件能迁移到什么程度。

## 当前结论

截至 2026-06-21，本机插件状态是：

| 口径 | 当前状态 |
| --- | --- |
| `codex plugin list` 可见 marketplace 插件 | 178 个 |
| 已安装启用的 marketplace 插件 | 36 个 |
| 未安装 marketplace 插件 | 142 个 |
| `~/.codex/config.toml` 启用项 | 40 个 |
| primary-runtime 能力 | Documents、PDF、Spreadsheets、Presentations |
| SignalProof repo 本地插件 | 已有 `plugins/signalproof/` 和 `.agents/plugins/marketplace.json` |

这说明：插件不是没装，而是 `codex plugin list` 会把“已安装”和“未安装但可选”的 marketplace 插件放在同一张表里。看 `STATUS` 列才是关键，只有 `installed, enabled` 表示已经安装启用。

## 为什么界面里看不到

常见原因有六类：

| 现象 | 解释 | 判断方式 |
| --- | --- | --- |
| `codex plugin list` 里有很多 `not installed` | 这是 marketplace 可选项，不是当前已安装项 | 只看 `STATUS = installed, enabled` |
| 装了插件但当前会话没出现工具 | 插件通常要新开线程后才进入新会话上下文 | 新开线程或重启后再看 skills / tools |
| 装了很多插件但技能列表里没全量展示 | Codex 对初始 skills 列表有上下文预算，插件多时可能只露出部分元信息，选中 skill 后仍会读取完整 `SKILL.md` | 用 `$` / `@` 显式调用，或搜索 skill 路径和插件缓存 |
| 有插件但没有直接 MCP tool | 有些插件只提供 Skill，有些只提供 app connector，有些提供 MCP | 看技能列表、`.app.json`、`.mcp.json` 和当前工具面 |
| app connector 已安装但读不到数据 | 还需要账号授权、真实数据源和当前线程工具入口 | 做具体 case 的只读探针 |
| primary-runtime 不在 `codex plugin list` 主表中完整呈现 | Documents/PDF/Spreadsheets/Presentations 属于运行时能力，当前通过 skill 和缓存路径可见 | 运行 `python3 scripts/signalproof.py capabilities` |

## 当前已安装启用的重点插件

按 `codex plugin list` 和 `~/.codex/config.toml` 复核，当前已启用的重点能力包括：

- 基础操作：`browser`、`chrome`、`computer-use`、`record-and-replay`
- 开发和发布：`github`、`vercel`、`netlify`、`cloudflare`、`openai-developers`、`codex-security`
- 研究和资料：`hugging-face`、`readwise`、`scite`、`zotero`、`google-drive`、`notion`、`deepnote`、`airtable`、`box`
- 数据和反馈：`posthog`、`mixpanel`、`amplitude`、`sentry`、`datadog`、`brand24`、`semrush`、`similarweb`、`dovetail`
- 产物表达：`documents`、`pdf`、`spreadsheets`、`presentations`、`build-web-data-visualization`、`hyperframes`、`canva`、`figma`

## 不能直接等同的三件事

| 看到的状态 | 不能直接推导为 |
| --- | --- |
| 插件已安装 | 外部账号已授权 |
| 外部网页已登录 | Codex connector 已能读数据 |
| 插件被调用过 | 结果可进入证据链 |

SignalProof 的规则仍然是：每个 case 只调用能改变判断、减少不确定性或验收产物的插件；调用后必须在 `tool-ledger.md` 记录结果质量。

## 可迁移性

插件迁移要分层看：

| 对象 | 是否可随仓库迁移 | 说明 |
| --- | --- | --- |
| `.agents/skills/signalproof/` | 可以 | repo 内 Skill，是 SignalProof 的核心可迁移资产。 |
| `plugins/signalproof/` | 可以 | repo 内 Codex 插件源码，可以随仓库发布。 |
| `.agents/plugins/marketplace.json` | 可以 | repo 本地 marketplace 入口，可以告诉 Codex 到哪里找本插件。 |
| `templates/`、`docs/`、`vault/` | 可以 | 协议、模板和案例资产都应随仓库走。 |
| `docs/codex-plugin-lock.md` | 可以 | 插件锁定清单，记录应安装插件、角色和迁移策略。 |
| `scripts/install-codex-plugins.sh` | 可以 | 新机器重装官方插件的脚本，只保存插件名，不保存凭据。 |
| `~/.codex/config.toml` 中的插件启用项 | 不能自动迁移 | 这是本机 Codex 配置，新机器需要重新安装或启用。 |
| `~/.codex/plugins/cache` | 不建议迁移 | 这是本机缓存，路径和版本依赖本机 Codex 环境。 |
| 外部账号 OAuth、浏览器 cookie、API key | 不应迁移 | 需要用户在新机器重新授权，避免凭据泄露。 |

## 推荐迁移流程

1. 迁移或克隆 SignalProof 仓库。
2. 确认这些文件存在：
   - `.agents/skills/signalproof/SKILL.md`
   - `.agents/plugins/marketplace.json`
   - `plugins/signalproof/.codex-plugin/plugin.json`
   - `docs/codex-plugin-lock.md`
   - `scripts/install-codex-plugins.sh`
3. 在新机器先运行：

```bash
bash scripts/install-codex-plugins.sh
```

4. 再运行：

```bash
codex plugin marketplace list
codex plugin list
python3 scripts/signalproof.py capabilities
python3 scripts/signalproof.py plugin-status
```

5. 如果要使用 repo 本地 SignalProof 插件，需要让 Codex 识别 repo marketplace，再安装 `signalproof` 插件。
6. 新开一个 Codex 线程，确认技能和插件能力是否进入上下文。
7. 对外部 app connector 重新授权：Readwise、Scite、Semrush、Similarweb、Brand24、Google Drive、Notion 等不能靠仓库迁移登录态。
8. 后续插件或流程更新时，同步更新 `docs/codex-plugin-lock.md`、`scripts/install-codex-plugins.sh` 和 `vault/runs/<date>-codex-plugin-status.md`。

## 官方文档复核记录

2026-06-21 已用本地 `openai-docs` skill 拉取当前 Codex manual，状态为 `local manual was already current`。本说明采用的官方依据是：

- `Plugins`：插件可以包含 Skills、Apps 和 MCP servers；安装后要开启新线程使用；外部 app 可能在安装或首次使用时要求登录授权。
- `Agent Skills`：skills 使用渐进加载，初始列表只展示有限元信息；repo skills 位于 `.agents/skills`，适合随仓库迁移；要分发给他人时再封装成 plugin。
- `Build plugins`：repo-scoped marketplace 推荐放在 `$REPO_ROOT/.agents/plugins/marketplace.json`，插件源码可放在 `$REPO_ROOT/plugins/`；添加或修改本地插件后需要重启 Codex。
- `MCP`：插件可以携带 MCP server 配置，但外部工具和认证仍需要在 Codex 配置或授权链路中生效。

## 本仓库命令

生成当前本机插件状态快照：

```bash
python3 scripts/signalproof.py plugin-status
```

输出路径：

```text
vault/runs/<date>-codex-plugin-status.md
```

`check-goal` 已把这份快照纳入目标检查，所以后续流程文档不会只停留在口头判断。

插件锁定清单和重装脚本：

```text
docs/codex-plugin-lock.md
scripts/install-codex-plugins.sh
```

## 官方依据

- OpenAI Codex Plugins 文档：插件浏览器按 marketplace 分组，安装后需要开启新线程使用；外部 app 可能在安装或首次使用时请求授权。
- OpenAI Build Plugins 文档：插件 marketplace 可以来自本地路径、GitHub repo、HTTPS/SSH Git URL，也可以用 sparse 路径；插件通过 `.codex-plugin/plugin.json` 声明能力。
- OpenAI Agent Skills 文档：skills 是可复用工作流的作者格式，plugins 是可安装分发单元；repo skills 可以随仓库走，但本机启用、授权和缓存不自动迁移。
