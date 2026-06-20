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
    "Computer Use": [r"Computer Use", r"电脑控制", r"计算机控制"],
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
