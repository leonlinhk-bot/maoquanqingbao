import re, html, os

def strip_tags(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

def parse_rss(path):
    raw = open(path, encoding='utf-8', errors='ignore').read()
    items = re.findall(r'<item>(.*?)</item>', raw, re.S)
    out = []
    for it in items:
        t = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', it, re.S)
        l = re.search(r'<link>(.*?)</link>', it, re.S)
        d = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
        out.append((strip_tags(t.group(1)) if t else '', l.group(1) if l else '', d.group(1) if d else ''))
    return out

for fn in ['ibmag-rss.xml', 'ibmag-rss2.html', 'ibmag-rss3.html']:
    p = os.path.join('data/_raw/t0822b', fn)
    print('=' * 25, fn, '=' * 25)
    try:
        for t, u, d in parse_rss(p)[:25]:
            print(f'  {d[:30]} | {t[:80]} | {u[:100]}')
    except Exception as e:
        print('  parse err', e)
