#!/usr/bin/env python3
"""查库内是否已有这些候选（按 URL / 标题关键词）。"""
import json, re

lib = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = lib['items']
urls = {i.get('originalUrl', '') for i in items}
titles = [i['title']['sc'] for i in items]

tests = [
    ('A1', 'ao', 'Evolving ILS capital landscape', ['ILS', 'O\'Donnell', 'RenRe CEO']),
    ('A2', 'ao', 'Scale of client needs', ['Aon CEO', 'Greg Case', '风险与资本']),
    ('A3', 'ao', 'VIG Re Charles Bridge', ['Charles Bridge', 'VIG Re', '维也纳']),
    ('A4', 'ao', 'Morocco securitization', ['Morocco', '摩洛哥']),
    ('A5', 'ao', 'Lockton Re Jeremy England Lee', ['Lockton', '洛克顿']),
    ('B1', 'ibm', 'Aon debt USI', ['Aon', 'USI']),
    ('B2', 'ibm', 'Arch primary insurance', ['Arch', '安达']),
    ('B3', 'ibm', 'Mining soft market', ['矿业', 'Mining']),
    ('B4', 'ibm', 'IUMI marine premium', ['IUMI', '海运']),
    ('C1', 'ia', 'Challenger Daiichi', ['Challenger', 'Daiichi', '第一生命']),
    ('C2', 'ia', 'Prudential AI operations', ['Prudential', '保诚']),
    ('C3', 'ia', 'Marsh rates fall 5%', ['Marsh', '达信']),
    ('C4', 'ia', 'Ping An NBV plunge', ['平安', 'Ping An']),
    ('C5', 'ia', 'Allianz Partners students', ['Allianz Partners', '安联']),
    ('C6', 'ia', 'AIA HSBC insurance chief regional CEO', ['AIA', '友邦']),
]

for code, src, label, kws in tests:
    hits = [t for t in titles if any(k.lower() in t.lower() for k in kws)]
    print(f'{code} {label:38} -> {len(hits)} hits')
    for h in hits[:3]:
        print('        ', h[:90])

print()
print('=== 库内最近 40 条 originalUrl ===')
for i in items[:40]:
    print(i['publishedAt'][:16], '|', i.get('sourceKey', '')[:20], '|', i.get('originalUrl', '')[:95])
