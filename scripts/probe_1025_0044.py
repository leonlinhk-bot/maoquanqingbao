#!/usr/bin/env python3
"""Probe multiple feeds/list pages for anything dated >= 2026-10-24."""
import os, re, json, sys, urllib.request, urllib.error
from datetime import datetime, timezone, timedelta

OUT = '/Users/leonliang/maoquanqingbao/data/_raw_1025_0044'
os.makedirs(OUT, exist_ok=True)
HKT = timezone(timedelta(hours=8))
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36'

TARGETS = [
    ('govhk', 'https://www.info.gov.hk/gia/rss/general_zh.xml'),
    ('hkma_rss', 'https://www.hkma.gov.hk/eng/news-and-media/press-releases/feed/'),
    ('insuranceasianews', 'https://insuranceasianews.com/wp-json/wp/v2/posts?per_page=30'),
    ('ian_hk', 'https://insuranceasianews.com/country/hong-kong/feed/'),
    ('insuranceasia', 'https://insuranceasia.com/rss.xml'),
    ('artemis', 'https://artemis.bm/feed/'),
    ('ibm_asia', 'https://www.insurancebusinessmag.com/asia/rss/'),
    ('scmp_biz', 'https://www.scmp.com/rss/92/feed'),
    ('hkfi', 'https://www.hkfi.org.hk/en/media-centre/press-release'),
    ('nfra', 'https://www.nfra.gov.cn/cn/view/pages/index/index.html'),
]

def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': '*/*'})
    with urllib.request.urlopen(req, timeout=25) as r:
        return r.read()

for key, url in TARGETS:
    try:
        b = get(url)
        p = os.path.join(OUT, key + ('_' + str(int(datetime.now().timestamp())) + '.raw'))
        open(p, 'wb').write(b)
        print(f'OK   {key:20s} {len(b):8d} bytes -> {os.path.basename(p)}')
    except Exception as e:
        print(f'FAIL {key:20s} {type(e).__name__}: {str(e)[:90]}')
