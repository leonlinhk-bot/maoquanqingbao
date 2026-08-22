import re, html, os

def strip_tags(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

def find_dated_links(path, limit=60):
    raw = open(path, encoding='utf-8', errors='ignore').read()
    out = []
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S | re.I):
        url, txt = m.group(1), strip_tags(m.group(2))
        if not txt or len(txt) < 12:
            continue
        if any(skip in url for skip in ['.css', '.js', '.png', '.jpg', '.ico', '.svg', '#', 'javascript', 'mailto']):
            continue
        out.append((txt[:100], url[:150]))
    return out[:limit]

for fn in ['aia.html', 'axa.html', 'prudential.html', 'sunlife.html']:
    p = os.path.join('data/_raw/t0822b', fn)
    print('=' * 22, fn, '=' * 22)
    for t, u in find_dated_links(p, 30):
        print(f'  {t} | {u}')
