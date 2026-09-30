#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items']

def show(pred, label, n=1):
    c = 0
    for it in items:
        if pred(it):
            print("=" * 10, label, "=" * 10)
            print(json.dumps(it, ensure_ascii=False, indent=1)[:3500])
            c += 1
            if c >= n:
                break

show(lambda i: i.get('sourceKey') == 'hkma' and 'hkicl' in (i.get('originalUrl') or '').lower(), 'HKMA HKICL alert')
show(lambda i: i.get('sourceKey') == 'ia', 'IA item')
show(lambda i: i.get('sourceKey') == 'scmp', 'SCMP item')
show(lambda i: i.get('sourceKey') == 'insurancebusinessmag', 'IBM item')
print("---- themes 词表 ----")
from collections import Counter
c = Counter()
for it in items:
    for t in it.get('themes', []):
        c[t] += 1
print(sorted(c.items(), key=lambda x: -x[1])[:60])
print("---- boards 词表 ----")
c2 = Counter()
for it in items:
    for b in it.get('boards', []):
        c2[b] += 1
print(sorted(c2.items(), key=lambda x: -x[1]))
print("---- sourceTier 词表 ----")
c3 = Counter(it.get('sourceTier') for it in items)
print(sorted(c3.items(), key=lambda x: -x[1]))
print("---- contentKind 词表 ----")
c4 = Counter(it.get('contentKind') for it in items)
print(sorted(c4.items(), key=lambda x: -x[1]))
