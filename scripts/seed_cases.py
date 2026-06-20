#!/usr/bin/env python3
"""生成五个差异化的 SignalProof 协议案例。

这些 seed 数据只服务本地可审计的内部协议验证。真实外部反馈和发布渠道在本轮
故意保持为空，避免把内部跑通误写成市场验证。
"""

from __future__ import annotations

from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "vault" / "cases"
RUNS = ROOT / "vault" / "runs"


TODAY = date.today().isoformat()


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


CASES_DATA = {
    "2026-06-20-ai-coding-repo-context-loss": {
        "title": "AI 编码仓库上下文丢失",
        "signal": "AI 编码用户经常丢失仓库局部约定，导致 agent 写出看起来合理、但违反本地契约的代码。",
        "research": "一次真实的 `last30days --days=3 --quick --auto-resolve` 只找到 2 条 Reddit 讨论，X、YouTube、HN、GitHub、Polymarket 都没有有效命中。这个结果可以作为弱证据和工具质量样本，不能作为市场证明。",
        "debate": "这是一个很贴合用户个人 AI 编码经验的工作流切口。最强反对意见是：公开讨论证据很薄，可能只是小圈层工作流话题，不代表广泛买方意图。",
        "thesis": "继续作为内部证明案例和可复用检查清单方向推进。没有真实前后对比任务前，不声称需求成立、不产品化、不销售。",
        "validation": "通过迁移 legacy run、保留仓库上下文审计资产、检查报告导出，并把弱 last30days 结果保存为研究证据来验证。",
        "artifact": "legacy 跑法已迁移到 `legacy/`；新的正式 case 已沉淀在 `vault/cases/2026-06-20-ai-coding-repo-context-loss/`。",
        "asset": "可复用资产：仓库上下文审计检查清单、AGENTS 模板、CLAUDE 模板、72 小时验证 SOP，以及一个弱证据研究样例。",
        "optimization": "下一轮应使用更窄查询，例如 `repo AGENTS.md context drift`、`Claude Code project instructions`、`AI coding agent verifiable workflow`，并把窗口扩到 `--days=7`。",
        "tool_quality": "`last30days`：弱但有用；Codex 官方手册：中；本地脚本：强；Browser：待验证报告预览；Computer Use：当前没有直接工具暴露。",
        "assumed": True,
    },
    "2026-06-20-codex-subthread-output-missing": {
        "title": "Codex 子线程完成但输出文件缺失",
        "signal": "Codex 子线程可能显示 completed，但委派任务要求的输出文件并没有真正生成。",
        "research": "证据来自上一轮 SignalProof 流程：一个 Day 2 审计子线程完成后没有创建 `subtasks/day2-loop-audit.md`，源线程只能接管修复。",
        "debate": "这本身不是市场机会，但它是高价值的协议可靠性门。反对意见是：这可能只是一次偶发系统失败。",
        "thesis": "继续作为内部协议质量案例。所有子线程 completion receipt 都必须做文件级验收。",
        "validation": "通过强制 `process-log.md`、`tool-ledger.md` 和脚本检查来验证，而不是相信线程 UI 状态。",
        "artifact": "案例级质量规则：completion 只有在回执列出的文件存在且非空时才接受。",
        "asset": "可复用资产：子任务文件级验收门。",
        "optimization": "后续新增 `audit-subtasks` 命令，解析结构化子任务台账并自动检查输出路径。",
        "tool_quality": "Codex 线程读取：中；文件系统检查：强；Browser：不相关；Computer Use：不相关；last30days：不相关，因为这是内部流程失败。",
        "assumed": False,
    },
    "2026-06-20-research-tool-coverage-gap": {
        "title": "研究工具覆盖和结果质量缺口",
        "signal": "一个案例即使用了研究工具，也可能只得到弱证据，所以 SignalProof 需要结果质量门。",
        "research": "新的 last30days 运行暴露了典型失败模式：planner/rerank 因 HTTP 402 回退，Reddit 只有 2 条弱命中，X/YouTube/HN/GitHub 都是 0。diagnose 显示来源可用，但来源可用不等于结果有用。",
        "debate": "正方很清楚：质量账本能阻止虚假信心。反方是：过多记录可能拖慢轻量探索。",
        "thesis": "继续。工具质量判断是 SignalProof 的核心能力，不是可选文书工作。",
        "validation": "把 `tool-ledger.md` 设为必需文件，并检查它覆盖 last30days、Browser、Computer Use、Skill、Plugin、MCP 和工具结果质量。",
        "artifact": "脚本现在会提醒过薄的工具账本，`check-goal` 要求出现优化记录。",
        "asset": "可复用资产：研究质量账本模式。",
        "optimization": "新增按阶段预设的候选能力：研究、产物验收、发布、反馈、决策。",
        "tool_quality": "last30days diagnose：用于可用性判断时强；last30days research run：用于市场证据时弱；脚本自检：强。",
        "assumed": False,
    },
    "2026-06-20-codex-plugin-skill-orchestration-boundary": {
        "title": "Codex 插件和 Skill 编排边界",
        "signal": "SignalProof 应该成为一个 Codex skill/plugin 包，用来协调其他能力，但不能假装自己能像代码 API 一样直接调用所有插件。",
        "research": "刷新后的 Codex 手册确认：Skill 是可复用工作流，Plugin 是分发单元，MCP 把模型连接到工具和上下文。Browser 和 Computer Use 是用于视觉或 GUI 验收的独立能力面。",
        "debate": "这支持 SignalProof 作为协议包存在。反对意见是过度自动化：太早把所有集成打包进去，会把项目拖成通用 agent 平台。",
        "thesis": "继续维护 repo 级 skill 和插件草案。MCP、hooks、automations 等先延后，等重复案例证明必要性再接入。",
        "validation": "通过创建 `.agents/skills/signalproof/`、`plugins/signalproof/.codex-plugin/plugin.json` 和 repo marketplace 入口来验证。",
        "artifact": "repo 级 skill 和本地插件草案包。",
        "asset": "可复用资产：Codex 能力地图和插件骨架。",
        "optimization": "下一版应测试本地插件安装，并判断是否用 hooks 在案例完成前强制 `check-all`。",
        "tool_quality": "OpenAI Codex manual：强；本地插件骨架：中；MCP：已映射但未集成；Browser：候选；Computer Use：候选但当前没有直接工具暴露。",
        "assumed": False,
    },
    "2026-06-20-assumed-feedback-decision-boundary": {
        "title": "假设反馈的决策边界",
        "signal": "用户明确允许暂时跳过真实外部反馈和发布渠道，因此协议需要一条安全的假设续跑路径。",
        "research": "现有 SignalProof 规则规定：假设反馈可以支持内部 MVP 继续推进，但不能替代真实反馈，也不能写成市场验证。",
        "debate": "这能保持推进速度，同时不伪造验证。反对意见是：假设反馈如果不被反复标边界，很容易偷偷变成假证明。",
        "thesis": "只以 `assumption-based-internal-continuation` 的状态继续。",
        "validation": "当案例引用假设时要求存在 `assumed-feedback.md`，并检查 decision 里的过度声称语言。",
        "artifact": "假设反馈案例和更强的过度声称检测。",
        "asset": "可复用资产：假设边界模板。",
        "optimization": "随着更多案例出现边缘写法，继续把危险短语加入过度声称检测。",
        "tool_quality": "本地脚本检查：强；personal-opportunity-os 规则：强；last30days：不相关；Browser/Computer Use：不相关。",
        "assumed": True,
    },
}


