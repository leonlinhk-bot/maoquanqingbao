import re, urllib.request, urllib.parse, html as htmllib

def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36'})
    return urllib.request.urlopen(req, timeout=30).read().decode('utf-8', 'ignore')

# Google News RSS queries - last 2 days
queries = [
    ('gnews-hk-ins', 'Hong Kong insurance when:2d', 'en'),
    ('gnews-hk-ia', '保监局 when:2d', 'zh'),
    ('gnews-hk-baoxian', '香港保险 when:2d', 'zh'),
    ('gnews-asia-ins', 'Asia insurance industry when:2d', 'en'),
]
for tag, q, lang in queries:
    url = 'https://news.google.com/rss/search?q=' + urllib.parse.quote(q) + '&hl=' + lang + '&gl=HK&ceid=HK:' + lang
    try:
        xml = fetch(url)
        items = re.findall(r'<item>(.*?)</item>', xml, re.S)
        print(f'=== {tag} ({q}): {len(items)} items ===')
        for it in items[:8]:
            t = re.search(r'<title>(.*?)</title>', it, re.S)
            l = re.search(r'<link>(.*?)</link>', it, re.S)
            p = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
            src = re.search(r'<source[^>]*>(.*?)</source>', it, re.S)
            title = htmllib.unescape(t.group(1)).strip() if t else '?'
            link = htmllib.unescape(l.group(1)).strip() if l else '?'
            print(f'  [{p.group(1).strip() if p else "?"}] ({src.group(1) if src else "?"}) {title[:90]}')
            print(f'    {link[:140]}')
    except Exception as e:
        print(tag, 'ERR', e)
