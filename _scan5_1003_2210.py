import json, re, html
raw = json.load(open('data/_raw_1003_2210.json'))
def clean(s):
    return html.unescape(re.sub('<[^>]+>', '', s)).strip()

print('##### ARTEMIS: date-tagged posts #####')
txt = raw['artemis']['text']
# find blocks: <a href=".../news/slug/"><h2/h3>title</h2></a> ... date
for m in re.finditer(r'href="(https://www\.artemis\.bm/news/([a-z0-9\-]{2,})/)"[^>]*>\s*(?:<[^>]+>\s*)*([^<]{15,200})', txt):
    pass
# simpler: find all date strings and nearby titles
for m in re.finditer(r'(\d{1,2}(?:st|nd|rd|th)?\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+20\d\d)', txt):
    s = max(0, m.start()-700)
    ctx = clean(txt[s:m.end()])
    print(f'  [{m.group(1)}] ...{ctx[-160:]}')

print('\n##### IBM ASIA: article slugs + dates #####')
t2 = raw['ibm_asia']['text']
slugs = re.findall(r'href="(/asia/news/[a-z0-9\-/]+-(\d{6})\.aspx)"', t2)
seen = []
for u, n in slugs:
    if u not in [x[0] for x in seen]:
        seen.append((u, n))
for u, n in seen[:40]:
    print('  ', n, '|', u)
print('\n##### IBM ASIA: date strings #####')
for m in re.finditer(r'(\w{3}\s+\d{1,2},\s+20\d\d)', t2):
    print('  ', m.group(1), '|', clean(t2[max(0,m.start()-120):m.start()])[-90:])
