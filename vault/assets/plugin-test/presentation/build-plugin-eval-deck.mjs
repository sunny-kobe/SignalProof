import fs from "node:fs/promises";
import { Presentation, PresentationFile } from "@oai/artifact-tool";

const base = new URL(".", import.meta.url);
const outputDir = new URL("./outputs/", base);

async function writeBlob(pathUrl, blob) {
  await fs.writeFile(pathUrl, new Uint8Array(await blob.arrayBuffer()));
}

function addText(slide, name, text, position, style) {
  const shape = slide.shapes.add({
    geometry: "textbox",
    name,
    position,
    fill: "none",
    line: { style: "solid", fill: "none", width: 0 },
  });
  shape.text = text;
  shape.text.style = style;
  return shape;
}

async function main() {
  await fs.mkdir(outputDir, { recursive: true });
  const presentation = Presentation.create({ slideSize: { width: 1280, height: 720 } });
  const palette = {
    ink: "slate-950",
    muted: "slate-600",
    rule: "slate-200",
    teal: "teal-700",
    amber: "amber-500",
    surface: "slate-50",
  };

  const s1 = presentation.slides.add();
  s1.background.fill = palette.surface;
  addText(s1, "eyebrow", "SIGNALPROOF PLUGIN TRIAL", { left: 72, top: 68, width: 520, height: 30 }, { fontSize: 16, bold: true, color: palette.teal });
  addText(s1, "title", "哪些 Codex 插件真的提升个人工作流", { left: 72, top: 140, width: 760, height: 160 }, { fontSize: 48, bold: true, color: palette.ink });
  addText(s1, "subtitle", "真实试跑结论：强增益、条件增益、环境失败、授权阻塞分开判断。", { left: 72, top: 330, width: 780, height: 70 }, { fontSize: 23, color: palette.muted });
  s1.shapes.add({ geometry: "roundRect", name: "summary-card", position: { left: 870, top: 120, width: 310, height: 360 }, fill: "white", line: { style: "solid", fill: palette.rule, width: 1 }, borderRadius: "rounded-xl", shadow: "shadow-sm" });
  addText(s1, "summary", "强增益\nGitHub\nRecord & Replay\nSpreadsheets\nData Visualization", { left: 905, top: 165, width: 250, height: 250 }, { fontSize: 28, bold: true, color: palette.ink, alignment: "center" });

  const s2 = presentation.slides.add();
  s2.background.fill = "white";
  addText(s2, "title", "调研类插件：能提速，但要承认来源缺口", { left: 72, top: 56, width: 980, height: 56 }, { fontSize: 35, bold: true, color: palette.ink });
  addText(s2, "body", "last30days 拉到 GitHub / Reddit / YouTube 证据，但 X 额度耗尽、Reddit public API 403、YouTube 评论 402。\n\nGitHub 和 Hugging Face 公开 API 适合作为默认初筛；Readwise / Scite / Semrush / Similarweb / Brand24 需要 connector 授权后再算真实调用。", { left: 90, top: 160, width: 760, height: 260 }, { fontSize: 24, color: palette.muted });
  s2.charts.add("bar", {
    position: { left: 880, top: 170, width: 300, height: 280 },
    categories: ["GitHub", "Reddit", "YouTube", "X"],
    series: [{ name: "本轮证据量", values: [4, 6, 3, 0], fill: "accent1" }],
    hasLegend: false,
    dataLabels: { showValue: true, position: "outEnd" },
  });

  const s3 = presentation.slides.add();
  s3.background.fill = palette.surface;
  addText(s3, "title", "默认策略：少数插件常驻，多数按 case 启用", { left: 72, top: 56, width: 1040, height: 58 }, { fontSize: 35, bold: true, color: palette.ink });
  const rows = [
    ["阶段", "默认", "条件启用"],
    ["调研", "GitHub, last30days", "Readwise, Scite, Semrush"],
    ["验证", "脚本自检, Spreadsheets", "Browser, Computer Use, Sentry"],
    ["产物", "Spreadsheets, Data Viz", "DOCX, PDF, PPTX, HyperFrames"],
    ["资产", "Record & Replay", "Notion, Drive, Mem"],
  ];
  s3.tables.add({
    rows: rows.length,
    columns: rows[0].length,
    left: 96,
    top: 150,
    width: 1088,
    height: 390,
    values: rows,
    columnTracks: [{ mode: "fixed", value: 170 }, { mode: "fr", value: 1 }, { mode: "fr", value: 1.25 }],
  });

  for (const [index, slide] of presentation.slides.items.entries()) {
    const stem = `slide-${String(index + 1).padStart(2, "0")}`;
    await writeBlob(new URL(`./outputs/${stem}.png`, base), await presentation.export({ slide, format: "png", scale: 1 }));
    await fs.writeFile(new URL(`./outputs/${stem}.layout.json`, base), await (await slide.export({ format: "layout" })).text(), "utf8");
  }
  await writeBlob(new URL("./outputs/plugin-eval-deck-montage.webp", base), await presentation.export({ format: "webp", montage: true, scale: 1 }));
  const inspect = await presentation.inspect({ kind: "slide,textbox,shape,chart,table,layout", maxChars: 12000 });
  await fs.writeFile(new URL("./outputs/plugin-eval-deck.inspect.ndjson", base), inspect.ndjson, "utf8");
  const pptx = await PresentationFile.exportPptx(presentation);
  await pptx.save(new URL("./outputs/plugin-eval-deck.pptx", base).pathname);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
