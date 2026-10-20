import json, os, re, urllib.request
from pathlib import Path

ENV = Path.home() / '.hermes' / '.env'
key = [l.split('=', 1)[1].strip().strip('"').strip("'") for l in ENV.read_text().splitlines()
       if l.strip().startswith('DEEPSEEK_API_KEY')][0]

for name, u in {
    'ia_press2': 'https://www.ia.org.hk/en/infocenter/press_releases/',
    'ia_whatsnew': 'https://www.ia.org.hk/en/infocenter/whats_new.html',
    'ia_speech': 'https://www.ia.org.hk/en/infocenter/speeches.html',
}.items():
    body = json.dumps({'url': u}).encode()
    req = urllib.request.Request('https://api.deepseek.com/v1/tools/fetch', data=body,
                                 headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            j = json.load(r)
        c = str(j.get('content') or j.get('data', {}).get('content') or '')
        open(f'data/_1021_1808/{name}.txt', 'w', encoding='utf-8').write(c)
        print(name, len(c))
        # print lines containing a 2026 date
        for line in c.splitlines():
            if re.search(r'(2026|2025)', line) and len(line) < 400:
                print('   ', line.strip()[:200])
    except Exception as e:
        print('ERR', name, repr(e)[:150])
