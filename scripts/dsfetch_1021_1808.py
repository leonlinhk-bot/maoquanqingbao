#!/usr/bin/env python3
"""DeepSeek Fetch：IA 站点被 Cloudflare 拦时唯一能看见列表的通道（见 skill）。"""
import json, os, re, urllib.request
from pathlib import Path

ENV = Path.home() / '.hermes' / '.env'
key = None
for line in ENV.read_text().splitlines():
    line = line.strip()
    if line.startswith('DEEPSEEK_API_KEY'):
        key = line.split('=', 1)[1].strip().strip('"').strip("'")
        break
if not key:
    key = os.environ.get('DEEPSEEK_API_KEY')
print('key:', 'set' if key else 'MISSING', (key or '')[:5])

TARGETS = [
    'https://www.ia.org.hk/en/infocenter/press_releases.html',
    'https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html',
    'https://www.ia.org.hk/en/enforcement/enforcement_news/news.html',
]

for u in TARGETS:
    body = json.dumps({'url': u}).encode()
    req = urllib.request.Request('https://api.deepseek.com/v1/tools/fetch', data=body,
                                 headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            j = json.load(r)
    except Exception as e:
        print('ERR', u, e)
        try:
            print(e.read().decode()[:300])
        except Exception:
            pass
        continue
    content = j.get('content') or j.get('data', {}).get('content') or json.dumps(j, ensure_ascii=False)
    print('\n=====', u, '=====')
    print(str(content)[:2500])
