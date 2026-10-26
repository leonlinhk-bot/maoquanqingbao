import json, collections
d = json.load(open('data/live-items.json'))
c = collections.Counter(i.get('sourceKey') for i in d['items'])
print(dict(c))
print('boards:', sorted({b for i in d['items'] for b in i.get('boards', [])}))
