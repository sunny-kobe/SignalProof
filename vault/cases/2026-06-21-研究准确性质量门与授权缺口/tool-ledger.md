---
type: tool_ledger
status: completed
updated_at: 2026-06-21
gate: passed
---

# 工具账本

## 候选能力账本

| 能力 | 是否相关 | 是否使用 | 结果质量 | 说明 | 下次动作 |
| --- | --- | --- | --- | --- | --- |
| Skill: signalproof | 是 | 是 | strong | repo 级 skill 提供本地流程规则，和 AGENTS.md 一致。 | 保留。 |
| Skill: personal-opportunity-os | 是 | 是 | strong | 提供长期方向和流程边界：本地优先、中文可读、不跳 SaaS。 | 保留为上层方法论。 |
| GitHub / gh auth | 是 | 是 | strong | `gh auth status` 显示当前活跃账号是 `sunny-kobe`，权限覆盖 repo/workflow/gist/read:org。 | 可用于开源信号、issue、发布和反馈查询。 |
| Skill: last30days | 是 | 是 | medium / x-optional-missing | `--diagnose` 返回可用来源和 OpenRouter provider；Full Disk Access 已修复；`xurl whoami` 成功，但 `xurl search` 返回 `CreditsDepleted`。X 当前只标记为暂缺，不作为必备付费项。 | 先用 HN / Reddit / YouTube / GitHub / 官方资料补证；只有 case 高度依赖 X 实时讨论时再提醒补 credits。 |
| Browser | 视产物而定 | 否 | historical-risk | 历史真实调用曾失败：`codex/sandbox-state-meta: missing field sandboxPolicy`。这不是当前必然失败结论。 | 有网页或报告预览目标时重新做只读探针，不作为默认硬 gate。 |
| Chrome | 视登录态而定 | 是 | medium / connector-unverified | 已做只读复查：Codex Chrome 插件层只枚举到 GitHub 标签页；本机 Chrome 窗口清单能看到 X Premium 和 Readwise Quick，但未看到 Scite、Semrush、Similarweb、Brand24 当前打开页。 | 具体 case 需要登录态页面时再打开目标页并做只读探针。 |
| Computer Use | 视 GUI 而定 | 是 | medium / conditional | `list_apps` 可响应；读取具体 App 状态可能受 macOS 权限影响。 | 修复权限或换目标 App 后再做 GUI 验收。 |
| Record & Replay | 视流程录制而定 | 否 | medium | 入口可响应，适合未来把用户操作录成 skill。 | 等分发/反馈流程稳定后再录。 |
| Plugin | 是 | 是 | medium | 推荐 marketplace 插件已安装启用，A 级推荐缺失为 0。 | 按 case 选择，不默认全跑。 |
| MCP | 中 | 否 | weak | 当前研究 gate 不需要新增 MCP 绑定。 | 等具体 API 或资料库需要时再接。 |
| Hooks | 中 | 否 | weak | 可用于未来强制研究 gate。 | 先用 `check-goal` 检查资产存在。 |
| Automation | 低 | 否 | weak | 外部反馈暂停，暂不设置 72h 复查。 | 分发渠道完成后再启用。 |

## 研究准确性账本

按 `docs/research-quality-gate.md` 记录研究阶段是否真的能支持结论，必须覆盖来源覆盖、交叉验证、反证、证据等级、结论许可和用户授权缺口：

| 检查项 | 是否覆盖 | 证据等级 | 说明 | 下一步 |
| --- | --- | --- | --- | --- |
| 公开讨论 | 部分覆盖 | weak / x-optional-missing | last30days 能诊断；但当前 case 未查具体外部人群，X 搜索因 credits 用尽不可用。X 暂缺不阻断主流程。 | 真实机会 case 优先补 last30days / HN / Reddit / YouTube / GitHub；必要时再提醒补 X credits。 |
| 项目和数据 | 部分覆盖 | medium | GitHub 可用；本 case 是流程质量，不需要竞品流量。 | 真实机会 case 补 GitHub / Hugging Face / Similarweb / Semrush。 |
| 官方和一手资料 | 覆盖 | medium | 仓库文档、AGENTS.md、脚本和 Codex 插件能力矩阵是当前流程的一手资料。 | 技术事实 case 继续补官方文档。 |
| 反证和替代方案 | 覆盖 | medium | 反证是“插件安装不等于研究准确”“内部闭环不等于市场验证”。 | 真实机会 case 补 Scite / Readwise / Zotero / 竞品文档。 |
| 结论许可 | 覆盖 | medium | 当前只允许流程内固化和低成本内部实验。 | 证据未升到 strong 前不写产品化。 |
| 用户授权 | 覆盖 | partial | Full Disk Access 和 X OAuth 已通过；X search 因 credits 暂缺但非阻断；账号类调研插件已网页登录但未完成 Codex connector 探针。 | 按具体 case 验证 connector；X 仅在高依赖 case 再提醒补。 |

## 阶段能力计划

运行：

```bash
python3 scripts/signalproof.py capabilities
```

然后把本 case 各阶段真正考虑过的 Codex 自带插件记录到这里：

| 阶段 | 候选 Codex 插件 | 是否使用 | 结果质量 | 跳过或失败原因 | 下一步 |
| --- | --- | --- | --- | --- | --- |
| signal | GitHub / Browser / Chrome / Record & Replay | 是 | medium | 信号来自用户会话和本地 repo，不需要网页登录态。 | 保留边界。 |
| research | GitHub / last30days / OpenAI Docs / Hugging Face / Readwise / Scite / Semrush / Similarweb / Brand24 / Zotero / Browser / Chrome / Documents / PDF / Spreadsheets / Data Visualization | 部分使用 | medium / x-optional-missing / connector-unverified | GitHub、last30days 诊断、本地文档和脚本已用；X search credits 用尽但暂不作为付费必备项；账号类网页登录已完成但当前工具面无直连 connector；Chrome 只读复查未证明研究增强 connector 可用。 | 真实机会 case 按质量门补跑；高依赖 X 时再提醒补 credits。 |
| debate | Browser / Chrome / Documents / PDF / Scite / Readwise / Zotero | 部分使用 | medium | 本 case 反证来自流程本身，不依赖论文或长文档。 | 真实机会 case 加反证来源。 |
| validation | Browser / Computer Use / Documents / PDF / Spreadsheets / Presentations | 部分使用 | strong | 主要用脚本自检；GUI 和文档产物不相关。 | 跑 check-all / check-goal / export-all。 |
| artifact | Documents / PDF / Spreadsheets / Presentations / HyperFrames / Data Visualization | 否 | weak | 本次产物是 Markdown 和脚本规则，不需要额外格式。 | 有正式资料包再启用。 |
| publication | Browser / Chrome | 否 | weak | 外部反馈和发布触达已暂停。 | 分发系统完成后再启用。 |
| feedback | Chrome / Browser / Spreadsheets / Record & Replay | 否 | weak | 真实反馈为空。 | 等用户恢复外部反馈。 |
| asset | Documents / PDF / Spreadsheets / Presentations / Record & Replay / Browser | 部分使用 | medium | 资产是中文文档、模板和脚本检查。 | 稳定后可录制成 skill。 |
| flow-review | Browser / Computer Use / Documents / PDF / Spreadsheets / Presentations | 是 | strong | 使用脚本和文件级检查。 | 保持为硬 gate。 |

## 能力结论

本 case 的工具使用足够支持内部协议验证和研究 gate 固化，但不能支持外部市场判断。
