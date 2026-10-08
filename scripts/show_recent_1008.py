#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Print 2 recent items fully (calibrate summary length / style / score by tier)."""
import json

d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json', encoding='utf-8'))
byid = {it['id']: it for it in d['items']}
for target in ('iaan-ok-financial-yebyeol-insurance-kdic-20261008',
               'artemis-ils-returns-short-term-rates-agecroft-20261008',
               'aia-genz-mpf-virtual-competition-20261005'):
    it = byid.get(target)
    if not it:
        print('MISSING', target)
        continue
    print('=' * 90)
    print(json.dumps(it, ensure_ascii=False, indent=1))
    print('summary len sc:', len(it.get('summary', {}).get('sc', '')))
