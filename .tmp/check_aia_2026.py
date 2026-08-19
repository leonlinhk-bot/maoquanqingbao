import re, html

raw = open('/Users/leonliang/maoquanqingbao/.tmp/fetch/aia_results.html', encoding='utf-8', errors='replace').read()
print("--- all 2026-related links ---")
seen = set()
for m in re.finditer(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S):
    tt = html.unescape(re.sub(r'<[^>]+>', ' ', m.group(2))).strip()
    tt = re.sub(r'\s+', ' ', tt)
    href = m.group(1)
    if ('2026' in tt or '2026' in href) and tt and href not in seen and len(tt) < 110:
        seen.add(href)
        print('-', tt, '|', href[:100])
print("--- 'results' heading text ---")
for m in re.finditer(r'(?:H1|Interim|Annual)[^<]{0,40}2026[^<]{0,60}', raw):
    print('*', html.unescape(m.group(0))[:90])
