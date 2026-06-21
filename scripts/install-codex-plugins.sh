#!/usr/bin/env bash
set -euo pipefail

# SignalProof Codex 插件恢复脚本。
# 只安装/启用官方 marketplace 插件；OAuth、浏览器 cookie、API key 需要在新机器手动重新授权。

plugins=(
  "browser@openai-bundled"
  "chrome@openai-bundled"
  "computer-use@openai-bundled"
  "record-and-replay@openai-bundled"
  "airtable@openai-curated"
  "amplitude@openai-curated"
  "box@openai-curated"
  "brand24@openai-curated"
  "build-web-data-visualization@openai-curated"
  "canva@openai-curated"
  "cloudflare@openai-curated"
  "codex-security@openai-curated"
  "datadog@openai-curated"
  "deepnote@openai-curated"
  "dovetail@openai-curated"
  "figma@openai-curated"
  "github@openai-curated"
  "google-drive@openai-curated"
  "hugging-face@openai-curated"
  "hyperframes@openai-curated"
  "jam@openai-curated"
  "linear@openai-curated"
  "mem@openai-curated"
  "mixpanel@openai-curated"
  "netlify@openai-curated"
  "notion@openai-curated"
  "openai-developers@openai-curated"
  "posthog@openai-curated"
  "readwise@openai-curated"
  "scite@openai-curated"
  "semrush@openai-curated"
  "sentry@openai-curated"
  "similarweb@openai-curated"
  "superpowers@openai-curated"
  "vercel@openai-curated"
  "zotero@openai-curated"
)

if ! command -v codex >/dev/null 2>&1; then
  echo "ERROR: 未找到 codex 命令。请先安装/登录 Codex。"
  exit 1
fi

echo "== Codex marketplace =="
codex plugin marketplace list || true

echo "== 安装 SignalProof 推荐插件 =="
for plugin in "${plugins[@]}"; do
  echo "-- ${plugin}"
  codex plugin add "${plugin}" || {
    echo "WARN: ${plugin} 安装失败。可能是已安装、marketplace 未刷新，或该插件在当前 Codex 版本不可用。"
  }
done

echo "== 安装后状态 =="
codex plugin list

echo
echo "完成。请新开 Codex 线程，然后运行："
echo "  python3 scripts/signalproof.py capabilities"
echo "  python3 scripts/signalproof.py plugin-status"
