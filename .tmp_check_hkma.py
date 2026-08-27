import json, re, urllib.request

d = json.load(open('data/live-items.json'))
urls = {it.get('originalUrl') for it in d['items']}
ids = {it['id'] for it in d['items']}
print("HKMA -3 in library:", any('20260825-3' in u for u in urls))
print("HKMA -4 in library:", any('20260825-4' in u for u in urls))
for it in d['items']:
    if it.get('sourceKey') == 'hkma' and '20260825' in it.get('id', ''):
        print('have:', it['id'], it.get('publishedAt'))

# fetch HKMA -3 and -4 pages for publish timestamps
for tag in ['20260825-3', '20260825-4']:
    url = f'https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/08/{tag}/'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, timeout=30).read().decode('utf-8', 'ignore')
        ts = re.findall(r'(\d{1,2} \w{3} \d{4}, \d{1,2}:\d{2} [AP]M)', html)
        date_meta = re.findall(r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2})', html)
        title = re.search(r'<title>(.*?)</title>', html, re.S)
        print(tag, '| pub:', ts[:3], '| iso:', date_meta[:2], '| title:', (title.group(1).strip()[:80] if title else '?'))
    except Exception as e:
        print(tag, 'ERR', e)
