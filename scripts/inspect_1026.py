import json, collections

d = json.load(open('data/live-items.json'))
items = d['items'] if isinstance(d, dict) else d
print('type:', type(d).__name__, 'keys:', list(d.keys())[:10] if isinstance(d, dict) else '')
print('total:', len(items))
print('meta:', json.dumps(d.get('meta', {}), ensure_ascii=False)[:600] if isinstance(d, dict) else '')
print('--- newest 12 by publishedAt ---')
s = sorted(items, key=lambda x: x.get('publishedAt', ''), reverse=True)
for it in s[:12]:
    print(it.get('publishedAt'), '|', it.get('sourceKey'), '|', it.get('verifyStatus'), '|', it.get('title', {}).get('sc', '')[:50])
print('--- per-day counts (last 8 days) ---')
c = collections.Counter(x.get('publishedAt', '?')[:10] for x in items)
for k in sorted(c, reverse=True)[:8]:
    print(k, c[k])
print('--- urls (recent 40 originalUrl) ---')
for it in s[:40]:
    print(it.get('sourceKey'), it.get('originalUrl'))
print('--- sample item ---')
print(json.dumps(s[0], ensure_ascii=False)[:1500])
