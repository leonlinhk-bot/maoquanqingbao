import re, html, sys, json

def parse_rss(path, n=30):
    raw = open(path, encoding='utf-8', errors='replace').read()
    items = re.findall(r'<item>(.*?)</item>', raw, re.S)
    out = []
    for it in items:
        t = re.search(r'<title>(.*?)</title>', it, re.S)
        d = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
        l = re.search(r'<link>(.*?)</link>', it, re.S)
        s = re.search(r'<source[^>]*url="([^"]+)"[^>]*>(.*?)</source>', it, re.S)
        out.append({
            'title': html.unescape(re.sub(r'<[^>]+>', '', t.group(1))).strip() if t else '',
            'pubDate': d.group(1).strip() if d else '',
            'link': html.unescape(l.group(1)).strip() if l else '',
            'source': html.unescape(s.group(2)).strip() if s else '',
            'sourceUrl': s.group(1) if s else '',
        })
    return out

for p in sys.argv[1:]:
    print('=====', p)
    for it in parse_rss(p)[:30]:
        print('-', it['pubDate'], '|', it['title'][:70], '|', it['source'], '|', it['link'][:70])
