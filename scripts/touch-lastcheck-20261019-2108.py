import json
from datetime import datetime, timezone, timedelta

PATH = '/Users/leonliang/maoquanqingbao/data/last-check.json'
NOW = datetime.now(timezone(timedelta(hours=8))).replace(second=0, microsecond=0).isoformat()

cfg = json.load(open(PATH, encoding='utf-8'))
cfg['lastCheck'] = NOW
n = 0
for k, v in (cfg.get('sources') or {}).items():
    v['last'] = NOW
    n += 1
json.dump(cfg, open(PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('updated sources:', n, 'lastCheck:', NOW)
