#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
live = json.load(open('/tmp/hkii_items3.json'))
print('site top keys:', list(live.keys()))
print('site itemCount:', live.get('itemCount'), 'len:', len(live['items']))
head = [it['id'] for it in live['items'][:16]]
print('site head ids:', head)
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
print('--- spot check local ---')
for it in d['items'][:3]:
    print(it['id'], '|', it['publishedAt'], '|', it['sourceKey'], '|', it['sourceTier'], it['score'])
    print('   T:', it['title']['sc'])
    print('   S:', it['summary']['sc'][:120])
    print('   W:', it['why']['sc'][:90])
lc = json.load(open('/Users/leonliang/maoquanqingbao/data/last-check.json'))
print('last-check sources:', len(lc['sources']), 'distinct last stamps:', {v['last'] for v in lc['sources'].values()})
