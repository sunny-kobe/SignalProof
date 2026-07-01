#!/usr/bin/env python3
"""SignalProof 本地协议自动化脚本。

脚本只依赖 Python 标准库，保证这个协议可以在一个干净的本地仓库里直接运行。
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import date
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "vault"
CASES = VAULT / "cases"
REPORTS = VAULT / "reports"
RUNS = VAULT / "runs"
ASSET_REGISTRY = VAULT / "assets" / "registry.md"
TEMPLATES = ROOT / "templates" / "case"
LAST30DAYS = Path("/Users/rust/.agents/skills/last30days/scripts/last30days.py")
PLUGIN_CACHE = Path("/Users/rust/.codex/plugins/cache")
CODEX_CONFIG = Path.home() / ".codex" / "config.toml"
RESEARCH_GATE_DOC = ROOT / "docs" / "research-quality-gate.md"
PLUGIN_STATUS_DOC = ROOT / "docs" / "codex-plugin-status-and-migration.md"
PLUGIN_LOCK_DOC = ROOT / "docs" / "codex-plugin-lock.md"
PLUGIN_INSTALL_SCRIPT = ROOT / "scripts" / "install-codex-plugins.sh"

REQUIRED_FILES = [
    "signal.md",
    "research.md",
    "debate.md",
    "thesis.md",
    "validation.md",
    "artifact.md",
    "feedback.md",
    "decision.md",
    "asset.md",
    "flow-review.md",
    "tool-ledger.md",
    "process-log.md",
    "report.md",
]

LITE_REQUIRED_FILES = [
    "signal.md",
    "research.md",
    "debate.md",
    "decision.md",
    "asset.md",
]

OPTIONAL_FILES = [
    "assumed-feedback.md",
]

SECTIONS = [
    ("signal.md", "信号"),
    ("research.md", "研究"),
    ("debate.md", "辩论"),
    ("thesis.md", "判断"),
    ("validation.md", "验证计划"),
    ("artifact.md", "产物"),
    ("feedback.md", "反馈"),
    ("decision.md", "决策"),
    ("asset.md", "资产"),
    ("flow-review.md", "流程自检"),
    ("tool-ledger.md", "工具账本"),
    ("process-log.md", "过程日志"),
]

TOOL_LEDGER_TERMS = {
    "last30days": [r"last30days"],
    "Browser": [r"Browser", r"浏览器"],
    "Chrome": [r"Chrome"],
    "Computer Use": [r"Computer Use", r"电脑控制", r"计算机控制"],
    "Record & Replay": [r"Record & Replay", r"Record and Replay", r"录制"],
    "Documents": [r"Documents", r"DOCX", r"文档"],
    "PDF": [r"PDF"],
    "Spreadsheets": [r"Spreadsheets", r"Sheets", r"表格"],
    "Presentations": [r"Presentations", r"Slides", r"演示文稿"],
    "Skill": [r"Skill", r"技能"],
    "Plugin": [r"Plugin", r"插件"],
    "MCP": [r"MCP"],
    "result quality": [r"result quality", r"结果质量", r"工具结果质量"],
}

PROCESS_TERMS = {
    "Iteration": [r"Iteration", r"迭代"],
    "Command": [r"Command", r"命令"],
    "Self-check": [r"Self-check", r"自检"],
    "Optimization": [r"Optimization", r"优化"],
}

UNRESOLVED_MARKERS = {
    "template variable": [r"\{\{[^}\n]+\}\}"],
    "TODO": [r"\bTODO\b", r"\bTBD\b"],
    "待补": [r"(^|[\s|：:，,。；;])待补($|[\s|：:，,。；;])"],
    "待定": [r"(^|[\s|：:，,。；;])待定($|[\s|：:，,。；;])"],
    "待填写": [r"待填写"],
}

PLACEHOLDER_CONTEXT_ALLOWLIST = [
    "不能只写",
    "不再写",
    "不得只写",
    "避免只写",
    "不要只写",
    "识别",
    "检查",
    "占位",
    "只看",
]

RESEARCH_GATE_TERMS = {
    "source coverage": [r"来源覆盖", r"source coverage"],
    "cross validation": [r"交叉验证", r"cross[- ]?validation"],
    "counterevidence": [r"反证", r"替代方案", r"counterevidence"],
    "evidence grade": [r"证据等级", r"strong", r"medium", r"weak", r"blocked"],
    "decision permission": [r"结论许可", r"决策许可", r"低成本实验", r"继续研究"],
    "user authorization": [r"用户授权", r"开通", r"认证", r"auth"],
}

ALLOWED_EVIDENCE_GRADES = {"strong", "medium", "weak", "blocked"}
ALLOWED_RESEARCH_PERMISSIONS = {"continue-research", "low-cost-experiment", "pause", "abandon"}
ALLOWED_FEEDBACK_STATUS = {
    "none",
    "internal",
    "synthetic-demo",
    "assumed",
    "published-no-feedback",
    "qualitative-real",
    "quantitative-real",
    "paid-signal",
}
NON_REAL_FEEDBACK_STATUS = {
    "none",
    "internal",
    "synthetic-demo",
    "assumed",
    "published-no-feedback",
}
ALLOWED_VALIDATION_STATUS = {"none", "artifact-built", "published", "externally-observed", "repeated"}
ALLOWED_ASSET_STATUS = {"none", "candidate", "registered", "reused", "retired"}
STRUCTURED_RESEARCH_FIELDS = [
    "evidence_grade",
    "permission",
    "source_types_covered",
    "primary_source_count",
    "external_quote_count",
    "counterevidence_count",
    "independent_source_count",
]
STRUCTURED_FEEDBACK_FIELDS = [
    "feedback_status",
    "validation_status",
    "real_feedback_count",
    "paid_signal_count",
    "published_url_count",
]
STRUCTURED_ASSET_FIELDS = [
    "asset_status",
    "registry_required",
    "reuse_count",
    "proof_of_reuse",
]
ALLOWED_CASE_INTENTS = {
    "external-opportunity",
    "product-iteration",
    "content-iteration",
    "workflow-improvement",
    "tool-evaluation",
    "learning-to-asset",
}
ALLOWED_LOOP_PROFILES = {"ai-work-loop-v1"}
ALLOWED_AGENTIC_LOOP_STATUS = {"required", "optional", "skipped"}
ALLOWED_DEVELOPER_FEEDBACK_LOOP_STATUS = {"required", "optional", "skipped"}
ALLOWED_EXTERNAL_FEEDBACK_LOOP_STATUS = {"required", "delayed", "skipped-with-reason"}
ALLOWED_ASSET_LOOP_STATUS = {"required", "optional", "skipped"}
STRUCTURED_SIGNAL_FIELDS = [
    "case_intent",
    "loop_profile",
    "agentic_loop",
    "developer_feedback_loop",
    "external_feedback_loop",
    "asset_loop",
]

CASE_TYPE_DEFAULT_INTENT = {
    "external-opportunity": "external-opportunity",
    "internal-audit": "workflow-improvement",
    "plugin-test": "tool-evaluation",
}

CASE_INTENT_LOOP_DEFAULTS = {
    "external-opportunity": {
        "agentic_loop": "optional",
        "developer_feedback_loop": "required",
        "external_feedback_loop": "delayed",
        "asset_loop": "required",
    },
    "product-iteration": {
        "agentic_loop": "required",
        "developer_feedback_loop": "required",
        "external_feedback_loop": "delayed",
        "asset_loop": "required",
    },
    "content-iteration": {
        "agentic_loop": "optional",
        "developer_feedback_loop": "required",
        "external_feedback_loop": "delayed",
        "asset_loop": "required",
    },
    "workflow-improvement": {
        "agentic_loop": "optional",
        "developer_feedback_loop": "required",
        "external_feedback_loop": "skipped-with-reason",
        "asset_loop": "required",
    },
    "tool-evaluation": {
        "agentic_loop": "optional",
        "developer_feedback_loop": "required",
        "external_feedback_loop": "skipped-with-reason",
        "asset_loop": "required",
    },
    "learning-to-asset": {
        "agentic_loop": "skipped",
        "developer_feedback_loop": "required",
        "external_feedback_loop": "skipped-with-reason",
        "asset_loop": "required",
    },
}

LOOP_CAPABILITY_MATRIX = [
    {
        "loop": "agentic-coding",
        "purpose": "把 Product Spec 和 Eval Set 交给 Codex/Claude Code 等 agent，执行构建、测试和回归。",
        "cadence": "分钟级。",
        "default_capabilities": "Product Spec、Eval Set、本地脚本、Git、测试命令、Browser/Playwright 验收。",
        "writes_to": "validation.md、artifact.md、tool-ledger.md、flow-review.md",
    },
    {
        "loop": "developer-feedback",
        "purpose": "用户用上下文优势和产品判断修正方向、UI、边界和下一轮 spec。",
        "cadence": "几十分钟到数小时。",
        "default_capabilities": "debate.md、thesis.md、decision.md、flow-review.md、Codex 子线程反方审查。",
        "writes_to": "decision.md、flow-review.md、process-log.md",
    },
    {
        "loop": "external-feedback",
        "purpose": "通过发布、访谈、alpha、A/B、评论、issue 或真实指标回收外部反馈。",
        "cadence": "小时到周级。",
        "default_capabilities": "Browser/Chrome、GitHub、PostHog/Mixpanel/Amplitude、Spreadsheets、人工反馈输入。",
        "writes_to": "feedback.md、day2-execution.md、tool-ledger.md",
    },
    {
        "loop": "asset-meta",
        "purpose": "把本轮可复用内容沉淀成模板、检查表、脚本、skill、资料包或复用账本条目。",
        "cadence": "每个 case 阶段结束时。",
        "default_capabilities": "asset.md、vault/assets/registry.md、Record & Replay、Documents/PDF/Spreadsheets/Presentations。",
        "writes_to": "asset.md、vault/assets/registry.md、flow-review.md",
    },
]

BUILTIN_PLUGIN_SPECS = [
    ("Browser", "openai-bundled/browser/*/skills/control-in-app-browser/SKILL.md"),
    ("Chrome", "openai-bundled/chrome/*/skills/control-chrome/SKILL.md"),
    ("Computer Use", "openai-bundled/computer-use/*/skills/computer-use/SKILL.md"),
    ("Record & Replay", "openai-bundled/record-and-replay/*/skills/record-and-replay/SKILL.md"),
    ("Documents", "openai-primary-runtime/documents/*/skills/documents/SKILL.md"),
    ("PDF", "openai-primary-runtime/pdf/*/skills/pdf/SKILL.md"),
    ("Spreadsheets", "openai-primary-runtime/spreadsheets/*/skills/spreadsheets/SKILL.md"),
    ("Presentations", "openai-primary-runtime/presentations/*/skills/presentations/SKILL.md"),
    ("Data Visualization", "openai-curated/build-web-data-visualization/*/.codex-plugin/plugin.json"),
    ("HyperFrames", "openai-curated/hyperframes/*/.codex-plugin/plugin.json"),
]

STAGE_CAPABILITY_MATRIX = [
    {
        "stage": "signal",
        "purpose": "捕捉信号，建立 case 边界。",
        "default_capabilities": "SignalProof skill、Codex 线程工具、本地文件系统。",
        "codex_plugins": "Browser 读取公开 URL；Chrome 读取用户已登录页面；Record & Replay 录制用户演示的真实工作流。",
        "use_when": "信号来自网页、已登录产品、用户演示或另一个 Codex 线程。",
        "write_to": "signal.md、process-log.md、tool-ledger.md",
    },
    {
        "stage": "research",
        "purpose": "收集证据，区分事实、推断、缺口和结论许可。",
        "default_capabilities": "last30days、Web/Search、GitHub/HN/RSS、官方文档、research-quality-gate。",
        "codex_plugins": "Browser 验证公开页面；Chrome 读取登录态页面；PDF/Documents/Spreadsheets 读取外部资料；Data Visualization 仅在需要看数据结构时使用。",
        "use_when": "信息时效性强、来源需要登录、资料是 PDF/DOCX/表格，或证据需要可视化判断；必须记录来源覆盖、交叉验证、反证和结论许可。",
        "write_to": "research.md、vault/assets/research/、tool-ledger.md",
    },
    {
        "stage": "debate",
        "purpose": "做正反方和反方审查，暴露风险。",
        "default_capabilities": "Codex 子线程、反方 prompt、本地证据包。",
        "codex_plugins": "Browser/Chrome 复核关键反证；PDF/Documents 读取长文档反证。",
        "use_when": "关键反对意见依赖外部页面、登录态页面或长文档证据。",
        "write_to": "debate.md、subtasks/index.md、tool-ledger.md",
    },
    {
        "stage": "thesis",
        "purpose": "给出继续、收窄、暂停或放弃判断。",
        "default_capabilities": "本地 case 文件、自检脚本、用户判断。",
        "codex_plugins": "通常不需要；只在关键判断缺证据时回到 research/debate 阶段补用。",
        "use_when": "判断依赖未核验证据或需要补查事实。",
        "write_to": "thesis.md、decision.md 草稿、flow-review.md",
    },
    {
        "stage": "validation",
        "purpose": "把机会压成可验证实验并验收产物。",
        "default_capabilities": "本地脚本、case 自检、文件级检查。",
        "codex_plugins": "Browser 验收 HTML/本地 Web；Computer Use 验收只能 GUI 操作的流程；PDF/Documents/Spreadsheets/Presentations 验收对应文件产物。",
        "use_when": "产物有界面、GUI、文档、表格、演示文稿或 PDF 布局质量要求。",
        "write_to": "validation.md、flow-review.md、tool-ledger.md",
    },
    {
        "stage": "artifact",
        "purpose": "生成公开产物或内部可复用产物。",
        "default_capabilities": "Codex 文件编辑、Git/GitHub CLI、本地脚本。",
        "codex_plugins": "Documents 做 DOCX/文档；PDF 做 PDF；Spreadsheets 做表格；Presentations 做 deck；HyperFrames 做网页视频/视觉叙事；Data Visualization 做数据图表。",
        "use_when": "产物格式不是纯 Markdown，或需要可视化、排版、演示、表格、视频化表达。",
        "write_to": "artifact.md、asset.md、vault/assets/",
    },
    {
        "stage": "publication",
        "purpose": "发布触达，但不伪造真实反馈。",
        "default_capabilities": "GitHub CLI、发布台账、本地文案。",
        "codex_plugins": "Browser 验证公开发布页；Chrome 在用户明确授权时使用登录态发布/查看数据。",
        "use_when": "需要确认公开 URL、截图、登录态后台或用户授权的渠道操作。",
        "write_to": "feedback.md、day2-execution.md、tool-ledger.md",
    },
    {
        "stage": "feedback",
        "purpose": "回收真实反馈和指标，区分 published 与 validated。",
        "default_capabilities": "GitHub CLI、last30days、人工反馈输入。",
        "codex_plugins": "Chrome 查看登录态评论/私信/后台；Browser 验证公开评论；Spreadsheets 统计反馈；Record & Replay 沉淀用户示范流程。",
        "use_when": "反馈来自登录态渠道、公开页面、表格数据，或用户用操作演示真实任务。",
        "write_to": "feedback.md、vault/assets/feedback/、tool-ledger.md",
    },
    {
        "stage": "decision",
        "purpose": "做继续、收窄、暂停、放弃或资产化决策。",
        "default_capabilities": "本地 case 文件、check-all、check-goal。",
        "codex_plugins": "通常不需要；缺少证据时回退到 research/feedback 补用插件。",
        "use_when": "决策依赖未核验反馈、指标或产物验收。",
        "write_to": "decision.md、flow-review.md",
    },
    {
        "stage": "asset",
        "purpose": "把有效产物沉淀成可复用资产。",
        "default_capabilities": "Markdown 模板、脚本、GitHub repo、Codex skill/plugin。",
        "codex_plugins": "Documents/PDF/Spreadsheets/Presentations 做资料包；Record & Replay 把用户流程变成 Skill；Browser 验收发布后的资产页。",
        "use_when": "资产需要变成文档、PDF、表格、PPT、可录制流程或公开页面。",
        "write_to": "asset.md、vault/assets/、plugins/、.agents/skills/",
    },
    {
        "stage": "flow-review",
        "purpose": "审计阶段完整性、工具覆盖和下一轮优化。",
        "default_capabilities": "check-all、check-goal、capabilities、export-all。",
        "codex_plugins": "Browser 预览报告索引；Computer Use 复核 GUI-only 验收；PDF/Documents/Spreadsheets/Presentations 复核格式产物。",
        "use_when": "需要证明报告可读、界面可用、文件格式正确或 GUI 流程真实可跑。",
        "write_to": "flow-review.md、tool-ledger.md、vault/runs/",
    },
]

CASE_TYPE_PRESETS = {
    "external-opportunity": {
        "case_type_label": "外部机会验证",
        "why_enter_flow": "- 这条信号可能对应外部真实问题，需要用来源覆盖、交叉验证和反证来判断是否继续。\n- 本 case 必须把真实反馈、公开来源证据和内部推断分开。",
        "initial_users": "- 目标用户：未覆盖，必须用公开讨论、真实反馈或一手资料确认。\n- 如果暂时无法确认，只能写成假设人群。",
        "current_boundary": "- 不声称市场验证。\n- 不默认产品化。\n- 不做 SaaS 或 dashboard。\n- weak / blocked 证据只能支持继续研究或低成本内部实验。",
        "research_process": "- 先读取本地协议、质量门和相关 case。\n- 再按研究质量门补公开讨论、项目和数据、官方和一手资料、反证和替代方案。\n- 如果某类来源没有跑通，写成来源缺口，不能写成反证。",
        "source_coverage_rows": "| 公开讨论 | last30days / Reddit / HN / X / YouTube / Browser / Chrome | 未覆盖 | weak | 未确认目标用户原话。 |\n| 项目和数据 | GitHub / Hugging Face / Similarweb / Semrush | 未覆盖 | weak | 未确认可核验指标。 |\n| 官方和一手资料 | 官方文档 / OpenAI Docs / PDF / Documents | 未覆盖 | weak | 未确认直接来源。 |\n| 反证和替代方案 | Scite / Readwise / Zotero / 竞品文档 / GitHub issues | 未覆盖 | weak | 未确认强替代或失败风险。 |",
        "cross_validation": "- 谁在说：未覆盖。\n- 说什么：未覆盖。\n- 在哪里说：未覆盖。\n- 有没有反证：未覆盖。\n- 能支持什么结论：当前只能支持内部流程实验或继续补研究。",
        "counterevidence": "- 未覆盖成熟替代方案。\n- 未覆盖失败案例或低意愿证据。\n- 未覆盖“用户现在怎么解决”的证据。",
        "evidence_grade": "当前为 weak：模板只提供研究结构，不提供已完成证据。完成 case 前必须把本节改成基于真实来源的 strong / medium / weak / blocked 判断。",
        "decision_permission": "当前许可：继续研究。不得写成已验证需求、市场已验证、可以产品化或可以做 SaaS。",
        "next_evidence_steps": "- 补 1 个公开讨论来源。\n- 补 1 个项目或数据指标。\n- 补 1 个官方或一手资料。\n- 补 1 个反证或替代方案。",
        "feedback_empty_reason": "如果本轮没有发布、访谈、评论或指标回收，必须明确写真实反馈为空；不能把内部判断写成市场验证。",
        "validation_object": "这个信号是否能被证据支持到下一步，而不是只被模板完整性支持。",
        "validation_method_steps": "1. 补齐研究质量门四类来源。\n2. 补充工具账本，记录结果质量和跳过原因。\n3. 补充流程日志。\n4. 运行 `python3 scripts/signalproof.py check-case <case-slug> --strict`。\n5. 运行 `python3 scripts/signalproof.py export-all`。\n6. 记录剩余证据缺口。",
        "product_spec": "- 目标用户：未覆盖。\n- 目标任务：判断这条外部信号是否值得继续。\n- 非目标：不在本轮做产品化、SaaS 或 dashboard。\n- 成功标准：研究证据和决策许可匹配，且不把发布或内部判断写成验证。",
        "eval_set": "- 通过样例：`research.md` 写明来源覆盖、反证、证据等级和结论许可。\n- 失败样例：只有工具调用记录，却没有判断结果质量。\n- 回归检查：`check-case --strict` 不允许未替换变量、TODO、待补、待定。",
        "agentic_acceptance": "- agentic loop 本轮为可选；只有当需要生成代码、内容包或工具产物时才启动。\n- 若启动，必须先明确 Product Spec 与 Eval Set，再让 agent 执行。",
        "artifact_summary": "本 case 的产物是一个可复查的 SignalProof 证明案例，可能包含研究包、验证计划、公开产物或内部决策包。",
        "asset_type": "外部机会验证案例。",
        "asset_reusable_content": "- 研究来源清单。\n- 工具覆盖记录。\n- 反证和替代方案。\n- 决策边界。",
        "decision_default": "基于证据强度决定继续研究、低成本实验、暂停或放弃。",
        "decision_reason": "- 本 case 只有在研究证据达到 medium 以上时才进入低成本实验。\n- 如果证据仍为 weak / blocked，决策应是继续补证、收窄或暂停，而不是默认继续。",
        "decision_next_steps": "- 补齐研究质量门四类来源。\n- 把结论改成继续 / 收窄 / 暂停 / 放弃之一。\n- 只有出现真实发布、访谈、评论或指标时，才更新真实反馈。",
        "decision_boundary": "真实反馈、发布渠道和外部来源如果没有实际覆盖，只能写成证据缺口，不能证明市场需求。",
        "report_boundary": "真实反馈、发布渠道和外部来源如果没有实际覆盖，只能写成证据缺口，不能证明市场需求。",
        "candidate_capability_rows": "| Skill: signalproof | 是 | 是 | 中 | repo 级 skill 提供本地流程规则。 | 保留。 |\n| Skill: personal-opportunity-os | 视主题而定 | 按需评估 | 弱 | 仅当上层个人机会系统方向会影响判断时使用。 | 按主题决定。 |\n| Skill: last30days | 视研究主题而定 | 按需评估 | 弱 | 真实趋势 case 需要运行；内部结构 case 可跳过但要写原因。 | 对真实趋势 case 用较新 Python 运行。 |\n| Browser | 视产物而定 | 按需评估 | 弱 | 适合验证网页、公开页面或本地报告预览。 | 有网页验收目标时使用。 |\n| Computer Use | 视 GUI 而定 | 按需评估 | 弱 | 适合 GUI-only 验收。 | 有 GUI 验收目标时使用。 |\n| Plugin | 是 | 按需评估 | 弱 | 先判断插件是否会改变判断或验收产物。 | 按 case 选择，不默认全跑。 |\n| MCP | 视证据源而定 | 按需评估 | 弱 | 可接官方文档、GitHub 或 Context7 等能力。 | 需要结构化外部来源时使用。 |",
        "tool_research_rows": "| 公开讨论 | 未覆盖 | weak | 需要目标用户原话、抱怨、采用或反对意见；X API credits 默认暂缺但非阻断。 | 优先补 last30days / HN / Reddit / YouTube / GitHub；必要时再提醒补 X。 |\n| 项目和数据 | 未覆盖 | weak | 需要 GitHub、下载、访问、流量或产品指标。 | 补 GitHub / Hugging Face / Similarweb / Semrush。 |\n| 官方和一手资料 | 未覆盖 | weak | 需要官方文档、API、价格、论文或一手说明。 | 补官方文档 / OpenAI Docs / PDF。 |\n| 反证和替代方案 | 未覆盖 | weak | 需要成熟替代、失败案例或低意愿证据。 | 补 Scite / Readwise / Zotero / 竞品文档。 |\n| 结论许可 | 已覆盖 | weak | weak 只能支持继续研究或低成本内部实验。 | 证据未升到 medium/strong 前不写产品化。 |",
        "stage_plugin_rows": "| signal | Browser / Chrome / Record & Replay | 按需评估 | weak | 尚未改变判断 | 未使用原因需按 case 补写 |\n| research | GitHub / last30days / OpenAI Docs / Hugging Face / Readwise / Scite / Semrush / Similarweb / Brand24 / Zotero / Browser / Chrome / Documents / PDF / Spreadsheets / Data Visualization | 按需评估 | weak | 尚未改变判断 | 未使用原因需按 case 补写 |\n| debate | Browser / Chrome / Documents / PDF | 按需评估 | weak | 尚未改变判断 | 未使用原因需按 case 补写 |\n| validation | Browser / Computer Use / Documents / PDF / Spreadsheets / Presentations | 按需评估 | weak | 尚未改变判断 | 未使用原因需按 case 补写 |\n| artifact | Documents / PDF / Spreadsheets / Presentations / HyperFrames / Data Visualization | 按需评估 | weak | 尚未改变判断 | 未使用原因需按 case 补写 |\n| publication | Browser / Chrome | 未使用 | weak | 未发布 | 有公开 URL 时再验收 |\n| feedback | Chrome / Browser / Spreadsheets / Record & Replay | 未使用 | weak | 真实反馈为空 | 外部反馈恢复后再用 |\n| asset | Documents / PDF / Spreadsheets / Presentations / Record & Replay / Browser | 按需评估 | weak | 尚未改变判断 | 需要资料包或流程录制时再用 |\n| flow-review | Browser / Computer Use / Documents / PDF / Spreadsheets / Presentations | 按需评估 | weak | 尚未改变判断 | 有报告预览或 GUI 验收目标时再用 |",
    },
    "internal-audit": {
        "case_type_label": "内部流程审计",
        "why_enter_flow": "- 这条信号用于检验 SignalProof 工作流本身是否能发现并修正流程缺口。\n- 本 case 的价值来自本地文档、模板、脚本和 case 记录的可执行改进，而不是外部市场反馈。",
        "initial_users": "- SignalProof 维护者。\n- 高频使用 Codex / Claude Code / MCP / 本地 AI coding 工作流，并希望把判断过程沉淀成可审计资产的人。",
        "current_boundary": "- 不声称市场验证。\n- 不默认产品化。\n- 不做 SaaS、dashboard、workflow builder 或通用知识库。\n- 内部流程反馈只能支持机制优化，不能支持外部需求成立。",
        "research_process": "- 读取 `AGENTS.md`、repo skill、协议文档、研究质量门和插件流程文档。\n- 复核最近自审 case 的报告、流程自检、工具账本和决策。\n- 用 `git diff`、脚本输出和 case 内容判断哪些改进已经落地，哪些仍只是建议。",
        "source_coverage_rows": "| 公开讨论 | 当前用户任务和历史记忆中的 SignalProof 口径 | 部分覆盖 | weak | 只能支持本轮内部审计，不支持市场判断。 |\n| 项目和数据 | 仓库文件、模板、脚本、case、报告索引、runs 快照 | 已覆盖 | strong | 足以判断本地工作流机制是否改变。 |\n| 官方和一手资料 | `AGENTS.md`、`.agents/skills/signalproof/SKILL.md`、`docs/protocol.md`、`docs/research-quality-gate.md`、`docs/codex-plugin-flow.md` | 已覆盖 | strong | 本轮事实来源限定在仓库和用户要求。 |\n| 反证和替代方案 | 最近自审 report、`check-all` warning、未完成占位标记、connector 授权缺口 | 已覆盖 | medium | 证明仍需脚本 gate，而不是只写复盘。 |",
        "cross_validation": "- 谁在说：用户要求二次审视并实际更新工作流；仓库规则要求本地优先和中文记录。\n- 说什么：最近自审 case 已有部分脚本改进，但仍可能让未完成占位内容通过严格检查。\n- 在哪里说：当前任务、`AGENTS.md`、repo skill、`docs/`、`scripts/signalproof.py`、`vault/cases/2026-06-21-signalproof-当前工作流自审/`。\n- 有没有反证：有，原报告已落地 `check-plugin-drift` 和 `check-case --strict`，不能说它只是空报告；但它没有处理模板占位和内部审计 case 类型。\n- 能支持什么结论：支持继续本地工作流优化；不支持市场验证。",
        "counterevidence": "- 原报告不是纯形式主义，因为已有脚本命令进入 `scripts/signalproof.py`。\n- 但如果 `check-case --strict` 只看 TODO 和研究质量门术语，就可能漏掉 `待补`、`待定`、未替换模板变量等半成品痕迹。\n- 普通 Markdown 复盘也能发现问题，但不能稳定阻止下一次误报完成。",
        "evidence_grade": "当前证据等级：medium。内部脚本、模板和 case 记录足以支持工作流机制改进；外部用户反馈仍为 weak。",
        "decision_permission": "当前许可：继续本地流程优化，并把高价值缺口落到脚本、模板、文档或 skill。不得写成市场验证、插件全部授权成功或 SaaS 可行。",
        "next_evidence_steps": "- 对新增占位检查运行本次 case 严格检查。\n- 更新模板和协议说明，避免内部审计默认套外部机会口径。\n- 保留真实 feedback 为空的边界。",
        "feedback_empty_reason": "本 case 是内部流程优化，没有发布、访谈、公开评论或产品指标；真实反馈为空。",
        "validation_object": "SignalProof 是否能把 Andrew Ng 的 agentic coding、developer feedback、external feedback 三个 loop 嵌入本地协议，并保持 published != validated 的证据边界。",
        "validation_method_steps": "1. 复核最近自审 case 和报告。\n2. 修改 `scripts/signalproof.py`、模板、协议或 skill。\n3. 新建或更新本次内部审计 case。\n4. 运行 `python3 scripts/signalproof.py check-plugin-drift`。\n5. 运行 `python3 scripts/signalproof.py check-case <case-slug> --strict`。\n6. 运行 `python3 scripts/signalproof.py export-all`、`check-all`、`check-goal --min-cases 5` 和 `git diff --check`。",
        "product_spec": "- 目标用户：SignalProof 维护者和高频使用 Codex/Claude Code 的个人工作流实践者。\n- 目标任务：把高不确定性的个人工作压成证据、Spec、AI 执行、反馈、决策和资产。\n- 非目标：不做 Web App、SaaS dashboard、workflow builder、通用知识库或自动雷达。\n- 成功标准：新 case 能声明 case_intent 与 loop_profile；validation.md 能承接 Product Spec 和 Eval Set；flow-review.md 能审计 loop 是否转动。",
        "eval_set": "- 通过样例：`init-case --case-intent workflow-improvement` 生成 signal.md loop frontmatter、validation.md Product Spec/Eval Set、flow-review.md loop review。\n- 失败样例：只生成旧线性 case 文件，没有 loop_profile，或把 external_feedback_loop=skipped-with-reason 写成验证成功。\n- 回归检查：`check-case --strict`、`check-all`、`check-assets`、`export-all`、`check-plugin-drift`。",
        "agentic_acceptance": "- agentic loop 本轮为 optional，因为产物是协议、模板和脚本，而不是独立产品功能。\n- 如果后续 case 选择 `case_intent=product-iteration`，agentic_loop 必须为 required，并要求 Product Spec 与 Eval Set 同时存在。",
        "artifact_summary": "本 case 的产物是一次 SignalProof 工作流机制优化：脚本能识别未完成占位标记，模板能区分内部流程审计与外部机会验证。",
        "asset_type": "内部流程审计和机制优化案例。",
        "asset_reusable_content": "- 严格检查未完成占位标记的脚本规则。\n- `internal-audit` case 类型。\n- 中文 case 记录模板。\n- 复核原报告时区分“已落地机制”和“仍是建议”的判断口径。",
        "decision_default": "继续使用当前工作流，但把本轮发现的缺口落实为确定性检查和模板约束。",
        "decision_reason": "- 本轮目标是优化个人工作流和 SignalProof 机制，不是外部机会验证。\n- 内部流程反馈只能证明机制是否更好用，不能证明市场需求。",
        "decision_next_steps": "- 如果本 case 暴露流程缺口，把缺口写入 `flow-review.md`。\n- 如果缺口可脚本化，更新 `scripts/signalproof.py`、模板或协议文档。\n- 如果下一步涉及真实机会，另开外部机会 case。",
        "decision_boundary": "真实反馈为空，内部流程测试不能写成市场验证、产品化或 SaaS 结论。",
        "report_boundary": "本报告只证明内部工作流机制完成一次优化，不证明外部用户需求、市场采用或产品化可行性。",
        "candidate_capability_rows": "| Skill: signalproof | 是 | 是 | 强 | 已读取 repo skill，确认必需 case 文件、插件记录、真实反馈和验证命令规则。 | 保留为默认入口。 |\n| Skill: user-working-profile | 是 | 是 | 强 | 已读取用户偏好，确认中文、边界、证据和少追问多执行。 | 保留。 |\n| Memory | 是 | 是 | 中 | 用于复核历史 SignalProof 方向和插件审计口径；只作上下文，不替代当前仓库证据。 | 需要历史口径时轻量使用。 |\n| last30days | 条件相关 | 未使用 | 中 | 本 case 是内部工作流机制审计，外部趋势不会改变脚本和模板判断。 | 真实外部机会 case 再运行。 |\n| Browser / Chrome | 条件相关 | 未使用 | 中 | 本轮没有网页、登录态或报告预览验收目标。 | 有页面验收时再用。 |\n| Computer Use | 条件相关 | 未使用 | 中 | 本轮没有 GUI-only 验收目标。 | 有本地 App 操作验收时再用。 |\n| Record & Replay | 条件相关 | 未使用 | 中 | 本轮没有用户演示录制目标。 | 需要沉淀操作流程时再用。 |\n| Documents / PDF / Spreadsheets / Presentations | 条件相关 | 未使用 | 中 | 本轮产物是 Markdown、模板和 Python 脚本。 | 正式资料包或格式产物再用。 |\n| Plugin / MCP | 是 | 使用本地脚本和已读插件流程文档 | 中 | 记录安装、暴露、授权、证据质量分层；没有默认全跑外部 connector。 | 具体 case 再做只读探针。 |",
        "tool_research_rows": "| 公开讨论 | 覆盖当前用户任务，未做外部扩散扫描 | weak | 本轮是内部流程审计，公开讨论不构成市场证据。 | 真实机会 case 再补。 |\n| 项目和数据 | 已覆盖仓库文件、脚本、模板、case 和 runs | strong | 可判断本地机制是否真实改变。 | 继续用脚本验证。 |\n| 官方和一手资料 | 已覆盖 AGENTS、repo skill、协议和质量门文档 | strong | 本轮按用户指定文档执行。 | 官方联网事实变更时再查。 |\n| 反证和替代方案 | 已覆盖原报告缺口、strict 漏检占位风险、connector 授权缺口 | medium | 反证足以支持新增脚本 gate。 | 后续 connector case 再探针。 |\n| 结论许可 | 已覆盖 | medium | 只允许内部机制优化和低成本实验。 | 不写市场验证。 |",
        "stage_plugin_rows": "| signal | Browser / Chrome / Record & Replay | 未使用 | 中 | 信号来自当前会话和本地仓库，不需要网页、登录态或录制。 | 保留为条件候选。 |\n| research | GitHub / last30days / OpenAI Docs / Browser / Documents / PDF / Spreadsheets | 部分使用本地文件和记忆；未调用外部插件 | 中 | 本轮按用户指定本地文档复核，外部趋势不会改变内部脚本判断。 | 真实外部机会 case 再跑。 |\n| debate | Browser / Chrome / Documents / PDF | 未使用 | 中 | 反证来自本地 case、diff 和脚本行为。 | 外部反证依赖页面时再用。 |\n| validation | 本地脚本 / Browser / Computer Use / Documents / PDF / Spreadsheets / Presentations | 使用本地脚本 | 强 | 本轮产物是 Markdown 和 Python 脚本，不需要 GUI 或格式插件。 | 按最终命令验证。 |\n| artifact | Documents / PDF / Spreadsheets / Presentations / HyperFrames / Data Visualization | 未使用 | 中 | 产物是本地 Markdown、模板和脚本。 | 正式资料包再启用。 |\n| publication | Browser / Chrome | 未使用 | 弱 | 未发布。 | 有公开 URL 时再验收。 |\n| feedback | Chrome / Browser / Spreadsheets / Record & Replay | 未使用 | 弱 | 真实反馈为空。 | 外部反馈恢复后再用。 |\n| asset | Documents / PDF / Spreadsheets / Presentations / Record & Replay / Browser | 未使用 | 中 | 资产沉淀为本地规则和 case。 | 需要演示或资料包时再用。 |\n| flow-review | 本地脚本 / Browser / Computer Use / Documents / PDF / Spreadsheets / Presentations | 使用本地脚本 | 强 | 指定验证命令足以验收本轮机制。 | 保留脚本 gate。 |",
    },
    "plugin-test": {
        "case_type_label": "插件流程试跑",
        "why_enter_flow": "- 这条信号用于验证某个 Codex skill、plugin、MCP 或本地工具是否能改变判断、减少不确定性或验收产物。\n- 本 case 只能证明工具调用路径、授权缺口、失败降级或产物验收能力，不证明外部机会成立。",
        "initial_users": "- SignalProof 维护者。\n- 需要把工具能力纳入个人工作流，但不想把插件安装状态误写成证据的人。",
        "current_boundary": "- 不声称市场验证。\n- 不默认产品化。\n- 不默认全跑插件。\n- 插件安装、状态快照或 marketplace 可见性不等于工具可用或证据成立。",
        "research_process": "- 读取插件说明、repo 协议、能力矩阵和迁移文档。\n- 做最小只读探针，记录成功、失败、阻塞和降级路径。\n- 判断工具结果是否改变本 case 的判断，而不是只记录调用成功。",
        "source_coverage_rows": "| 公开讨论 | 当前未覆盖 | 未覆盖 | weak | 本 case 目标不是市场判断。 |\n| 项目和数据 | 插件 manifest、能力矩阵、状态快照、只读探针 | 已覆盖 | medium | 能支持工具流程判断。 |\n| 官方和一手资料 | 插件 skill、官方文档或 repo 文档 | 按需覆盖 | medium | 需要记录版本和入口。 |\n| 反证和替代方案 | 授权失败、工具未暴露、降级命令、本地脚本替代 | 已覆盖 | medium | 能避免工具崇拜。 |",
        "cross_validation": "- 谁在说：当前 case、插件文档、脚本输出或只读探针。\n- 说什么：工具是否可用、结果是否相关、失败如何降级。\n- 在哪里说：tool-ledger、process-log、flow-review。\n- 有没有反证：插件可能未授权、未暴露、结果弱或不会改变判断。\n- 能支持什么结论：只能支持保留、条件使用、降级或移出候选能力。",
        "counterevidence": "- 插件可见但账号未授权。\n- 插件调用成功但结果不相关。\n- 本地脚本或官方文档已经足够，不需要额外 connector。",
        "evidence_grade": "当前证据等级：medium。工具路径和本地探针可以支持流程判断；外部用户需求仍为 weak。",
        "decision_permission": "当前许可：低成本内部实验或条件保留工具。不得写成市场验证或产品化结论。",
        "next_evidence_steps": "- 做最小只读探针。\n- 把失败和降级写入工具账本。\n- 判断是否改变本 case 决策。",
        "feedback_empty_reason": "本 case 是工具流程试跑，没有真实目标用户反馈；真实反馈为空。",
        "validation_object": "候选工具是否能改变判断、减少不确定性或验收产物。",
        "validation_method_steps": "1. 读取插件 skill 或官方文档。\n2. 运行最小只读探针。\n3. 保存成功输出或失败错误。\n4. 在 `tool-ledger.md` 判断结果质量。\n5. 运行 `python3 scripts/signalproof.py check-case <case-slug> --strict`。",
        "product_spec": "- 目标用户：SignalProof 维护者。\n- 目标任务：判断候选工具是否值得纳入某个阶段。\n- 非目标：不证明市场需求，不扩大插件治理范围。\n- 成功标准：工具结果质量、失败原因、降级路径和是否改变判断都被记录。",
        "eval_set": "- 通过样例：工具探针有原始结果或明确失败原因，并写入 `tool-ledger.md`。\n- 失败样例：只写“已安装”或“已调用”，不判断结果质量。\n- 回归检查：`check-case --strict` 不允许模板占位和过度声称。",
        "agentic_acceptance": "- agentic loop 本轮为 optional；只有工具用于构建或验收产物时才启动。",
        "artifact_summary": "本 case 的产物是候选工具的流程试跑记录、失败降级路径和可复用工具选择规则。",
        "asset_type": "工具评估和能力治理案例。",
        "asset_reusable_content": "- 工具选择规则。\n- 只读探针记录。\n- 失败降级路径。\n- 是否改变判断的标准。",
        "decision_default": "条件保留、降级使用或移出候选能力。",
        "decision_reason": "- 工具只有在改变判断、减少不确定性或验收产物时才有价值。\n- 插件治理只作为候选能力治理，不作为证据本身。",
        "decision_next_steps": "- 若工具结果强，写入对应阶段候选能力。\n- 若结果弱或失败，记录降级路径。\n- 若需要真实数据授权，明确交给用户授权或暂停。",
        "decision_boundary": "工具试跑不能证明外部机会成立，也不能替代真实反馈。",
        "report_boundary": "本报告只证明工具流程状态，不证明市场需求、用户采用或产品化可行性。",
        "candidate_capability_rows": "| Skill: signalproof | 是 | 是 | 强 | 提供本地流程规则。 | 保留。 |\n| Plugin / MCP | 是 | 按本 case 选择 | 待评估 | 候选工具是本 case 目标。 | 只做最小必要探针。 |\n| Browser / Chrome | 条件相关 | 按需 | 中 | 页面或登录态验收时使用。 | 需要时再启用。 |\n| 本地脚本 | 是 | 是 | 强 | 用于确定性检查和降级。 | 保留。 |",
        "tool_research_rows": "| 来源覆盖 | 已覆盖工具文档和本地探针 | medium | 本 case 只判断工具流程。 | 需要外部机会时另开 case。 |\n| 交叉验证 | 已覆盖工具结果和降级路径 | medium | 不把调用成功写成证据合格。 | 继续记录失败原因。 |\n| 反证 | 已覆盖授权、未暴露、弱结果风险 | medium | 防止工具崇拜。 | 必要时移出候选。 |\n| 证据等级 | 已覆盖 | medium | 支持内部工具决策。 | 不支持市场判断。 |\n| 结论许可 | 已覆盖 | medium | 只能保留、降级或暂停工具。 | 不写产品化。 |",
        "stage_plugin_rows": "| signal | Browser / Chrome / Record & Replay | 按需 | 中 | 信号可能来自插件状态或页面。 | 保留条件候选。 |\n| research | 插件 skill / 官方文档 / 本地脚本 | 按需 | medium | 需要确认入口和限制。 | 记录原始来源。 |\n| validation | 本地脚本 / Browser / Computer Use | 按需 | medium | 只读探针或产物验收。 | 失败先记账。 |\n| feedback | Chrome / Browser / Spreadsheets | 未使用 | weak | 真实反馈为空。 | 有真实渠道再用。 |\n| flow-review | 本地脚本 | 使用 | strong | 检查工具是否改变判断。 | 保留 gate。 |",
    },
}


@dataclass
class CaseCheck:
    slug: str
    path: Path
    errors: list[str]
    warnings: list[str]

    @property
    def ok(self) -> bool:
        return not self.errors


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text()


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def has_phrase(text: str, pattern: str) -> bool:
    return re.search(pattern, text, flags=re.IGNORECASE) is not None


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    fields: dict[str, str] = {}
    for raw_line in text[4:end].splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip().strip('"').strip("'")
        fields[key.strip()] = value
    return fields


def parse_int_field(fields: dict[str, str], key: str, warnings: list[str], filename: str) -> int | None:
    raw_value = fields.get(key, "")
    if raw_value == "":
        return None
    try:
        return int(raw_value)
    except ValueError:
        warnings.append(f"{filename} frontmatter field `{key}` must be an integer")
        return None


def missing_frontmatter_fields(fields: dict[str, str], required: list[str]) -> list[str]:
    return [key for key in required if fields.get(key, "") == ""]


def normalize_scalar(value: str) -> str:
    return value.strip().strip("`").strip().lower()


def parse_asset_registry_rows() -> list[dict[str, str]]:
    if not ASSET_REGISTRY.exists():
        return []
    rows: list[dict[str, str]] = []
    headers: list[str] = []
    for raw_line in read_text(ASSET_REGISTRY).splitlines():
        line = raw_line.strip()
        if not line.startswith("|") or "---" in line:
            continue
        cells = [cell.strip().strip("`") for cell in line.strip("|").split("|")]
        if not headers:
            headers = cells
            continue
        if len(cells) != len(headers):
            continue
        rows.append(dict(zip(headers, cells)))
    return rows


def asset_registry_contains(asset_text: str) -> bool:
    rows = parse_asset_registry_rows()
    if not rows:
        return False
    lowered_asset = asset_text.lower()
    for row in rows:
        for key in ("asset_id", "title"):
            value = normalize_scalar(row.get(key, ""))
            if value and value.lower() in lowered_asset:
                return True
    return False


def scrub_boundaries(text: str) -> str:
    boundary_patterns = [
        r"不能写[“\"]?验证成功",
        r"不能声称市场已验证",
        r"不能声称[^\n。]*验证成功",
        r"不能说[“\"]?市场已验证",
        r"不支持[“\"]?验证成功",
        r"不是验证成功",
        r"不能替代真实反馈",
        r"不能把.*写成真实用户反馈",
        r"不可用于：验证成功",
        r"cannot claim market validation",
        r"not market validation",
    ]
    scrubbed = text
    for pattern in boundary_patterns:
        scrubbed = re.sub(pattern, "", scrubbed, flags=re.IGNORECASE)
    return scrubbed


def has_overclaim(text: str) -> bool:
    scrubbed = scrub_boundaries(text)
    patterns = [
        r"已验证需求",
        r"市场已验证",
        r"验证成功",
        r"可以开始做插件/SaaS",
        r"可以产品化",
        r"validated demand",
        r"market validated",
        r"ready for SaaS",
    ]
    return any(has_phrase(scrubbed, pattern) for pattern in patterns)


def unresolved_markers(text: str) -> list[str]:
    markers: list[str] = []
    for index, line in enumerate(text.splitlines(), start=1):
        if any(term in line for term in PLACEHOLDER_CONTEXT_ALLOWLIST):
            continue
        for label, patterns in UNRESOLVED_MARKERS.items():
            if any(has_phrase(line, pattern) for pattern in patterns):
                markers.append(f"line {index}: {label}")
                break
    return markers


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fff]+", "-", title.strip().lower())
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug or "untitled-case"


def today_slug(title: str) -> str:
    return f"{date.today().isoformat()}-{slugify(title)}"


def case_mode_for(case_dir: Path) -> str:
    signal_path = case_dir / "signal.md"
    if not signal_path.exists():
        return "full"
    match = re.search(r"^case_mode:\s*([a-zA-Z0-9_-]+)\s*$", read_text(signal_path), flags=re.MULTILINE)
    if match and match.group(1) == "lite":
        return "lite"
    return "full"


def required_files_for(case_dir: Path) -> list[str]:
    if case_mode_for(case_dir) == "lite":
        return LITE_REQUIRED_FILES
    return REQUIRED_FILES


def default_case_intent(case_type: str) -> str:
    return CASE_TYPE_DEFAULT_INTENT.get(case_type, "external-opportunity")


def loop_defaults_for(case_intent: str) -> dict[str, str]:
    return CASE_INTENT_LOOP_DEFAULTS.get(case_intent, CASE_INTENT_LOOP_DEFAULTS["external-opportunity"])


def diagnose(_: argparse.Namespace | None = None) -> int:
    result = {
        "repo": str(ROOT),
        "python": sys.version.split()[0],
        "last30days_script": str(LAST30DAYS),
        "last30days_script_exists": LAST30DAYS.exists(),
        "recommended_last30days_python": None,
        "last30days_diagnose": None,
        "notes": [],
    }

    for candidate in ["python3.14", "python3.13", "python3.12", "python3"]:
        path = shutil.which(candidate)
        if not path:
            continue
        probe = subprocess.run(
            [path, "-c", "import sys; raise SystemExit(0 if sys.version_info >= (3, 12) else 1)"],
            text=True,
            capture_output=True,
        )
        if probe.returncode == 0:
            result["recommended_last30days_python"] = candidate
            break

    if result["recommended_last30days_python"] and LAST30DAYS.exists():
        proc = subprocess.run(
            [result["recommended_last30days_python"], str(LAST30DAYS), "--diagnose"],
            text=True,
            capture_output=True,
            timeout=60,
        )
        result["last30days_diagnose"] = {
            "returncode": proc.returncode,
            "stdout": proc.stdout.strip(),
            "stderr": proc.stderr.strip(),
        }
        if "Permission denied reading Cookies.binarycookies" in proc.stdout + proc.stderr:
            result["notes"].append("Safari cookie read permission denied; browser-cookie extraction is a capability gap.")

    write_text(RUNS / f"{date.today().isoformat()}-capability-snapshot.json", json.dumps(result, indent=2, ensure_ascii=False))
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


def detect_builtin_plugins() -> dict[str, dict[str, object]]:
    detected: dict[str, dict[str, object]] = {}
    for name, pattern in BUILTIN_PLUGIN_SPECS:
        matches = sorted(PLUGIN_CACHE.glob(pattern))
        detected[name] = {
            "available": bool(matches),
            "path": str(matches[-1]) if matches else None,
        }
    return detected


def capability_matrix(_: argparse.Namespace | None = None) -> int:
    detected = detect_builtin_plugins()
    lines = [
        "# SignalProof Codex 能力矩阵",
        "",
        f"生成日期：{date.today().isoformat()}",
        "",
        "## Codex 自带插件可用性",
        "",
        "| 插件 | 状态 | 本机路径 |",
        "| --- | --- | --- |",
    ]
    for name, info in detected.items():
        status = "available" if info["available"] else "missing"
        path = info["path"] or ""
        lines.append(f"| {name} | {status} | `{path}` |")
    lines.extend([
        "",
        "## 阶段能力计划",
        "",
        "| 阶段 | 目标 | 默认能力 | Codex 自带插件候选 | 何时使用 | 写入位置 |",
        "| --- | --- | --- | --- | --- | --- |",
    ])
    for row in STAGE_CAPABILITY_MATRIX:
        lines.append(
            "| {stage} | {purpose} | {default_capabilities} | {codex_plugins} | {use_when} | {write_to} |".format(
                **row
            )
        )
    lines.extend([
        "",
        "## AI Native Work Loop 能力视角",
        "",
        "这些 loop 来自 Andrew Ng 对 0-to-1 software building 的拆分。SignalProof 只把它们作为本地协议检查点，不把项目扩成 workflow builder。",
        "",
        "| Loop | 目标 | 节奏 | 默认能力 | 写入位置 |",
        "| --- | --- | --- | --- | --- |",
    ])
    for row in LOOP_CAPABILITY_MATRIX:
        lines.append(
            "| {loop} | {purpose} | {cadence} | {default_capabilities} | {writes_to} |".format(
                **row
            )
        )
    lines.extend([
        "",
        "边界：插件和 agent 能力只是候选能力。只有结果改变判断、减少不确定性或验收产物时，才算 loop 产生证据价值。",
    ])
    text = "\n".join(lines) + "\n"
    write_text(RUNS / f"{date.today().isoformat()}-codex-capability-matrix.md", text)
    print(text)
    return 0


def parse_enabled_plugins_from_config() -> list[str]:
    if not CODEX_CONFIG.exists():
        return []
    enabled: list[str] = []
    current: str | None = None
    for raw_line in read_text(CODEX_CONFIG).splitlines():
        line = raw_line.strip()
        match = re.match(r'^\[plugins\."([^"]+)"\]$', line)
        if match:
            current = match.group(1)
            continue
        if current and line == "enabled = true":
            enabled.append(current)
            current = None
        elif line.startswith("["):
            current = None
    return sorted(enabled)


def parse_plugin_list_output(output: str) -> dict[str, list[str]]:
    installed: list[str] = []
    not_installed: list[str] = []
    marketplaces: list[str] = []
    current_marketplace = ""
    for line in output.splitlines():
        market_match = re.match(r"^Marketplace `([^`]+)`", line)
        if market_match:
            current_marketplace = market_match.group(1)
            marketplaces.append(current_marketplace)
            continue
        columns = line.split()
        if not columns or "@" not in columns[0]:
            continue
        plugin = columns[0]
        if current_marketplace and "@" not in plugin:
            plugin = f"{plugin}@{current_marketplace}"
        if "installed, enabled" in line:
            installed.append(plugin)
        elif "not installed" in line:
            not_installed.append(plugin)
    return {
        "marketplaces": sorted(marketplaces),
        "installed": sorted(installed),
        "not_installed": sorted(not_installed),
    }


def parse_marketplace_list_output(output: str) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    for line in output.splitlines():
        if not line.strip() or line.startswith("MARKETPLACE"):
            continue
        parts = line.split(None, 1)
        if len(parts) == 2:
            rows.append((parts[0], parts[1]))
    return rows


def parse_plugin_install_script() -> list[str]:
    if not PLUGIN_INSTALL_SCRIPT.exists():
        return []
    plugins: list[str] = []
    for raw_line in read_text(PLUGIN_INSTALL_SCRIPT).splitlines():
        line = raw_line.strip().strip('"').strip("'")
        if re.match(r"^[a-z0-9][a-z0-9-]*@[a-z0-9-]+$", line):
            plugins.append(line)
    return sorted(set(plugins))


def parse_plugin_lock_doc() -> list[str]:
    if not PLUGIN_LOCK_DOC.exists():
        return []
    plugins: list[str] = []
    for raw_line in read_text(PLUGIN_LOCK_DOC).splitlines():
        match = re.match(r"^\| `([^`]+)` \| `([^`]+)` \|", raw_line.strip())
        if not match:
            continue
        name, source = match.groups()
        if source.startswith("openai-"):
            plugins.append(f"{name}@{source}")
    return sorted(set(plugins))


def parse_plugin_status_snapshot(path: Path) -> dict[str, list[str]]:
    if not path.exists():
        return {"installed": [], "script": []}
    installed: list[str] = []
    script: list[str] = []
    section: str | None = None
    for raw_line in read_text(path).splitlines():
        line = raw_line.strip()
        if line.startswith("## "):
            if "已安装启用的 marketplace 插件" in line:
                section = "installed"
            elif "repo 重装脚本记录的插件" in line:
                section = "script"
            else:
                section = None
            continue
        match = re.match(r"^- `([^`]+)`", line)
        if not match or section not in {"installed", "script"}:
            continue
        if section == "installed":
            installed.append(match.group(1))
        else:
            script.append(match.group(1))
    return {"installed": sorted(set(installed)), "script": sorted(set(script))}


def add_set_diff(
    messages: list[str],
    label: str,
    left_name: str,
    left: set[str],
    right_name: str,
    right: set[str],
) -> None:
    missing = sorted(left - right)
    extra = sorted(right - left)
    if not missing and not extra:
        return
    messages.append(f"{label}: `{left_name}` 和 `{right_name}` 不一致")
    if missing:
        messages.append(f"  - 只在 `{left_name}` 中存在：{', '.join(missing)}")
    if extra:
        messages.append(f"  - 只在 `{right_name}` 中存在：{', '.join(extra)}")


def plugin_drift_report(run_codex: bool) -> tuple[str, list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    lines = [
        "# SignalProof 插件漂移检查",
        "",
        f"生成日期：{date.today().isoformat()}",
        "",
    ]

    lock_plugins = set(parse_plugin_lock_doc())
    script_plugins = set(parse_plugin_install_script())
    snapshot_path = RUNS / f"{date.today().isoformat()}-codex-plugin-status.md"
    snapshot = parse_plugin_status_snapshot(snapshot_path)
    snapshot_installed = set(snapshot["installed"])
    snapshot_script = set(snapshot["script"])
    current_installed: set[str] = set()

    if not PLUGIN_LOCK_DOC.exists():
        errors.append("缺少 docs/codex-plugin-lock.md")
    if not PLUGIN_INSTALL_SCRIPT.exists():
        errors.append("缺少 scripts/install-codex-plugins.sh")
    if not snapshot_path.exists():
        errors.append("缺少当天 plugin-status 快照，请先运行 `python3 scripts/signalproof.py plugin-status`")

    add_set_diff(errors, "锁定清单和安装脚本漂移", "docs/codex-plugin-lock.md", lock_plugins, "scripts/install-codex-plugins.sh", script_plugins)

    if snapshot_script:
        add_set_diff(errors, "状态快照中的脚本清单漂移", "scripts/install-codex-plugins.sh", script_plugins, snapshot_path.name, snapshot_script)

    if snapshot_installed:
        missing_from_snapshot = sorted(script_plugins - snapshot_installed)
        if missing_from_snapshot:
            errors.append("状态快照显示部分锁定插件未安装启用: " + ", ".join(missing_from_snapshot))
        extra_in_snapshot = sorted(snapshot_installed - script_plugins)
        if extra_in_snapshot:
            warnings.append("状态快照存在未写入锁定清单的已安装插件: " + ", ".join(extra_in_snapshot))

    if run_codex:
        proc = subprocess.run(
            ["codex", "plugin", "list"],
            text=True,
            capture_output=True,
            timeout=60,
        )
        if proc.returncode != 0:
            errors.append("无法读取当前 `codex plugin list`，请确认 Codex CLI 可用")
            if proc.stderr.strip():
                warnings.append(proc.stderr.strip())
        else:
            current_installed = set(parse_plugin_list_output(proc.stdout)["installed"])
            missing_current = sorted(script_plugins - current_installed)
            if missing_current:
                errors.append("当前 Codex 环境缺少锁定插件: " + ", ".join(missing_current))
            extra_current = sorted(current_installed - script_plugins)
            if extra_current:
                warnings.append("当前 Codex 环境存在未写入锁定清单的已安装插件: " + ", ".join(extra_current))

    lines.extend([
        "## 对比对象",
        "",
        f"- 锁定清单插件数：{len(lock_plugins)}",
        f"- 安装脚本插件数：{len(script_plugins)}",
        f"- 当天状态快照脚本插件数：{len(snapshot_script)}",
        f"- 当天状态快照已安装插件数：{len(snapshot_installed)}",
    ])
    if run_codex:
        lines.append(f"- 当前 `codex plugin list` 已安装插件数：{len(current_installed)}")
    lines.extend([
        "",
        "## 结论",
        "",
    ])
    if errors:
        lines.append("状态：failed")
    elif warnings:
        lines.append("状态：passed-with-warnings")
    else:
        lines.append("状态：passed")
    lines.append("")
    if errors:
        lines.append("### 错误")
        lines.append("")
        for error in errors:
            lines.append(f"- {error}")
        lines.append("")
    if warnings:
        lines.append("### 警告")
        lines.append("")
        for warning in warnings:
            lines.append(f"- {warning}")
        lines.append("")
    if not errors and not warnings:
        lines.append("- 插件锁定清单、安装脚本、当天状态快照和当前安装列表一致。")
        lines.append("")
    lines.extend([
        "## 边界",
        "",
        "- 本检查只证明插件安装和记录没有漂移。",
        "- 本检查不证明外部账号已授权，也不证明 connector 能读取真实数据。",
        "- 本检查不支持市场验证、产品化或 SaaS 结论。",
    ])
    return "\n".join(lines) + "\n", errors, warnings


def check_plugin_drift(args: argparse.Namespace | None = None) -> int:
    run_codex = not bool(getattr(args, "no_codex", False))
    text, errors, _warnings = plugin_drift_report(run_codex=run_codex)
    write_text(RUNS / f"{date.today().isoformat()}-plugin-drift-check.md", text)
    print(text)
    return 1 if errors else 0


def plugin_status(_: argparse.Namespace | None = None) -> int:
    enabled = parse_enabled_plugins_from_config()
    marketplace_proc = subprocess.run(
        ["codex", "plugin", "marketplace", "list"],
        text=True,
        capture_output=True,
        timeout=30,
    )
    list_proc = subprocess.run(
        ["codex", "plugin", "list"],
        text=True,
        capture_output=True,
        timeout=60,
    )
    marketplace_rows = parse_marketplace_list_output(marketplace_proc.stdout if marketplace_proc.returncode == 0 else "")
    plugin_list = parse_plugin_list_output(list_proc.stdout if list_proc.returncode == 0 else "")
    install_script_plugins = parse_plugin_install_script()
    runtime_plugins = [name for name in enabled if "@openai-primary-runtime" in name]
    runtime_cache_plugins = sorted(
        path.parent.parent.parent.name
        for path in PLUGIN_CACHE.glob("openai-primary-runtime/*/*/.codex-plugin/plugin.json")
    )
    local_signalproof_exists = (ROOT / ".agents" / "plugins" / "marketplace.json").exists() and (
        ROOT / "plugins" / "signalproof" / ".codex-plugin" / "plugin.json"
    ).exists()

    lines = [
        "# Codex 插件状态快照",
        "",
        f"生成日期：{date.today().isoformat()}",
        "",
        "## 结论",
        "",
        f"- `~/.codex/config.toml` 中启用项：{len(enabled)} 个。",
        f"- `codex plugin list` 中已安装启用的 marketplace 插件：{len(plugin_list['installed'])} 个。",
        f"- `codex plugin list` 中未安装的 marketplace 插件：{len(plugin_list['not_installed'])} 个。",
        f"- primary-runtime 配置启用项：{len(runtime_plugins)} 个。",
        f"- primary-runtime 本机缓存可用能力：{len(runtime_cache_plugins)} 个，通常包括 Documents / PDF / Spreadsheets / Presentations。",
        f"- SignalProof 本地 repo marketplace：{'存在' if local_signalproof_exists else '缺失'}。",
        f"- repo 插件锁定清单：{'存在' if PLUGIN_LOCK_DOC.exists() else '缺失'}。",
        f"- repo 插件重装脚本：{'存在' if PLUGIN_INSTALL_SCRIPT.exists() else '缺失'}，脚本记录 {len(install_script_plugins)} 个插件。",
        "",
        "## 怎么看是否安装",
        "",
        "- 以 `codex plugin list` 的 `STATUS` 列为准：只有 `installed, enabled` 才是已安装启用。",
        "- `not installed` 只是 marketplace 里可选但没有安装的插件，会和已安装插件一起显示。",
        "- `~/.codex/config.toml` 里的 `[plugins.\"...\"] enabled = true` 是本机启用状态；它不是 repo 内容，换机器不会自动跟着仓库走。",
        "- 插件安装后通常要开启新线程才会进入新会话的技能/工具上下文。",
        "- skills 初始列表有上下文预算，插件多时界面可能不展示全部 skills；选中或显式调用后仍会读取完整 `SKILL.md`。",
        "- app connector、MCP server 和外部账号授权是独立层；插件已安装不等于 connector 已能读取真实数据。",
        "",
        "## marketplace",
        "",
        "| 名称 | 路径 |",
        "| --- | --- |",
    ]
    for name, path in marketplace_rows:
        lines.append(f"| `{name}` | `{path}` |")
    lines.extend([
        "",
        "## 已安装启用的 marketplace 插件",
        "",
    ])
    for name in plugin_list["installed"]:
        lines.append(f"- `{name}`")
    lines.extend([
        "",
        "## repo 重装脚本记录的插件",
        "",
        "这些插件由 `scripts/install-codex-plugins.sh` 记录，用于换电脑后重装。脚本只保存插件名，不保存 OAuth、cookie、API key。",
        "",
    ])
    installed_set = set(plugin_list["installed"])
    for name in install_script_plugins:
        state = "installed, enabled" if name in installed_set else "not installed or not visible in current marketplace list"
        lines.append(f"- `{name}`：{state}")
    lines.extend([
        "",
        "## primary-runtime / 配置启用项",
        "",
    ])
    for name in runtime_plugins:
        lines.append(f"- `{name}`")
    lines.extend([
        "",
        "## primary-runtime / 本机缓存可用能力",
        "",
    ])
    for name in runtime_cache_plugins:
        lines.append(f"- `{name}`")
    lines.extend([
        "",
        "## 可迁移性判断",
        "",
        "| 对象 | 能否跟仓库迁移 | 说明 |",
        "| --- | --- | --- |",
        "| `plugins/signalproof/` | 可以 | repo 内本地插件源码，应纳入版本控制。 |",
        "| `.agents/plugins/marketplace.json` | 可以 | repo marketplace 入口，应纳入版本控制。 |",
        "| `.agents/skills/signalproof/` | 可以 | repo skill，可随仓库迁移。 |",
        "| `vault/` 与 `templates/` | 可以 | SignalProof 的主要事实资产。 |",
        "| `docs/codex-plugin-lock.md` | 可以 | 插件锁定清单，记录应该安装哪些插件和迁移策略。 |",
        "| `scripts/install-codex-plugins.sh` | 可以 | 新机器重装官方插件的脚本，只保存插件名。 |",
        "| `~/.codex/config.toml` 的插件启用项 | 不能自动随 repo 迁移 | 新机器需要重新安装或导入对应 marketplace，再启用插件。 |",
        "| 官方/curated 插件缓存 | 不建议直接迁移 | 缓存路径和版本与本机 Codex 相关，应该用 `codex plugin add` 或插件目录重新安装。 |",
        "| 外部账号 OAuth / 浏览器登录态 / API key | 不应随 repo 迁移 | 需要在新机器按账号重新授权，避免泄露凭据。 |",
        "",
        "## 迁移时最小清单",
        "",
        "1. 克隆或复制 SignalProof 仓库。",
        "2. 确认 `.agents/plugins/marketplace.json` 和 `plugins/signalproof/.codex-plugin/plugin.json` 存在。",
        "3. 运行 `bash scripts/install-codex-plugins.sh` 重装官方插件。",
        "4. 在新机器运行 `codex plugin marketplace list`，确认是否能看到需要的 marketplace。",
        "5. 新开 Codex 线程，再检查技能和工具是否出现。",
        "6. 运行 `python3 scripts/signalproof.py capabilities` 和 `python3 scripts/signalproof.py plugin-status` 复核。",
        "7. 对 Readwise、Scite、Semrush、Similarweb、Brand24、Google Drive、Notion 等外部 app connector 重新登录授权。",
        "",
        "## 官方文档复核",
        "",
        "- OpenAI Codex Plugins 文档：插件可以包含 Skills、Apps 和 MCP servers；安装后开启新线程使用；外部 app 可能在安装或首次使用时要求授权。",
        "- OpenAI Agent Skills 文档：skills 使用渐进加载，初始列表只展示有限元信息；repo skills 位于 `.agents/skills`，适合随仓库迁移。",
        "- OpenAI Build Plugins 文档：repo marketplace 可放在 `$REPO_ROOT/.agents/plugins/marketplace.json`，插件源码可放在 `$REPO_ROOT/plugins/`；添加或修改本地插件后需要重启 Codex。",
        "- OpenAI MCP 文档：插件可以携带 MCP server 配置，但外部工具、认证和 tool policy 仍需要单独生效。",
        "- SignalProof 本地规则：插件或流程更新时，同步更新 `docs/codex-plugin-lock.md`、`scripts/install-codex-plugins.sh` 和本状态快照。",
        "",
        "## 官方依据",
        "",
        "- OpenAI Codex Plugins 文档：插件浏览器按 marketplace 分组；安装后新开线程使用；外部 app 可能在安装或首次使用时要求授权。",
        "- OpenAI Build Plugins 文档：可用 `codex plugin marketplace add` 添加本地路径、GitHub repo、Git URL 或 sparse marketplace。",
    ])
    text = "\n".join(lines) + "\n"
    write_text(RUNS / f"{date.today().isoformat()}-codex-plugin-status.md", text)
    print(text)
    return 0 if marketplace_proc.returncode == 0 and list_proc.returncode == 0 else 1


def init_case(args: argparse.Namespace) -> int:
    slug = args.slug or today_slug(args.title)
    case_dir = CASES / slug
    case_dir.mkdir(parents=True, exist_ok=True)
    preset = CASE_TYPE_PRESETS.get(args.case_type, CASE_TYPE_PRESETS["external-opportunity"])
    case_intent = args.case_intent or default_case_intent(args.case_type)
    loop_defaults = loop_defaults_for(case_intent)
    context = {
        "slug": slug,
        "title": args.title,
        "case_type": args.case_type,
        "case_intent": case_intent,
        "case_mode": args.case_mode,
        "loop_profile": "ai-work-loop-v1",
        **loop_defaults,
        "signal": args.signal or args.title,
        "created_at": date.today().isoformat(),
        "assumed_feedback": "yes" if args.assumed_feedback else "no",
    }
    context.update(preset)
    required_files = LITE_REQUIRED_FILES if args.case_mode == "lite" else REQUIRED_FILES
    for name in required_files:
        path = case_dir / name
        if path.exists() and not args.force:
            continue
        template = template_for(name)
        write_text(path, render_template(template, context))
    if args.assumed_feedback:
        write_text(case_dir / "assumed-feedback.md", render_template(template_for("assumed-feedback.md"), context))
    print(case_dir)
    return 0


def template_for(name: str) -> str:
    path = TEMPLATES / name
    if path.exists():
        return read_text(path)
    title = name.removesuffix(".md").replace("-", " ").title()
    return f"# {title}\n\nTODO\n"


def render_template(template: str, context: dict[str, str]) -> str:
    text = template
    for key, value in context.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def check_case(case_dir: Path) -> CaseCheck:
    errors: list[str] = []
    warnings: list[str] = []
    slug = case_dir.name
    if not case_dir.is_dir():
        return CaseCheck(slug, case_dir, [f"not a directory: {case_dir}"], [])

    required_files = required_files_for(case_dir)
    for name in required_files:
        path = case_dir / name
        if not path.exists():
            errors.append(f"missing required file: {name}")
            continue
        text = read_text(path)
        if not text.strip():
            errors.append(f"empty required file: {name}")
        markers = unresolved_markers(text)
        if markers:
            warnings.append(f"{name} has unresolved marker(s): {', '.join(markers[:5])}")

    feedback_path = case_dir / "feedback.md"
    decision_path = case_dir / "decision.md"
    tool_ledger_path = case_dir / "tool-ledger.md"
    process_log_path = case_dir / "process-log.md"
    research_path = case_dir / "research.md"
    signal_path = case_dir / "signal.md"
    validation_path = case_dir / "validation.md"
    assumed_path = case_dir / "assumed-feedback.md"

    if feedback_path.exists():
        feedback = read_text(feedback_path)
        if has_phrase(feedback, r"真实反馈为空|真实用户反馈为空|real feedback is empty") and has_overclaim(feedback):
            errors.append("feedback.md overclaims despite empty real feedback")
        if (
            has_phrase(feedback, r"假设反馈|assumed feedback|assumption")
            and not has_phrase(feedback, r"假设反馈\s*\n+\s*不需要|不需要.*内部流程|not needed")
            and not assumed_path.exists()
        ):
            errors.append("feedback.md references assumed feedback but assumed-feedback.md is missing")

    if decision_path.exists():
        decision = read_text(decision_path)
        if has_phrase(decision, r"真实反馈为空|真实用户反馈为空|real feedback is empty") and has_overclaim(decision):
            errors.append("decision.md overclaims despite empty real feedback")
        if has_phrase(decision, r"assumption|假设评价|中等假设") and not assumed_path.exists():
            errors.append("decision.md uses assumption-based continuation but assumed-feedback.md is missing")

    if tool_ledger_path.exists():
        ledger = read_text(tool_ledger_path)
        for term, patterns in TOOL_LEDGER_TERMS.items():
            if not any(has_phrase(ledger, pattern) for pattern in patterns):
                warnings.append(f"tool-ledger.md missing capability term: {term}")
        if not has_phrase(ledger, r"强|中|弱|失败|strong|medium|weak|failed"):
            warnings.append("tool-ledger.md may not judge result quality / 工具账本可能没有判断结果质量")
        for term, patterns in RESEARCH_GATE_TERMS.items():
            if not any(has_phrase(ledger, pattern) for pattern in patterns):
                warnings.append(f"tool-ledger.md missing research gate term: {term}")

    if research_path.exists():
        research = read_text(research_path)
        for term, patterns in RESEARCH_GATE_TERMS.items():
            if not any(has_phrase(research, pattern) for pattern in patterns):
                warnings.append(f"research.md missing research gate term: {term}")
        check_research_frontmatter(research, warnings)

    if signal_path.exists():
        signal = read_text(signal_path)
        check_signal_frontmatter(signal, warnings)
        if validation_path.exists():
            check_loop_validation_requirements(signal, read_text(validation_path), warnings)

    if feedback_path.exists():
        feedback = read_text(feedback_path)
        decision = read_text(decision_path) if decision_path.exists() else ""
        check_feedback_frontmatter(feedback, decision, errors, warnings)

    asset_path = case_dir / "asset.md"
    if asset_path.exists():
        asset = read_text(asset_path)
        check_asset_frontmatter(asset, errors, warnings)

    if process_log_path.exists():
        process = read_text(process_log_path)
        for term, patterns in PROCESS_TERMS.items():
            if not any(has_phrase(process, pattern) for pattern in patterns):
                warnings.append(f"process-log.md missing process term: {term}")

    for name in OPTIONAL_FILES:
        path = case_dir / name
        if path.exists() and not read_text(path).strip():
            errors.append(f"empty optional file: {name}")

    return CaseCheck(slug, case_dir, errors, warnings)


def check_research_frontmatter(text: str, warnings: list[str]) -> None:
    fields = parse_frontmatter(text)
    missing = missing_frontmatter_fields(fields, STRUCTURED_RESEARCH_FIELDS)
    if missing:
        warnings.append("research.md missing structured frontmatter field(s): " + ", ".join(missing))
        return

    evidence_grade = normalize_scalar(fields["evidence_grade"])
    permission = normalize_scalar(fields["permission"])
    if evidence_grade not in ALLOWED_EVIDENCE_GRADES:
        warnings.append("research.md frontmatter `evidence_grade` must be strong / medium / weak / blocked")
    if permission not in ALLOWED_RESEARCH_PERMISSIONS:
        warnings.append("research.md frontmatter `permission` must be continue-research / low-cost-experiment / pause / abandon")

    source_types = parse_int_field(fields, "source_types_covered", warnings, "research.md")
    primary_sources = parse_int_field(fields, "primary_source_count", warnings, "research.md")
    external_quotes = parse_int_field(fields, "external_quote_count", warnings, "research.md")
    counterevidence = parse_int_field(fields, "counterevidence_count", warnings, "research.md")
    parse_int_field(fields, "independent_source_count", warnings, "research.md")

    if permission == "low-cost-experiment":
        if source_types is None or source_types < 2:
            warnings.append("research.md `permission=low-cost-experiment` requires source_types_covered >= 2")
        if counterevidence is None or counterevidence < 1:
            warnings.append("research.md `permission=low-cost-experiment` requires counterevidence_count >= 1")
    if evidence_grade == "strong":
        if source_types is None or source_types < 3:
            warnings.append("research.md `evidence_grade=strong` requires source_types_covered >= 3")
        source_or_quote_count = (primary_sources or 0) + (external_quotes or 0)
        if source_or_quote_count < 1:
            warnings.append("research.md `evidence_grade=strong` requires primary_source_count + external_quote_count >= 1")


def check_signal_frontmatter(text: str, warnings: list[str]) -> None:
    fields = parse_frontmatter(text)
    missing = missing_frontmatter_fields(fields, STRUCTURED_SIGNAL_FIELDS)
    if missing:
        warnings.append("signal.md missing loop frontmatter field(s): " + ", ".join(missing))
        return

    case_intent = normalize_scalar(fields["case_intent"])
    loop_profile = normalize_scalar(fields["loop_profile"])
    agentic_loop = normalize_scalar(fields["agentic_loop"])
    developer_feedback_loop = normalize_scalar(fields["developer_feedback_loop"])
    external_feedback_loop = normalize_scalar(fields["external_feedback_loop"])
    asset_loop = normalize_scalar(fields["asset_loop"])

    if case_intent not in ALLOWED_CASE_INTENTS:
        warnings.append("signal.md frontmatter `case_intent` has unsupported value")
    if loop_profile not in ALLOWED_LOOP_PROFILES:
        warnings.append("signal.md frontmatter `loop_profile` must be ai-work-loop-v1")
    if agentic_loop not in ALLOWED_AGENTIC_LOOP_STATUS:
        warnings.append("signal.md frontmatter `agentic_loop` must be required / optional / skipped")
    if developer_feedback_loop not in ALLOWED_DEVELOPER_FEEDBACK_LOOP_STATUS:
        warnings.append("signal.md frontmatter `developer_feedback_loop` must be required / optional / skipped")
    if external_feedback_loop not in ALLOWED_EXTERNAL_FEEDBACK_LOOP_STATUS:
        warnings.append("signal.md frontmatter `external_feedback_loop` must be required / delayed / skipped-with-reason")
    if asset_loop not in ALLOWED_ASSET_LOOP_STATUS:
        warnings.append("signal.md frontmatter `asset_loop` must be required / optional / skipped")


def check_loop_validation_requirements(signal_text: str, validation_text: str, warnings: list[str]) -> None:
    fields = parse_frontmatter(signal_text)
    agentic_loop = normalize_scalar(fields.get("agentic_loop", ""))
    if agentic_loop == "required":
        for heading in ["Product Spec", "Eval Set"]:
            if not re.search(r"^##\s+" + re.escape(heading) + r"\s*$", validation_text, flags=re.MULTILINE):
                warnings.append(f"validation.md missing `{heading}` while agentic_loop=required")


def check_feedback_frontmatter(text: str, decision: str, errors: list[str], warnings: list[str]) -> None:
    fields = parse_frontmatter(text)
    missing = missing_frontmatter_fields(fields, STRUCTURED_FEEDBACK_FIELDS)
    if missing:
        warnings.append("feedback.md missing structured frontmatter field(s): " + ", ".join(missing))
        return

    feedback_status = normalize_scalar(fields["feedback_status"])
    validation_status = normalize_scalar(fields["validation_status"])
    if feedback_status not in ALLOWED_FEEDBACK_STATUS:
        warnings.append("feedback.md frontmatter `feedback_status` has unsupported value")
    if validation_status not in ALLOWED_VALIDATION_STATUS:
        warnings.append("feedback.md frontmatter `validation_status` has unsupported value")

    parse_int_field(fields, "real_feedback_count", warnings, "feedback.md")
    parse_int_field(fields, "paid_signal_count", warnings, "feedback.md")
    parse_int_field(fields, "published_url_count", warnings, "feedback.md")

    if feedback_status in NON_REAL_FEEDBACK_STATUS and has_overclaim(decision):
        errors.append("decision.md overclaims despite non-real feedback_status")
    if validation_status == "published" and feedback_status in NON_REAL_FEEDBACK_STATUS:
        warnings.append("feedback.md `validation_status=published` is not externally-observed; keep published-no-feedback separate from validation")


def check_asset_frontmatter(text: str, errors: list[str], warnings: list[str]) -> None:
    fields = parse_frontmatter(text)
    missing = missing_frontmatter_fields(fields, STRUCTURED_ASSET_FIELDS)
    if missing:
        warnings.append("asset.md missing structured frontmatter field(s): " + ", ".join(missing))
        return

    asset_status = normalize_scalar(fields["asset_status"])
    if asset_status not in ALLOWED_ASSET_STATUS:
        warnings.append("asset.md frontmatter `asset_status` has unsupported value")

    reuse_count = parse_int_field(fields, "reuse_count", warnings, "asset.md")
    proof_of_reuse = normalize_scalar(fields.get("proof_of_reuse", ""))
    if asset_status == "reused":
        if reuse_count is None or reuse_count < 1:
            warnings.append("asset.md `asset_status=reused` requires reuse_count >= 1")
        if proof_of_reuse in {"", "none"}:
            warnings.append("asset.md `asset_status=reused` requires proof_of_reuse != none")
    if asset_status in {"registered", "reused"} and not asset_registry_contains(text):
        errors.append("asset.md claims registered/reused but registry has no matching asset_id or title")


def print_check(check: CaseCheck) -> None:
    status = "PASSED" if check.ok else "FAILED"
    print(f"{check.slug}: {status}")
    for error in check.errors:
        print(f"  ERROR: {error}")
    for warning in check.warnings:
        print(f"  WARNING: {warning}")


def check_all(_: argparse.Namespace) -> int:
    CASES.mkdir(parents=True, exist_ok=True)
    checks = [check_case(path) for path in sorted(CASES.iterdir()) if path.is_dir()]
    if not checks:
        print("No cases found.")
        return 1
    for check in checks:
        print_check(check)
    failed = [check for check in checks if not check.ok]
    warning_count = sum(len(check.warnings) for check in checks)
    if failed:
        overall = "failed"
    elif warning_count:
        overall = "passed-with-warnings"
    else:
        overall = "passed"
    print(f"Checked {len(checks)} case(s), failures: {len(failed)}, warnings: {warning_count}")
    print(f"Overall status: {overall}")
    return 1 if failed else 0


def row_int(row: dict[str, str], key: str) -> int:
    value = normalize_scalar(row.get(key, ""))
    if value in {"", "none", "unknown"}:
        return 0
    try:
        return int(value)
    except ValueError:
        return 0


def check_assets(args: argparse.Namespace) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    if not ASSET_REGISTRY.exists():
        errors.append("registry does not exist: vault/assets/registry.md")
        rows: list[dict[str, str]] = []
    else:
        rows = parse_asset_registry_rows()

    required_columns = {
        "asset_id",
        "title",
        "type",
        "source_case",
        "strength",
        "usable_for",
        "last_used_by",
        "reuse_count",
        "proof_of_reuse",
        "reuse_cost_minutes",
        "preconditions",
        "public_or_private",
        "supersedes",
        "owner_scope",
        "next_action",
    }
    if ASSET_REGISTRY.exists():
        text = read_text(ASSET_REGISTRY)
        header_line = next((line for line in text.splitlines() if line.startswith("| asset_id |")), "")
        headers = {cell.strip() for cell in header_line.strip("|").split("|")} if header_line else set()
        missing_columns = sorted(required_columns - headers)
        if missing_columns:
            errors.append("asset registry missing column(s): " + ", ".join(missing_columns))

    registered_assets = len(rows)
    reused_assets = 0
    candidate_assets = 0
    zero_reuse_assets = 0
    strong_zero_reuse: list[str] = []

    for row in rows:
        asset_id = row.get("asset_id", "")
        reuse_count = row_int(row, "reuse_count")
        last_used_by = normalize_scalar(row.get("last_used_by", ""))
        proof_of_reuse = normalize_scalar(row.get("proof_of_reuse", ""))
        strength = normalize_scalar(row.get("strength", ""))
        asset_status = normalize_scalar(row.get("asset_status", ""))

        if reuse_count > 0 or proof_of_reuse not in {"", "none", "unknown"}:
            reused_assets += 1
        if asset_status == "candidate" or reuse_count == 0:
            candidate_assets += 1
        if reuse_count == 0 or last_used_by in {"", "none", "unknown"}:
            zero_reuse_assets += 1
            warnings.append(f"{asset_id or row.get('title', 'unknown asset')} has no proven reuse")
            if strength == "strong":
                strong_zero_reuse.append(asset_id or row.get("title", "unknown asset"))

    if getattr(args, "strict", False) and strong_zero_reuse:
        errors.append("strong asset(s) with reuse_count=0 or last_used_by=none: " + ", ".join(strong_zero_reuse))

    ratio = (zero_reuse_assets / registered_assets * 100) if registered_assets else 0.0
    if errors:
        status = "failed"
    elif warnings:
        status = "passed-with-warnings"
    else:
        status = "passed"

    print(f"registered_assets: {registered_assets}")
    print(f"reused_assets: {reused_assets}")
    print(f"candidate_assets: {candidate_assets}")
    print(f"zero_reuse_assets: {zero_reuse_assets}")
    print(f"zero_reuse_ratio: {ratio:.1f}%")
    print(f"status: {status}")
    for error in errors:
        print(f"ERROR: {error}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    return 1 if errors else 0


def resolve_case_dir(case: str) -> Path:
    candidate = Path(case)
    if candidate.is_absolute() and candidate.exists():
        return candidate
    direct = CASES / case
    if direct.exists():
        return direct
    matches = sorted(path for path in CASES.iterdir() if path.is_dir() and case in path.name)
    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise FileNotFoundError(f"case not found: {case}")
    names = ", ".join(path.name for path in matches)
    raise ValueError(f"case name is ambiguous: {case}; matches: {names}")


def check_case_command(args: argparse.Namespace) -> int:
    try:
        case_dir = resolve_case_dir(args.case)
    except (FileNotFoundError, ValueError) as exc:
        print(f"SignalProof case check: FAILED")
        print(f"- ERROR: {exc}")
        return 1
    check = check_case(case_dir)
    print_check(check)
    if args.strict and check.warnings:
        print("Strict mode: FAILED")
        for warning in check.warnings:
            print(f"  STRICT: {warning}")
        return 1
    return 0 if check.ok else 1


def list_cases(_: argparse.Namespace) -> int:
    CASES.mkdir(parents=True, exist_ok=True)
    for path in sorted(CASES.iterdir()):
        if path.is_dir():
            print(path.name)
    return 0


def export_case(case_dir: Path) -> Path:
    parts = [
        f"# SignalProof 案例报告：{case_dir.name}\n",
        "\n## 0. 决策先行\n\n",
        decision_summary(case_dir),
        "\n\n## 1. 详细记录\n",
    ]
    for filename, heading in SECTIONS:
        path = case_dir / filename
        if not path.exists():
            continue
        parts.append(f"\n## {heading}\n\n")
        text = read_text(path).strip()
        text = re.sub(r"^# .*$", "", text, count=1, flags=re.MULTILINE).strip()
        parts.append(text + "\n")
    report_path = REPORTS / f"{case_dir.name}.md"
    write_text(report_path, "".join(parts))
    return report_path


def clean_markdown(text: str) -> str:
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.DOTALL)
    text = re.sub(r"^# .*$", "", text, count=1, flags=re.MULTILINE)
    return text.strip()


def section_body(text: str, headings: list[str]) -> str:
    cleaned = clean_markdown(text)
    for heading in headings:
        pattern = r"^##\s+" + re.escape(heading) + r"\s*$\n(?P<body>.*?)(?=^##\s+|\Z)"
        match = re.search(pattern, cleaned, flags=re.MULTILINE | re.DOTALL)
        if match and match.group("body").strip():
            return match.group("body").strip()
    return ""


def summarize_block(text: str, max_lines: int = 4) -> str:
    lines = []
    in_fence = False
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or not line or line.startswith("| ---"):
            continue
        lines.append(line)
        if len(lines) >= max_lines:
            break
    return "\n".join(lines) if lines else "未记录"


def frontmatter_value(text: str, key: str) -> str:
    match = re.search(r"^" + re.escape(key) + r":\s*(.+?)\s*$", text, flags=re.MULTILINE)
    return match.group(1).strip() if match else ""


def file_section_summary(case_dir: Path, filename: str, headings: list[str], fallback: str = "未记录") -> str:
    path = case_dir / filename
    if not path.exists():
        return fallback
    body = section_body(read_text(path), headings)
    return summarize_block(body) if body else fallback


def decision_summary(case_dir: Path) -> str:
    signal_text = read_text(case_dir / "signal.md") if (case_dir / "signal.md").exists() else ""
    research_text = read_text(case_dir / "research.md") if (case_dir / "research.md").exists() else ""
    decision_text = read_text(case_dir / "decision.md") if (case_dir / "decision.md").exists() else ""
    feedback_text = read_text(case_dir / "feedback.md") if (case_dir / "feedback.md").exists() else ""

    signal = summarize_block(section_body(signal_text, ["原始信号"]), max_lines=2) if signal_text else "未记录"
    decision = summarize_block(section_body(decision_text, ["决策", "决策结论"]), max_lines=3) if decision_text else "未记录"
    evidence = summarize_block(section_body(research_text, ["证据等级", "证据强度", "证据质量"]), max_lines=4) if research_text else "未记录"
    if evidence == "未记录" and research_text:
        gate = frontmatter_value(research_text, "gate")
        evidence = gate or "未记录"
    feedback = summarize_block(section_body(feedback_text, ["当前反馈状态", "反馈状态", "真实反馈"]), max_lines=2) if feedback_text else "lite case 未进入反馈阶段"
    next_action = file_section_summary(case_dir, "decision.md", ["下一步", "下一步优先级"], fallback="未记录")
    asset = file_section_summary(case_dir, "asset.md", ["资产名称", "可复用资产", "复用资产", "可复用内容"], fallback="未记录")
    mode = case_mode_for(case_dir)
    if mode == "lite":
        boundary = "lite case 只用于快速判断和资产候选，不代表完整 SignalProof proof；真实反馈为空时不能写成市场验证。"
    else:
        boundary = "full case 只证明本轮已覆盖完整 SignalProof 记录；真实反馈为空时仍不能写成市场验证。"

    return "\n".join([
        f"- case_mode：`{mode}`",
        f"- 信号：{signal}",
        f"- 决策：{decision}",
        f"- 证据等级：{evidence}",
        f"- 反馈状态：{feedback}",
        f"- 可复用资产：{asset}",
        f"- 下一步：{next_action}",
        f"- 边界：{boundary}",
    ])


def export_all(_: argparse.Namespace) -> int:
    REPORTS.mkdir(parents=True, exist_ok=True)
    exported = []
    for case_dir in sorted(CASES.iterdir()):
        if case_dir.is_dir():
            exported.append(export_case(case_dir))
    write_report_index(exported)
    for path in exported:
        print(path)
    return 0


def write_report_index(report_paths: list[Path]) -> None:
    lines = ["# SignalProof 报告索引\n", f"生成日期：{date.today().isoformat()}\n", "## 报告\n"]
    html_items = []
    for path in sorted(report_paths):
        rel = path.relative_to(ROOT)
        lines.append(f"- [{path.stem}]({path.name})")
        html_items.append(f'<li><a href="{path.name}">{path.stem}</a></li>')
    write_text(REPORTS / "index.md", "\n".join(lines))
    html = f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>SignalProof 报告索引</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; margin: 40px; line-height: 1.55; color: #172033; }}
    main {{ max-width: 920px; margin: 0 auto; }}
    h1 {{ font-size: 32px; margin-bottom: 8px; }}
    .meta {{ color: #596579; margin-bottom: 28px; }}
    li {{ margin: 10px 0; }}
    a {{ color: #0f5bd3; text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    .boundary {{ margin-top: 32px; padding: 16px; border-left: 4px solid #d28b00; background: #fff8e6; }}
  </style>
</head>
<body>
  <main>
    <h1>SignalProof 报告索引</h1>
    <p class="meta">生成日期：{date.today().isoformat()}</p>
    <ul>
      {''.join(html_items)}
    </ul>
    <p class="boundary">边界：这些报告只能证明内部协议跑通。本轮故意跳过真实外部反馈和发布渠道验证，不能写成市场验证成功。</p>
  </main>
</body>
</html>"""
    write_text(REPORTS / "index.html", html)


