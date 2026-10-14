#!/usr/bin/env python3
import json, re
d = json.load(open('data/_feed-inbox.json'))
print('feed inbox generated_at:', d.get('generated_at'), 'total_new:', d.get('total_new'))
for i in d.get('items', []):
    print('-', i.get('published_hkt'), '|', i.get('title'), '|', i.get('link'))

raw = open('data/live-items.json', encoding='utf-8').read()
print('\n--- GAIP mentions ---')
for m in re.finditer(r'.{60}GAIP.{60}', raw):
    print(m.group(0))
print('\n--- sidecar ids ---')
for m in re.finditer(r'"id":"([^"]*sidecar[^"]*)"', raw):
    print(m.group(1))
print('\n--- 侧挂车/PICC sidecar item blocks ---')
for m in re.finditer(r'\{"id":"[^"]{0,80}"[^{]{0,400}?側掛車.{0,200}', raw):
    print(m.group(0)[:420], '\n')
