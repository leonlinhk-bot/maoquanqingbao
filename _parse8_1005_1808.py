import re, html, os
CACHE = '/Users/leonliang/maoquanqingbao/data/_cache1005_1808/'

def txt(s):
    s = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', s, flags=re.S | re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()

FILES = {
    'a_art_ucits': 'artemis',
    'a_art_eaton': 'artemis',
    'a_art_marshre': 'artemis',
    'a_ibm_lifesci': 'ibm',
    'a_ian_koreanre': 'ian',
    'a_iaasia_dc': 'insuranceasia',
}
for f, kind in FILES.items():
    p = CACHE + f
    if not os.path.exists(p):
        print(f, 'MISSING'); continue
    d = open(p, encoding='utf-8', errors='replace').read()
    print('=' * 20, f, f'({len(d)}b)')
    # dates
    for pat in (r'"datePublished"\s*:\s*"([^"]+)"', r'property="article:published_time"\s+content="([^"]+)"',
                r'<time[^>]*datetime="([^"]+)"', r'content="(\d{4}-\d{2}-\d{2}T[^"]+)"'):
        m = re.search(pat, d)
        if m:
            print('  DATE:', m.group(1)); break
    for pat in (r'<title>(.*?)</title>', r'"headline"\s*:\s*"([^"]+)"'):
        m = re.search(pat, d, re.S)
        if m:
            print('  TITLE:', txt(m.group(1))[:160]); break
    body = re.search(r'<article[^>]*>(.*?)</article>', d, re.S) or re.search(r'<body[^>]*>(.*?)</body>', d, re.S)
    tx = txt(body.group(1) if body else d)
    # skip nav-ish
    print('  BODY:', tx[:1300])
    print()
