#!/usr/bin/env python3
"""Probe HKMA, NFRA, insurer newsrooms, IA (via r.jina.ai / direct)."""
import os, urllib.request, urllib.error
from datetime import datetime

OUT = '/Users/leonliang/maoquanqingbao/data/_raw_1025_0044'
os.makedirs(OUT, exist_ok=True)
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36'

TARGETS = [
    ('hkma_press', 'https://www.hkma.gov.hk/eng/news-and-media/press-releases/'),
    ('ia_press', 'https://www.ia.org.hk/en/infocenter/press_releases.html'),
    ('ia_circ', 'https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html'),
    ('aia', 'https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/'),
    ('manulife', 'https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html'),
    ('prudential', 'https://www.prudential.com.hk/tc/about-us/newsroom/'),
    ('axa', 'https://www.axa.com.hk/zh/news-room/'),
    ('sunlife', 'https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/'),
    ('hkfi', 'https://www.hkfi.org.hk/en/media-centre/press-release/'),
    ('nfra_list', 'https://www.nfra.gov.cn/cn/view/pages/ItemList.html?itemPId=923&itemId=931&itemUrl=ItemListRightList.html&itemName=%E7%9B%91%E7%AE%A1%E5%8A%A8%E6%80%81'),
]

def get(url, timeout=25):
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': 'text/html,*/*'})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()

stamp = datetime.now().strftime('%H%M')
for key, url in TARGETS:
    try:
        b = get(url)
        p = os.path.join(OUT, f'{key}_{stamp}.html')
        open(p, 'wb').write(b)
        print(f'OK   {key:12s} {len(b):8d} -> {os.path.basename(p)}')
    except Exception as e:
        print(f'FAIL {key:12s} {type(e).__name__}: {str(e)[:80]}')
