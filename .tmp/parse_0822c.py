import re, html, os

def strip_tags(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

def extract_links(path, limit=100):
    raw = open(path, encoding='utf-8', errors='ignore').read()
    out = []
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S | re.I):
        url, txt = m.group(1), strip_tags(m.group(2))
        if not txt or len(txt) < 8:
            continue
        if any(skip in url for skip in ['.css', '.js', '.png', '.jpg', '.ico', '.svg', '#', 'javascript', 'mailto']):
            continue
        out.append((txt[:100], url[:150]))
    return out[:limit]

for fn in ['hkma-press.html', 'fstb-press.html']:
    p = os.path.join('data/_raw/t0822c', fn)
    print('=' * 25, fn, '=' * 25)
    for t, u in extract_links(p, 45):
        if '/2026/' in u or '2026' in t:
            print(f'  {t} | {u}')
