#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract InsuranceAsia homepage cards (url/title/date) and flag ones not in DB."""
import re, json, html
from datetime import datetime, timezone, timedelta

HKT = timezone(timedelta(hours=8))
raw = open('/Users/leonliang/maoquanqingbao/data/_1015/insuranceasia.raw', encoding='utf-8').read()
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json', encoding='utf-8'))
urls = {(it.get('originalUrl') or '').rstrip('/') for it in d['items']}
titles_in_db = {(it.get('title', {}).get('sc') or '') for it in d['items']}

# article cards: <a href=".../insurance/news/...">...<h3 ...>title</h3> ... date text
cards = {}
for m in re.finditer(r'href="(https://insuranceasia\.com/[a-z\-]+/[a-z\-]+/[^"?#]+)"', raw):
    u = m.group(1)
    if u not in cards:
        cards[u] = raw[m.start(): m.start() + 3000]

print(f'cards found: {len(cards)}')
for u, blob in cards.items():
    txt = re.sub(r'(?s)<[^>]+>', ' ', blob)
    txt = re.sub(r'\s+', ' ', html.unescape(txt)).strip()
    dm = re.search(r'(\d{1,2} \w{3} 2026|\w+ \d{1,2}, 2026|2026-\d{2}-\d{2}|\d{1,2}/\d{1,2}/\d{4})', txt)
    date = dm.group(0) if dm else '?'
    flag = 'IN-DB' if u.rstrip('/') in urls else 'NEW '
    print(f'  [{flag}] [{date}] {u}')
    print(f'        {txt[:150]}')
