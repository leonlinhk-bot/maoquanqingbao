#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items']
print("---- IA official items (publishedAt + id + contentKind) ----")
n = 0
for it in items:
    if it.get('sourceKey') == 'ia' and it.get('contentKind') in ('circular', 'press'):
        print(it.get('publishedAt'), '|', it.get('contentKind'), '|', it.get('verifyStatus'), '|', it['id'])
        n += 1
        if n > 22:
            break
print()
print("---- 是否有 date-only 条目 ----")
n = 0
for it in items:
    p = it.get('publishedAt', '')
    if len(p) == 10:
        n += 1
        if n <= 8:
            print(p, '|', it.get('sourceKey'), '|', it['title']['sc'][:60])
print("date-only 总数:", n)
print()
print("---- 最近 3 条 IA 条目完整 ----")
n = 0
for it in items:
    if it.get('sourceKey') == 'ia':
        print(json.dumps({k: it.get(k) for k in ('id', 'publishedAt', 'contentKind', 'boards', 'themes', 'source', 'originalUrl', 'verifyStatus')}, ensure_ascii=False, indent=1))
        n += 1
        if n >= 3:
            break
