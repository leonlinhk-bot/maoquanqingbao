import json, re, html, os, datetime

C = 'data/_cache1006_0156'
CUT = datetime.datetime(2026, 10, 5, 2, 39, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))

def clean(s):
    s = re.sub(r'<[^>]+>', '', s or '')
    return html.unescape(s).strip()

def show(tag, rows):
    print('=' * 70)
    print(tag, len(rows))
    for r in rows[:20]:
        print('  ', ' | '.join(str(x)[:110] for x in r))

# --- RSS feeds ---
import xml.etree.ElementTree as ET
def rss(name, path, limit=25):
    try:
        t = ET.parse(os.path.join(C, path))
    except Exception as e:
        print('RSS FAIL', name, e); return
    out = []
    for it in t.getroot().iter('item'):
        ti = clean(it.findtext('title') or '')
        li = (it.findtext('link') or '').strip()
        pd = (it.findtext('pubDate') or '').strip()
        de = clean(it.findtext('description') or '')[:90]
        out.append((pd, ti[:95], li[:95]))
    print('=' * 70)
    print('RSS', name, len(out))
    for r in out[:limit]:
        print('  ', r[0], '|', r[1])

rss('insuranceasia', 'insuranceasia.xml')
rss('scmp_insurance', 'scmp_ins.xml')
rss('govhk_zh', 'govhk_zh.xml', 15)
rss('govhk_en', 'govhk_en.xml', 10)

# --- insuranceasianews WP JSON ---
try:
    posts = json.load(open(os.path.join(C, 'ian.json')))
    print('=' * 70); print('IAN posts', len(posts))
    for p in posts[:22]:
        print('  ', p.get('date'), '|', clean(p.get('title', {}).get('rendered', ''))[:100], '|', p.get('link', '')[:90])
except Exception as e:
    print('IAN FAIL', e)

# --- HKMA press: find dated rows ---
h = open(os.path.join(C, 'hkma_press.html'), encoding='utf-8', errors='ignore').read()
links = re.findall(r'href="(/(?:eng|en)/news-and-media/press-releases/[^"]+)"[^>]*>(.*?)</a>', h, re.S)
print('=' * 70); print('HKMA raw links', len(links))
seen = set()
for u, t in links:
    t = clean(t)
    if not t or u in seen:
        continue
    seen.add(u)
    print('  ', t[:110], '|', u[:95])

# --- Artemis ---
a = open(os.path.join(C, 'artemis.html'), encoding='utf-8', errors='ignore').read()
items = re.findall(r'<h[23][^>]*>\s*<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', a, re.S)
print('=' * 70); print('ARTEMIS', len(items))
for u, t in items[:20]:
    print('  ', clean(t)[:110], '|', u[:90])

# --- IBM Asia ---
b = open(os.path.join(C, 'ibm.html'), encoding='utf-8', errors='ignore').read()
items = re.findall(r'href="(/asia/news/[^"]+)"[^>]*>(.*?)</a>', b, re.S)
print('=' * 70); print('IBM', len(items))
seen = set()
for u, t in items:
    t = clean(t)
    if len(t) < 15 or u in seen:
        continue
    seen.add(u)
    print('  ', t[:110], '|', u[:90])
