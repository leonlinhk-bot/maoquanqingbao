import json, collections
d = json.load(open('data/live-items.json'))
items = d['items']
print('total items:', len(items))
print('meta:', json.dumps(d.get('meta', {}), ensure_ascii=False))
print('--- newest 25 by publishedAt ---')
def key(it):
    return it.get('publishedAt') or ''
for it in sorted(items, key=key, reverse=True)[:25]:
    print(it.get('publishedAt'), '|', it.get('sourceKey'), '|', it.get('id'), '|', it.get('title', {}).get('sc', '')[:45])
print('--- sourceKey counts (newest 200) ---')
c = collections.Counter(it.get('sourceKey') for it in sorted(items, key=key, reverse=True)[:200])
for k, v in c.most_common():
    print(k, v)
print('--- existing ids (all) sample of source-date pattern for today ---')
today = [it.get('id') for it in items if '2026-09-22' in str(it.get('id', ''))]
print('today ids count:', len(today))
for t in today[:60]:
    print(' ', t)
