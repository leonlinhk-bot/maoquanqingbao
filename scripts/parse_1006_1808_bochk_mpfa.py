import re, html
RAW='/Users/leonliang/maoquanqingbao/data/_raw_1006_1808'
def p(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s))).strip()
print('=== BOCHK press release page ===')
t=open(f'{RAW}/bochk.html',encoding='utf-8',errors='ignore').read()
for m in re.finditer(r'href="([^"]*(?:press|news)[^"]*)"[^>]*>([^<]{4,120})<', t, re.I):
    print('-', p(m.group(2))[:90], '=>', m.group(1)[:100])
print(p(t)[:400])
print('\n=== MPFA sitemap press-release urls ===')
s=open(f'{RAW}/mpfa_sitemap.xml',encoding='utf-8',errors='ignore').read()
urls=re.findall(r'<loc>([^<]+)</loc>', s)
pr=[u for u in urls if 'press-release' in u]
print('total locs', len(urls), 'press-release', len(pr))
for u in pr[:40]:
    print('-', u)
