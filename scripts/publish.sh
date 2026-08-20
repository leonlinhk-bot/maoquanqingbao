#!/usr/bin/env bash
# 港险情报站发布脚本：rebuild + 条数验证 + commit + push
# 用途：cron 采集完成后统一调用，避免「漏跑 rebuild 导致 app.js 没同步」的问题
set -euo pipefail
cd "$(dirname "$0")/.."

# 1. 重建 feed + 同步 app.js DATA
python3 scripts/rebuild-feeds.py

# 2. 验证 app.js 与 live-items.json 条数一致（漏 rebuild 会在此报错）
python3 - <<'PY'
import json
live = json.load(open('data/live-items.json'))
txt = open('app.js').read()
app = json.loads(txt.split('window.HKII_DATA = ')[1].split(';')[0])
n_live = len(live['items']); n_app = len(app['items'])
assert n_live == n_app, f"条数不一致: live={n_live} app={n_app}"
print(f"验证通过: live={n_live} app={n_app}")
PY

# 3. 提交 + 推送
git add -A
if git diff --cached --quiet; then
  echo "无改动，跳过提交"
else
  git commit -m "每日更新 $(date '+%Y-%m-%d %H:%M'): 数据采集+rebuild同步"
fi
git push origin main
echo "发布完成"
