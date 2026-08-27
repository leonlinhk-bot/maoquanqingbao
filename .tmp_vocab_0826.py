import json, collections

d = json.load(open('data/live-items.json'))
items = d['items']

boards = collections.Counter()
themes = collections.Counter()
kinds = collections.Counter()
tiers = collections.Counter()
for it in items:
    for b in it.get('boards', []):
        boards[b] += 1
    for t in it.get('themes', []):
        themes[t] += 1
    kinds[it.get('contentKind')] += 1
    tiers[it.get('sourceTier')] += 1

print('boards:', dict(boards))
print('contentKind:', dict(kinds))
print('sourceTier:', dict(tiers))
print('top themes:', dict(themes.most_common(40)))

# check formatting of file end
with open('data/live-items.json', 'rb') as f:
    raw = f.read()
print('file ends with newline:', raw.endswith(b'\n'))
print('last 40 chars:', raw[-40:])
print('first 30 chars:', raw[:30])
