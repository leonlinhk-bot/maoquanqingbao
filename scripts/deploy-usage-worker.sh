#!/usr/bin/env bash
# 一键部署使用度 Worker，并把 endpoint 写回 index.html
# 用法：bash scripts/deploy-usage-worker.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT/workers/usage"

echo "==> 1. wrangler 登录检查"
if ! npx wrangler whoami 2>/dev/null | grep -qiE 'account|email|user'; then
  echo "需要登录 Cloudflare："
  echo "  npx wrangler login"
  echo "登录后再跑本脚本。"
  exit 1
fi

echo "==> 2. 确保 KV namespace"
if grep -q 'REPLACE_WITH_KV_NAMESPACE_ID' wrangler.toml; then
  echo "创建 KV namespace USAGE_KV ..."
  OUT=$(npx wrangler kv namespace create USAGE_KV 2>&1 || true)
  echo "$OUT"
  ID=$(echo "$OUT" | grep -oE 'id\s*=\s*"[a-f0-9]+"' | head -1 | grep -oE '[a-f0-9]{32}' || true)
  if [ -z "${ID:-}" ]; then
    ID=$(echo "$OUT" | grep -oE '[a-f0-9]{32}' | head -1 || true)
  fi
  if [ -z "${ID:-}" ]; then
    echo "未能解析 KV id，请手动填 wrangler.toml 后重跑"
    exit 1
  fi
  # macOS sed
  sed -i '' "s/REPLACE_WITH_KV_NAMESPACE_ID/$ID/" wrangler.toml
  echo "KV id = $ID"
fi

echo "==> 3. 部署 Worker"
DEPLOY_OUT=$(npx wrangler deploy 2>&1)
echo "$DEPLOY_OUT"
URL=$(echo "$DEPLOY_OUT" | grep -oE 'https://[a-zA-Z0-9.-]+\.workers\.dev' | head -1 || true)
if [ -z "${URL:-}" ]; then
  echo "部署完成但未解析到 workers.dev URL，请手动填 index.html 的 HKII_USAGE_ENDPOINT"
  exit 0
fi
echo "Worker URL = $URL"

echo "==> 4. 写回 index.html endpoint"
python3 - <<PY
from pathlib import Path
import re
p = Path("$ROOT")/"index.html"
t = p.read_text(encoding="utf-8")
url = "$URL"
t2 = re.sub(
    r'window\.HKII_USAGE_ENDPOINT\s*=\s*window\.HKII_USAGE_ENDPOINT\s*\|\|\s*"[^"]*"',
    f'window.HKII_USAGE_ENDPOINT = window.HKII_USAGE_ENDPOINT || "{url}"',
    t, count=1)
if t2 == t:
    # fallback: 直接赋值行
    t2 = re.sub(
        r'(window\.HKII_USAGE_ENDPOINT\s*=\s*)[^;]+',
        rf'\1"{url}"',
        t, count=1)
p.write_text(t2, encoding="utf-8")
print("index.html endpoint updated")
PY

echo "==> 5. 冒烟"
curl -sS "$URL/health" || true
echo
curl -sS -X POST "$URL/e" -H 'Content-Type: application/json' \
  -H 'Origin: https://hkmaoquanqingbao.com' \
  -d '{"t":"search","v":"smoke-test"}' || true
echo
echo "完成。下一步："
echo "  1) Cloudflare 仪表盘 → Analytics → Web Analytics → 添加 hkmaoquanqingbao.com → 复制 token"
echo "  2) 把 token 填进 index.html 的 HKII_CF_BEACON"
echo "  3) bash scripts/publish.sh"
