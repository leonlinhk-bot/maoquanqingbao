import re, html
CACHE = '/Users/leonliang/maoquanqingbao/data/_cache1005_1808/'

def txt(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()

for f in ('bing_ia.html', 'ddg_ia.html'):
    print(f'===== {f} =====')
    d = open(CACHE+f, encoding='utf-8', errors='replace').read()
    # bing: <li class="b_algo"><h2><a href="..">title</a>
    for m in re.finditer(r'<h2[^>]*>\s*<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', d, re.S):
        print('  ', txt(m.group(2))[:110])
        print('      ', m.group(1)[:160])
    # ddg
    for m in re.finditer(r'result__a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', d, re.S):
        print('  DDG:', txt(m.group(2))[:110], '|', m.group(1)[:120])
    print()
