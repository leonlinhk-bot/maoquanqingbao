import re
p = '/Users/leonliang/.hermes/cache/web/www.insurancebusinessmag.com-51110a875f.md'
t = open(p, encoding='utf-8', errors='replace').read()
for kw in ['promotes', 'Finch', 'appointed', 'chief technology', 'Chief']:
    for m in re.finditer(kw, t):
        s = re.sub(r'\s+', ' ', t[max(0, m.start() - 400):m.start() + 500])
        print('##', kw, ':', s[:700])
        print('---')
        break
