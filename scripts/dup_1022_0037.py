import json, re
LIVE = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))['items']
urls = {it.get('originalUrl', '').split('?')[0].rstrip('/') for it in LIVE}
titles = [(it.get('title', {}).get('sc', '') + ' ' + it.get('title', {}).get('tc', '')) for it in LIVE]

cands = [
 ('Chubb-asia', 'chubbs-asia-life-and-consumer-lines'),
 ('Pacific-rates', 'pacific-rates-fall-12'),
 ('Skuld', 'skulds-wei-fan'),
 ('AusCyclone', 'cyclone-pool'),
 ('CyberCube', 'cybercube'),
 ('Chubb-capacity', 'hungry'),
 ('CRC', 'crc-group'),
 ('MarshRates', 'marsh-risk'),
 ('AcornRe', 'acorn-re'),
 ('EastonRe', 'easton-re'),
 ('PICC-sidecar', 'picc'),
 ('MAS-EO', 'mas-ai-governance'),
 ('Aon-pension', 'pension-risk-settlement'),
 ('Isaias', 'isaias'),
 ('Sompo', 'sompo'),
 ('Korra', 'korra'),
 ('APEC', 'apec'),
 ('YuanHK', 'yuan-trading'),
]
for name, kw in cands:
    hits = [it for it in LIVE if kw in (it.get('originalUrl', '') + ' ' + it.get('title', {}).get('sc', '') + ' ' + it.get('title', {}).get('tc', ''))]
    print(f'{name:15s} kw={kw:28s} hits={len(hits)}')
    for h in hits[:3]:
        print('     ', h['id'], '|', (h.get('publishedAt') or '')[:10], h['title']['sc'][:70])

print('\n--- live items published 2026-10-21 or later ---')
for it in LIVE:
    if (it.get('publishedAt') or '') >= '2026-10-21':
        print(it['id'], '|', it['publishedAt'], '|', it['title']['sc'][:70], '|', it.get('sourceKey'))
