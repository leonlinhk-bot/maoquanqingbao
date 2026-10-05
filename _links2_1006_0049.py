import re, html, os
CACHE = '/Users/leonliang/maoquanqingbao/data/_cache1006_0049/'


def cl(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()


# ---- Artemis: article blocks with date ----
data = open(CACHE + 'artemis.html', encoding='utf-8', errors='ignore').read()
print('##### ARTEMIS (date | title | url) #####')
for m in re.finditer(r'<div class="col-sm-9 col-8">(.*?)</article>', data, re.S):
    blk = m.group(1)
    h = re.search(r'<h2><a href="([^"]+)"[^>]*>(.*?)</a></h2>', blk, re.S)
    d = re.search(r'card-subtitle">(.*?)</span>', blk, re.S)
    if h:
        print(' ', (cl(d.group(1)) if d else '?'), '|', cl(h.group(2))[:95])

# ---- Sun Life dates ----
data = open(CACHE + 'sunlife.html', encoding='utf-8', errors='ignore').read()
print('\n##### SUNLIFE #####')
for m in re.finditer(r'<a[^>]+href="(/zh-hant/about-us/newsroom/news-releases/[^"]+)"[^>]*>(.*?)</a>(.{0,300})', data, re.S):
    u, t, tail = m.group(1), cl(m.group(2)), cl(m.group(3))
    if len(t) < 15:
        continue
    dm = re.search(r'(20\d\d)[年\-/](\d{1,2})[月\-/](\d{1,2})', tail)
    print(' ', (dm.group(0) if dm else '?'), '|', t[:85], '|', u[:95])

# ---- Prudential: look for any zh article links ----
data = open(CACHE + 'prudential.html', encoding='utf-8', errors='ignore').read()
print('\n##### PRUDENTIAL entries #####')
urls = set(re.findall(r'href="([^"]*(?:newsroom|news|press)[^"]*)"', data))
for u in sorted(urls)[:30]:
    print('  ', u)

# ---- AXA ----
data = open(CACHE + 'axa.html', encoding='utf-8', errors='ignore').read()
print('\n##### AXA entries #####')
for u, t in set((m.group(1), cl(m.group(2))) for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', data, re.S)):
    if re.search(r'(news|press)/', u) and len(t) > 10:
        print('  ', t[:80], '|', u[:100])
