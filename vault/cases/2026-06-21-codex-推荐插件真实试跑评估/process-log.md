---
type: process_log
status: completed
updated_at: 2026-06-21
gate: passed
---

# 过程日志

## 迭代 1：创建 case

命令：

```bash
python3 scripts/signalproof.py init-case "Codex 推荐插件真实试跑评估"
```

结果：

- 生成完整 case 文件。
- 初始文件还是模板状态，需要用真实插件试跑结果替换。

自检：

- 文件齐全。
- 真实反馈为空边界明确。

优化：

- 后续不能只写“待定”，必须记录真实调用、失败和阻塞。

## 迭代 2：安装 A 级推荐插件

命令：

```bash
codex plugin add <plugin>@openai-curated
codex plugin add <plugin>@openai-bundled
```

结果：

- A 级推荐 marketplace 插件安装成功：36 个。
- primary-runtime 插件不通过 marketplace 安装：`documents`、`pdf`、`spreadsheets`、`presentations`。
- 当前 `codex plugin list` 显示 178 个 marketplace 插件，36 个 installed/enabled，142 个 not installed。

自检：

- 曾出现一次解析脚本错误，把 installed 算成 0；原因是列格式解析不当。
- 已改用原始文本包含 `installed, enabled` 的方式重新统计，结果为 36。

优化：

- 后续应写脚本统一解析 `codex plugin list`，避免人工和 awk 误判。

## 迭代 3：官方口径核对

命令：

```bash
node /Users/rust/.codex/skills/.system/openai-docs/scripts/fetch-codex-manual.mjs
```

结果：

- Codex manual 本地缓存已是最新。
- 官方手册确认插件可包含 Skills、Apps、MCP servers。
- 官方手册确认安装插件后通常要开启新线程并在需要时连接外部 app。

自检：

- 不能把“安装成功”直接写成“可在当前线程调用”。

优化：

- 每个 case 的 `tool-ledger.md` 必须记录：已安装、已授权、当前线程可见、已实际调用。

## 迭代 4：验证类插件试跑

工具调用：

```text
mcp__event_stream.event_stream_status
mcp__computer_use.get_app_state(app="Codex")
mcp__node_repl.js 通过 Browser 插件 setup in-app Browser
```

结果：

- Record & Replay：成功返回 `isRecording=false`，`maxDurationSeconds=1800`。
- Computer Use：失败，返回 macOS 错误 `-1743`。
- Browser：失败，返回 `codex/sandbox-state-meta: missing field sandboxPolicy`。

自检：

- Record & Replay 可作为资产化入口，但不能在用户未准备好时启动录制。
- Browser 和 Computer Use 当前不能作为硬性验收依赖。

优化：

- 对 GUI/浏览器验收设置降级路径：文件级检查、runtime render、截图预览或人工复核。

## 迭代 5：调研类插件试跑

命令：

```bash
gh repo view sunny-kobe/SignalProof --json nameWithOwner,description,url,stargazerCount,forkCount,isPrivate
gh issue list --repo sunny-kobe/SignalProof --limit 5 --json number,title,state,updatedAt
curl -sS "https://datasets-server.huggingface.co/is-valid?dataset=stanfordnlp/imdb"
curl -sS "https://datasets-server.huggingface.co/splits?dataset=stanfordnlp/imdb"
curl -sS "https://huggingface.co/api/models/openai/gpt-oss-20b"
python3 /Users/rust/.codex/plugins/cache/openai-curated/zotero/43313cc9/skills/zotero/scripts/zotero.py status --json
```

结果：

- GitHub：读取 `sunny-kobe/SignalProof` 成功；issues 为空。
- Hugging Face：公开 model API 和 Dataset Viewer API 成功；`hf` CLI 缺失。
- Zotero：本地 API 未运行，`127.0.0.1:23119` connection refused。
- Readwise、Scite、Semrush、Similarweb、Brand24 等：当前线程未暴露 app connector 工具，只能记录 manifest 和阻塞状态。

自检：

- 公开只读成功可以作为弱到中等研究证据。
- auth/tool 缺失不能当作反证或 0 结果。

优化：

- 账号类调研插件应单独做授权专项 case，不和普通公开调研混在一起。

## 迭代 6：反馈/运行态插件试跑

命令：

```bash
for v in SENTRY_AUTH_TOKEN POSTHOG_API_KEY MIXPANEL_TOKEN AMPLITUDE_API_KEY DATADOG_API_KEY SEMRUSH_API_KEY; do ...; done
python3 /Users/rust/.codex/plugins/cache/openai-curated/sentry/43313cc9/skills/sentry/scripts/sentry_api.py --help
```

结果：

- Sentry helper 可运行，但 `SENTRY_AUTH_TOKEN` 缺失。
- PostHog、Mixpanel、Amplitude、Datadog、Semrush 相关环境变量均缺失。
- 当前线程没有这些 app connector 的可调用工具。

自检：

- 这些插件只有在真实产品、真实埋点、真实日志存在时才会明显提升。

优化：

- 反馈阶段需要先判断是否已有数据源；没有数据源时不要调用产品分析插件。

## 迭代 7：产物类插件试跑

命令：

```bash
ln -sfn /Users/rust/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules vault/assets/plugin-test/workbook/node_modules
/Users/rust/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node vault/assets/plugin-test/workbook/build-plugin-eval-workbook.mjs
```

结果：

- 生成 `vault/assets/plugin-test/workbook/outputs/plugin-eval-workbook.xlsx`。
- 生成 `vault/assets/plugin-test/workbook/outputs/plugin-eval-workbook-preview.png`。
- 生成 `vault/assets/plugin-test/workbook/outputs/inspect.ndjson`。
- 生成 `vault/assets/plugin-test/visual/plugin-eval-summary.html`。

