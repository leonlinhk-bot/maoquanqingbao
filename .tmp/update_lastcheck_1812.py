import json
from datetime import datetime, timezone, timedelta

TZ = timezone(timedelta(hours=8))
NOW = datetime(2026, 8, 22, 18, 12, 0, tzinfo=TZ).isoformat()

path = 'data/last-check.json'
d = json.load(open(path, encoding='utf-8'))
d['lastCheck'] = NOW
for k, v in d['sources'].items():
    v['last'] = NOW
json.dump(d, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('last-check updated:', d['lastCheck'], '| sources:', len(d['sources']))