def check_goal(args: argparse.Namespace) -> int:
    CASES.mkdir(parents=True, exist_ok=True)
    case_dirs = [path for path in sorted(CASES.iterdir()) if path.is_dir()]
    checks = [check_case(path) for path in case_dirs]
    errors: list[str] = []
    if len(case_dirs) < args.min_cases:
        errors.append(f"expected at least {args.min_cases} cases, found {len(case_dirs)}")
    for check in checks:
        if not check.ok:
            errors.append(f"{check.slug} failed case check")
    if not (REPORTS / "index.html").exists():
        errors.append("missing vault/reports/index.html; run export-all")
    else:
        html_errors = check_report_index_links(REPORTS / "index.html", min_links=args.min_cases)
        errors.extend(html_errors)
    if not (RUNS / f"{date.today().isoformat()}-capability-snapshot.json").exists():
        errors.append("missing today's capability snapshot; run diagnose")
    if not (RUNS / f"{date.today().isoformat()}-codex-capability-matrix.md").exists():
        errors.append("missing today's Codex capability matrix; run capabilities")
    if not (ROOT / "docs" / "codex-plugin-flow.md").exists():
        errors.append("missing docs/codex-plugin-flow.md")
    agents_path = ROOT / "AGENTS.md"
    if agents_path.exists():
        agents_text = read_text(agents_path)
        for required in ["docs/codex-plugin-lock.md", "scripts/install-codex-plugins.sh", "plugin-status"]:
            if required not in agents_text:
                errors.append(f"AGENTS.md missing plugin sync rule: {required}")
    else:
        errors.append("missing AGENTS.md")
    if not PLUGIN_STATUS_DOC.exists():
        errors.append("missing docs/codex-plugin-status-and-migration.md")
    if not PLUGIN_LOCK_DOC.exists():
        errors.append("missing docs/codex-plugin-lock.md")
    if not PLUGIN_INSTALL_SCRIPT.exists():
        errors.append("missing scripts/install-codex-plugins.sh")
    else:
        install_plugins = parse_plugin_install_script()
        if len(install_plugins) < 10:
            errors.append("scripts/install-codex-plugins.sh has too few plugin entries")
        install_text = read_text(PLUGIN_INSTALL_SCRIPT)
        if "OAuth" not in install_text or "cookie" not in install_text or "API key" not in install_text:
            errors.append("scripts/install-codex-plugins.sh must say credentials are not migrated")
    if not (RUNS / f"{date.today().isoformat()}-codex-plugin-status.md").exists():
        errors.append("missing today's Codex plugin status; run plugin-status")
    if not ASSET_REGISTRY.exists():
        errors.append("missing vault/assets/registry.md")
    elif len(re.findall(r"^\| `[^`]+` \|", read_text(ASSET_REGISTRY), flags=re.MULTILINE)) < 3:
        errors.append("vault/assets/registry.md has too few registered reusable assets")
    drift_text, drift_errors, _drift_warnings = plugin_drift_report(run_codex=False)
    write_text(RUNS / f"{date.today().isoformat()}-plugin-drift-check.md", drift_text)
    errors.extend(drift_errors)
    errors.extend(check_research_gate_assets())
    legacy_dir = CASES / "2026-06-20-ai-coding-repo-context-loss" / "legacy"
    if not legacy_dir.exists() or not any(legacy_dir.iterdir()):
        errors.append("missing migrated legacy artifacts under ai-coding case")
    plugin_errors = check_plugin_marketplace()
    errors.extend(plugin_errors)
    for case_dir in case_dirs:
        feedback_path = case_dir / "feedback.md"
        ledger_path = case_dir / "tool-ledger.md"
        process = read_text(case_dir / "process-log.md") if (case_dir / "process-log.md").exists() else ""
        flow = read_text(case_dir / "flow-review.md") if (case_dir / "flow-review.md").exists() else ""
        feedback = read_text(feedback_path) if feedback_path.exists() else ""
        ledger = read_text(ledger_path) if ledger_path.exists() else ""
        if not any(has_phrase(process, pattern) for pattern in PROCESS_TERMS["Optimization"]):
            errors.append(f"{case_dir.name} process-log.md lacks optimization entries")
        if not has_phrase(flow, r"优化|Optimization|下次"):
            errors.append(f"{case_dir.name} flow-review.md lacks optimization notes")
        if "真实反馈为空" not in feedback:
            errors.append(f"{case_dir.name} feedback.md does not explicitly say real feedback is empty")
        for term, patterns in TOOL_LEDGER_TERMS.items():
            if not any(has_phrase(ledger, pattern) for pattern in patterns):
                errors.append(f"{case_dir.name} tool-ledger.md missing {term}")
    if errors:
        print("SignalProof goal check: FAILED")
        for error in errors:
            print(f"- ERROR: {error}")
        return 1
    print("SignalProof goal check: PASSED")
    print(f"- cases: {len(case_dirs)}")
    print(f"- reports index: {REPORTS / 'index.html'}")
    return 0


