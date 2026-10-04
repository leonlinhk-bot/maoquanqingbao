import re, html, sys
def clean(s):
    s = re.sub(r'<[^>]+>', ' ', s); s = html.unescape(s); return re.sub(r'\s+', ' ', s).strip()
for p in ['/tmp/govhk_en.xml', '/tmp/govhk_fin.xml']:
    try:
        t = open(p, encoding='utf-8', errors='ignore').read()
    except Exception as e:
        print(p, 'ERR', e); continue
    print('#' * 70)
    print('###', p, 'items', len(re.findall(r'<item>', t)))
    for it in re.findall(r'<item>(.*?)</item>', t, re.S):
        ti = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', it, re.S)
        da = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
        lk = re.search(r'<link>(.*?)</link>', it, re.S)
        d = clean(da.group(1)) if da else ''
        if any(x in d for x in ['03 Oct 2026', '04 Oct 2026']):
            print(' *', d, '|', clean(ti.group(1))[:120] if ti else '', '|', (lk.group(1).strip() if lk else '')[:90])
