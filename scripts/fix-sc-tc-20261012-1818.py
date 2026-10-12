#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix sc/tc variants for the 2026-10-12 18:18 batch: sc=zh-hans, tc=zh-hant."""
import json

try:
    import zhconv
except Exception:
    raise SystemExit('zhconv missing')

PATH = '/Users/leonliang/maoquanqingbao/data/live-items.json'
IDS = {
 "ian-fwd-bolttech-hk-pc-25pct-21m-20261012",
 "ian-japan-domestic-reinsurance-captive-regime-20261012",
 "ian-lloyds-asia-gaip-supporting-partner-20261012",
 "ian-indonesia-solvency-rbc-consolidation-fitch-20261012",
 "ian-hartford-singapore-energy-launch-2027-20261012",
 "ian-nat-re-am-best-underwriting-improves-20261012",
 "iaasia-ai-spending-beyond-underwriting-globaldata-20261012",
 "iaasia-mox-bank-qbe-home-insurance-app-20261012",
 "iaasia-taiwan-fc-policy-sales-39-july-2026-20261012",
 "iaasia-japan-life-sales-fall-premium-growth-july-2026-20261012",
 "iaasia-tune-protect-airpaz-travel-3-asean-20261012",
 "iaasia-gic-re-underwriting-losses-am-best-20261012",
 "scmp-trp-hk-workers-ai-retirement-survey-20261012",
 "scmp-ex-hsbc-ai-agents-wealth-platform-20261012",
 "artemis-ils-diversification-sage-advisory-20261012",
 "artemis-pillar-capital-sagesure-investment-20261012",
 "manulife-hk-just-feel-my-flag-day-2026-20261010",
}

D = json.load(open(PATH, encoding='utf-8'))


def sv(s):
    """Simplified variant."""
    return zhconv.convert(s, 'zh-hans')


def tv(s):
    """Traditional variant."""
    return zhconv.convert(s, 'zh-hant')


def fix_pair(d):
    """d: {'sc':..., 'tc':...} -> normalize both from the current sc."""
    base = d.get('sc') or d.get('tc') or ''
    d['sc'] = sv(base)
    d['tc'] = tv(base)


fixed = 0
for it in D['items']:
    if it.get('id') not in IDS:
        continue
    fixed += 1
    for k in ('title', 'summary', 'why', 'contentRole'):
        if isinstance(it.get(k), dict):
            fix_pair(it[k])
    for k, v in (it.get('actions') or {}).items():
        if isinstance(v, dict):
            fix_pair(v)
    if isinstance(it.get('tags'), dict):
        it['tags']['sc'] = [sv(x) for x in it['tags'].get('sc', [])]
        it['tags']['tc'] = [tv(x) for x in it['tags'].get('tc', [])]
    if isinstance(it.get('source'), dict):
        it['source']['sc'] = sv(it['source'].get('sc', ''))
        it['source']['tc'] = tv(it['source'].get('tc', ''))

json.dump(D, open(PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('fixed items:', fixed)

for it in D['items'][:3]:
    print(it['id'])
    print(' sc:', it['title']['sc'][:56])
    print(' tc:', it['title']['tc'][:56])
