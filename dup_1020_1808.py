import json, glob, re
from datetime import datetime, timezone, timedelta
HKT = timezone(timedelta(hours=8))
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items']
urls = set()
titles = []
for it in items:
    u = it.get('originalUrl', '')
    if u:
        urls.add(u.split('?')[0].rstrip('/'))
    titles.append(it['title']['sc'])

# recent 3 days items for context
cut = datetime(2026, 10, 18, tzinfo=HKT)
print('=== items since 10-18 ===')
for it in items:
    try:
        dt = datetime.fromisoformat(it['publishedAt'])
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=HKT)
    except Exception:
        continue
    if dt >= cut:
        print(it['publishedAt'][:16], '|', it['sourceKey'], '|', it['title']['sc'][:70])

print('\n=== dup check for candidate urls ===')
cands = [
 'https://www.reinsurancene.ws/nms-capital-launches-specialty-mga-ascendra/',
 'https://insuranceasianews.com/australias-cyclone-pool-cuts-up-to-37-of-home-insurance-premiums-in-high-risk-areas/',
 'https://insuranceasianews.com/a-lot-of-hunger-to-grow-strong-reinsurer-results-drive-further-apac-softening-howden-res-souter-says/',
 'https://insuranceasianews.com/cybercube-adds-sompo-japan-to-growing-apac-client-base/',
 'https://insuranceasia.com/insurance/news/sunlife-adopts-new-global-branding',
 'https://insuranceasia.com/insurance/news/hdfc-life-lifts-new-business-value-15-122m',
 'https://insuranceasia.com/insurance/news/taiwan-approves-full-health-insurance-subsidies-seniors',
 'https://insuranceasia.com/insurance/news/taiping-reinsurance-sustains-strong-capital-position-am-best',
 'https://insuranceasia.com/insurance/in-focus/indonesia-insurers-face-profit-squeeze-despite-stable-outlook',
 'https://insuranceasia.com/insurance/news/canara-hsbc-life-launches-dollar-based-wealth-plan',
 'https://www.artemis.bm/news/clear-exit-terms-and-liquid-collateral-key-to-lowering-casualty-sidecar-tail-risk-charges-am-best/',
 'https://www.artemis.bm/news/franklin-templeton-moderates-cat-bond-conviction-to-overweight-turns-neutral-on-ils/',
 'https://www.reinsurancene.ws/howden-re-highlights-reinsurances-role-as-a-capital-tool-as-prices-soften/',
 'https://www.reinsurancene.ws/moodys-forecasts-further-growth-in-german-insurers-private-credit-investments/',
 'https://www.reinsurancene.ws/w-r-berkleys-q326-gwp-rise-to-3-95bn/',
]
for c in cands:
    k = c.split('?')[0].rstrip('/')
    print(('DUP ' if k in urls else 'NEW '), c)
