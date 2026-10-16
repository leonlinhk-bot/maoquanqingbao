#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html, json
D = '/Users/leonliang/maoquanqingbao/data/_1017_0048/'
def strip(t):
    t = re.sub(r'<[^>]+>', ' ', t or '')
    return html.unescape(re.sub(r'\s+', ' ', t)).strip()

raw = open(D + 'ibm.out', encoding='utf-8', errors='replace').read()
items = re.findall(r'<item[\s>].*?</item>', raw, re.S)
print('items', len(items))
for e in items[:8]:
    t = re.search(r'<title[^>]*>(.*?)</title>', e, re.S)
    l = re.search(r'<link[^>]*>(.*?)</link>', e, re.S)
    d = re.search(r'<pubDate[^>]*>(.*?)</', e, re.S)
    print('-', strip(t.group(1))[:95], '|', strip(d.group(1)) if d else '', '|', strip(l.group(1))[:130])

d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
it = d['items'][3]
print('keys:', list(it.keys()))
print(json.dumps({k: it[k] for k in it if k in ('rolesImpact', 'actions', 'hot', 'verifyStatus')}, ensure_ascii=False)[:900])
print('hot:', json.dumps(d.get('hot'), ensure_ascii=False)[:300])
print('feedFacets keys:', list(d.get('feedFacets', {}).keys())[:10])
