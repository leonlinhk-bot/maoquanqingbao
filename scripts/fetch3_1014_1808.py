#!/usr/bin/env python3
"""Fetch specific article pages via proxy with retries; extract plain text."""
import re, html, zlib, time, urllib.request

PROXY = 'http://127.0.0.1:17891'
op = urllib.request.build_opener(urllib.request.ProxyHandler({'http': PROXY, 'https': PROXY}))
op.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36'),
                 ('Accept-Language', 'zh-HK,zh;q=0.9,en;q=0.8'),
                 ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]

URLS = {
    'govhk_cdta': 'https://www.info.gov.hk/gia/general/202610/14/P2026101400351.htm',
    'govhk_flp': 'https://www.info.gov.hk/gia/general/202610/14/P2026101300384.htm',
    'nfra_macau': 'https://www.nfra.gov.cn/cn/view/pages/ItemDetail.html?docId=1274663&itemId=915&generaltype=0',
    'iaasia_hsbc': 'https://insuranceasia.com/insurance/news/hsbc-life-expands-cross-border-healthcare-four-new-lounges',
    'iaasia_natre': 'https://insuranceasia.com/insurance/news/nat-res-capital-strength-opens-door-higher-underwriting-volumes',
    'iaasia_retire': 'https://insuranceasia.com/insurance/in-focus/life-insurers-face-pressure-retirement-savings-shift',
    'ibm_manulife_ai': 'https://www.insurancebusinessmag.com/asia/news/life-insurance/manulife-launches-enterprise-ai-platform-as-it-targets-1-billion-in-value-by-2027-593466.aspx',
    'ibm_indonesia': 'https://www.insurancebusinessmag.com/asia/news/breaking-news/indonesias-draft-capital-rules-would-restrict-smaller-insurers-credit-and-specialty-lines-593443.aspx',
    'ibm_moodys': 'https://www.insurancebusinessmag.com/asia/news/breaking-news/credit-cover-alone-will-not-scale-emergingmarket-climate-finance-moodys-says-593478.aspx',
    'scmp_imf': 'https://www.scmp.com/business/banking-finance/article/3370722/imf-warns-higher-borrowing-costs-are-straining-public-finances-worldwide',
}


def get(url, tries=3):
    last = ''
    for i in range(tries):
        try:
            r = op.open(url, timeout=30)
            raw = r.read()
            if r.headers.get('Content-Encoding') == 'gzip':
                raw = zlib.decompress(raw, 16 + zlib.MAX_WBITS)
            return raw.decode('utf-8', 'replace')
        except Exception as e:
            last = f'{type(e).__name__}: {str(e)[:90]}'
            time.sleep(4)
    return '__ERR__ ' + last


def text(h):
    h = re.sub(r'(?is)<(script|style|nav|header|footer)\b.*?</\1>', ' ', h)
    h = re.sub(r'<!\[CDATA\[(.*?)\]\]>', r'\1', h, flags=re.S)
    h = re.sub(r'<br\s*/?>', '\n', h)
    h = re.sub(r'</p>', '\n', h)
    h = re.sub(r'<[^>]+>', ' ', h)
    h = html.unescape(h)
    h = re.sub(r'[ \t\u00a0\u3000]+', ' ', h)
    h = re.sub(r'\n\s*\n+', '\n', h)
    return h.strip()


for k, u in URLS.items():
    raw = get(u)
    print(f'\n======== {k} ========')
    if raw.startswith('__ERR__'):
        print(raw)
        continue
    t = text(raw)
    open(f'data/_1014/{k}.txt', 'w', encoding='utf-8').write(t)
    print(t[:2600])
