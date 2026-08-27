import re, urllib.request, urllib.parse, html as htmllib, json

UA = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36'}

def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers=UA)
    return urllib.request.urlopen(req, timeout=timeout).read().decode('utf-8', 'ignore')

def show_rss_items(xml, limit=10):
    items = re.findall(r'<item>(.*?)</item>', xml, re.S)
    print(f'  [{len(items)} items total]')
    for it in items[:limit]:
        t = re.search(r'<title>(.*?)</title>', it, re.S)
        l = re.search(r'<link>(.*?)</link>', it, re.S)
        p = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
        src = re.search(r'<source[^>]*>(.*?)</source>', it, re.S)
        title = htmllib.unescape(t.group(1)).strip() if t else '?'
        link = htmllib.unescape(l.group(1)).strip() if l else '?'
        print(f'  [{p.group(1).strip() if p else "?"}] ({src.group(1) if src else "?"}) {title[:100]}')
        print(f'    {link[:160]}')

print('===== 1. InsuranceAsia RSS =====')
try:
    xml = fetch('https://insuranceasia.com/insurance/rss.xml')
    show_rss_items(xml, 10)
except Exception as e:
    print('ERR', e)

print()
print('===== 2. Google News RSS queries =====')
queries = [
    ('gnews-hk-ins', 'Hong Kong insurance when:1d', 'en'),
    ('gnews-hk-ia', '保监局 when:1d', 'zh'),
    ('gnews-hk-baoxian', '香港保险 when:1d', 'zh'),
    ('gnews-asia-ins', 'Asia insurance industry when:1d', 'en'),
    ('gnews-hk-family-office', '香港 家族办公室 when:1d', 'zh'),
]
for tag, q, lang in queries:
    url = 'https://news.google.com/rss/search?q=' + urllib.parse.quote(q) + '&hl=' + lang + '&gl=HK&ceid=HK:' + lang
    print(f'=== {tag} ({q}) ===')
    try:
        xml = fetch(url)
        show_rss_items(xml, 8)
    except Exception as e:
        print(tag, 'ERR', e)

print()
print('===== 3. IA press releases page =====')
try:
    html = fetch('https://www.ia.org.hk/en/infocenter/press_releases.html')
    # find dated entries
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>([^<]{15,120})</a>', html):
        href, txt = m.group(1), htmllib.unescape(m.group(2)).strip()
        if 'press' in href or '2026' in href:
            print(' ', txt[:90], '->', href[:130])
except Exception as e:
    print('ERR', e)

print()
print('===== 4. IA circulars 2026 page =====')
try:
    html = fetch('https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html')
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>([^<]{15,120})</a>', html):
        href, txt = m.group(1), htmllib.unescape(m.group(2)).strip()
        print(' ', txt[:90], '->', href[:130])
except Exception as e:
    print('ERR', e)
