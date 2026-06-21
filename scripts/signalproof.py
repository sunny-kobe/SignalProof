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

RESEARCH_GATE_TERMS = {
    "source coverage": [r"来源覆盖", r"source coverage"],
    "cross validation": [r"交叉验证", r"cross[- ]?validation"],
    "counterevidence": [r"反证", r"替代方案", r"counterevidence"],
    "evidence grade": [r"证据等级", r"strong", r"medium", r"weak", r"blocked"],
    "decision permission": [r"结论许可", r"决策许可", r"低成本实验", r"继续研究"],
    "user authorization": [r"用户授权", r"开通", r"认证", r"auth"],
}

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


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fff]+", "-", title.strip().lower())
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug or "untitled-case"


def today_slug(title: str) -> str:
    return f"{date.today().isoformat()}-{slugify(title)}"


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
    context = {
        "slug": slug,
        "title": args.title,
        "case_type": args.case_type,
        "signal": args.signal or args.title,
        "created_at": date.today().isoformat(),
        "assumed_feedback": "yes" if args.assumed_feedback else "no",
    }
    for name in REQUIRED_FILES:
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

    for name in REQUIRED_FILES:
        path = case_dir / name
        if not path.exists():
            errors.append(f"missing required file: {name}")
            continue
        text = read_text(path)
        if not text.strip():
            errors.append(f"empty required file: {name}")
        if "TODO" in text:
            warnings.append(f"{name} still contains TODO")

    feedback_path = case_dir / "feedback.md"
    decision_path = case_dir / "decision.md"
    tool_ledger_path = case_dir / "tool-ledger.md"
    process_log_path = case_dir / "process-log.md"
    research_path = case_dir / "research.md"
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
    print(f"Checked {len(checks)} case(s), failures: {len(failed)}")
    return 1 if failed else 0


def list_cases(_: argparse.Namespace) -> int:
    CASES.mkdir(parents=True, exist_ok=True)
    for path in sorted(CASES.iterdir()):
        if path.is_dir():
            print(path.name)
    return 0


def export_case(case_dir: Path) -> Path:
    parts = [f"# SignalProof 案例报告：{case_dir.name}\n"]
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
    sub.add_parser("list", help="List cases.").set_defaults(func=list_cases)
    sub.add_parser("check-all", help="Check all cases.").set_defaults(func=check_all)
    sub.add_parser("export-all", help="Export all case reports.").set_defaults(func=export_all)
    goal = sub.add_parser("check-goal", help="Check MVP goal evidence.")
    goal.add_argument("--min-cases", type=int, default=5)
    goal.set_defaults(func=check_goal)

    init = sub.add_parser("init-case", help="Create a case from templates.")
    init.add_argument("title")
    init.add_argument("--slug")
    init.add_argument("--signal")
    init.add_argument("--case-type", default="external-opportunity")
    init.add_argument("--assumed-feedback", action="store_true")
    init.add_argument("--force", action="store_true")
    init.set_defaults(func=init_case)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
