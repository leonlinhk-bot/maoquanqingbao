import json, shutil
from pathlib import Path
P = Path('/Users/leonliang/maoquanqingbao/data/last-check.json')
d = json.load(open(P))
NOW = '2026-10-24T01:08:00+08:00'
shutil.copy2(P, '/Users/leonliang/maoquanqingbao/data/last-check.json.bak-1024-0108')
d['lastCheck'] = NOW
for k, v in d['sources'].items():
    v['last'] = NOW
P.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding='utf-8')
print('updated sources:', len(d['sources']), 'lastCheck', d['lastCheck'])
