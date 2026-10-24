#!/usr/bin/env python3
import json, sys, urllib.request
from pathlib import Path
ENV = Path.home() / '.hermes' / '.env'
key, base = None, 'https://api.deepseek.com'
for line in ENV.read_text().splitlines():
    if line.startswith('DEEPSEEK_API_KEY='):
        key = line.split('=', 1)[1].strip().strip('"').strip("'")
    elif line.startswith('DEEPSEEK_BASE_URL='):
        base = line.split('=', 1)[1].strip().strip('"').strip("'").rstrip('/')
u = sys.argv[1]
out = sys.argv[2]
payload = {'url': u, 'need_content': True}
req = urllib.request.Request(base + '/v1/tools/fetch', data=json.dumps(payload).encode(),
                             headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'},
                             method='POST')
with urllib.request.urlopen(req, timeout=150) as r:
    d = json.loads(r.read().decode())
c = d.get('content') or d.get('text') or ''
open(out, 'w', encoding='utf-8').write(c)
print('wrote', out, len(c))
print(c[:6000])
