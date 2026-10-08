#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dump full rendered bodies from InsuranceAsia News WP API JSON for selected slugs."""
import json
import re
import html

data = json.load(open('/tmp/ian.json', encoding='utf-8'))
WANT = [
    'specialty-mga-hires-david-higgins',
    'apac-data-centre-expansion-concentrates-risk',
    'gic-res-investment-income',
    'marsh-elevates-sonya-febbo',
    'aviso-specialty-hires-marsh-veteran-eric-wojcik',
    'ms-amlin-seeks-investors',
    'business-interruption-claim-severity',
]


def clean(h):
    h = re.sub(r'<script.*?</script>', ' ', h, flags=re.S)
    h = re.sub(r'<style.*?</style>', ' ', h, flags=re.S)
    h = re.sub(r'<[^>]+>', '\n', h)
    h = html.unescape(h)
    lines = [ln.strip() for ln in h.split('\n')]
    return '\n'.join(ln for ln in lines if ln)


for p in data:
    link = p.get('link', '')
    if any(w in link for w in WANT):
        print('=' * 90)
        print('TITLE:', html.unescape(re.sub('<[^>]+>', '', p.get('title', {}).get('rendered', ''))))
        print('DATE_GMT:', p.get('date_gmt'), '| DATE:', p.get('date'))
        print('LINK:', link)
        body = clean(p.get('content', {}).get('rendered', ''))
        print('BODY:')
        print(body[:2600])
        print()
print('keys available:', sorted(data[0].keys()))