自检：

- 工作簿预览图已人工查看，可读，无明显空白或错位。
- HTML 文件已生成，但 Browser 插件验收失败，因此只算文件级通过。

优化：

- Spreadsheets/Data Visualization 可以作为默认资产化插件。
- Documents/PDF/Presentations 已在后续迭代补跑；最终策略是按正式交付场景启用，避免每个 case 都生成全套文件。

## 迭代 7b：多 case 补跑调研与产物插件

命令：

```bash
python3.14 /Users/rust/.agents/skills/last30days/scripts/last30days.py "AI coding repo context loss" --emit=compact --auto-resolve --save-dir="/Users/rust/Documents/SignalProof/vault/cases/2026-06-21-插件试跑-case-1-ai-coding-repo-context-loss-调研验证/evidence" --save-suffix=plugintrial
python3 vault/assets/plugin-test/document/build-plugin-eval-docx.py
python3 vault/assets/plugin-test/pdf/build-plugin-eval-pdf.py
/Users/rust/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node vault/assets/plugin-test/presentation/build-plugin-eval-deck.mjs
```

结果：

- `last30days` 成功生成 13 条证据，覆盖 GitHub、Reddit、YouTube，但 X/HN/YouTube 评论缺失。
- Documents 生成 DOCX 简报。
- PDF 生成 PDF 简报并完成文本抽取。
- Presentations 生成 PPTX、slide PNG、montage、inspect。
- HyperFrames HTML lint `ok=true`，但缺 `ffmpeg` 未导出 mp4。

自检：

- `last30days` 是调研初筛增强，不是市场验证。
- DOCX/PDF/PPTX/HyperFrames 证明产物能力，但依赖缺口必须写清。

优化：

- 调研类 case 默认候选 `last30days`，但来源不足时 gate 写 `weak`。
- 产物类插件按场景启用，避免每个 case 都生成全套文件。

## 迭代 8：写入 case 文档

修改文件：

- `signal.md`
- `research.md`
- `validation.md`
- `artifact.md`
- `decision.md`
- `flow-review.md`
- `tool-ledger.md`
- `process-log.md`
- `report.md`

结果：

- 从模板记录改为真实插件试跑记录。
- 每个插件组都有默认用、条件用或暂不默认的判断。

自检：

- 没有把真实反馈为空写成市场验证。
- 没有把插件已安装写成插件已有效。

优化：

- 下一步运行 `python3 scripts/signalproof.py check-all` 和 `python3 scripts/signalproof.py export-all`。

## 迭代 9：新线程插件暴露探针

工具：

```text
codex_app.create_thread
codex_app.read_thread
```

历史探针线程：

```text
019ee5fc-4bb9-74e0-99d0-0555618313fc
```

重启后复核线程：

```text
019ee803-b71e-7b01-a7b6-1608b91e9916
```

重启后证据文件：

```text
vault/cases/2026-06-21-codex-推荐插件真实试跑评估/evidence/restart-thread-plugin-deepcheck-receipt.md
```

任务：

- 在新线程里运行 `codex plugin list`。
- 检查安装后的插件 Skills 是否可见。
- 用 `tool_search` 搜索 app connector 工具是否暴露。
- 只读，不改仓库文件，不登录，不写外部服务。

结果：

- 重启后新线程确认 marketplace 总数 178，installed/enabled 36，not installed 142。
- A 级推荐 marketplace 插件缺失为 0。
- primary-runtime 的 `documents`、`pdf`、`spreadsheets`、`presentations` 可见。
- 新线程初始 Skills 列表能看到更多插件能力，包括 browser、chrome、computer-use、record-and-replay、github、hugging-face、posthog、sentry、zotero、spreadsheets、documents、presentations、build-web-data-visualization、hyperframes、codex-security、openai-developers、notion、google-drive、airtable、figma、canva。
- 新线程没有看到 readwise、scite、semrush、similarweb、brand24、mixpanel、amplitude、datadog、dovetail、mem 的初始 Skills。
- `tool_search` 搜索 app connector 后仍只返回 Codex app 线程管理类工具，没有暴露 PostHog/Mixpanel/Semrush 等专用工具。
- Record & Replay 的 `event_stream_status` 成功返回 `isRecording=false`。
- Computer Use 的 `list_apps` 成功返回本机 app 列表；但这不覆盖历史 `get_app_state(Codex)` 的 macOS 权限失败。

自检：

- 新线程证明“安装后新线程 Skills 更完整”成立。
- 但 app connector 仍不能算已授权或已实际读取真实数据。
- 安装不等于授权，入口可响应不等于证据合格。

优化：

- 后续账号类插件必须单独授权后再跑，不再把它们混入默认 case。

## 迭代 10：整合进个人工作流文档

修改文件：

- `docs/current-flow.md`
- `docs/codex-plugin-flow.md`
- `docs/codex-capability-map.md`
- `vault/cases/2026-06-21-codex-推荐插件真实试跑评估/evidence/restart-thread-plugin-deepcheck-receipt.md`

结果：

- 把“Codex 自带插件接入”扩展为“推荐插件分层接入”。
- 调研类插件分成默认候选、授权后候选和暂不纳入。
- 验证类插件分成脚本/文件级默认、Browser/Computer Use 条件验收、Sentry/PostHog/Datadog 等真实运行态数据源。
- 明确写入重启后线程 `019ee803-b71e-7b01-a7b6-1608b91e9916` 的只读深测回执。

自检：

- 没有把外部 SaaS connector 写成已授权。
- 没有把 Browser/Computer Use 历史失败写掉；只修正为“入口可响应”和“具体目标可能失败”两个层次。

优化：

- 后续每个 case 开始时，先从阶段表里选最小必要插件，再写入 `tool-ledger.md`。
