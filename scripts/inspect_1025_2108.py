import json, re, sys
from pathlib import Path

p = Path('data/live-items.json')
d = json.loads(p.read_text())
items = d['items']
print('TOTAL', len(items))
print('META', json.dumps(d.get('meta', {}), ensure_ascii=False))
print('--- TOP 8 ---')
for it in items[:8]:
    print(it['publishedAt'], '|', it['sourceKey'], '|', it['id'], '|', it['title']['sc'][:60])
print('--- KEYWORD SCAN ---')
for kw in ['毛保费', '5736', '禁止6人', '洗钱', '中期', '上半年']:
    hits = [i for i in items if kw in json.dumps(i, ensure_ascii=False)]
    print(kw, len(hits), [h['id'] for h in hits][:5])
print('--- SOURCE COVERAGE (last 7 days by sourceKey) ---')
from collections import Counter
c = Counter(i['sourceKey'] for i in items[:120])
print(json.dumps(c, ensure_ascii=False))
print('--- last 10 publishedAt ---')
for it in items[:15]:
    print(it['publishedAt'], it['sourceKey'])
