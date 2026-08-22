import re, html

raw = open('.tmp/0821/scmp.html', encoding='utf-8', errors='ignore').read()
print('SCMP len', len(raw))
seen = set()
for m in re.finditer(r'<a[^>]+href="(https://www\.scmp\.com/[^"]+)"[^>]*>(.*?)</a>', raw, re.S):
    href = m.group(1)
    txt = html.unescape(re.sub(r'<[^>]+>', '', m.group(2))).strip()
    txt = re.sub(r'\s+', ' ', txt)
    if len(txt) < 25:
        continue
    key = (txt[:50], href[:90])
    if key in seen:
        continue
    seen.add(key)
    ctx = raw[max(0, m.start()-800):m.start()]
    dm = re.findall(r'(20\d{2}-\d{1,2}-\d{1,2})', ctx)
    d = dm[-1] if dm else ''
    print(f'[{d}] {txt[:85]} -> {href[:110]}')
