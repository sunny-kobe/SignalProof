# Codex 插件状态快照

生成日期：2026-06-23

## 结论

- `~/.codex/config.toml` 中启用项：7 个。
- `codex plugin list` 中已安装启用的 marketplace 插件：3 个。
- `codex plugin list` 中未安装的 marketplace 插件：175 个。
- primary-runtime 配置启用项：3 个。
- primary-runtime 本机缓存可用能力：4 个，通常包括 Documents / PDF / Spreadsheets / Presentations。
- SignalProof 本地 repo marketplace：存在。
- repo 插件锁定清单：存在。
- repo 插件重装脚本：存在，脚本记录 36 个插件。

## 怎么看是否安装

- 以 `codex plugin list` 的 `STATUS` 列为准：只有 `installed, enabled` 才是已安装启用。
- `not installed` 只是 marketplace 里可选但没有安装的插件，会和已安装插件一起显示。
- `~/.codex/config.toml` 里的 `[plugins."..."] enabled = true` 是本机启用状态；它不是 repo 内容，换机器不会自动跟着仓库走。
- 插件安装后通常要开启新线程才会进入新会话的技能/工具上下文。
- skills 初始列表有上下文预算，插件多时界面可能不展示全部 skills；选中或显式调用后仍会读取完整 `SKILL.md`。
- app connector、MCP server 和外部账号授权是独立层；插件已安装不等于 connector 已能读取真实数据。

## marketplace

| 名称 | 路径 |
| --- | --- |
| `openai-bundled` | `/Users/rust/.codex/.tmp/bundled-marketplaces/openai-bundled` |
| `openai-curated` | `/Users/rust/.codex/.tmp/plugins` |

## 已安装启用的 marketplace 插件

- `browser@openai-bundled`
- `chrome@openai-bundled`
- `computer-use@openai-bundled`

## repo 重装脚本记录的插件

这些插件由 `scripts/install-codex-plugins.sh` 记录，用于换电脑后重装。脚本只保存插件名，不保存 OAuth、cookie、API key。

- `airtable@openai-curated`：not installed or not visible in current marketplace list
- `amplitude@openai-curated`：not installed or not visible in current marketplace list
- `box@openai-curated`：not installed or not visible in current marketplace list
- `brand24@openai-curated`：not installed or not visible in current marketplace list
- `browser@openai-bundled`：installed, enabled
- `build-web-data-visualization@openai-curated`：not installed or not visible in current marketplace list
- `canva@openai-curated`：not installed or not visible in current marketplace list
- `chrome@openai-bundled`：installed, enabled
- `cloudflare@openai-curated`：not installed or not visible in current marketplace list
- `codex-security@openai-curated`：not installed or not visible in current marketplace list
- `computer-use@openai-bundled`：installed, enabled
- `datadog@openai-curated`：not installed or not visible in current marketplace list
- `deepnote@openai-curated`：not installed or not visible in current marketplace list
- `dovetail@openai-curated`：not installed or not visible in current marketplace list
- `figma@openai-curated`：not installed or not visible in current marketplace list
- `github@openai-curated`：not installed or not visible in current marketplace list
- `google-drive@openai-curated`：not installed or not visible in current marketplace list
- `hugging-face@openai-curated`：not installed or not visible in current marketplace list
- `hyperframes@openai-curated`：not installed or not visible in current marketplace list
- `jam@openai-curated`：not installed or not visible in current marketplace list
- `linear@openai-curated`：not installed or not visible in current marketplace list
- `mem@openai-curated`：not installed or not visible in current marketplace list
- `mixpanel@openai-curated`：not installed or not visible in current marketplace list
- `netlify@openai-curated`：not installed or not visible in current marketplace list
- `notion@openai-curated`：not installed or not visible in current marketplace list
- `openai-developers@openai-curated`：not installed or not visible in current marketplace list
- `posthog@openai-curated`：not installed or not visible in current marketplace list
- `readwise@openai-curated`：not installed or not visible in current marketplace list
- `record-and-replay@openai-bundled`：not installed or not visible in current marketplace list
- `scite@openai-curated`：not installed or not visible in current marketplace list
- `semrush@openai-curated`：not installed or not visible in current marketplace list
- `sentry@openai-curated`：not installed or not visible in current marketplace list
- `similarweb@openai-curated`：not installed or not visible in current marketplace list
- `superpowers@openai-curated`：not installed or not visible in current marketplace list
- `vercel@openai-curated`：not installed or not visible in current marketplace list
- `zotero@openai-curated`：not installed or not visible in current marketplace list

