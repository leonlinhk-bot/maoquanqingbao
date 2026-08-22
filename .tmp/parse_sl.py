import re, html, os

def strip_tags(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

def extract_links(path, limit=120):
    raw = open(path, encoding='utf-8', errors='ignore').read()
    out = []
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S | re.I):
        url, txt = m.group(1), strip_tags(m.group(2))
        if not txt or len(txt) < 10:
            continue
        if any(skip in url for skip in ['.css', '.js', '.png', '.jpg', '.ico', '.svg', '#', 'javascript', 'mailto']):
            continue
        out.append((txt[:95], url[:140]))
    return out[:limit]

for fn in ['sl-135b.html', 'sl-bbawards.html', 'sl-col2.html', 'sl-finlit2.html', 'sl-hsu2.html', 'sl-mpf2.html', 'sl-pw2.html', 'sl-free-ride.html']:
    p = os.path.join('data/_raw/t0822b', fn)
    print('=' * 22, fn, '=' * 22)
    for t, u in extract_links(p, 12):
        print(f'  {t} | {u}')
