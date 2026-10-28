import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items']
cands = [
 ('hong-kong-insurers-see-premium-boom', 'premium boom'),
 ('insurance-information-platform-deploys-ai', 'HK Insurance Hub'),
 ('south-korean-regulator-blocks', 'korean regulator'),
 ('indian-brokers-face', 'commission caps'),
 ('eu-unveils-climate-resilience', 'climate resilience'),
 ('former-regulator-suspended-death', 'bribery'),
 ('challenger-rejects-daiichi', 'Challenger'),
 ('staged-car-crashes', 'staged'),
 ('envest-agencies-rebrands', 'Envest'),
 ('sompo-apacs-consumer', 'Sompo'),
]
for slug, kw in cands:
    hits = [i for i in items if slug in i.get('originalUrl', '') or kw.lower() in (i.get('title', {}).get('sc', '') + i.get('title', {}).get('tc', '')).lower()]
    print(f'{slug:45s} dup={len(hits)}', [h.get('publishedAt')[:10] for h in hits][:3])
# also look for same-event different headline
for kw in ['Jefferies', '保费', '佣金上限', '氣候韌性', '气候', '第一生命', 'AI合资', 'AI 合資', '骗保', '騙保', 'AI解读', 'AI解讀']:
    hits = [i for i in items[:200] if kw in i.get('title', {}).get('sc', '') + i.get('title', {}).get('tc', '')]
    if hits:
        print('KW', kw, '->', [(h['publishedAt'][:10], h['title']['sc'][:45]) for h in hits[:3]])
