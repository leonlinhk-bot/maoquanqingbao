import json

d = json.load(open('data/live-items.json'))
items = d['items']
for it in items:
    if it['id'] in ('stcn-sfc-hkex-etf-20260818', 'scmp-beijing-insurers-hk-etfs-20260818'):
        print(json.dumps({k: it.get(k) for k in ('id', 'title', 'summary', 'originalUrl', 'publishedAt', 'sourceKey', 'contentKind')}, ensure_ascii=False, indent=1))
        print('-' * 90)
