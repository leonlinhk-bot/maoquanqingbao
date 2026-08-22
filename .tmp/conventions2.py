import json

d = json.load(open('data/live-items.json'))
items = d['items']

print("== items mentioning 内地访客/內地訪客 ==")
n = 0
for it in items:
    t = it['title']['sc'] + it['title'].get('tc', '')
    if ('内地访客' in t or '內地訪客' in t or 'MCV' in t or 'mcv' in it.get('themes', [])) and it.get('publishedAt', '').startswith('2026'):
        print(it['id'], '|', it.get('publishedAt'), '|', it.get('sourceKey'), '|', it.get('themes'), '|', t[:50])
        n += 1
        if n >= 8:
            break

print("\n== insuranceasia items 2026-08 (score/format sample) ==")
n = 0
for it in items:
    if it.get('sourceKey') == 'insuranceasia' and it.get('publishedAt', '').startswith('2026-08'):
        print(it['id'], '| score', it.get('score'), '|', it.get('sourceTier'), '|', it.get('boards'), '|', it.get('themes'), '|', it.get('contentKind'), '|', it['title']['sc'][:45])
        n += 1
        if n >= 6:
            break
