import re
p = '/Users/leonliang/.hermes/cache/web/www.insurancebusinessmag.com-51110a875f.md'
t = open(p, encoding='utf-8', errors='replace').read()
i = t.find('Manulife')
print(re.sub(r'\n{2,}', '\n', t[2000:4200]))
