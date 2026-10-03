import json
d = json.load(open('data/live-items.json'))
for k in ['Ant Health', '螞蟻', '蚂蚁', 'Sun Life', '永明', '永明金融']:
    hits = [it['id'] + ' | ' + it['publishedAt'] for it in d['items'] if k in json.dumps(it, ensure_ascii=False)]
    print(k, '->', hits[:6])
