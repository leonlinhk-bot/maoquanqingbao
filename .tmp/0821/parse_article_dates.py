import re, html, glob, json

def get_date(raw):
    # try meta tags
    for p in [r'property="article:published_time"\s+content="([^"]+)"',
              r'name="article:published_time"\s+content="([^"]+)"',
              r'"datePublished"\s*:\s*"([^"]+)"',
              r'property="og:published_time"\s+content="([^"]+)"',
              r'"dateModified"\s*:\s*"([^"]+)"']:
        m = re.search(p, raw)
        if m:
            return m.group(1)
    # ISO date in JSON-LD
    m = re.search(r'"datePublished"\s*:\s*"([^"]+)"', raw)
    if m:
        return m.group(1)
    # fallback: date string patterns
    for p in [r'(20\d{2}-\d{1,2}-\d{1,2}T\d{2}:\d{2}[^"]*)',
              r'(\d{1,2}\s+[A-Z][a-z]{2,8}\s+20\d{2})']:
        m = re.search(p, raw)
        if m:
            return m.group(1)
    return ''

def get_title(raw):
    m = re.search(r'<title>(.*?)</title>', raw, re.S)
    if m:
        return html.unescape(m.group(1)).strip()[:120]
    return ''

for f in sorted(glob.glob('.tmp/0821/iaa_*.html')) + sorted(glob.glob('.tmp/0821/ib_*.html')):
    raw = open(f, encoding='utf-8', errors='ignore').read()
    d = get_date(raw)
    t = get_title(raw)
    print(f"{f.split('/')[-1]:28s} | {d:32s} | {t[:90]}")
