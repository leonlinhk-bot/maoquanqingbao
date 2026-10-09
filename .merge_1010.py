#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""合并新条目到 live-items.json 最前，并更新 last-check.json"""
import json, shutil, datetime

P = 'data/live-items.json'
NOW = datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()

new = []
for f in ['/tmp/_new_part1.json', '/tmp/_new_part2.json', '/tmp/_new_part3.json']:
    new += json.load(open(f, encoding='utf-8'))


def key(it):
    p = it.get('publishedAt') or ''
    return p if len(p) > 10 else p + 'T00:00:00+08:00'


d = json.load(open(P, encoding='utf-8'))
items = d['items']
existing = {it['id'] for it in items}

shutil.copy(P, P + '.bak-1010')
added, skipped = [], []
for it in new:
    if it['id'] in existing:
        skipped.append(it['id'])
        continue
    added.append(it)
    existing.add(it['id'])

added.sort(key=key, reverse=True)
d['items'] = added + items
d['meta']['generatedAt'] = NOW
json.dump(d, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('新增 %d 条，跳过重复 %d 条，库总量 %d' % (len(added), len(skipped), len(d['items'])))
if skipped:
    print('重复:', skipped)
for it in added:
    print('  +', it['publishedAt'], '|', it['sourceKey'], '|', it['score'], it['verifyStatus'], '|', it['title']['sc'][:40])

# ---- last-check 回写
LC = 'data/last-check.json'
lc = json.load(open(LC, encoding='utf-8'))
lc['lastCheck'] = NOW
for k, v in lc.get('sources', {}).items():
    v['last'] = NOW
json.dump(lc, open(LC, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('last-check 回写完成:', NOW, '信源数', len(lc.get('sources', {})))
