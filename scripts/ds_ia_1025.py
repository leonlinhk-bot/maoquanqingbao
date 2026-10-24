#!/usr/bin/env python3
"""Fetch IA press-release list pages via DeepSeek and extract Date|Title rows."""
import json, re, sys, urllib.request
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
                                headers={'Authorization': f'Bearer {key}',
                                         'Content-Type': 'application/json'},
                                method='POST')
    with urllib.request.urlopen(req, timeout=150) as r:
        return json.loads(r.read().decode())

urls = sys.argv[1:]
for u in urls:
    print('=' * 30, u)
    try:
        d = fetch(u)
        c = d.get('content') or d.get('text') or json.dumps(d, ensure_ascii=False)
        # keep only lines that look like Date | Title
        hits = [ln for ln in c.splitlines()
                if re.search(r'\b(20\d\d|2026)\b', ln) and ('|' in ln or 'press' in ln.lower())]
        print('LEN', len(c), 'HITS', len(hits))
        for ln in c[-4000:].splitlines():
            if re.search(r'(20\d\d|\d{1,2} \w+ 2026)', ln):
                print('  >', ln.strip()[:200])
    except Exception as e:
        print('FAIL', type(e).__name__, str(e)[:200])
