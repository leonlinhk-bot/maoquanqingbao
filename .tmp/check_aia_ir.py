import re, html

raw = open('/Users/leonliang/maoquanqingbao/.tmp/fetch/aia_ir.html', encoding='utf-8', errors='replace').read()
t = re.search(r'<title[^>]*>(.*?)</title>', raw, re.S)
print('TITLE:', html.unescape(t.group(1)).strip() if t else '?')
# look for links mentioning results/interim/2026
links = re.findall(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S)
print('--- links ---')
for href, txt in links:
    tt = html.unescape(re.sub(r'<[^>]+>', ' ', txt)).strip()
    tt = re.sub(r'\s+', ' ', tt)
    if re.search(r'interim|results|2026|業績|中期', tt, re.I) and len(tt) < 90:
        print('-', tt, '|', href[:100])
