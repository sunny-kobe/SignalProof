import fs from "node:fs/promises";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const outputDir = new URL("./outputs/", import.meta.url);
const workbook = Workbook.create();
const sheet = workbook.worksheets.add("插件评估");

const rows = [
  ["插件组", "插件", "本轮状态", "证据", "对 SignalProof 的影响", "建议"],
  ["安装基线", "36 个 marketplace 插件", "installed/enabled", "codex plugin list", "中", "保留清单，进入分组试跑"],
  ["运行时", "Documents / PDF / Spreadsheets / Presentations", "runtime available", "capabilities + runtime manifest", "高", "作为产物类默认候选"],
  ["验证", "Record & Replay", "可调用状态查询", "event_stream_status: isRecording=false", "高", "保留，用于把用户演示沉淀为 Skill"],
  ["验证", "Computer Use", "调用失败", "get_app_state(Codex) 返回 -1743", "中", "保留但不设为默认，先修权限或换目标 App"],
  ["调研", "GitHub", "公开只读成功", "gh repo view + issue list", "高", "默认用于开源信号、发布和反馈"],
  ["调研", "Hugging Face", "公开 API 成功，CLI 缺失", "HF model API + dataset viewer", "中", "用于模型/数据集信号，CLI 需另装"],
  ["调研", "Zotero", "本地 App 未运行", "127.0.0.1:23119 refused", "条件", "有 Zotero 资料库时再启用"],
  ["反馈/数据", "PostHog / Mixpanel / Amplitude", "已安装但本线程无 connector/API key", "tool search + env check", "条件", "真实产品埋点后再用"],
  ["市场", "Semrush / Similarweb / Brand24 / Scite / Readwise", "已安装但本线程无 connector", "manifest apps=true", "条件", "账号授权后做专项 case"],
  ["产物", "Data Visualization", "本地 HTML 资产生成", "plugin-eval-summary.html", "高", "保留，用于工具覆盖和结果展示"],
];

sheet.getRangeByIndexes(0, 0, rows.length, rows[0].length).values = rows;
sheet.getRange("A1:F1").format.fill.color = "#174A5A";
sheet.getRange("A1:F1").format.font.color = "#FFFFFF";
sheet.getRange("A1:F1").format.font.bold = true;
sheet.getRange("A1:F1").format.rowHeight = 28;
sheet.getRange("A:F").format.wrapText = true;
sheet.getRange("A:F").format.verticalAlignment = "Top";
sheet.getRange("A:A").format.columnWidth = 18;
sheet.getRange("B:B").format.columnWidth = 28;
sheet.getRange("C:C").format.columnWidth = 24;
sheet.getRange("D:D").format.columnWidth = 34;
sheet.getRange("E:E").format.columnWidth = 20;
sheet.getRange("F:F").format.columnWidth = 34;
sheet.getRangeByIndexes(0, 0, rows.length, rows[0].length).format.borders = {
  preset: "all",
  style: "thin",
  color: "#D7DEE2",
};
sheet.freezePanes.freezeRows(1);
sheet.showGridLines = false;

await fs.mkdir(outputDir, { recursive: true });
const inspect = await workbook.inspect({
  kind: "table",
  range: "插件评估!A1:F11",
  include: "values",
  tableMaxRows: 12,
  tableMaxCols: 6,
});
await fs.writeFile(new URL("./outputs/inspect.ndjson", import.meta.url), inspect.ndjson, "utf8");
const preview = await workbook.render({ sheetName: "插件评估", range: "A1:F11", scale: 1.5, format: "png" });
await fs.writeFile(new URL("./outputs/plugin-eval-workbook-preview.png", import.meta.url), new Uint8Array(await preview.arrayBuffer()));
const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save(new URL("./outputs/plugin-eval-workbook.xlsx", import.meta.url).pathname);
