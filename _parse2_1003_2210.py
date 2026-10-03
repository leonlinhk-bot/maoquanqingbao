import json, re, datetime, xml.etree.ElementTree as ET

raw = json.load(open('data/_raw_1003_2210.json'))
NOW = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
CUT = NOW - datetime.timedelta(hours=30)
print('NOW', NOW.isoformat(), 'CUT', CUT.isoformat())

# 1) insuranceasia RSS
txt = raw['insuranceasia_rss']['text']
root = ET.fromstring(txt)
print('\n=== insuranceasia_rss ===')
for it in root.iter('item'):
    title = (it.findtext('title') or '').strip()
    link = (it.findtext('link') or '').strip()
    pub = (it.findtext('pubDate') or '').strip()
    try:
        dt = datetime.datetime.strptime(pub, '%a, %d %b %Y %H:%M:%S %z')
        ds = dt.astimezone(datetime.timezone(datetime.timedelta(hours=8))).isoformat()
    except Exception:
        ds = pub
    print(f'  {ds} | {title[:110]}')
    print(f'      {link}')

# 2) insuranceasianews WP API
posts = json.loads(raw['insuranceasianews_api']['text'])
print('\n=== insuranceasianews_api ===')
for p in posts:
    t = p['title']['rendered']
    print(f"  {p.get('date')} | {t[:110]}")
    print(f"      {p.get('link')}")

# 3) artemis actual news posts
txt = raw['artemis']['text']
urls = re.findall(r'href="(https://www\.artemis\.bm/news/[a-z0-9\-]{15,}/)"', txt)
seen = []; 
for u in urls:
    if u not in seen and '/news/topic/' not in u and u.rstrip('/').split('/')[-1] not in ('news',):
        seen.append(u)
print(f'\n=== artemis posts ({len(seen)}) ===')
for u in seen[:25]:
    print('  ', u)

# 4) hkma full list
txt = raw['hkma_press']['text']
rows = re.findall(r'(\d{1,2}\s+\w+\s+20\d\d)(.{0,400}?)href="(/eng/news-and-media/press-releases/2026/\d\d/[^"]+)"[^>]*>([^<]{5,160})<', txt, re.S)
print(f'\n=== hkma rows ({len(rows)}) ===')
for d, _, u, t in rows[:30]:
    print(f'  {d} | {t.strip()[:100]} | {u}')

# 5) govhk zh rss
txt = raw['govhk_zh']['text']
root = ET.fromstring(txt)
print('\n=== govhk_zh ===')
for it in list(root.iter('item'))[:40]:
    title = (it.findtext('title') or '').strip()
    link = (it.findtext('link') or '').strip()
    pub = (it.findtext('pubDate') or '').strip()
    print(f'  {pub} | {title[:100]}')

# 6) nfra
txt = raw['nfra']['text']
print('\n=== nfra head ===')
for m in re.findall(r'<a[^>]*href="([^"]+)"[^>]*>([^<]{8,80})</a>', txt)[:40]:
    print('  ', m[1].strip()[:80], '|', m[0])
