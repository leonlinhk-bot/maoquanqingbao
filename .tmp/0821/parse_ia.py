import re, html, json

def parse(path, label):
    raw = open(path, encoding='utf-8', errors='ignore').read()
    print(f'== {label} len={len(raw)}')
    out = []
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S):
        href = m.group(1)
        txt = html.unescape(re.sub(r'<[^>]+>', '', m.group(2))).strip()
        if not txt:
            continue
        out.append((txt[:100], href))
    return out

links = parse('.tmp/0821/ia-press.html', 'IA-PRESS')
for t, h in links[:40]:
    print(repr(t), '->', h[:140])

print()
links2 = parse('.tmp/0821/ia-circ.html', 'IA-CIRC')
for t, h in links2[:40]:
    print(repr(t), '->', h[:140])
