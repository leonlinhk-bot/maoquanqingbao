import json, re, os, html, subprocess
DB = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json', encoding='utf-8'))
urls = set()
for i in DB['items']:
    u = (i.get('originalUrl') or '').strip()
    if u: urls.add(u)
print('DB items', len(DB['items']), 'unique urls', len(urls))
# also index titles
titles = [i['title']['sc'] for i in DB['items']]
def has(u):
    return any(u.split('?')[0] in x or x in u.split('?')[0] for x in urls if x)
cands = [
 'https://insuranceasia.com/insurance/news/insurers-boost-facultative-cover-markets-soften',
 'https://insuranceasia.com/insurance/news/reinsurers-lift-returns-capital-hits-record-688b',
 'https://insuranceasia.com/insurance/news/airline-insurers-brace-q4-claims-pressure',
 'https://insuranceasia.com/insurance/news/cyber-insurers-gain-sharper-risk-view-digital-footprints',
 'https://insuranceasia.com/insurance/in-focus/insurance-assets-lose-ground-securities-surge',
 'https://insuranceasianews.com/australia-new-zealand-join-uk-canada-to-launch-joint-alliance-to-confront-escalating-shared-risks/',
 'https://insuranceasianews.com/brokers-warn-indias-distribution-reform-plan-risks-job-cuts-sector-disruption/',
 'https://insuranceasianews.com/many-dont-appreciate-what-can-go-wrong-bloodstock-insurance-finds-its-footing-in-north-asia/',
 'https://insuranceasianews.com/lockton-taps-kenichiro-miki-as-senior-consultant-for-japan-business/',
 'https://insurancebusinessmag.com/asia/news/cyber/cfc-adds-executive-protection-ai-cover-to-cyber-policy-592583.aspx',
 'https://www.insurancebusinessmag.com/asia/news/breaking-news/cyber-is-now-the-risk-most-likely-to-trigger-everything-else-hiscox-592641.aspx',
 'https://www.insurancebusinessmag.com/asia/news/marine/ship-sunk-crew-missing-after-drone-strike-inside-nato-members-economic-zone-592511.aspx',
 'https://www.insurancebusinessmag.com/asia/news/life-insurance/philhealth-targets-benefit-overlap-with-hmos-and-private-insurers-592521.aspx',
 'https://www.scmp.com/native/business/topics/fostering-future-innovators/article/3369878/family-offices-branch-out-private-equity-infrastructure-and-alternative-investments',
 'https://www.scmp.com/business/money/investment-products/article/3369945/hong-kongs-mpf-has-gained-nearly-hk100b-year-despite-september-loss',
 'https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/10/20261007-3/',
]
for c in cands:
    print(('DUP ' if has(c) else 'NEW '), c[:105])
print()
print('--- govhk insurance-related today ---')
t = open('/Users/leonliang/maoquanqingbao/data/_raw_1007_1808/govhk_zh.xml', encoding='utf-8', errors='ignore').read()
for m in re.finditer(r'<item>(.*?)</item>', t, re.S):
    b = m.group(1)
    if re.search(r'保險|保險業|年金|強積金|財庫局|財經事務', b):
        ti = re.search(r'<title>(.*?)</title>', b, re.S).group(1)
        ti = re.sub(r'^<!\[CDATA\[|\]\]>$', '', ti.strip())
        d = re.search(r'<pubDate>(.*?)</pubDate>', b).group(1)
        lk = re.search(r'<link>(.*?)</link>', b).group(1)
        print(' -', d, '|', ti[:120], '|', lk)
print()
print('--- nfra list sample ---')
n = open('/Users/leonliang/maoquanqingbao/data/_raw_1007_1808/nfra_list.html', encoding='utf-8', errors='ignore').read()
n2 = re.sub(r'<script.*?</script>', ' ', n, flags=re.S)
ms = re.findall(r'<a[^>]*href="([^"]+)"[^>]*>([^<]{6,120})</a>', n2)
print('links', len(ms))
for u, ttl in ms[:40]:
    c = html.unescape(re.sub(r'\s+', ' ', ttl)).strip()
    if c: print('  *', c[:100], '||', u[:90])
