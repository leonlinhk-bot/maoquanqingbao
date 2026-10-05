import re, html, os
CACHE = '/Users/leonliang/maoquanqingbao/data/_cache1006_0049/'
files = ['a_dc.html', 'a_unimed.html', 'a_aero.html', 'a_drought.html', 'a_cyber.html',
         'a_picc.html', 'a_ucits.html', 'a_eaton.html', 'a_arc.html', 'ian_marsh.html']


def cl(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()


for fn in files:
    data = open(CACHE + fn, encoding='utf-8', errors='ignore').read()
    print('#' * 80)
    print('###', fn)
    for pat in (r'<meta[^>]+property="og:description"[^>]+content="([^"]{30,600})"',
                r'<meta[^>]+name="description"[^>]+content="([^"]{30,600})"',
                r'"datePublished"\s*:\s*"([^"]+)"'):
        m = re.search(pat, data)
        if m:
            print('  META:', cl(m.group(1))[:400])
    t = re.search(r'(?is)<title>(.*?)</title>', data)
    print('  TITLE:', cl(t.group(1))[:180] if t else '?')
    # article paragraphs
    body = re.findall(r'(?is)<p[^>]*>(.*?)</p>', data)
    shown = 0
    for p in body:
        s = cl(p)
        if len(s) < 70 or 'cookie' in s.lower() or 'subscribe' in s.lower():
            continue
        print('   -', s[:330])
        shown += 1
        if shown >= 10:
            break
    print()
