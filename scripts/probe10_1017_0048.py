#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html, json
D = '/Users/leonliang/maoquanqingbao/data/_1017_0048/'
def strip(t):
    t = re.sub(r'<[^>]+>', ' ', t or '')
    return html.unescape(re.sub(r'\s+', ' ', t)).strip()
raw = open(D + 'ibm.out', encoding='utf-8', errors='replace').read()
for m in re.findall(r'<link[^>]*href="([^"]+)"', raw):
    if 'mental-health' in m or 'poaching' in m or 'axa-finds' in m:
        print('FULLURL', m)
print('--- iaasia latest dates ---')
r = open(D + 'iaasia.out', encoding='utf-8', errors='replace').read()
titles = re.findall(r'<item[\s>].*?</item>', r, re.S)
print('iaasia items', len(titles))
for e in titles[:5]:
    t = re.search(r'<title[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', e, re.S)
    p = re.search(r'<pubDate[^>]*>(.*?)</', e, re.S)
    print('  ', strip(p.group(1)) if p else '', '|', strip(t.group(1))[:80] if t else '')

d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
blob = json.dumps(d['items'][:120], ensure_ascii=False)
for k in ['Donaldson Brown', 'people moves', 'Generali Central', 'Nepal', 'Isaias', 'Stand ']:
    print(k, '->', k in blob)
