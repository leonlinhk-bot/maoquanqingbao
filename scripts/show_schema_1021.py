import json
d = json.load(open('data/live-items.json'))
items = d['items']
for it in items[:2]:
    print(json.dumps(it, ensure_ascii=False, indent=1))
    print('======')
# IA item from Sep 24 for url pattern
for it in items:
    if it.get('sourceKey') == 'ia' and (it.get('publishedAt') or '').startswith('2026-09-24'):
        print('IA FWD item url:', it.get('originalUrl'))
        print(json.dumps(it, ensure_ascii=False, indent=1)[:1500])
        break
