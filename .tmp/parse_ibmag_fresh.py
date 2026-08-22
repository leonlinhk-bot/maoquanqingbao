import re, html

def strip_tags(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

def parse_atom(path):
    raw = open(path, encoding='utf-8', errors='ignore').read()
    entries = re.findall(r'<entry>(.*?)</entry>', raw, re.S)
    out = []
    for it in entries:
        t = re.search(r'<title[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', it, re.S)
        l = re.search(r'<link[^>]*href="([^"]+)"', it, re.S)
        d = re.search(r'<updated>(.*?)</updated>', it, re.S)
        out.append((strip_tags(t.group(1)) if t else '', l.group(1) if l else '', d.group(1) if d else ''))
    return out

for t, u, d in parse_atom('data/_raw/t0822c/ibmag.xml'):
    print(f'{d[:19]} | {t[:80]} | {u}')
