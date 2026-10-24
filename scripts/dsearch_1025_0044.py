#!/usr/bin/env python3
"""Targeted DeepSeek Search for 2026-10-24/25 window. Prints everything with a date."""
import json, os, re, time, urllib.request, urllib.error
from datetime import datetime, timezone, timedelta
from pathlib import Path

ENV = Path.home() / '.hermes' / '.env'
key, base = None, 'https://api.deepseek.com'
for line in ENV.read_text().splitlines():
    if line.startswith('DEEPSEEK_API_KEY='):
        key = line.split('=', 1)[1].strip().strip('"').strip("'")
    elif line.startswith('DEEPSEEK_BASE_URL='):
        base = line.split('=', 1)[1].strip().strip('"').strip("'").rstrip('/')
if not key:
    raise SystemExit('no DEEPSEEK_API_KEY')

QUERIES = [
    '香港保险业 最新 消息',
    '香港保监局 最新 公告',
    '香港保险 新产品 最新 消息',
    '香港 保险经纪 最新 消息',
    '香港 家族办公室 最新 消息',
    '金融监管总局 保险 最新 消息',
    '友邦 保诚 宏利 安盛 最新 消息',
    '香港 保险 监管 通函 最新',
]

def search(q):
    payload = {'query': q, 'count': 12, 'need_content': False}
    req = urllib.request.Request(base + '/v1/tools/search',
                                data=json.dumps(payload).encode(),
                                headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'},
                                method='POST')
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode()).get('results', [])

seen = set()
rows = []
for q in QUERIES:
    try:
        res = search(q)
    except Exception as e:
        print(f'!! {q} FAIL {type(e).__name__}: {str(e)[:80]}')
        continue
    print(f'== {q} -> {len(res)}')
    for r in res:
        u = (r.get('url') or '').split('?')[0]
        t = (r.get('title') or '').strip()
        d = (r.get('date') or '').strip()
        a = r.get('authority')
        rows.append({'q': q, 'title': t, 'url': u, 'date': d, 'authority': a,
                     'snippet': (r.get('snippet') or r.get('content') or '')[:220]})
        if u in seen:
            continue
        seen.add(u)
        print(f"   [{a}] {d[:10]:10s} {t[:90]}")
        print(f"        {u[:110]}")

json.dump(rows, open('/Users/leonliang/maoquanqingbao/data/_raw_1025_0044/ds_search.json', 'w'),
          ensure_ascii=False, indent=1)
print('\ntotal rows', len(rows), 'unique', len(seen))
