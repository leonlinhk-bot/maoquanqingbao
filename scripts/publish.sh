#!/usr/bin/env bash
# 港险情报站发布脚本：rebuild + 条数验证 + commit + push
# 用途：cron 采集完成后统一调用，避免「漏跑 rebuild 导致 app.js 没同步」的问题
set -euo pipefail
cd "$(dirname "$0")/.."

# 1. 条目增强（同题聚合 clusterCount + 导语 summaryShort）——必须在 rebuild 之前，
#    否则新条目不会被 enrich，字段只存在于「跑过一次」的那批（R4 建成/运转尺的坑）
python3 scripts/enrich-items.py --apply

# 1b. 重建 feed + 同步 app.js DATA
python3 scripts/rebuild-feeds.py

# 2. 验证外链数据与 live-items.json 条数一致（漏 rebuild 会在此报错）
python3 - <<'PY'
import json
live = json.load(open('data/live-items.json'))
items = json.load(open('data/items.json'))
core = json.load(open('data/core.json'))
n_live = len(live['items']); n_items = len(items['items']); n_core = len(core['items'])
assert n_live == n_items, f"条数不一致: live={n_live} items.json={n_items}"
assert 0 < n_core <= n_live, f"core.json 条数异常: {n_core}"
assert n_items == items.get('itemCount'), "items.json itemCount 不匹配"
print(f"验证通过: live={n_live} items.json={n_items} core.json={n_core}(首屏)")
PY

# 2.5 发布前健康检查：HTML 结构 + JS 语法（拦「整页白屏」类故障）
# 教训：① tags 字符串致渲染崩溃 ② 正则全局替换把 index.html 改坏——两者都表现为页面空白
python3 - <<'PY'
import re, json, sys
idx = open('index.html', encoding='utf-8').read()
opens = len(re.findall(r'<script\b', idx))
closes = len(re.findall(r'</script>', idx))
assert opens == closes, f"script 标签不配对: {opens} 开 / {closes} 闭"
assert re.search(r'<script src="app\.js\?v=[^"]+"></script>', idx), "app.js 脚本标签异常"
assert 'window.HKII_corePromise' in idx, "首屏数据加载代码缺失"
assert 'window.HKII_VER' in idx, "数据版本号缺失"
core = json.load(open('data/core.json', encoding='utf-8'))
assert isinstance(core.get('items'), list) and core['items'], "core.json items 为空"
for it in core['items'][:200]:
    t = it.get('tags')
    if isinstance(t, dict):
        for k in ('sc', 'tc'):
            if k in t and not isinstance(t[k], list):
                raise AssertionError(f"tags.{k} 非数组: {it.get('id')}")
print(f"健康检查 OK (script {opens} 对 · core {len(core['items'])} 条 · tags 格式正常)")
PY
node --check app.js && echo "app.js 语法 OK"

# 3. 提交 + 推送
git add -A
if git diff --cached --quiet; then
  echo "无改动，跳过提交"
else
  git commit -m "每日更新 $(date '+%Y-%m-%d %H:%M'): 数据采集+rebuild同步"
fi
git push origin main
echo "发布完成"
