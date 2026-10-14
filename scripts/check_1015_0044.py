#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dump NFRA rows + check candidate URLs against live-items DB."""
import json, os
from datetime import datetime, timezone, timedelta

HKT = timezone(timedelta(hours=8))
DIR = '/Users/leonliang/maoquanqingbao/data/_1015'

j = json.load(open(os.path.join(DIR, 'nfra_dyn.raw'), encoding='utf-8'))
rows = j['data']['rows']
print(f'NFRA rows: {len(rows)} (total {j["data"]["total"]})')
for r in rows:
    print(f"  [{r.get('publishDate')}] {r.get('docTitle')}")
    print(f"        https://www.nfra.gov.cn/cn/view/pages/ItemDetail.html?docId={r.get('docId')}")

d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json', encoding='utf-8'))
items = d['items']
urls = {(it.get('originalUrl') or '').rstrip('/') for it in items}
ids = {it.get('id') for it in items}

print('\n-- candidate URL check --')
cands = [
 'https://www.artemis.bm/news/cat-bonds-offer-flexibility-across-fixed-income-and-alternative-investment-allocations-victory-capital/',
 'https://www.artemis.bm/news/picc-pcs-new-12m-great-wall-re-is-the-first-hong-kong-sidecar-ils-issuance/',
 'https://www.insurancebusinessmag.com/asia/business-strategy/demographic-changes-to-shrink-canadas-workforce-bank-of-canada-593491.aspx',
 'https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/10/20261014-7/',
 'https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/10/20261014-6/',
 'https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/10/20261014-5/',
 'https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/10/20261014-3/',
 'https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/10/20261014-4/',
 'https://insuranceasianews.com/mclarens-nathan-baran-swaps-sydney-for-singapore-named-regional-loss-adjuster/',
 'https://www.insurancebusinessmag.com/asia/news/breaking-news/credit-cover-alone-will-not-scale-emergingmarket-climate-finance-moodys-says-593437.aspx',
]
for u in cands:
    print(('DUP ' if u.rstrip('/') in urls else 'NEW '), u)

print('\n-- existing sourceKeys count --')
from collections import Counter
c = Counter(it.get('sourceKey') for it in items)
for k, v in c.most_common():
    print(f'  {k}: {v}')
