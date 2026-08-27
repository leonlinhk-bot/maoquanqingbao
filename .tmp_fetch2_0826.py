import re, urllib.request, urllib.parse, html as htmllib

UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/126.0.0.0 Safari/537.36')

def fetch(url, timeout=30, referer=None):
    hdrs = {
        'User-Agent': UA,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-HK,zh;q=0.9,en;q=0.8',
        'Accept-Encoding': 'identity',
    }
    if referer:
        hdrs['Referer'] = referer
    req = urllib.request.Request(url, headers=hdrs)
    return urllib.request.urlopen(req, timeout=timeout).read().decode('utf-8', 'ignore')

print('===== 1. InsuranceAsia RSS candidates =====')
for u in ['https://insuranceasia.com/rss.xml',
          'https://www.insuranceasia.com/insurance/rss.xml',
          'https://insuranceasia.com/insurance/feed/']:
    try:
        xml = fetch(u)
        items = re.findall(r'<item>(.*?)</item>', xml, re.S)
        print(f'{u} -> OK, {len(items)} items')
        for it in items[:6]:
            t = re.search(r'<title>(.*?)</title>', it, re.S)
            p = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
            l = re.search(r'<link>(.*?)</link>', it, re.S)
            print(f'  [{p.group(1).strip() if p else "?"}] {htmllib.unescape(t.group(1)).strip()[:90] if t else "?"}')
            print(f'    {htmllib.unescape(l.group(1)).strip()[:140] if l else "?"}')
        break
    except Exception as e:
        print(f'{u} -> ERR {e}')

print()
print('===== 2. HKMA press releases =====')
try:
    html = fetch('https://www.hkma.gov.hk/eng/news-and-media/press-releases/')
    # Extract list items with dates
    print('len html:', len(html))
    for m in re.finditer(r'<a[^>]+href="(/eng/news-and-media/press-releases/2026/\d+/\d+/[^"]+)"[^>]*>([^<]{10,140})</a>', html):
        href, txt = m.group(1), htmllib.unescape(m.group(2)).strip()
        print(' ', txt[:95], '->', href)
except Exception as e:
    print('ERR', e)

print()
print('===== 3. IA press releases (retry w/ referer) =====')
try:
    html = fetch('https://www.ia.org.hk/en/infocenter/press_releases.html',
                 referer='https://www.ia.org.hk/en/')
    print('len html:', len(html))
    seen = set()
    for m in re.finditer(r'<a[^>]+href="([^"]*press[^"]*\.html[^"]*)"[^>]*>\s*([^<]{10,140})', html):
        href, txt = m.group(1), htmllib.unescape(m.group(2)).strip()
        if href in seen or 'javascript' in href:
            continue
        seen.add(href)
        print(' ', txt[:95], '->', href)
except Exception as e:
    print('ERR', e)
