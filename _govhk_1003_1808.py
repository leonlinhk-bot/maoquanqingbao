import re, html
def strip(t): return html.unescape(re.sub(r'<[^>]+>', '', t or '')).strip()

KW = ['保險', '保险', '理賠', '理赔', '強積金', '强积金', '保監局', '保监局', '年金', '退休', '再保險', '巨災', '風險管理', '家族辦公室', '財經事務及庫務局', '財經事務']

for path, label in [('/tmp/govhk.xml', 'govhk'), ('/tmp/fstb.xml', 'fstb')]:
    raw = open(path, encoding='utf-8', errors='replace').read()
    items = re.findall(r'<item>(.*?)</item>', raw, re.S)
    print(f'===== {label}: {len(items)} items =====')
    if not items:
        print(raw[:400])
    for it in items[:400]:
        t = re.search(r'<title[^>]*>(.*?)</title>', it, re.S)
        l = re.search(r'<link>(.*?)</link>', it, re.S)
        d = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
        title = strip(t.group(1)) if t else '?'
        desc = strip(re.search(r'<description>(.*?)</description>', it, re.S).group(1)) if '<description>' in it else ''
        blob = title + ' ' + desc
        if any(k in blob for k in KW):
            print('  ', strip(d.group(1)) if d else '?', '|', title[:100])
            print('     ', strip(l.group(1)) if l else '?')
