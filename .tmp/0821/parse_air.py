import re, html, glob

for f in sorted(glob.glob('.tmp/0821/air-*.html')):
    raw = open(f, encoding='utf-8', errors='ignore').read()
    print(f'===== {f} ({len(raw)} bytes) =====')
    # titles
    for m in re.finditer(r'<h2[^>]*>(.*?)</h2>', raw, re.S)[:0] if False else re.finditer(r'<h2[^>]*>(.*?)</h2>', raw, re.S):
        t = html.unescape(re.sub(r'<[^>]+>', '', m.group(1))).strip()
        if t:
            print('  H2:', t[:100])
    # links with text
    n = 0
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S):
        href = m.group(1)
        txt = html.unescape(re.sub(r'<[^>]+>', '', m.group(2))).strip()
        txt = re.sub(r'\s+', ' ', txt)
        if len(txt) < 20 or 'javascript' in href:
            continue
        print(f'  [{txt[:70]}] -> {href[:100]}')
        n += 1
        if n > 15:
            break
