---
type: research
status: completed
updated_at: 2026-06-21
gate: weak
---

# 研究

## 要回答的问题

- 这个信号背后最真实的问题是什么？
- 哪些证据足够支撑继续内部验证？
- 哪些证据缺口会阻止对外验证或产品化？
- 当前结论到底是 strong、medium、weak 还是 blocked？

## 已确认事实

- SignalProof 当前阶段是 Codex 协议 MVP。
- 真实外部反馈和发布渠道在本轮被用户明确暂时跳过。
- 研究阶段必须记录候选能力和结果质量。
- 研究准确性按 `docs/research-quality-gate.md` 判断，工具调用不等于证据合格。
- `python3 scripts/signalproof.py check-all` 已能检查 case 结构和过度声称风险。
- `python3 scripts/signalproof.py capabilities` 已能生成阶段到 Codex 插件的能力矩阵。
- `gh auth status` 显示当前活跃账号是 `sunny-kobe`，GitHub 权限可用于仓库、issue、workflow 和 gist。
- `last30days --diagnose` 显示 GitHub、ScrapeCreators、OpenRouter provider 可用；Full Disk Access 已通过复核，不再报 Safari cookie 权限错误。
- `xurl whoami` 已返回 `sunny-kobe` 的 X 账号，说明 X OAuth 已通；但 `xurl search` 返回 `CreditsDepleted`，所以 X 搜索暂缺。这个缺口不阻断 SignalProof 主流程，只在具体 case 高度依赖 X 实时讨论、早期热度或 KOL 扩散时再提醒补 credits。
- `codex plugin list` 显示推荐 A 级 marketplace 插件已安装启用，当前缺口主要是账号授权、真实数据源和 connector tool 入口。

## 调研过程

- 读取当前流程文档、case 模板和 `scripts/signalproof.py`。
- 运行 `check-all`、`check-goal` 和 `capabilities`，确认现有流程能否被脚本验证。
- 新增 `docs/research-quality-gate.md`，并把质量门接入协议文档、插件流程、case 模板和脚本检查。
- 记录授权缺口，不把未认证来源写成反证。

## 来源覆盖表

| 来源类型 | 候选能力 | 当前状态 | 结果质量 | 缺口 |
| --- | --- | --- | --- | --- |
| 公开讨论 | last30days / Reddit / HN / X / YouTube / Browser / Chrome | 部分可用 | weak / x-optional-missing | last30days 可跑；Full Disk Access 已修复；X OAuth 已通但 API credits 用尽；X 暂缺不阻断主流程；还没有针对具体机会的目标用户原话。 |
| 项目和数据 | GitHub / Hugging Face / Similarweb / Semrush | 部分可用 | medium / blocked | GitHub 已可用；Hugging Face 可作为技术信号候选；Similarweb/Semrush 需账号授权和具体竞品对象。 |
| 官方和一手资料 | 官方文档 / OpenAI Docs / PDF / Documents | 可用 | medium | OpenAI Docs 和官方文档适合技术事实；具体 case 仍需记录日期、链接和限制。 |
| 反证和替代方案 | Scite / Readwise / Zotero / 竞品文档 / GitHub issues | 部分可用 | weak / blocked | Zotero 状态可检查；Scite/Readwise 需授权或真实资料库；反证规则已固化但具体 case 仍需补证。 |

## 交叉验证

- 谁在说：当前只能确认用户本人提出流程质量诉求；还没有外部目标用户原话。
- 说什么：用户关心研究是否准确、是否确定、是否能验证，以及哪些 API/网站需要本人授权。
- 在哪里说：当前来源是本 Codex 会话、仓库文件和本机诊断输出。
- 有没有反证：有，插件安装和内部 case 通过并不能证明研究准确，也不能证明市场需求。
- 能支持什么结论：可以支持把研究准确性 gate 固化为内部流程；不能支持市场验证、产品化或 SaaS 化。

## 反证和替代方案

- 替代方案：继续用普通 Markdown 模板、Notion/Obsidian、Linear/GitHub issue 或临时 prompt，也能完成部分记录。
- 失败风险：如果 gate 只变成填表，研究会更慢但不更准。
- 低意愿风险：用户当前真正需要的是更准确的前几步，不是更完整的全流程或外部分发。
- 反证处理：质量门只卡结论许可，不强制所有插件全跑，避免流程变重。

## 证据等级

当前为 medium 内部证据、weak 外部证据。

- 内部证据 medium：脚本、模板、文档已经能表达并检查研究 gate。
- 外部证据 weak：没有真实外部用户反馈，X 搜索因 credits 用尽仍不可用。
- 暂缺但非阻断：X API credits 当前不建议单独付费，后续遇到高度依赖 X 实时讨论的 case 再提醒补；账号类调研插件 connector 仍需在具体 case 中验证是否能被 Codex 读取。

## 结论许可

当前许可：继续研究 / 低成本内部实验 / 流程内固化。

不得写成已验证需求、市场已验证、可以产品化或可以做 SaaS。

## 需要用户授权或开通

- 若需要 X/Twitter 来源：X OAuth 已通，但 API credits 暂缺；默认继续把 X 写成来源缺口，不作为阻断。只有当 X 对该 case 的判断权重明显升高时，再提醒补 credits。
- 浏览器 cookie：Full Disk Access 已复核通过。
- 若需要 Readwise、Scite、Semrush、Similarweb、Brand24：用户已网页登录，但当前 Codex 工具面未暴露直接 connector，按真实 case 做只读探针。
- 若需要产品行为数据：PostHog、Mixpanel、Amplitude、Sentry、Datadog 等要等真实产品或公开实验存在后再授权。

## 证据缺口

- 真实用户原话为空。
- 真实发布反馈为空。
- 真实 before/after 为空。
- X API credits 暂缺但非阻断。
- 研究增强类 app connector 还没有在具体 case 中完成 Codex 侧只读探针。

## 下一步补证

- 下一个真实机会 case 必须按 `docs/research-quality-gate.md` 补 1 个公开讨论来源。
- 补 1 个项目或数据指标，例如 GitHub issue/star/release 或 Hugging Face 下载/更新。
- 补 1 个官方或一手资料，并记录日期和限制。
- 补 1 个反证或替代方案。

继续内部协议验证，并把研究质量门作为下一轮 case 的前置 gate。
