#!/usr/bin/env python3
"""Validate structure of the newly added items (and whole library sanity)."""
import json, re
from datetime import datetime, timedelta, timezone

HKT = timezone(timedelta(hours=8))
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json', encoding='utf-8'))
items = d['items']
print('total items:', len(items), '| meta.itemCount:', d['meta'].get('itemCount'),
      '| generatedAt:', d['meta'].get('generatedAt'))

new = [it for it in items if '20261014' in (it.get('id') or '') and it['publishedAt'] >= '2026-10-14T02:11']
print(f'items with publishedAt >= 2026-10-14T02:11 and id containing 20261014: {len(new)}')

bad = []
ids = {}
for it in new:
    errs = []
    for f in ['id', 'publishedAt', 'originalUrl', 'sourceTier', 'sourceKey', 'score',
              'verifyStatus', 'boards', 'themes', 'title', 'summary', 'why', 'source', 'tags']:
        if not it.get(f):
            errs.append('missing:' + f)
    if len(it.get('boards') or []) < 1:
        errs.append('boards<1')
    if len(it.get('themes') or []) < 2:
        errs.append('themes<2')
    for k in ('sc', 'tc'):
        t = (it.get('title') or {}).get(k, '')
        s = (it.get('summary') or {}).get(k, '')
        if not t or not s:
            errs.append(f'empty:{k}')
    sl = len((it.get('summary') or {}).get('sc', ''))
    if not (40 <= sl <= 260):
        errs.append(f'summary_sc_len={sl}')
    if not (it.get('source') or {}).get('lang') in ('zh', 'en', 'zh+en'):
        errs.append('source.lang')
    if it['id'] in ids:
        errs.append('dup-id')
    ids[it['id']] = 1
    if errs:
        bad.append((it['id'], errs))

print(f'\ninvalid new items: {len(bad)}')
for i, e in bad:
    print('  !', i, e)

print('\n--- new items list ---')
for it in sorted(new, key=lambda x: x['publishedAt']):
    print(f"  {it['publishedAt']}  {it['sourceKey']:20} {it['sourceTier']:9} {it['score']:>3} "
          f"{it['verifyStatus']:9} {(it['title'].get('sc') or '')[:60]}")
