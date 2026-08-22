import re, html, os

def strip_tags(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

for fn in ['sl-135b.html', 'sl-bbawards.html', 'sl-col2.html', 'sl-finlit2.html', 'sl-hsu2.html', 'sl-mpf2.html', 'sl-pw2.html', 'sl-free-ride.html']:
    p = os.path.join('data/_raw/t0822b', fn)
    raw = open(p, encoding='utf-8', errors='ignore').read()
    og = re.search(r'<meta[^>]+property="og:title"[^>]+content="([^"]+)"', raw) or re.search(r'<meta[^>]+content="([^"]+)"[^>]+property="og:title"', raw)
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', raw, re.S)
    dts = re.findall(r'(20\d\d[-/年]\s?\d{1,2}[-/月]\s?\d{1,2}[日号]?|2026[-/]\d{2}[-/]\d{2})', raw)
    print(fn, '| og:', og.group(1)[:90] if og else '-', '| h1:', strip_tags(h1.group(1))[:90] if h1 else '-', '| dates:', dts[:6])
