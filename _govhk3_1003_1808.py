import re, html
raw = open('/tmp/govhk.xml', encoding='utf-8', errors='replace').read()
items = re.findall(r'<item>(.*?)</item>', raw, re.S)
targets = ['2026100200677', '2026100200518', '2026100200194', '2026100100509', '2026093000360', '2026093000271', '2026092900625']
def cdata_title(it):
    m = re.search(r'<title><!\[CDATA\[(.*?)\]\]></title>', it, re.S)
    if m:
        return m.group(1).strip()
    m = re.search(r'<title>(.*?)</title>', it, re.S)
    return html.unescape(m.group(1)).strip() if m else ''
for it in items:
    l = re.search(r'<link>(.*?)</link>', it, re.S)
    d = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
    link = l.group(1).strip() if l else ''
    if any(x in link for x in targets):
        print((d.group(1).strip() if d else '?'), '|', cdata_title(it)[:170])
        print('   ', link)
