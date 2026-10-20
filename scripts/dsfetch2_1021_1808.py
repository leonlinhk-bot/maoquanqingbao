import json, os, re, urllib.request
from pathlib import Path

ENV = Path.home() / '.hermes' / '.env'
key = None
for line in ENV.read_text().splitlines():
    line = line.strip()
    if line.startswith('DEEPSEEK_API_KEY'):
        key = line.split('=', 1)[1].strip().strip('"').strip("'")
        break

TARGETS = {
    'ia_press': 'https://www.ia.org.hk/en/infocenter/press_releases.html',
    'ia_circ': 'https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html',
    'ia_enf': 'https://www.ia.org.hk/en/enforcement/enforcement_news/news.html',
    'ia_stats': 'https://www.ia.org.hk/en/infocenter/statistics/statistics.html',
}
os.makedirs('data/_1021_1808', exist_ok=True)
for name, u in TARGETS.items():
    body = json.dumps({'url': u}).encode()
    req = urllib.request.Request('https://api.deepseek.com/v1/tools/fetch', data=body,
                                 headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            j = json.load(r)
    except Exception as e:
        print('ERR', name, repr(e)[:200])
        continue
    content = j.get('content') or j.get('data', {}).get('content') or ''
    if isinstance(content, dict):
        content = json.dumps(content, ensure_ascii=False)
    p = f'data/_1021_1808/{name}.txt'
    open(p, 'w', encoding='utf-8').write(str(content))
    print(name, len(str(content)), '->', p)
