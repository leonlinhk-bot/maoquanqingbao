import xml.etree.ElementTree as ET, re, html, json
t = ET.parse('/tmp/scmp92.xml')
for it in t.getroot().iter('item'):
    ti = it.findtext('title') or ''
    if 'Ping An move' in ti:
        d = html.unescape(re.sub('<[^>]+>', '', it.findtext('description') or ''))
        print('TITLE:', ti)
        print('DATE :', it.findtext('pubDate'))
        print('LINK :', it.findtext('link'))
        print('DESC :', d[:1200])

d = json.load(open('data/live-items.json'))
print('\n--- DB matches for pingan/ai-rules/gba-travel ---')
for it in d['items']:
    blob = json.dumps(it, ensure_ascii=False)
    for k in ['Ping An', '平保', '平安', 'GBA travel', '來港安居寶', '来港安居宝']:
        if k in blob:
            print(f"  {it['id']} | {it['publishedAt']} | {k}")
            break
