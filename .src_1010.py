import json, collections
d = json.load(open('data/live-items.json'))
it = d['items']
cnt = collections.Counter(x.get('sourceKey') for x in it)
print(cnt)
print('--- sourceKey=ia items (last 8) ---')
ia = [x for x in it if x.get('sourceKey') in ('ia', 'ia_press', 'ia_circular')]
ia.sort(key=lambda x: str(x.get('publishedAt')), reverse=True)
for x in ia[:8]:
    print(x.get('publishedAt'), x.get('title', {}).get('sc', '')[:50], '|', x.get('originalUrl'))
print('--- hkma last 5 ---')
h = [x for x in it if x.get('sourceKey') == 'hkma']
h.sort(key=lambda x: str(x.get('publishedAt')), reverse=True)
for x in h[:5]:
    print(x.get('publishedAt'), x.get('title', {}).get('sc', '')[:50], '|', x.get('originalUrl'))
print('--- hkfi last 5 ---')
h = [x for x in it if x.get('sourceKey') in ('hkfi', 'govhk', 'fstb')]
h.sort(key=lambda x: str(x.get('publishedAt')), reverse=True)
for x in h[:8]:
    print(x.get('sourceKey'), x.get('publishedAt'), x.get('title', {}).get('sc', '')[:55])
