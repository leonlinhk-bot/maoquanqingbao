import json
d=json.load(open('data/live-items.json'))
print('meta:',json.dumps(d.get('meta'),ensure_ascii=False)[:800])
items=d['items']
print('total items:',len(items))
for it in items[:10]:
    print(it['id'],'|',it.get('publishedAt'),'|',it.get('sourceKey'),'|',it['title']['sc'][:44])
print('--- keys of first item ---')
print(list(items[0].keys()))
