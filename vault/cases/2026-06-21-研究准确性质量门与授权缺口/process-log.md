---
type: process_log
status: completed
updated_at: 2026-06-21
gate: passed
---

# 过程日志

## 迭代 1

命令：

```bash
python3 scripts/signalproof.py init-case "研究准确性质量门与授权缺口"
```

结果：

- 生成完整 case 文件。
- 新增 `docs/research-quality-gate.md`。
- 更新 `docs/protocol.md`、`docs/codex-plugin-flow.md`、`docs/current-flow.md`、`docs/codex-capability-map.md`。
- 更新 `templates/case/research.md`、`templates/case/tool-ledger.md`、`templates/case/flow-review.md`。
- 更新 `scripts/signalproof.py`，新增研究 gate 术语检查和资产检查。

自检：

- 文件齐全。
- 真实反馈为空边界明确。

优化：

- 后续把重复检查脚本化。

## 迭代 2

命令：

```bash
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py check-goal --min-cases 5
```

结果：

- `check-all` 初次通过，但旧 case 出现研究 gate warning。
- `check-goal` 初次失败，指出模板缺少来源覆盖、交叉验证和用户授权等术语。

自检：

- 检查 `tool-ledger.md` 是否记录 Skill / Plugin / MCP / Browser / Computer Use / last30days。
- 检查研究 gate 文档和模板是否覆盖来源覆盖、交叉验证、反证、证据等级、结论许可、用户授权。

优化：

- 修正模板措辞，让 `check-goal` 可以卡住研究 gate 资产缺失。

## 迭代 3

命令：

```bash
python3 scripts/signalproof.py capabilities
```

结果：

- 刷新 Codex 能力矩阵。
- research 阶段已经显示 `research-quality-gate` 和结论许可。

自检：

- 该能力矩阵仍是候选能力说明，不代表账号类插件已授权。

优化：

- 下一轮真实机会 case 才按质量门补外部证据。

## 迭代 4

命令：

```bash
codex plugin marketplace list
codex plugin list
python3 scripts/signalproof.py plugin-status
python3 scripts/signalproof.py capabilities
```

结果：

- 新增 `docs/codex-plugin-status-and-migration.md`。
- `plugin-status` 生成 `vault/runs/2026-06-21-codex-plugin-status.md`。
- 确认 `codex plugin list` 中 marketplace 插件合计 178 个，其中 36 个已安装启用、142 个未安装。
- 确认 `~/.codex/config.toml` 启用项为 40 个；primary-runtime 配置启用项 3 个，本机缓存可见 runtime 能力 4 个。
- 明确 SignalProof 可迁移部分：repo skill、repo plugin、repo marketplace、模板、文档和 vault。
- 明确不可随仓库迁移部分：外部账号 OAuth、浏览器登录态、API key、官方插件缓存和本机 Codex 启用配置。

自检：

- 清理旧口径：X API credits 不再写成必做；Browser 历史失败不再写成当前必然失败。
- `plugin-status` 已加入 `check-goal` 的目标检查。

优化：

- 以后回答“插件是否装好”时，先跑 `python3 scripts/signalproof.py plugin-status`，不要凭 UI 感觉判断。

## 迭代 5

命令：

```bash
node /Users/rust/.codex/skills/.system/openai-docs/scripts/fetch-codex-manual.mjs
python3 scripts/signalproof.py plugin-status
python3 scripts/signalproof.py capabilities
```

结果：

- OpenAI Codex manual 状态为 `local manual was already current`。
- 补充官方依据：Plugins 可包含 Skills / Apps / MCP；安装后新线程使用；外部 app 可能安装或首次使用时授权。
- 补充 skills 渐进加载口径：初始 skills 列表有上下文预算，界面看不到全量 skill 不等于插件没装。
- 补充可迁移口径：repo skill、repo marketplace 和 repo plugin 源码可以随仓库迁移；本机 `config.toml`、插件缓存、OAuth、cookie、API key 不能自动迁移。

自检：

- 当前插件状态仍为 marketplace 已安装启用 36 个、未安装 142 个，`~/.codex/config.toml` 启用项 40 个。
- 这些结论来自当前命令输出和官方手册，不依赖聊天记忆。

优化：

- `plugin-status` 生成的快照也记录 skills 上下文预算、app connector/MCP/授权分层，防止后续又把“界面看不到”误判成“未安装”。

## 迭代 6

命令：

```bash
codex plugin --help
python3 scripts/signalproof.py plugin-status
python3 scripts/signalproof.py check-goal --min-cases 5
```

结果：

- 新增 `docs/codex-plugin-lock.md`，记录 SignalProof 推荐插件锁定清单、迁移策略和后续同步规则。
- 新增 `scripts/install-codex-plugins.sh`，用于换电脑后按清单重装 36 个官方 marketplace 插件。
- `plugin-status` 已能读取重装脚本并对照当前 installed/enabled 状态；本轮脚本 36 个插件与当前 36 个 installed/enabled 插件一致。
- `check-goal` 已纳入插件锁定清单和重装脚本检查，避免后续插件更新时只改口头说明。

自检：

- 重装脚本只保存插件名，不保存 OAuth、cookie、API key。
- `docs/codex-plugin-lock.md` 已补研究质量门边界：来源覆盖、交叉验证、证据等级、结论许可和用户授权缺口仍需按具体 case 判断。

优化：

- 后续新增/移除插件，或某个插件从“条件触发”变成“默认候选”时，必须同步更新 `docs/codex-plugin-lock.md`、`scripts/install-codex-plugins.sh`、`docs/codex-plugin-status-and-migration.md` 和当天 `plugin-status` 快照。
