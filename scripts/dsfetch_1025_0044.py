#!/usr/bin/env python3
"""DeepSeek /v1/tools/fetch — bypass CF for ia.org.hk lists + fetch article bodies."""
import json, sys, urllib.request
from pathlib import Path

ENV = Path.home() / '.hermes' / '.env'
key, base = None, 'https://api.deepseek.com'
for line in ENV.read_text().splitlines():
    if line.startswith('DEEPSEEK_API_KEY='):
        key = line.split('=', 1)[1].strip().strip('"').strip("'")
    elif line.startswith('DEEPSEEK_BASE_URL='):
        base = line.split('=', 1)[1].strip().strip('"').strip("'").rstrip('/')

def fetch(url):
    payload = {'url': url, 'need_content': True}
    req = urllib.request.Request(base + '/v1/tools/fetch',
                                data=json.dumps(payload).encode(),
                                headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'},
                                method='POST')
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode())

urls = sys.argv[1:]
for u in urls:
    print('=' * 30, u)
    try:
        d = fetch(u)
        c = d.get('content') or d.get('text') or json.dumps(d, ensure_ascii=False)
        print(c[:3000])
    except Exception as e:
        print('FAIL', type(e).__name__, str(e)[:200])
