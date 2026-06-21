from pathlib import Path

import pdfplumber
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


BASE = Path(__file__).resolve().parent
OUT = BASE / "outputs"
OUT.mkdir(parents=True, exist_ok=True)
PDF = OUT / "plugin-eval-brief.pdf"
TEXT = OUT / "plugin-eval-brief.text.txt"
INSPECT = OUT / "plugin-eval-brief.inspect.txt"
FONT_PATH = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
FONT_NAME = "ArialUnicode"

pdfmetrics.registerFont(TTFont(FONT_NAME, FONT_PATH))

styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    "TitleLocal",
    parent=styles["Title"],
    fontName=FONT_NAME,
    fontSize=20,
    leading=24,
    textColor=colors.HexColor("#0B2545"),
    alignment=0,
    spaceAfter=10,
)
body_style = ParagraphStyle(
    "BodyLocal",
    parent=styles["BodyText"],
    fontName=FONT_NAME,
    fontSize=10.5,
    leading=14,
    spaceAfter=8,
)

doc = SimpleDocTemplate(
    str(PDF),
    pagesize=letter,
    rightMargin=0.8 * inch,
    leftMargin=0.8 * inch,
    topMargin=0.8 * inch,
    bottomMargin=0.8 * inch,
)

story = [
    Paragraph("Codex 推荐插件真实试跑评估", title_style),
    Paragraph("PDF 插件试跑产物 | SignalProof | 2026-06-21", body_style),
    Paragraph(
        "本 PDF 用于验证 PDF 产物生成和文本抽取检查。由于当前环境缺少 pdftoppm/pdfinfo，"
        "本轮无法完成 Poppler PNG 渲染，但 reportlab 生成和 pdfplumber 抽取均可运行。",
        body_style,
    ),
]

data = [
    ["插件组", "结果", "建议"],
    ["GitHub / last30days", "调研增益明显，但受来源额度影响", "默认候选"],
    ["Record & Replay", "能证明录制能力可见", "资产化默认候选"],
    ["Spreadsheets / Data Viz", "已产出 XLSX/PNG/HTML", "默认进入工具账本"],
    ["App connector", "未授权或工具入口缺失", "授权后专项跑"],
]
table = Table(data, colWidths=[1.8 * inch, 3.0 * inch, 1.5 * inch])
table.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E8EEF5")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#0B2545")),
            ("FONTNAME", (0, 0), (-1, -1), FONT_NAME),
            ("FONTSIZE", (0, 0), (-1, -1), 9),
            ("LEADING", (0, 0), (-1, -1), 12),
            ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#D7DEE2")),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 6),
            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ]
    )
)
story.extend([Spacer(1, 10), table])
story.append(Spacer(1, 12))
story.append(
    Paragraph(
        "边界：本轮证明插件工作流增益，不证明市场验证；真实反馈仍为空。",
        body_style,
    )
)
doc.build(story)

with pdfplumber.open(PDF) as pdf:
    extracted = []
    for idx, page in enumerate(pdf.pages, start=1):
        text = page.extract_text() or ""
        extracted.append(f"--- page {idx} ---\n{text}")
    TEXT.write_text("\n".join(extracted), encoding="utf-8")
    INSPECT.write_text(
        f"pages={len(pdf.pages)}\nchars={sum(len(x) for x in extracted)}\ncontains_title={'Codex 推荐插件真实试跑评估' in ''.join(extracted)}\n",
        encoding="utf-8",
    )
