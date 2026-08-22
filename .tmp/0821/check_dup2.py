import json

d = json.load(open('data/live-items.json'))
items = d['items']
kw = ['医保', '医疗', 'sumitomo', '三井住友', 'hdi', '安联贸易', 'allianz trade', '平安', 'ping an', 'healthcare', '全民']
hits = []
for it in items:
    blob = (it['id'] + ' ' + it['title']['sc'] + ' ' + it['title']['tc']).lower()
    for k in kw:
        if k in blob:
            hits.append((k, it['id'], it.get('publishedAt', ''), it['title']['sc'][:50]))
            break
for h in hits:
    print(h)
print('total hits:', len(hits))
