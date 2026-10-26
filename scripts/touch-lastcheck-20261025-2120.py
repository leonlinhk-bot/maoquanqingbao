import json
from pathlib import Path

P = Path('/Users/leonliang/maoquanqingbao/data/last-check.json')
d = json.loads(P.read_text())
NOW = '2026-10-25T21:20:00+08:00'
d['lastCheck'] = NOW
for k, v in d['sources'].items():
    v['last'] = NOW
P.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding='utf-8')
print('updated sources:', len(d['sources']), '| lastCheck:', d['lastCheck'])