## primary-runtime / 配置启用项

- `documents@openai-primary-runtime`
- `presentations@openai-primary-runtime`
- `spreadsheets@openai-primary-runtime`

## primary-runtime / 本机缓存可用能力

- `documents`
- `pdf`
- `presentations`
- `spreadsheets`

## 可迁移性判断

| 对象 | 能否跟仓库迁移 | 说明 |
| --- | --- | --- |
| `plugins/signalproof/` | 可以 | repo 内本地插件源码，应纳入版本控制。 |
| `.agents/plugins/marketplace.json` | 可以 | repo marketplace 入口，应纳入版本控制。 |
| `.agents/skills/signalproof/` | 可以 | repo skill，可随仓库迁移。 |
| `vault/` 与 `templates/` | 可以 | SignalProof 的主要事实资产。 |
| `docs/codex-plugin-lock.md` | 可以 | 插件锁定清单，记录应该安装哪些插件和迁移策略。 |
| `scripts/install-codex-plugins.sh` | 可以 | 新机器重装官方插件的脚本，只保存插件名。 |
| `~/.codex/config.toml` 的插件启用项 | 不能自动随 repo 迁移 | 新机器需要重新安装或导入对应 marketplace，再启用插件。 |
| 官方/curated 插件缓存 | 不建议直接迁移 | 缓存路径和版本与本机 Codex 相关，应该用 `codex plugin add` 或插件目录重新安装。 |
| 外部账号 OAuth / 浏览器登录态 / API key | 不应随 repo 迁移 | 需要在新机器按账号重新授权，避免泄露凭据。 |

## 迁移时最小清单

1. 克隆或复制 SignalProof 仓库。
2. 确认 `.agents/plugins/marketplace.json` 和 `plugins/signalproof/.codex-plugin/plugin.json` 存在。
3. 运行 `bash scripts/install-codex-plugins.sh` 重装官方插件。
4. 在新机器运行 `codex plugin marketplace list`，确认是否能看到需要的 marketplace。
5. 新开 Codex 线程，再检查技能和工具是否出现。
6. 运行 `python3 scripts/signalproof.py capabilities` 和 `python3 scripts/signalproof.py plugin-status` 复核。
7. 对 Readwise、Scite、Semrush、Similarweb、Brand24、Google Drive、Notion 等外部 app connector 重新登录授权。

## 官方文档复核

- OpenAI Codex Plugins 文档：插件可以包含 Skills、Apps 和 MCP servers；安装后开启新线程使用；外部 app 可能在安装或首次使用时要求授权。
- OpenAI Agent Skills 文档：skills 使用渐进加载，初始列表只展示有限元信息；repo skills 位于 `.agents/skills`，适合随仓库迁移。
- OpenAI Build Plugins 文档：repo marketplace 可放在 `$REPO_ROOT/.agents/plugins/marketplace.json`，插件源码可放在 `$REPO_ROOT/plugins/`；添加或修改本地插件后需要重启 Codex。
- OpenAI MCP 文档：插件可以携带 MCP server 配置，但外部工具、认证和 tool policy 仍需要单独生效。
- SignalProof 本地规则：插件或流程更新时，同步更新 `docs/codex-plugin-lock.md`、`scripts/install-codex-plugins.sh` 和本状态快照。

## 官方依据

- OpenAI Codex Plugins 文档：插件浏览器按 marketplace 分组；安装后新开线程使用；外部 app 可能在安装或首次使用时要求授权。
- OpenAI Build Plugins 文档：可用 `codex plugin marketplace add` 添加本地路径、GitHub repo、Git URL 或 sparse marketplace。
