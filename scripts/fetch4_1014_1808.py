#!/usr/bin/env python3
"""Retry fetching a few article bodies via proxy."""
import re, html, zlib, time, urllib.request

PROXY = 'http://127.0.0.1:17891'
op = urllib.request.build_opener(urllib.request.ProxyHandler({'http': PROXY, 'https': PROXY}))
op.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36'),
                 ('Accept-Language', 'zh-HK,zh;q=0.9,en;q=0.8')]

URLS = {
    'iaasia_hsbc': 'https://insuranceasia.com/insurance/news/hsbc-life-expands-cross-border-healthcare-four-new-lounges',
    'iaasia_natre': 'https://insuranceasia.com/insurance/news/nat-res-capital-strength-opens-door-higher-underwriting-volumes',
    'iaasia_retire': 'https://insuranceasia.com/insurance/in-focus/life-insurers-face-pressure-retirement-savings-shift',
    'ibm_manulife_ai': 'https://www.insurancebusinessmag.com/asia/news/life-insurance/manulife-launches-enterprise-ai-platform-as-it-targets-1-billion-in-value-by-2027-593434.aspx',
    'ibm_indonesia': 'https://www.insurancebusinessmag.com/asia/news/breaking-news/indonesias-draft-capital-rules-would-restrict-smaller-insurers-credit-and-specialty-lines-593358.aspx',
    'ibm_moodys': 'https://www.insurancebusinessmag.com/asia/news/breaking-news/credit-cover-alone-will-not-scale-emergingmarket-climate-finance-moodys-says-593437.aspx',
    'scmp_imf': 'https://www.scmp.com/business/banking-finance/article/3370722/imf-warns-higher-borrowing-costs-are-straining-public-finances-worldwide',
}


def text(h):
    h = re.sub(r'(?is)<(script|style|nav|header|footer|svg)\b.*?</\1>', ' ', h)
    h = re.sub(r'<br\s*/?>', '\n', h)
    h = re.sub(r'</p>', '\n', h)
    h = re.sub(r'<[^>]+>', ' ', h)
    h = html.unescape(h)
    h = re.sub(r'[ \t\u00a0\u3000]+', ' ', h)
    return re.sub(r'\n\s*\n+', '\n', h).strip()


ok = 0
for k, u in URLS.items():
    got = None
    for i in range(4):
        try:
            r = op.open(u, timeout=35)
            raw = r.read()
            if r.headers.get('Content-Encoding') == 'gzip':
                raw = zlib.decompress(raw, 16 + zlib.MAX_WBITS)
            got = raw.decode('utf-8', 'replace')
            break
        except Exception as e:
            last = f'{type(e).__name__}: {str(e)[:80]}'
            time.sleep(5)
    print(f'\n======== {k} ========')
    if got is None:
        print('FAIL', last)
        continue
    ok += 1
    t = text(got)
    open(f'data/_1014/{k}.txt', 'w', encoding='utf-8').write(t)
    print(t[:1800])
print(f'\nOK {ok}/{len(URLS)}')
