import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items']
urls = {it.get('originalUrl', '').split('?')[0].rstrip('/') for it in items}
ids = {it.get('id') for it in items}

cands = [
 'https://www.insurancebusinessmag.com/asia/news/breaking-news/syariah-spinoff-deadline-creates-new-counterparties-for-indonesia-brokers-594586.aspx',
 'https://www.insurancebusinessmag.com/asia/news/cyber/osaka-brokerage-breach-raises-thirdparty-cyber-risk-questions-for-insurers-594580.aspx',
 'https://www.insurancebusinessmag.com/asia/news/breaking-news/pvi-insurance-takes-vietnams-largest-nonlife-book-into-central-asia-and-the-middle-east-594577.aspx',
 'https://www.insurancebusinessmag.com/asia/news/cyber/smes-rank-cyber-their-top-risk-but-misread-the-threats-cfc-594508.aspx',
 'https://www.artemis.bm/news/world-food-programme-buys-parametric-tropical-cyclone-insurance-from-ccrif/',
 'https://www.artemis.bm/news/hannover-re-raises-acorn-re-parametric-cat-bond-target-size-again-to-450m/',
 'https://www.artemis.bm/news/usaa-lowers-pricing-again-for-still-350m-residential-re-2026-2-cat-bond/',
 'https://www.scmp.com/business/banking-finance/article/3371810/hong-kong-targets-financial-innovation-help-ease-economic-pain-points',
 'https://insuranceasia.com/insurance/in-focus/chinas-medical-insurance-costs-rise-6-in-2027',
 'https://insuranceasia.com/insurance/news/global-insurance-market-hit-20t-2035t',
 'https://insuranceasia.com/insurance/news/ping-ans-new-business-value-plunge-44-in-q3-2026',
 'https://insuranceasia.com/insurance/news/luen-fung-hang-stays-profitable-despite-macau-insurance-slowdown',
 'https://insuranceasianews.com/beazley-navigating-geopolitical-risks-at-sea/',
 'https://insuranceasianews.com/iag-confident-raci-deal-will-be-completed-in-2027-despite-opposition/',
 'https://www.axa.com.hk/zh/news-room/',
]
for c in cands:
    k = c.split('?')[0].rstrip('/')
    print('IN ' if k in urls else 'NEW', c[:110])

print('\n--- recent 25 items (id | publishedAt | sourceKey | title) ---')
for it in items[:25]:
    print(it['id'], '|', it.get('publishedAt'), '|', it.get('sourceKey'), '|', (it['title'].get('sc') or '')[:55])

print('\n--- sourceKeys used in last 40 ---')
from collections import Counter
print(Counter(it.get('sourceKey') for it in items[:40]))
print('\n--- all known sourceKeys ---')
print(sorted({it.get('sourceKey') for it in items}))
