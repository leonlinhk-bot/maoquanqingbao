import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json', encoding='utf-8'))
items = [it for it in d['items'] if (it.get('publishedAt') or '') >= '2026-10-20']
items.sort(key=lambda x: x.get('score', 0), reverse=True)
print('recent (>=10-20) count:', len(items))
for it in items[:10]:
    print(it['score'], it['publishedAt'][:16], it['title']['sc'][:60])
