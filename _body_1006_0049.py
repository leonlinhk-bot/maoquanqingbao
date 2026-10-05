import re, html, os, sys
CACHE = '/Users/leonliang/maoquanqingbao/data/_cache1006_0049/'
files = ['p_ibm_howden.html', 'p_ibm_mas_who.html', 'p_ibm_lifesci.html', 'p_hkma_bakai.html',
         'p_sunlife_cuhk.html', 'p_fstb_tax.html']


def txt(h):
    h = re.sub(r'(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>', ' ', h)
    h = re.sub(r'(?is)<br\s*/?>|</p>|</div>|</li>|</h[1-6]>', '\n', h)
    h = re.sub(r'<[^>]+>', ' ', h)
    h = html.unescape(h)
    lines = [re.sub(r'\s+', ' ', x).strip() for x in h.split('\n')]
    return [x for x in lines if len(x) > 25]


for fn in files:
    data = open(CACHE + fn, encoding='utf-8', errors='ignore').read()
    print('#' * 90)
    print('###', fn)
    t = re.search(r'(?is)<title>(.*?)</title>', data)
    print('TITLE:', html.unescape(re.sub(r'\s+', ' ', t.group(1)).strip()) if t else '?')
    for pat in (r'"datePublished"\s*:\s*"([^"]+)"', r'property="article:published_time" content="([^"]+)"',
                r'name="date"\s+content="([^"]+)"', r'(?:Published|Updated)[^0-9]{0,20}(\d{1,2}\s+\w+\s+20\d\d)', r'(20\d\d-\d\d-\d\d)'):
        m = re.search(pat, data)
        if m:
            print('DATE?', pat[:35], '->', m.group(1))
    body = txt(data)
    # skip nav junk: print from longest run
    shown = 0
    for line in body:
        if len(line) < 40:
            continue
        print('   ', line[:400])
        shown += 1
        if shown >= 22:
            break
    print()
