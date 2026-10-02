import re, html
def strip(t): return html.unescape(re.sub(r'<[^>]+>', '', t or '')).strip()
raw = open('/tmp/govhk.xml', encoding='utf-8', errors='replace').read()
items = re.findall(r'<item>(.*?)</item>', raw, re.S)
targets = ['P2026100200677', 'P2026100200518', 'P2026100200194', 'P2026100100509', 'P2026093000360', 'P2026093000271', 'P2026092900625']
for it in items:
    t = re.search(r'<title>(.*?)</title>', it, re.S)
    l = re.search(r'<link>(.*?)</link>', it, re.S)
    d = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
    title = strip(t.group(1)) if t else ''
    link = strip(l.group(1)) if l else ''
    if any(x in link for x in targets):
        print(strip(d.group(1)) if d else '?', '|', title[:160])
        print('   ', link)
