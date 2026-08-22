import re, html, os

def strip_tags(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

def find_press(path):
    raw = open(path, encoding='utf-8', errors='ignore').read()
    # press release detail links look like: .../press-releases/2026/... or contain date
    out = []
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S | re.I):
        url, txt = m.group(1), strip_tags(m.group(2))
        if not txt or len(txt) < 8:
            continue
        if ('press-releases' in url or '2026' in url) and ('2026' in txt or 'Aug' in txt or '8月' in txt or '2026-08' in url):
            out.append((txt[:110], url[:150]))
    return out

for fn in ['hkma-20260821-3.html', 'hkma-20260820-4.html', 'hkma-press.html']:
    p = os.path.join('data/_raw/t0822b', fn)
    print('=' * 25, fn, '=' * 25)
    for t, u in find_press(p)[:50]:
        print(f'  {t} | {u}')
