import re, urllib.request, urllib.parse, html as htmllib
from datetime import datetime, timezone, timedelta

UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/126.0.0.0 Safari/537.36')
WINDOW = datetime(2026, 8, 25, 10, 18, 0, tzinfo=timezone.utc)

def fetch(url, timeout=30, referer=None, accept='text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'):
    hdrs = {
        'User-Agent': UA,
        'Accept': accept,
        'Accept-Language': 'zh-HK,zh;q=0.9,en;q=0.8',
        'Accept-Encoding': 'identity',
    }
    if referer:
        hdrs['Referer'] = referer
    req = urllib.request.Request(url, headers=hdrs)
    return urllib.request.urlopen(req, timeout=timeout).read().decode('utf-8', 'ignore')

print('===== HKMA press releases list =====')
try:
    html = fetch('https://www.hkma.gov.hk/eng/news-and-media/press-releases/')
    # entries: <li>DATE</li><li><a href="..." title="TITLE">TITLE</a></li>
    pat = re.compile(r'<li>(\d{1,2} \w{3} \d{4})</li><li><a href="([^"]+)"[^>]*title="([^"]+)"', re.S)
    hits = pat.findall(html)
    print('total hits:', len(hits))
    for d, href, title in hits[:25]:
        try:
            dt = datetime.strptime(d, '%d %b %Y').replace(tzinfo=timezone.utc)
        except Exception:
            dt = None
        mark = ' <<< NEW' if dt and dt >= WINDOW else ''
        print(f'[{d}] {title[:95]}{mark}')
        print(f'    https://www.hkma.gov.hk{href}')
except Exception as e:
    print('ERR', e)

print()
print('===== Insurance Business Asia breaking news =====')
try:
    html = fetch('https://www.insurancebusinessmag.com/asia/news/breaking-news/')
    print('len:', len(html))
    pat = re.compile(r'<a[^>]+href="([^"]*news/[^"]*\.aspx)"[^>]*>([^<]{15,120})</a>', re.S)
    seen = set()
    for href, txt in pat.findall(html):
        t = htmllib.unescape(txt).strip()
        if href in seen or t in seen:
            continue
        seen.add(href); seen.add(t)
        print(' ', t[:90], '->', href)
except Exception as e:
    print('ERR', e)

print()
print('===== AIA HK press releases =====')
for u in ['https://www.aia.com.hk/en/about-aia/about-us/media-centre/press-releases/',
          'https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/']:
    try:
        html = fetch(u)
        print(f'{u} len={len(html)}')
        for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>([^<]{15,120})</a>', html):
            href, txt = m.group(1), htmllib.unescape(m.group(2)).strip()
            if 'press' in href.lower() or '2026' in href:
                print('  ', txt[:80], '->', href[:120])
        break
    except Exception as e:
        print(f'{u} ERR {e}')

print()
print('===== NFRA (中国金融监管总局) =====')
try:
    html = fetch('http://www.nfra.gov.cn/cn/view/pages/ItemList.html?itemPId=921&itemId=922&itemUrl=ItemListRightList.html&itemName=%E9%87%8D%E8%A6%81%E5%85%AC%E5%91%8A&itemsubImage=')
    print('len:', len(html))
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>\s*([^<]{10,100})', html):
        href, txt = m.group(1), htmllib.unescape(m.group(2)).strip()
        if '2026' in href or 'Item' in href:
            print('  ', txt[:70], '->', href[:120])
except Exception as e:
    print('ERR', e)

print()
print('===== FSTB family office / 香港家族办公室 =====')
try:
    html = fetch('https://www.fstb.gov.hk/en/')
    print('len:', len(html))
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>([^<]{15,100})</a>', html):
        href, txt = m.group(1), htmllib.unescape(m.group(2)).strip()
        if 'family' in href.lower() or 'family' in txt.lower():
            print('  ', txt[:70], '->', href[:120])
except Exception as e:
    print('ERR', e)
