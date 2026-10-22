import re, html
p = '/Users/leonliang/maoquanqingbao/.cache1023_0023/bodies/rn_iceye.html'
raw = open(p, encoding='utf-8', errors='ignore').read()
t = re.sub(r'(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>', ' ', raw)
t = re.sub(r'<[^>]+>', '\n', t)
t = html.unescape(t)
ls = [re.sub(r'\s+', ' ', l).strip() for l in t.split('\n')]
ls = [l for l in ls if len(l) > 50]
for l in ls[:14]:
    print('-', l[:420])
