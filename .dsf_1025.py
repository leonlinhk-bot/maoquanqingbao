#!/usr/bin/env python3
"""Filter ds_search results: whitelist + authority + date, show 10-23..10-25."""
import json, re
from datetime import datetime, timezone, timedelta

HKT = timezone(timedelta(hours=8))
rows = json.load(open('/Users/leonliang/maoquanqingbao/data/_raw_1025_0044/ds_search.json'))
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
known = set()
for i in d['items']:
    u = (i.get('originalUrl') or '').split('?')[0]
    if u: known.add(u)

WL = re.compile(r'(ia\.org\.hk|hkma\.gov\.hk|info\.gov\.hk|nfra\.gov\.cn|fstb\.gov\.hk|hkfi\.org\.hk|'
                r'insurancebusinessmag|insuranceasia|reinsurancene|insuranceasianews|artemis\.bm|'
                r'scmp\.com|hket\.com|mingpao|hkej\.com|stheadline|hk01|aastocks|caixin|yicai|'
                r'bloomberg|reuters|ft\.com|wsj\.com|nikkei|ambest|swissre|munichre|zurich|'
                r'allianz|blackrock|goldmansachs|morganstanley|jpmorgan|pimco|ubs|aia\.com|'
                r'prudential|manulife|axa\.com|sunlife|fwd|boclife|chubb|hsbc)')
rows.sort(key=lambda r: r.get('date') or '', reverse=True)
print('=== 2026-10-23..25, authority>=3, whitelisted ===')
for r in rows:
    dt = (r.get('date') or '')[:10]
    if dt < '2026-10-23':
        continue
    a = r.get('authority') or 0
    u = r.get('url') or ''
    flag = 'WL' if WL.search(u) else '--'
    dup = 'DUP' if u.split('?')[0] in known else '   '
    print(f"{dt} a{a} {flag} {dup} | {r['title'][:80]}")
    print(f"                 {u[:120]}")
