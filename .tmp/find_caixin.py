import json
d = json.load(open('data/live-items.json'))
for it in d['items']:
    if it.get('sourceKey') == 'caixin':
        print(json.dumps({k: it.get(k) for k in ['id', 'title', 'publishedAt', 'ingestedAt', 'originalUrl', 'verifyStatus']}, ensure_ascii=False)[:600])
        print('---')
