import json, re, html

d = json.load(open('data/_raw_1004_0037.json'))
live = json.load(open('data/live-items.json'))
its = live['items']

def clean(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

print('--- DB items with publishedAt >= 2026-10-03 ---')
recent = [i for i in its if str(i.get('publishedAt', '')) >= '2026-10-03']
recent.sort(key=lambda x: x.get('publishedAt', ''), reverse=True)
print('count:', len(recent))
for i in recent:
    print(' ', i.get('publishedAt'), '|', i.get('sourceKey'), '|', i.get('id'))

print()
print('--- insuranceasia_rss first 8 pubDates/titles ---')
t = d['insuranceasia_rss']['text']
for it in re.findall(r'<item>(.*?)</item>', t, re.S)[:8]:
    ti = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', it, re.S)
    da = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
    print('  ', clean(da.group(1)) if da else '?', '|', clean(ti.group(1))[:90] if ti else '')

print()
print('--- artemis: first 10 date-ish tokens ---')
t = d['artemis']['text']
toks = re.findall(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+2026', t)
print('  ', toks[:10])
toks2 = re.findall(r'2026-\d\d-\d\d', t)
print('  iso:', toks2[:10])

print()
print('--- ibm_asia: first 10 date-ish tokens ---')
t = d['ibm_asia']['text']
print('  ', re.findall(r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s+2026', t)[:10])
print('  iso:', re.findall(r'2026-\d\d-\d\d', t)[:10])

print()
print('--- hkma_press: first 12 date-ish ---')
t = d['hkma_press']['text']
print('  ', re.findall(r'\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+2026', t)[:12])

print()
print('--- scmp: newest date tokens ---')
t = d['scmp_insurance']['text']
print('  ', re.findall(r'\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+2026', t)[:12])

print()
print('--- insurers/nfra newest date tokens ---')
for k in ['prudential_news', 'axa_news', 'sunlife_news', 'nfra']:
    t = d[k]['text']
    toks = re.findall(r'2026[-/年]\d{1,2}[-/月]\d{1,2}', t)[:8]
    toks2 = re.findall(r'\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s*[,]?\s*2026', t)[:8]
    print(f'  {k}:', toks, toks2)
