#!/usr/bin/env python3
"""Fetch IA / HKFI / NFRA pages that need direct HTTP."""
import re, html, zlib, urllib.request
from datetime import datetime, timezone, timedelta

HKT = timezone(timedelta(hours=8))
PROXY = 'http://127.0.0.1:17891'
op = urllib.request.build_opener(urllib.request.ProxyHandler({'http': PROXY, 'https': PROXY}))
op.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36'),
                 ('Accept-Language', 'zh-HK,zh;q=0.9,en;q=0.8')]


def get(url, timeout=30):
    try:
        r = op.open(url, timeout=timeout)
        raw = r.read()
        if r.headers.get('Content-Encoding') == 'gzip':
            raw = zlib.decompress(raw, 16 + zlib.MAX_WBITS)
        return raw.decode('utf-8', 'replace')
    except Exception as e:
        return f'__ERR__ {type(e).__name__}: {str(e)[:150]}'


URLS = {
    'ia_pr_2026': 'https://www.ia.org.hk/en/infocenter/press_releases/2026.html',
    'ia_pr_list': 'https://www.ia.org.hk/en/infocenter/press_releases.html',
    'ia_speeches': 'https://www.ia.org.hk/en/infocenter/speeches_articles.html',
    'ia_stats': 'https://www.ia.org.hk/en/infocenter/statistics/statistics.html',
    'hkfi': 'https://www.hkfi.org.hk/en/media-release',
    'nfra_dynamics': 'https://www.nfra.gov.cn/cn/static/data/DocInfo/SelectDocByItemIdAndChild/data_itemId=915,pageIndex=1,pageSize=18.json',
    'ia_rss_press': 'https://www.ia.org.hk/en/rss/press_releases.xml',
}
for k, u in URLS.items():
    t = get(u)
    print(f'=== {k} len={len(t)} ===')
    if t.startswith('__ERR__'):
        print(t)
    else:
        open(f'data/_1014/{k}.raw', 'w', encoding='utf-8').write(t)
