#!/usr/bin/env python3
import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json', encoding='utf-8'))
items = d['items']
old = [it for it in items if it['publishedAt'] < '2026-10-14T02:11']
new = [it for it in items if it['publishedAt'] >= '2026-10-14T02:11']


def stats(xs, label):
    L = sorted(len((it.get('summary') or {}).get('sc', '')) for it in xs)
    if not L:
        return
    n = len(L)
    print(f'{label:10} n={n:5} min={L[0]:4} p25={L[n//4]:4} med={L[n//2]:4} p75={L[3*n//4]:4} max={L[-1]:4} '
          f'| >260: {sum(1 for x in L if x > 260)}')


stats(old, 'existing')
stats(new, 'new')
print()
for tier in ['official', 'insurer', 'pro', 'media']:
    stats([it for it in old if it.get('sourceTier') == tier], f'old/{tier}')
print()
# what does app.js render? show one existing official item summary
ex = [it for it in old if it.get('sourceTier') == 'official']
ex.sort(key=lambda x: -len((x.get('summary') or {}).get('sc', '')))
if ex:
    print('longest existing official summary:', len(ex[0]['summary']['sc']))
    print(ex[0]['summary']['sc'][:500])
