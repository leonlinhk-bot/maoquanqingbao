import json, collections
d = json.load(open('data/live-items.json'))
items = d['items']
ids = [it['id'] for it in items]
dups = [k for k, v in collections.Counter(ids).items() if v > 1]
print('items:', len(items), '| dup ids:', dups[:5], '| meta.itemCount:', d['meta']['itemCount'],
      '| generatedAt:', d['meta']['generatedAt'])
today = [it for it in items if (it.get('publishedAt') or '')[:10] == '2026-10-26']
print('today items:', len(today))
for it in today:
    print(' ', it['publishedAt'][:16], '|', it['sourceKey'], '|', it['verifyStatus'], '|', it['title']['sc'][:52])
lc = json.load(open('data/last-check.json'))
print('lastCheck:', lc['lastCheck'], '| sources:', len(lc['sources']))
print('missing required fields:', [it['id'] for it in today if not (it.get('originalUrl') and it.get('boards') and len(it.get('themes', [])) >= 2 and it.get('sourceTier'))])
