import json, re, urllib.request, html as htmllib

UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/126.0.0.0 Safari/537.36')

def fetch(url, timeout=30, referer=None):
    hdrs = {'User-Agent': UA, 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-HK,zh;q=0.9,en;q=0.8', 'Accept-Encoding': 'identity'}
    if referer:
        hdrs['Referer'] = referer
    req = urllib.request.Request(url, headers=hdrs)
    return urllib.request.urlopen(req, timeout=timeout).read().decode('utf-8', 'ignore')

d = json.load(open('data/live-items.json'))
items = d['items']
print('library total:', len(items))
print('--- existing HKMA ids (Aug 2026) ---')
for it in items:
    if it.get('sourceKey') == 'hkma' and '202608' in it.get('id', ''):
        print(' ', it['id'], '|', it.get('publishedAt'), '|', it['title']['sc'][:60])
print('--- existing IA ids (Aug 2026) ---')
for it in items:
    if it.get('sourceKey') == 'ia' and '202608' in it.get('id', ''):
        print(' ', it['id'], '|', it.get('publishedAt'), '|', it['title']['sc'][:60])
print('--- existing insuranceasia ids (last 10) ---')
n = 0
for it in items:
    if it.get('sourceKey') == 'insuranceasia':
        print(' ', it['id'], '|', it.get('publishedAt'), '|', it['title']['sc'][:60])
        n += 1
        if n >= 10:
            break
print('--- existing sourceKeys set ---')
keys = {}
for it in items:
    keys[it.get('sourceKey')] = keys.get(it.get('sourceKey'), 0) + 1
print(sorted(keys.items()))

print()
print('--- HKMA item pages timestamps ---')
for tag in ['20260825-5', '20260825-6']:
    url = f'https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/08/{tag}/'
    try:
        html = fetch(url)
        ts = re.findall(r'(\d{1,2} \w{3} \d{4}, \d{1,2}:\d{2} [AP]M)', html)
        title = re.search(r'<title>(.*?)</title>', html, re.S)
        print(tag, '| pub:', ts[:2], '| title:', (title.group(1).strip()[:90] if title else '?'))
    except Exception as e:
        print(tag, 'ERR', e)

print()
print('--- AIA page links ---')
try:
    html = fetch('https://www.aia.com.hk/en/about-aia/about-us/media-centre/press-releases/')
    # try to find press release list links
    pat = re.compile(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', re.S)
    seen = set()
    for href, inner in pat.findall(html):
        txt = re.sub(r'<[^>]+>', '', inner)
        txt = htmllib.unescape(txt).strip()
        if len(txt) < 12 or not txt:
            continue
        low = (href + txt).lower()
        if 'press' in low or 'media' in low or '2026' in low:
            key = (href[:80], txt[:60])
            if key in seen:
                continue
            seen.add(key)
            print(' ', txt[:80], '->', href[:130])
except Exception as e:
    print('ERR', e)
