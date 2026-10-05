import re, html, os
CACHE = '/Users/leonliang/maoquanqingbao/data/_cache1006_0049/'


def cl(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()


def links(fn, pat, base=''):
    data = open(CACHE + fn, encoding='utf-8', errors='ignore').read()
    out = []
    seen = set()
    for m in re.finditer(r'<a\b[^>]*href="([^"]+)"[^>]*>(.*?)</a>', data, re.S):
        u, t = m.group(1), cl(m.group(2))
        if not re.search(pat, u):
            continue
        if u in seen or len(t) < 12:
            continue
        seen.add(u)
        out.append((base + u, t))
    return out


print('##### IBM #####')
for u, t in links('ibm.html', r'/asia/news/[a-z0-9\-]+/?$')[:25]:
    print('  ', t[:90], '|', u)
print('\n##### ARTEMIS (article) #####')
for u, t in links('artemis.html', r'artemis\.bm/news/[a-z0-9\-]+/')[0:]:
    print('  ', t[:90], '|', u)
print('\n##### AIA #####')
for u, t in links('aia.html', r'(press-release|media-centre|news)')[:20]:
    print('  ', t[:90], '|', u)
print('\n##### PRUDENTIAL #####')
for u, t in links('prudential.html', r'newsroom|press|news')[:20]:
    print('  ', t[:90], '|', u)
print('\n##### AXA #####')
for u, t in links('axa.html', r'news-room|news|press')[:20]:
    print('  ', t[:90], '|', u)
print('\n##### SUNLIFE #####')
for u, t in links('sunlife.html', r'news|press')[:20]:
    print('  ', t[:90], '|', u)
print('\n##### NFRA #####')
for u, t in links('nfra.html', r'')[:40]:
    print('  ', t[:80], '|', u)
