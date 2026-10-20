import json
from datetime import datetime
p = 'data/last-check.json'
d = json.load(open(p, encoding='utf-8'))
now = datetime.now().astimezone().replace(microsecond=0).isoformat()
d['lastCheck'] = now
for k, v in d['sources'].items():
    v['last'] = now
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('lastCheck ->', now, '| sources:', len(d['sources']))
