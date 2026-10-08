#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dump excerpt / acf / taxonomy fields for selected InsuranceAsia News posts."""
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
]


def clean(h):
    h = re.sub(r'<[^>]+>', ' ', h or '')
    return re.sub(r'\s+', ' ', html.unescape(h)).strip()


for p in data:
    if any(w in p.get('link', '') for w in WANT):
        print('=' * 80)
        print('TITLE:', clean(p['title']['rendered']))
        print('EXCERPT:', clean(p.get('excerpt', {}).get('rendered', ''))[:900])
        print('TOPIC:', p.get('topic'), '| LOB:', p.get('line_of_business'), '| CO:', p.get('companies_category'))
        print('SUBJECT:', p.get('subject'))
        acf = p.get('acf') or {}
        keep = {k: v for k, v in acf.items() if isinstance(v, (str, int, float)) and v}
        print('ACF:', json.dumps(keep, ensure_ascii=False)[:900])
