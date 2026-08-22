import re, html

def strip_tags(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

for fn in ['ib-aia-broker.html', 'ib-etf-mainland.html', 'ib-pingan.html', 'hkma-pboC-bills.html', 'hkma-scam-banks-0820.html']:
    raw = open('data/_raw/t0822c/' + fn, encoding='utf-8', errors='ignore').read()
    title = re.search(r'<title[^>]*>(.*?)</title>', raw, re.S)
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', raw, re.S)
    meta = re.search(r'<meta[^>]+name="description"[^>]+content="([^"]+)"', raw) or re.search(r'<meta[^>]+property="og:description"[^>]+content="([^"]+)"', raw)
    print('=' * 20, fn)
    print('  TITLE:', strip_tags(title.group(1))[:110] if title else '-')
    print('  H1:', strip_tags(h1.group(1))[:110] if h1 else '-')
    print('  DESC:', strip_tags(meta.group(1))[:220] if meta else '-')
    # publication date if visible
    d = re.search(r'(2026-08-2\dT[\d:]+)', raw)
    print('  DATESTR:', d.group(1) if d else '-')
