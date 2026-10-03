import json, re, datetime, xml.etree.ElementTree as ET

raw = json.load(open('data/_raw_1003_2210.json'))
NOW = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
CUT = NOW - datetime.timedelta(hours=30)  # 2026-10-02 ~16:00 onwards
print('NOW', NOW.isoformat(), 'CUT', CUT.isoformat())

def show(tag, items):
    print(f'\n=== {tag} ({len(items)}) ===')
    for t, d in items[:30]:
        print(f'  {d} | {t[:110]}')

# 1) insuranceasia RSS
try:
    txt = raw['insuranceasia_rss']['text']
    root = ET.fromstring(txt)
    items = []
    for it in root.iter('item'):
        title = (it.findtext('title') or '').strip()
        link = (it.findtext('link') or '').strip()
        pub = (it.findtext('pubDate') or '').strip()
        desc = (it.findtext('description') or '').strip()
        try:
            dt = datetime.datetime.strptime(pub, '%a, %d %b %Y %H:%M:%S %z')
        except Exception:
            dt = None
        items.append((title, dt.isoformat() if dt else pub, link, desc[:200]))
    show('insuranceasia_rss', items)
except Exception as e:
    print('insuranceasia_rss ERR', e)

# 2) insuranceasianews WP API
try:
    posts = json.loads(raw['insuranceasianews_api']['text'])
    items = []
    for p in posts:
        items.append((p['title']['rendered'], p.get('date'), p.get('link'), re.sub('<[^>]+>','',p.get('excerpt',{}).get('rendered',''))[:180]))
    show('insuranceasianews_api', items)
except Exception as e:
    print('ian ERR', e)

# 3) artemis
try:
    txt = raw['artemis']['text']
    urls = re.findall(r'href="(https://www\.artemis\.bm/news/[^"]+)"[^>]*>([^<]{10,140})<', txt)
    seen = set(); out = []
    for u, t in urls:
        if u in seen: continue
        seen.add(u); out.append((t.strip(), u))
    print(f'\n=== artemis links ({len(out)}) ===')
    for t, u in out[:30]:
        print('  ', t[:110], '|', u)
except Exception as e:
    print('artemis ERR', e)

# 4) hkma press
try:
    txt = raw['hkma_press']['text']
    # look for press release links + dates
    rows = re.findall(r'(\d{1,2}\s+\w+\s+20\d\d)[^<]*</[^>]+>\s*<[^>]*>?\s*<a[^>]*href="([^"]+)"[^>]*>([^<]{10,160})<', txt, re.S)
    print(f'\n=== hkma rows ({len(rows)}) ===')
    for d, u, t in rows[:25]:
        print('  ', d, '|', t.strip()[:100], '|', u)
except Exception as e:
    print('hkma ERR', e)
