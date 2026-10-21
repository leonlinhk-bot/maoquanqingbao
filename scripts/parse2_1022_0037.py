import xml.etree.ElementTree as ET, datetime, re, email.utils, html
D = '/Users/leonliang/maoquanqingbao/data/_1022_0037'
HKT = datetime.timezone(datetime.timedelta(hours=8))
tree = ET.parse(D + '/iaasia.xml')
for it in tree.getroot().iter('item'):
    pd = it.findtext('pubDate') or ''
    try:
        dt = email.utils.parsedate_to_datetime(pd).astimezone(HKT)
    except Exception:
        dt = None
    print(f"{dt.strftime('%m-%d %H:%M') if dt else '?'} | {it.findtext('title')}")
    print('   ', it.findtext('link'))
    print('   ', re.sub(r'<[^>]+>', ' ', it.findtext('description') or '')[:150].strip())

print('\n\n=== HKMA press releases (page) ===')
txt = open(D + '/hkma.html', encoding='utf-8', errors='ignore').read()
# HKMA list: find links to press release detail pages with dates
links = re.findall(r'href="(/eng/news-and-media/press-releases/20\d{6}/[^"]+)"[^>]*>(.*?)</a>', txt, re.S)
seen = set()
for href, label in links[:40]:
    label = re.sub(r'<[^>]+>', '', label).strip()
    label = html.unescape(re.sub(r'\s+', ' ', label))
    if href in seen:
        continue
    seen.add(href)
    print(f"{href} | {label[:110]}")
print('total links:', len(links))
# also look for date strings near
dates = re.findall(r'(20\d{6})', txt)
print('date tokens sample:', dates[:20])
