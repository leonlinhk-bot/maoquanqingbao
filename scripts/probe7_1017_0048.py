#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html, json
from collections import Counter
D = '/Users/leonliang/maoquanqingbao/data/_1017_0048/'
def strip(t):
    t = re.sub(r'<[^>]+>', ' ', t or '')
    return html.unescape(re.sub(r'\s+', ' ', t)).strip()

raw = open(D + 'ibm.out', encoding='utf-8', errors='replace').read()
for e in re.findall(r'<item[\s>].*?</item>', raw, re.S):
    t = re.search(r'<title[^>]*>(.*?)</title>', e, re.S)
    l = re.search(r'<link[^>]*>(.*?)</link>', e, re.S)
    d = re.search(r'<pubDate[^>]*>(.*?)</', e, re.S)
    de = re.search(r'<description[^>]*>(.*?)</description>', e, re.S)
    title = strip(t.group(1)) if t else ''
    if 'mental health' in title or 'Poaching' in title:
        print('T:', title)
        print('L:', strip(l.group(1)) if l else '')
        print('D:', strip(d.group(1)) if d else '')
        print('S:', (strip(de.group(1)) if de else '')[:700])
        print('---')

d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items']
print('sourceKeys top200:', Counter(it.get('sourceKey') for it in items[:200]).most_common(30))
print('boards:', Counter(tuple(it.get('boards', [])) for it in items[:200]).most_common(12))
print('themes sample:', [it.get('themes') for it in items[:6]])
for it in items:
    if it.get('sourceKey') == 'insurancebusinessmag':
        print('--- ibm full ---')
        print(json.dumps(it, ensure_ascii=False, indent=1)[:1800])
        break