def frontmatter(kind: str, title: str, status: str, gate: str) -> str:
    return f"""---
type: {kind}
title: {title}
status: {status}
updated_at: {TODAY}
gate: {gate}
---"""


def seed_case(slug: str, data: dict[str, object]) -> None:
    d = CASES / slug
    title = str(data["title"])
    write(d / "signal.md", f"""{frontmatter('signal', title, 'captured', 'passed')}

# 信号

## 原始信号

{data['signal']}

## 为什么值得进入流程

- 这是一个真实 SignalProof 工作流问题。
- 它能检验协议是否能从信号推进到资产。

## 当前边界

- 真实外部反馈和发布渠道本轮跳过。
- 本 case 只能证明内部协议能力。
""")
    write(d / "research.md", f"""{frontmatter('research', title, 'completed', 'weak')}

# 研究

## 研究结论

{data['research']}

## 证据强度

- 内部流程证据：中到强。
- 外部市场证据：弱或为空。

## 证据缺口

- 真实用户原话为空。
- 真实发布反馈为空。
- 真实 before/after 为空。
""")
    write(d / "debate.md", f"""{frontmatter('debate', title, 'completed', 'passed')}

# 辩论

## 正反方结论

{data['debate']}

## 最强反对意见

内部协议跑通不等于外部需求成立。

## 收窄后判断

继续内部验证，不进入市场验证结论。
""")
    write(d / "thesis.md", f"""{frontmatter('thesis', title, 'accepted', 'passed')}

# 判断

## 当前判断

{data['thesis']}

## 成功标准

- 全部阶段文件存在。
- 工具账本记录结果质量。
- 流程日志记录迭代和优化。
- 自检脚本通过。
""")
    write(d / "validation.md", f"""{frontmatter('validation', title, 'planned', 'passed')}

# 验证计划

## 验证方式

{data['validation']}

## 命令

```bash
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py export-all
python3 scripts/signalproof.py check-goal --min-cases 5
```
""")
    write(d / "artifact.md", f"""{frontmatter('artifact', title, 'created', 'passed')}

# 产物

## 产物内容

{data['artifact']}

## 产物边界

该产物是内部协议验证，不是外部市场验证。
""")
    write(d / "feedback.md", f"""{frontmatter('feedback', title, 'skipped-real-feedback', 'weak')}

# 反馈

## 当前反馈状态

真实反馈为空。

## 内部反馈

- 本 case 用脚本自检和流程审计替代外部反馈。
- 这只适合内部协议迭代。

## 不能得出的结论

- 不能写验证成功。
- 不能声称市场已验证。
- 不能声称用户需要这个产品。
""")
    write(d / "decision.md", f"""{frontmatter('decision', title, 'accepted-internal', 'passed')}

# 决策

## 决策

继续内部协议验证。

## 理由

{data['thesis']}

## 边界

真实反馈为空，不能声称验证成功。
""")
    write(d / "asset.md", f"""{frontmatter('asset', title, 'reusable-internal', 'passed')}

# 资产

## 复用资产

{data['asset']}

## 如何复用

- 作为后续 SignalProof 案例的模板或规则来源。
- 作为脚本、skill、plugin 迭代的证据。

## 边界

不能替代真实外部反馈。
""")
    write(d / "flow-review.md", f"""{frontmatter('flow_review', title, 'completed', 'passed')}

# 流程自检

## 阶段完整性

| 阶段 | 状态 | 说明 |
| --- | --- | --- |
| signal | passed | 真实流程信号已记录。 |
| research | weak | 有内部证据，外部证据不足。 |
| debate | passed | 已写最强反对意见。 |
| thesis | passed | 已限定为内部继续。 |
| validation | passed | 已绑定脚本检查。 |
| artifact | passed | 已生成可复用产物。 |
| feedback | weak | 真实反馈为空。 |
| decision | passed | 未声称验证成功。 |
| asset | passed | 已沉淀内部资产。 |

## 优化空间

{data['optimization']}

## 过度声称检查

未把 synthetic demo、假设反馈或内部流程反馈写成市场验证。
""")
    write(d / "tool-ledger.md", f"""{frontmatter('tool_ledger', title, 'completed', 'passed')}

# 工具账本

## 候选能力账本

| 能力 | 是否相关 | 是否使用 | 结果质量 | 说明 | 下次动作 |
| --- | --- | --- | --- | --- | --- |
| Skill: signalproof | 是 | 是 | 中 | repo 级 skill 约束本地案例。 | 保留。 |
| Skill: personal-opportunity-os | 是 | 是 | 中 | 上层个人机会 OS 方法论。 | 保留。 |
| Skill: last30days | 视主题而定 | 视主题而定 | 弱 | {data['tool_quality']} | 真实趋势判断时补跑更窄查询。 |
| Browser | 视产物而定 | 待验证 | 中 | 适合验证报告索引或本地预览。 | 用文件预览检查报告页。 |
| Computer Use | 低到中 | 否 | 失败 | 插件文件存在，但当前没有直接控制工具暴露。 | 工具可用后再接入只能通过 GUI 操作的流程。 |
| Plugin | 是 | 是 | 中 | 已创建插件草案骨架。 | 后续安装测试。 |
| MCP | 中 | 否 | 弱 | 已映射能力，未绑定服务器。 | 按阶段接 OpenAI Docs / Context7 / GitHub。 |
| Hooks | 中 | 否 | 弱 | 可强制 case check。 | 后续加 pre-finish hook。 |
| Automation | 中 | 否 | 弱 | 可做 72 小时反馈复查。 | 等发布渠道恢复后启用。 |

## 工具结果质量结论

工具覆盖足够支持内部协议验证，不足以支持外部市场判断。
""")
    write(d / "process-log.md", f"""{frontmatter('process_log', title, 'completed', 'passed')}

# 过程日志

## 迭代 1

命令：

```bash
python3 scripts/signalproof.py init-case "{title}"
```

结果：

- 生成完整案例文件。

自检：

- 模板文件齐全。

优化：

- 发现模板案例过于相似，需要按主题 seed 差异化内容。

## 迭代 2

命令：

```bash
python3 scripts/seed_cases.py
python3 scripts/signalproof.py check-all
```

结果：

- 进入差异化案例校验。

自检：

- `tool-ledger.md` 覆盖 last30days、Browser、Computer Use、Skill、Plugin、MCP。

优化：

{data['optimization']}
""")
    write(d / "report.md", f"""# 报告

## 摘要

{title} 已跑完 SignalProof 内部协议闭环。

## 关键判断

{data['thesis']}

## 工具结果质量

{data['tool_quality']}

## 边界

真实反馈和发布渠道本轮跳过，所以不能声称市场验证。
""")
    if data.get("assumed"):
        write(d / "assumed-feedback.md", f"""{frontmatter('assumed_feedback', title, 'recorded', 'weak')}

# 假设反馈

## 假设输入

本 case 在无真实外部反馈的情况下继续推进。

## 使用边界

假设反馈只能用于内部协议验证，不能替代真实反馈，不能支持市场验证或产品化结论。
""")


def main() -> int:
    for slug, data in CASES_DATA.items():
        seed_case(slug, data)
    write(RUNS / f"{TODAY}-seed-cases.md", f"""# Seed Cases 生成记录

生成日期：{TODAY}

已生成案例：

{chr(10).join(f'- {slug}' for slug in CASES_DATA)}

目的：

- 让五个 case 分别代表五类不同的 SignalProof 工作流风险。
- 真实外部反馈和发布渠道保持跳过状态。
- 保留工具质量和优化证据，供后续迭代使用。
""")
    print(f"Seeded {len(CASES_DATA)} cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
