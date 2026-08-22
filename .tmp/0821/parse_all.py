import re, html, os

def extract(path, label, date_hint=None):
    raw = open(path, encoding='utf-8', errors='ignore').read()
    print(f'===== {label} ({len(raw)} bytes) =====')
    if 'Just a moment' in raw[:500] or 'cf-challenge' in raw[:2000]:
        print('  [Cloudflare challenge]')
        return
    seen = set()
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S):
        href = m.group(1)
        txt = html.unescape(re.sub(r'<[^>]+>', '', m.group(2))).strip()
        txt = re.sub(r'\s+', ' ', txt)
        if len(txt) < 15:
            continue
        key = (txt[:50], href[:100])
        if key in seen:
            continue
        seen.add(key)
        # date patterns nearby
        ctx = raw[max(0, m.start()-600):m.end()+200]
        dates = re.findall(r'(20\d{2}[/\-.]\d{1,2}[/\-.]\d{1,2})', ctx)
        datestr = dates[-1] if dates else ''
        print(f'  [{datestr}] {txt[:95]} -> {href[:130]}')

for f, label in [('aia','AIA'), ('prudential','PRUDENTIAL'), ('axa','AXA'),
                 ('sunlife','SUNLIFE'), ('ibmag','IB-MAG'), ('iaasia_home','IAASIA-HOME'),
                 ('manulife','MANULIFE')]:
    extract(f'.tmp/0821/{f}.html', label)
