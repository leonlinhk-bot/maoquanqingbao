import json, datetime
P = '/Users/leonliang/maoquanqingbao/data/live-items.json'
d = json.load(open(P))
# keep the 5 newest straight in publishedAt-desc order at the head
head = d['items'][:5]
tail = d['items'][5:]
head.sort(key=lambda i: i['publishedAt'], reverse=True)
d['items'] = head + tail
json.dump(d, open(P, 'w'), ensure_ascii=False, indent=1)
for i in d['items'][:6]:
    print(i['publishedAt'][:16], i['sourceKey'], i['id'][:50])

# --- last-check.json: all sources -> now ---
LP = '/Users/leonliang/maoquanqingbao/data/last-check.json'
lc = json.load(open(LP))
now = '2026-11-02T10:40:00+08:00'
lc['lastCheck'] = now
for k in lc['sources']:
    lc['sources'][k]['last'] = now
json.dump(lc, open(LP, 'w'), ensure_ascii=False, indent=2)
print('lastCheck ->', lc['lastCheck'], '| sources updated:', len(lc['sources']))
