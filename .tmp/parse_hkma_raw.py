import re, html, os

def strip_tags(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

def extract_links(path, limit=80):
    raw = open(path, encoding='utf-8', errors='ignore').read()
    out = []
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S | re.I):
        url, txt = m.group(1), strip_tags(m.group(2))
        if not txt or len(txt) < 6:
            continue
        if any(skip in url for skip in ['.css', '.js', '.png', '.jpg', '.ico', '.svg', '#', 'javascript', 'mailto']):
            continue
        out.append((txt[:100], url[:130]))
    return out[:limit]

for fn in ['hkma-20260821-3.html', 'hkma-20260820-4.html']:
    p = os.path.join('data/_raw/t0822b', fn)
    print('=' * 25, fn, '=' * 25)
    for t, u in extract_links(p, 40):
        print(f'  {t} | {u}')
