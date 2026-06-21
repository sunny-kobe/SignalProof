---
type: research
status: completed
updated_at: 2026-06-21
gate: medium
---

# 研究

## 要回答的问题

- 最近的自审报告是否准确，还是只是写得像完成？
- 哪些结论已经有脚本、模板或文档支撑？
- 哪些仍只是建议或待验证假设？
- 本轮最值得落地的机制改进是什么？

## 已确认事实

- SignalProof 当前阶段是 Codex 协议 MVP。
- 本轮是内部流程审计，不做真实外部反馈和发布渠道。
- 研究阶段必须记录候选能力和结果质量。
- 研究准确性按 `docs/research-quality-gate.md` 判断，工具调用不等于证据合格。
- 最近自审报告已经把 `check-plugin-drift` 和 `check-case <case-slug> --strict` 写入脚本、AGENTS、repo skill 和质量门文档；这不是纯复盘。
- 复核后发现新增 strict 仍有一个漏洞：如果 case 文件保留 `待补`、`待定` 或未替换模板变量，旧检查不一定把它视为未完成。
- 复核后发现另一个流程缺口：内部流程审计 case 默认套用外部机会验证模板，容易把内部审计写成市场研究。

## 调研过程

- 读取 `AGENTS.md`、repo skill、协议文档、研究质量门和插件流程文档。
- 复核最近自审 case 的报告、流程自检、工具账本和决策。
- 用 `git diff`、脚本输出和 case 内容判断哪些改进已经落地，哪些仍只是建议。

## 来源覆盖表

| 来源类型 | 候选能力 | 当前状态 | 结果质量 | 缺口 |
| --- | --- | --- | --- | --- |
| 公开讨论 | 当前用户任务和历史记忆中的 SignalProof 口径 | 部分覆盖 | weak | 只能支持本轮内部审计，不支持市场判断。 |
| 项目和数据 | 仓库文件、模板、脚本、case、报告索引、runs 快照 | 已覆盖 | strong | 足以判断本地工作流机制是否改变。 |
| 官方和一手资料 | `AGENTS.md`、`.agents/skills/signalproof/SKILL.md`、`docs/protocol.md`、`docs/research-quality-gate.md`、`docs/codex-plugin-flow.md` | 已覆盖 | strong | 本轮事实来源限定在仓库和用户要求。 |
| 反证和替代方案 | 最近自审 report、`check-all` warning、未完成占位标记、connector 授权缺口 | 已覆盖 | medium | 证明仍需脚本 gate，而不是只写复盘。 |

## 交叉验证

- 谁在说：用户要求二次审视并实际更新工作流；仓库规则要求本地优先和中文记录。
- 说什么：最近自审 case 已有部分脚本改进，但仍可能让未完成占位内容通过严格检查。
- 在哪里说：当前任务、`AGENTS.md`、repo skill、`docs/`、`scripts/signalproof.py`、`vault/cases/2026-06-21-signalproof-当前工作流自审/`。
- 有没有反证：有，原报告已落地 `check-plugin-drift` 和 `check-case --strict`，不能说它只是空报告；但它没有处理模板占位和内部审计 case 类型。
- 能支持什么结论：支持继续本地工作流优化；不支持市场验证。

## 反证和替代方案

- 原报告不是纯形式主义，因为已有脚本命令进入 `scripts/signalproof.py`。
- 但如果 `check-case --strict` 只看 TODO 和研究质量门术语，就可能漏掉 `待补`、`待定`、未替换模板变量等半成品痕迹。
- 原报告把“下一步优先做内部审计类模板优化”写成建议，但当时没有真正落入 `init-case` 或模板机制。
- 普通 Markdown 复盘也能发现问题，但不能稳定阻止下一次误报完成。

## 证据等级

当前证据等级：medium。

- strong：脚本 diff、模板 diff、AGENTS 和 repo skill 的规则变更，可以证明本地机制已经改变。
- medium：最近自审 case 的结论整体可靠，但它对模板占位、内部审计类型和 connector 探针仍只是建议。
- weak：外部用户反馈、真实市场反馈、外部 connector 可读性和 X 侧实时讨论。

## 结论许可

当前许可：继续本地流程优化，并把高价值缺口落到脚本、模板、文档或 skill。不得写成市场验证、插件全部授权成功或 SaaS 可行。

## 需要用户授权或开通

- 若需要 X/Twitter 来源：先把 X API credits 记为暂缺但非阻断；只有 case 高度依赖 X 实时讨论、早期热度或 KOL 扩散时再提醒补 credits。
- 若需要浏览器 cookie：先运行 `python3 scripts/signalproof.py diagnose`，根据结果判断是否需要用户处理 Full Disk Access。
- 若需要 Readwise、Scite、Semrush、Similarweb、Brand24：按真实 case 做只读探针，不默认全开。

## 证据缺口

- 真实用户原话为空。
- 真实发布反馈为空。
- 真实 before/after 为空。

## 下一步补证

- 对新增占位检查运行本次 case 严格检查。
- 更新模板和协议说明，避免内部审计默认套外部机会口径。
- 保留真实 feedback 为空的边界。

## 本轮研究判断

原报告基本准确，但不完整。

准确部分：

- `passed-with-gaps` 判断准确。
- 插件安装、工具暴露、账号授权、证据质量需要分层，这个判断准确。
- 真实反馈为空，不能写成市场验证，这个边界准确。
- `check-plugin-drift` 和 `check-case --strict` 已经进入脚本，不是只写在报告里。

不足部分：

- 原报告仍偏向“发现缺口后建议下一步”，没有把内部审计 case 类型落到 `init-case`。
- 原 strict 检查没有覆盖 `待补`、`待定` 和未替换模板变量，可能让新 case 看似完成。
- 原模板会让内部审计和外部机会验证共用一套默认话术，容易混淆证据许可。

本轮选择的高价值改进：

- 给 `check-case --strict` 增加未完成占位标记检查。
- 给 `init-case` 增加 `--case-type internal-audit`。
- 让模板按 case 类型渲染信号、研究、工具账本、验证、反馈、决策和报告边界。
- 把新规则写入 `AGENTS.md`、repo skill、`docs/protocol.md` 和 `docs/research-quality-gate.md`。
