import json

d = json.load(open('data/live-items.json'))
items = d['items']
print("total items:", len(items))
print("meta.generatedAt:", d['meta'].get('generatedAt'))
print("meta.itemCount:", d['meta'].get('itemCount'))
print("---- top 20 ----")
for it in items[:20]:
    print(it.get('publishedAt'), '|', it.get('sourceKey'), '|', it.get('verifyStatus'), '|', it['title']['sc'][:70], '|', it.get('originalUrl','')[:90])
print("---- sourceKey counts (last 40 items) ----")
from collections import Counter
c = Counter(it.get('sourceKey') for it in items[:40])
print(c)