def check_research_gate_assets() -> list[str]:
    errors: list[str] = []
    paths = [
        RESEARCH_GATE_DOC,
        TEMPLATES / "research.md",
        TEMPLATES / "tool-ledger.md",
        TEMPLATES / "flow-review.md",
        PLUGIN_LOCK_DOC,
    ]
    for path in paths:
        if not path.exists():
            errors.append(f"missing research gate asset: {path.relative_to(ROOT)}")
            continue
        text = read_text(path)
        for term, patterns in RESEARCH_GATE_TERMS.items():
            if not any(has_phrase(text, pattern) for pattern in patterns):
                errors.append(f"{path.relative_to(ROOT)} missing research gate term: {term}")
    return errors


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.title = ""
        self._in_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "title":
            self._in_title = True
        if tag == "a":
            for key, value in attrs:
                if key == "href" and value:
                    self.links.append(value)

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title += data


def check_report_index_links(index_path: Path, min_links: int) -> list[str]:
    parser = LinkParser()
    parser.feed(read_text(index_path))
    errors: list[str] = []
    if parser.title.strip() not in {"SignalProof 报告索引", "SignalProof Report Index"}:
        errors.append("report index HTML has unexpected title")
    if len(parser.links) < min_links:
        errors.append(f"report index has too few links: {len(parser.links)}")
    for href in parser.links:
        if not (index_path.parent / href).exists():
            errors.append(f"report index link target missing: {href}")
    return errors


