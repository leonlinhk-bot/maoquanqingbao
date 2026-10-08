#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check candidate URLs / keywords against live-items.json for dedup."""
import json

d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json', encoding='utf-8'))
items = d['items']
urls = {(it.get('originalUrl') or '').rstrip('/') for it in items}
titles = [(it.get('id'), ' '.join((it.get('title') or {}).values())) for it in items]

CANDS = [
    'insuranceasianews.com/specialty-mga-hires-david-higgins-to-lead-global-bloodstock-expansion',
    'insuranceasianews.com/apac-data-centre-expansion-concentrates-risk',
    'insuranceasianews.com/gic-res-investment-income-makes-up-for-lack-of-technical-profits-am-best',
    'insuranceasianews.com/marsh-elevates-sonya-febbo-to-australia-head-of-authorised-representatives',
    'insuranceasianews.com/aviso-specialty-hires-marsh-veteran-eric-wojcik-to-stand-up-capital-solutions-group',
    'insuranceasianews.com/ms-amlin-seeks-investors-for-new-us40-50m-singapore-sidecar',
    'insuranceasianews.com/business-interruption-claim-severity-up-more-than-30-a-year-allianz-commercial',
    'insurancebusinessmag.com/asia/news/cyber/aipowered-bank-hacks-in-south-korea',
    'insurancebusinessmag.com/asia/news/mergers-acquisitions/dealmakers-are-moving-faster-and-bigger-yet-underperforming-wtw-says',
    'insurancebusinessmag.com/asia/news/claims/average-business-interruption-claim-now-70-larger-than-property-damage',
    'artemis.bm/news/from-hard-market-to-normalisation-cat-bond-discipline-in-practice-artemis-london-2026-video',
    'artemis.bm/news/reask-to-provide-settlement-data-for-interactive-brokers-forecastex-live-hurricane-contracts',
    'insuranceasia.com/insurance/news/insurtech-funding-hits-24b-ai-dominates-deals',
    'insuranceasia.com/insurance/news/prudential-plan-eases-protection-gap-caregivers',
    'insuranceasia.com/insurance/news/manulife-cuts-risk-32b-reinsurance-deal-closes',
    'insuranceasia.com/insurance/news/aia-loses-china-bancassurance-share-sales-fall-6',
    'insuranceasia.com/insurance/in-focus/asia-casualty-insurers-face-rising-claims-costs',
]
print('=== URL presence check ===')
for c in CANDS:
    hit = [u for u in urls if c in u]
    print(('PRESENT ' if hit else 'MISSING '), c, ('-> ' + hit[0]) if hit else '')

print()
print('=== keyword check ===')
for kw in ['Allianz Commercial', '業務中斷', 'Manulife', 'AIA', 'Prudential', 'insurtech', '資料中心', '數據中心',
           'sidecar', 'Howden', 'GIC Re', 'bloodstock', 'Wojcik', 'Febbo', 'Reask', 'ForecastEx']:
    hits = [i for i, t in titles if kw.lower() in t.lower()]
    print(f'  {kw}: {len(hits)}', hits[:6])

print()
print('=== items with publishedAt >= 2026-10-08 (all) ===')
for it in sorted(items, key=lambda x: x.get('publishedAt') or '', reverse=True):
    pa = it.get('publishedAt') or ''
    if pa >= '2026-10-08':
        print(f"  {pa} | {it.get('sourceKey')} | {it.get('id')} | {(list((it.get('title') or {}).values()) or [''])[0]}")

print()
print('=== the allianz item in full ===')
for it in items:
    if it.get('id') == 'allianz-commercial-bi-claims-severity-20261008':
        print(json.dumps(it, ensure_ascii=False, indent=1))

print()
print('=== the manulife / prudential / aia recent items ===')
for it in items:
    sid = it.get('id') or ''
    if any(k in sid for k in ('manulife', 'prudential', 'aia-')) and (it.get('publishedAt') or '') >= '2026-09-20':
        print(f"  {it.get('publishedAt')} | {it.get('sourceKey')} | {sid} | {(list((it.get('title') or {}).values()) or [''])[0]}")
