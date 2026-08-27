import re, urllib.request, urllib.parse, html as htmllib, json
from datetime import datetime, timezone, timedelta

UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/126.0.0.0 Safari/537.36')

def fetch(url, timeout=30, referer=None):
    hdrs = {
        'User-Agent': UA,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-HK,zh;q=0.9,en;q=0.8',
        'Accept-Encoding': 'identity',
    }
    if referer:
        hdrs['Referer'] = referer
    req = urllib.request.Request(url, headers=hdrs)
    return urllib.request.urlopen(req, timeout=timeout).read().decode('utf-8', 'ignore')

WINDOW = datetime(2026, 8, 25, 10, 18, 0, tzinfo=timezone.utc)  # 2026-08-25T18:18+08:00
HK = timezone(timedelta(hours=8))

print('===== InsuranceAsia RSS: full parse (last 30) =====')
xml = fetch('https://insuranceasia.com/rss.xml')
items = re.findall(r'<item>(.*?)</item>', xml, re.S)
for it in items:
    t = re.search(r'<title>(.*?)</title>', it, re.S)
    l = re.search(r'<link>(.*?)</link>', it, re.S)
    p = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
    d = re.search(r'<description>(.*?)</description>', it, re.S)
    title = htmllib.unescape(t.group(1)).strip() if t else '?'
    link = htmllib.unescape(l.group(1)).strip() if l else '?'
    desc = htmllib.unescape(d.group(1)).strip()[:120] if d else ''
    if p:
        try:
            dt = datetime.strptime(p.group(1).strip(), '%a, %d %b %Y %H:%M:%S %z')
        except Exception:
            dt = None
    else:
        dt = None
    mark = ''
    if dt and dt >= WINDOW:
        mark = ' <<< NEW'
    print(f'[{p.group(1).strip() if p else "?"}] {title[:85]}{mark}')
    print(f'    {link}')

print()
print('===== HKMA page: find link patterns =====')
html = fetch('https://www.hkma.gov.hk/eng/news-and-media/press-releases/')
# find all hrefs with 2026 dates
hrefs = re.findall(r'href="([^"]*press-releases/2026/\d+/\d+/[^"]*)"', html)
print('direct pattern hits:', len(hrefs))
for h in hrefs[:15]:
    print(' ', h)
# maybe entries in JSON or with different structure; show a snippet around 'press-releases/2026'
idx = html.find('press-releases/2026')
if idx > -1:
    print('--- snippet around first hit ---')
    print(html[max(0, idx-400):idx+300])
