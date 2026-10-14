#!/usr/bin/env python3
"""Dump description text for specific candidate URLs + dedup check vs live-items."""
import json, re, html
import xml.etree.ElementTree as ET

D = '/Users/leonliang/maoquanqingbao/data/_1014_2108'
WANT = [
    'ils-investors-need-to-speak-up',
    'tata-aia-eases-wellness-targets',
    'philippine-legacy-planning-leaves-82',
    'nrma-western-australia-renewal-rights',
    'picc-pc-raises-us12m',
]


def clean(s):
    return html.unescape(re.sub(r'\s+', ' ', re.sub('<[^>]+>', '', s or ''))).strip()


for f in ['artemis', 'insuranceasia', 'insuranceasianews']:
    raw = open(f'{D}/{f}.raw', encoding='utf-8', errors='replace').read()
    if f == 'insuranceasianews':
        for p in json.loads(raw):
            for w in WANT:
                if w in p['link']:
                    print(f'\n[{f}] {clean(p["title"]["rendered"])}\n  date_gmt={p["date_gmt"]}\n  {p["link"]}\n  EXCERPT: {clean(p.get("excerpt",{}).get("rendered",""))[:600]}')
        continue
    root = ET.fromstring(raw)
    for it in root.iter():
        if it.tag.split('}')[-1] != 'item':
            continue
        link = title = desc = pub = ''
        for ch in it:
            t = ch.tag.split('}')[-1]
            if t == 'link':
                link = (ch.text or '').strip()
            elif t == 'title':
                title = clean(ch.text)
            elif t == 'description':
                desc = clean(ch.text)
            elif t == 'pubDate':
                pub = ch.text
        for w in WANT:
            if w in link:
                print(f'\n[{f}] {title}\n  pubDate={pub}\n  {link}\n  DESC: {desc[:700]}')

print('\n===== DEDUP CHECK vs live-items =====')
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json', encoding='utf-8'))
urls = {(it.get('originalUrl') or '').rstrip('/') for it in d['items']}
ids = {it.get('id') for it in d['items']}
for u in [
    'https://www.artemis.bm/news/ils-investors-need-to-speak-up-and-ask-for-alternative-model-views-karen-clark/',
    'https://insuranceasia.com/insurance/news/tata-aia-eases-wellness-targets-insurance-rewards',
    'https://insuranceasia.com/insurance/news/philippine-legacy-planning-leaves-82-fearing-wealth-loss',
    'https://insuranceasianews.com/iag-offers-to-trade-nrma-western-australia-renewal-rights-for-raci-deal-approval/',
    'https://www.artemis.bm/news/picc-pcs-new-12m-great-wall-re-is-the-first-hong-kong-sidecar-ils-issuance/',
]:
    print(('DUP ' if u.rstrip('/') in urls else 'NEW '), u[:110])
print('recent ids with 20261014:', [i for i in ids if i and '20261014' in i])
