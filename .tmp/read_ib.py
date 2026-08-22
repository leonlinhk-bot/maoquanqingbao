import re, html

def strip_tags(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

def main_text(path, maxlen=1800):
    raw = open(path, encoding='utf-8', errors='ignore').read()
    # try article body containers
    m = re.search(r'<div[^>]*class="[^"]*(article-body|article__body|story-body|entry-content|body-content|article-content)[^"]*"[^>]*>(.*?)</div>\s*(?:<div|<footer|</article)', raw, re.S | re.I)
    if not m:
        m = re.search(r'<article[^>]*>(.*?)</article>', raw, re.S | re.I)
    seg = m.group(1) if m else raw
    txt = strip_tags(seg)
    # collapse repeated
    return txt[:maxlen]

for fn in ['ib-aia-broker.html', 'ib-etf-mainland.html', 'ib-pingan.html']:
    print('=' * 25, fn)
    print(main_text('data/_raw/t0822c/' + fn))
    print()
