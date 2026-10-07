import json, re, html
p = '/Users/leonliang/maoquanqingbao/data/_raw_1007_1808/ian.json'
j = json.load(open(p, encoding='utf-8'))
print('--- ian.json items (date / date_gmt / title) ---')
for it in j:
    print(it.get('date'), '|', it.get('date_gmt'), '|', html.unescape(re.sub('<[^>]+>', '', it['title']['rendered']))[:90])
print()
print('--- sidebar links in art_india.html ---')
t = open('/Users/leonliang/maoquanqingbao/data/_raw_1007_1808/art_india.html', encoding='utf-8', errors='ignore').read()
seen = set()
for m in re.finditer(r'href="(https://insuranceasianews\.com/[^"]+)"[^>]*>([^<]{15,140})</a>', t):
    u, ti = m.group(1), html.unescape(m.group(2)).strip()
    if u in seen: continue
    seen.add(u)
    print(' -', ti[:105], '||', u)
