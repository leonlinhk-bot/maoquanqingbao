import json
PATH = '/Users/leonliang/maoquanqingbao/data/live-items.json'
d = json.load(open(PATH, encoding='utf-8'))
n = 0
for it in d['items']:
    if it.get('ingestedAt') == '2026-10-23T00:45:00+08:00':
        it['ingestedAt'] = '2026-10-23T00:28:00+08:00'
        n += 1
json.dump(d, open(PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('fixed ingestedAt:', n)
