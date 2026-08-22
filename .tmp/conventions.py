import json, collections

d = json.load(open('data/live-items.json'))
items = d['items']
print('sourceKeys:', collections.Counter(it.get('sourceKey') for it in items).most_common(40))
print()
print('boards used:', collections.Counter(tuple(it.get('boards', [])) for it in items).most_common(15))
print()
print('contentKinds:', collections.Counter(it.get('contentKind') for it in items).most_common(20))
print()
# full example items (one official, one insurer, one media)
for it in items[:3]:
    print('=' * 80)
    print(json.dumps(it, ensure_ascii=False, indent=1))
