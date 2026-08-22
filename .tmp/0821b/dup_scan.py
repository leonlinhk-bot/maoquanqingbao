#!/usr/bin/env python3
import json

d = json.load(open('data/live-items.json'))
items = d['items']
kw = ['平安', 'ping an', 'pingan', '再保险资本', 'reinsurance capital', '医保', 'healthcare plan',
      'etf connect', '南向', '央票', 'renminbi bills', '人民币', '安联贸易', 'allianz trade',
      '太古坊', 'taikoo', '保费融资', 'premium financing', 'julius', 'wealth plans', 'life insurance books',
      'insolvency']
print('=== keyword scan ===')
for it in items:
    blob = (it['id'] + ' ' + it['title']['sc'] + ' ' + it['title']['tc']).lower()
    for k in kw:
        if k in blob:
            print(f'  [{k}] {it["id"]} | {it.get("publishedAt","")} | {it["title"]["sc"][:55]}')
            break
print()
print('=== insuranceasia items 8/19-8/21 ===')
for it in items:
    if it.get('sourceKey') in ('insuranceasia', 'InsuranceAsia', 'asiainsurancereview'):
        print(it['id'], '|', it.get('publishedAt'), '|', it['title']['sc'][:60])
print()
print('=== hkma items 8/18-8/21 ===')
for it in items:
    if 'hkma' in it['id'] or it.get('sourceKey') in ('hkma', 'hkma_press'):
        print(it['id'], '|', it.get('publishedAt'), '|', it['title']['sc'][:60])
