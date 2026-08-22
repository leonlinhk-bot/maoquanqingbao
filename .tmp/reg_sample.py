import json
d = json.load(open('data/live-items.json'))
n = 0
for it in d['items']:
    if 'reg' in it.get('boards', []) and it.get('contentKind') in ('circular', 'press', 'news'):
        print(json.dumps({k: it.get(k) for k in ['id', 'sourceTier', 'sourceKey', 'themes', 'tags', 'contentKind', 'publishedAt', 'score', 'verifyStatus']}, ensure_ascii=False)[:420])
        print('---')
        n += 1
        if n >= 3:
            break
