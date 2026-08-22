import re, html, json, os

def strip_tags(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

def extract_links(path):
    try:
        raw = open(path, encoding='utf-8', errors='ignore').read()
    except Exception as e:
        return [('ERR', str(e), '')]
    # find link blocks: <a href="...">text</a>
    out = []
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S | re.I):
        url, txt = m.group(1), strip_tags(m.group(2))
        if not txt:
            continue
        if any(skip in url for skip in ['.css', '.js', '.png', '.jpg', '.ico', '.svg', '#', 'javascript']):
            continue
        out.append((txt[:90], url))
    return out

for fn in ['ia-circ2026.html', 'ia-insurtech.html', 'fstb.html', 'wb-nfra.html', 'wb-fstb-press.html', 'wb-ia-circ.html', 'wb-ia-press2.html', 'ia-press-list.html']:
    p = os.path.join('data/_raw/t0822b', fn)
    print('=' * 20, fn, '=' * 20)
    links = extract_links(p)
    for t, u in links[:60]:
        print(f'  {t} | {u[:110]}')
