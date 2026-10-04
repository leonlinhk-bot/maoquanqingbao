import json
from collections import Counter
d = json.load(open('data/live-items.json'))
items = d['items'] if isinstance(d, dict) else d
print('total items:', len(items))
c = Counter()
for it in items[:60]:
    c[it.get('publishedAt', '')[:10]] += 1
print('recent publishedAt dates:', dict(sorted(c.items())))
print('--- top 20 (most recent inserted) ---')
for it in items[:20]:
    print(it.get('publishedAt', '')[:16], '|', it.get('sourceKey'), '|', it.get('verifyStatus'), '|', it.get('title', {}).get('sc', '')[:44])
print('--- existing ids sample for dup check ---')
import re
keys = set()
for it in items:
    keys.add(it.get('id', ''))
open('/tmp/_existing_ids.txt', 'w').write('\n'.join(sorted(keys)))
print('unique ids:', len(keys))
