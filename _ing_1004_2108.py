# -*- coding: utf-8 -*-
import json
from collections import Counter
live = json.load(open('data/live-items.json', encoding='utf-8'))['items']
c = Counter(it.get('ingestedAt', '')[:10] for it in live)
print('ingestedAt date counts:', dict(sorted(c.items())))
print()
print('--- items ingested 2026-10-04 ---')
for it in live:
    if it.get('ingestedAt', '').startswith('2026-10-04'):
        print(it.get('ingestedAt'), '|', it.get('sourceKey'), '|', it.get('id'))
print()
print('--- items ingested 2026-10-03 ---')
for it in live:
    if it.get('ingestedAt', '').startswith('2026-10-03'):
        print(it.get('ingestedAt'), '|', it.get('sourceKey'), '|', it.get('id'))
