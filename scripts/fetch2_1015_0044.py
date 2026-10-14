#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Second fetch batch: additional sources for 1015 run."""
import os, gzip, zlib, urllib.request
from datetime import datetime, timezone, timedelta

HKT = timezone(timedelta(hours=8))
PROXY = 'http://127.0.0.1:17891'
DIR = '/Users/leonliang/maoquanqingbao/data/_1015'
os.makedirs(DIR, exist_ok=True)
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/126.0 Safari/537.36')


def get(url, timeout=30):
    err = ''
    for proxy in (PROXY, None):
        h = {'http': proxy, 'https': proxy} if proxy else {}
        op = urllib.request.build_opener(urllib.request.ProxyHandler(h))
        op.addheaders = [('User-Agent', UA), ('Accept', '*/*'),
                         ('Accept-Language', 'zh-HK,zh;q=0.9,en;q=0.8')]
        try:
            r = op.open(url, timeout=timeout)
            raw = r.read()
            ce = r.headers.get('Content-Encoding', '')
            if ce == 'gzip':
                raw = gzip.decompress(raw)
            elif ce == 'deflate':
                raw = zlib.decompress(raw, -zlib.MAX_WBITS)
            return raw.decode('utf-8', 'replace')
        except Exception as e:
            err = f'__ERR__ {type(e).__name__}: {str(e)[:110]}'
    return err


URLS = {
    'air_rss': 'https://www.asiainsurancereview.com/rss',
    'air_rss2': 'https://www.asiainsurancereview.com/Portal/RSS',
    'air_news': 'https://www.asiainsurancereview.com/News',
    'ian_feed': 'https://insuranceasianews.com/feed/',
    'hkfi_pr2': 'https://www.hkfi.org.hk/en/media-release',
    'hkfi_pr3': 'https://www.hkfi.org.hk/en/news-and-events/press-release',
    'iasia_news': 'https://insuranceasia.com/insurance/news',
    'hkma_speeches': 'https://www.hkma.gov.hk/eng/news-and-media/speeches/',
    'hkma_insight': 'https://www.hkma.gov.hk/eng/news-and-media/insight/',
    'ia_home_sc': 'https://www.ia.org.hk/tc/infocenter/press_releases.html',
    'ia_gi': 'https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html',
}

print('now:', datetime.now(HKT).isoformat())
for k, u in URLS.items():
    t = get(u)
    if t.startswith('__ERR__'):
        print(f'=== {k}: {t}')
    else:
        p = os.path.join(DIR, k + '.raw')
        open(p, 'w', encoding='utf-8').write(t)
        print(f'=== {k}: len={len(t)} -> {p}')
