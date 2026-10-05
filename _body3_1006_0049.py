import re, html, os
CACHE = '/Users/leonliang/maoquanqingbao/data/_cache1006_0049/'


def cl(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()


for fn in ['p_hkma_bakai.html', 'p_hkma_cargox.html', 'p_govhk_cargox.html']:
    if not os.path.exists(CACHE + fn):
        print('missing', fn); continue
    data = open(CACHE + fn, encoding='utf-8', errors='ignore').read()
    print('#' * 80)
    print('###', fn)
    t = re.search(r'(?is)<title>(.*?)</title>', data)
    print('TITLE:', cl(t.group(1))[:160] if t else '?')
    m = re.search(r'name="date"\s+content="([^"]+)"', data)
    print('DATE:', m.group(1) if m else '?')
    # main content div
    for pat in (r'(?is)<div[^>]+class="[^"]*(?:content|press|news)[^"]*"[^>]*>(.*?)(?:<footer|</main>)',
                r'(?is)<main[^>]*>(.*?)</main>'):
        pass
    body = re.findall(r'(?is)<p[^>]*>(.*?)</p>', data)
    n = 0
    for p in body:
        s = cl(p)
        if len(s) < 45:
            continue
        print('   -', s[:420])
        n += 1
        if n >= 14:
            break
    print()
