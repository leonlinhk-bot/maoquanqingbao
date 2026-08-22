import re, html

def near_dates(raw, pos, span=1500):
    ctx = raw[max(0, pos-span):pos+200]
    pats = [
        r'(20\d{2}-\d{1,2}-\d{1,2})',
        r'(20\d{2}/\d{1,2}/\d{1,2})',
        r'(20\d{2}\.\d{1,2}\.\d{1,2})',
        r'([A-Z][a-z]{2,8}\s+\d{1,2},?\s+20\d{2})',
        r'(\d{1,2}\s+[A-Z][a-z]{2,8}\s+20\d{2})',
    ]
    found = []
    for p in pats:
        found += re.findall(p, ctx)
    return found[-1] if found else ''

# IAASIA home: find article links + dates
raw = open('.tmp/0821/iaasia_home.html', encoding='utf-8', errors='ignore').read()
print('===== IAASIA dates =====')
for m in re.finditer(r'<a[^>]+href="(https://insuranceasia\.com/insurance/[^"]+)"[^>]*>(.*?)</a>', raw, re.S):
    href = m.group(1)
    txt = html.unescape(re.sub(r'<[^>]+>', '', m.group(2))).strip()
    txt = re.sub(r'\s+', ' ', txt)
    if len(txt) < 15 or 'news' not in href:
        continue
    d = near_dates(raw, m.start())
    print(f'[{d}] {txt[:80]} -> {href[:110]}')