def check_plugin_marketplace() -> list[str]:
    errors: list[str] = []
    plugin_manifest = ROOT / "plugins" / "signalproof" / ".codex-plugin" / "plugin.json"
    marketplace = ROOT / ".agents" / "plugins" / "marketplace.json"
    if not plugin_manifest.exists():
        errors.append("missing plugin manifest: plugins/signalproof/.codex-plugin/plugin.json")
        return errors
    if not marketplace.exists():
        errors.append("missing repo marketplace: .agents/plugins/marketplace.json")
        return errors
    try:
        plugin_data = json.loads(read_text(plugin_manifest))
        market_data = json.loads(read_text(marketplace))
    except json.JSONDecodeError as exc:
        errors.append(f"invalid plugin or marketplace JSON: {exc}")
        return errors
    if plugin_data.get("name") != "signalproof":
        errors.append("plugin manifest name must be signalproof")
    entries = market_data.get("plugins", [])
    match = next((entry for entry in entries if entry.get("name") == "signalproof"), None)
    if not match:
        errors.append("marketplace missing signalproof entry")
        return errors
    source_path = match.get("source", {}).get("path")
    if not source_path:
        errors.append("marketplace signalproof entry missing source.path")
        return errors
    resolved = (marketplace.parent / source_path).resolve()
    if not (resolved / ".codex-plugin" / "plugin.json").exists():
        errors.append(f"marketplace source.path does not resolve to plugin manifest: {source_path}")
    policy = match.get("policy", {})
    if policy.get("installation") != "AVAILABLE":
        errors.append("marketplace signalproof policy.installation must be AVAILABLE")
    if policy.get("authentication") != "ON_INSTALL":
        errors.append("marketplace signalproof policy.authentication must be ON_INSTALL")
    if not match.get("category"):
        errors.append("marketplace signalproof entry missing category")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="SignalProof 本地协议自动化。")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("diagnose", help="Record local capability snapshot.").set_defaults(func=diagnose)
    sub.add_parser("capabilities", help="Print the stage-to-Codex-plugin capability matrix.").set_defaults(func=capability_matrix)
    sub.add_parser("plugin-status", help="Record local Codex plugin install and migration status.").set_defaults(func=plugin_status)
    drift = sub.add_parser("check-plugin-drift", help="Check plugin lock, install script, status snapshot, and current Codex install drift.")
    drift.add_argument("--no-codex", action="store_true", help="Skip live `codex plugin list` and only compare repo files plus today's status snapshot.")
    drift.set_defaults(func=check_plugin_drift)
    sub.add_parser("list", help="List cases.").set_defaults(func=list_cases)
    case_check = sub.add_parser("check-case", help="Check one case. Use --strict for new cases so warnings fail.")
    case_check.add_argument("case", help="Case slug, unique slug fragment, or case directory path.")
    case_check.add_argument("--strict", action="store_true", help="Treat warnings as failures for new or actively maintained cases.")
    case_check.set_defaults(func=check_case_command)
    sub.add_parser("check-all", help="Check all cases.").set_defaults(func=check_all)
    assets = sub.add_parser("check-assets", help="Check asset registry reuse ledger.")
    assets.add_argument("--strict", action="store_true", help="Fail if strong assets do not have proven reuse.")
    assets.set_defaults(func=check_assets)
    sub.add_parser("export-all", help="Export all case reports.").set_defaults(func=export_all)
    goal = sub.add_parser("check-goal", help="Check MVP goal evidence.")
    goal.add_argument("--min-cases", type=int, default=5)
    goal.set_defaults(func=check_goal)

    init = sub.add_parser("init-case", help="Create a case from templates.")
    init.add_argument("title")
    init.add_argument("--slug")
    init.add_argument("--signal")
    init.add_argument("--case-type", default="external-opportunity", choices=sorted(CASE_TYPE_PRESETS))
    init.add_argument("--case-intent", choices=sorted(ALLOWED_CASE_INTENTS), help="Work intent: product/content iteration, workflow improvement, tool evaluation, learning-to-asset, or external opportunity.")
    init.add_argument("--case-mode", default="full", choices=["full", "lite"], help="Use lite for fast signal-to-decision screening; full for complete SignalProof proof cases.")
    init.add_argument("--assumed-feedback", action="store_true")
    init.add_argument("--force", action="store_true")
    init.set_defaults(func=init_case)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
