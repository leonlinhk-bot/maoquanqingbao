#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, re, html
from datetime import datetime, timezone, timedelta
D = '/Users/leonliang/maoquanqingbao/data/_1017_0048/'

def strip(t):
    t = re.sub(r'<[^>]+>', ' ', t or '')
    return html.unescape(re.sub(r'\s+', ' ', t)).strip()

j = json.load(open(D + 'ian.out', encoding='utf-8'))
for p in j[:6]:
    print('IAN', p.get('date'), '|', p.get('date_gmt'), '|', strip(p.get('title', {}).get('rendered', ''))[:80], '|', p.get('link'))
print('=====HKMA=====')
raw = open(D + 'hkma.out', encoding='utf-8', errors='replace').read()
print('len', len(raw))
for m in re.findall(r'<a[^>]+href="(/eng/news-and-media/press-releases/[^"]+)"[^>]*>(.*?)</a>', raw, re.S)[:25]:
    print(' ', m[0], '|', strip(m[1])[:90])
print('=====HKMA date blocks=====')
for m in re.findall(r'(\d{1,2} \w+ \d{4})', raw)[:20]:
    print(' ', m)
