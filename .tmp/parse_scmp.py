import re, html, os

def strip_tags(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

def extract_links(path, limit=60):
    raw = open(path, encoding='utf-8', errors='ignore').read()
    out = []
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S | re.I):
        url, txt = m.group(1), strip_tags(m.group(2))
        if not txt or len(txt) < 12:
            continue
        if any(skip in url for skip in ['.css', '.js', '.png', '.jpg', '.ico', '.svg', '#', 'javascript', 'mailto']):
            continue
        out.append((txt[:95], url[:130]))
    return out[:limit]

# SCMP topic page - look for article headlines
p = 'data/_raw/t0822b/scmp.html'
raw = open(p, encoding='utf-8', errors='ignore').read()
print('SCMP size:', len(raw))
# SCMP articles usually in links with /scmp.com/... or relative
for t, u in extract_links(p, 40):
    if 'insurance' in u.lower() or 'insurance' in t.lower() or 'hk' in u.lower():
        print(f'  {t} | {u}')
