#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Normalise SC/TC for the 11 items added at 2026-10-13 21:08.

I authored the copy in Traditional; the site convention is sc=Simplified, tc=Traditional.
So derive sc by converting the authored (Traditional) text to zh-hans.
"""
import json
import zhconv

NEW_IDS = {
    "ibm-japan-fsa-prudential-life-suspension-593252-20261013",
    "artemis-leadenhall-ils-controlled-ai-20261013",
    "artemis-swiss-re-reinsurance-supply-alt-capital-20261013",
    "artemis-liberty-mutual-re-mexico-parametric-quake-payout-20261013",
    "ian-barcelona-floods-urban-flood-risk-20261013",
    "ian-ibisa-parametric-india-ceo-20261013",
    "ian-howden-australia-sport-entertainment-practice-20261013",
    "iaasia-singlife-ai-human-oversight-20261013",
    "iaasia-singapore-insurance-adequacy-retirement-20261013",
    "iaa-taiwan-insurers-invest-health-ltc-97223-20261013",
    "iaa-mental-health-absences-organisational-risk-97222-20261013",
}

path = 'data/live-items.json'
d = json.load(open(path, encoding='utf-8'))
fixed = 0
for it in d['items']:
    if it.get('id') not in NEW_IDS:
        continue
    for field in ('title', 'summary', 'why', 'source'):
        v = it.get(field)
        if isinstance(v, dict) and 'tc' in v:
            hant = zhconv.convert(v['tc'], 'zh-hant')
            v['tc'] = hant
            v['sc'] = zhconv.convert(hant, 'zh-hans')
    for k, v in (it.get('actions') or {}).items():
        if isinstance(v, dict) and 'tc' in v:
            hant = zhconv.convert(v['tc'], 'zh-hant')
            v['tc'] = hant
            v['sc'] = zhconv.convert(hant, 'zh-hans')
    tg = it.get('tags')
    if isinstance(tg, dict) and 'tc' in tg:
        hant = [zhconv.convert(x, 'zh-hant') for x in tg['tc']]
        tg['tc'] = hant
        tg['sc'] = [zhconv.convert(x, 'zh-hans') for x in hant]
    fixed += 1

json.dump(d, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print("normalised items:", fixed)

# spot check
for it in d['items'][:11]:
    print("-", it['id'])
    print("   sc:", it['title']['sc'][:34])
    print("   tc:", it['title']['tc'][:34])
    print("   tags sc:", it['tags']['sc'][:3], "| tags tc:", it['tags']['tc'][:3])
