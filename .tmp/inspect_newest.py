import json
from datetime import datetime

d = json.load(open('data/live-items.json'))
items = d['items']
print('total items:', len(items))

def key(x):
    try:
        dt = datetime.fromisoformat(x['publishedAt'])
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=__import__('datetime').timezone.utc)
        return dt
    except Exception:
        return datetime.min.replace(tzinfo=__import__('datetime').timezone.utc)

items_sorted = sorted(items, key=key, reverse=True)
for it in items_sorted[:20]:
    print(it['publishedAt'], '|', it['sourceKey'], '|', it['id'])
