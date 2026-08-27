import json
d = json.load(open('data/live-items.json'))
for it in d['items'][:12]:
    print(it['id'], '|', it['sourceKey'], '|', it['boards'], '|', it.get('publishedAt', ''))
