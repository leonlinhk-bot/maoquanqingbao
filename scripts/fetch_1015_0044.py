#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Catch-up run 2026-10-15 00:44 — fetch all 14-source pages/feeds raw."""
import os, gzip, zlib, urllib.request
from datetime import datetime, timezone, timedelta

HKT = timezone(timedelta(hours=8))
PROXY = 'http://127.0.0.1:17891'
DIR = '/Users/leonliang/maoquanqingbao/data/_1015'
os.makedirs(DIR, exist_ok=True)
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/126.0 Safari/537.36')


def mk(proxy=True):
    if proxy:
        return urllib.request.build_opener(urllib.request.ProxyHandler({'http': PROXY, 'https': PROXY}))
    return urllib.request.build_opener(urllib.request.ProxyHandler({}))


def get(url, timeout=30, proxy=True):
    for attempt in (proxy, not proxy):
        op = mk(attempt)
        op.addheaders = [('User-Agent', UA), ('Accept-Language', 'zh-HK,zh;q=0.9,en;q=0.8'),
                         ('Accept', '*/*')]
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
            err = f'__ERR__ {type(e).__name__}: {str(e)[:120]}'
    return err


URLS = {
    'ia_pr_2026': 'https://www.ia.org.hk/en/infocenter/press_releases/2026.html',
    'ia_pr_list': 'https://www.ia.org.hk/en/infocenter/press_releases.html',
    'ia_rss_press': 'https://www.ia.org.hk/en/rss/press_releases.xml',
    'ia_circ_reg_2026': 'https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html',
    'ia_circ_list': 'https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters.html',
    'hkma_press': 'https://www.hkma.gov.hk/eng/news-and-media/press-releases/',
    'hkma_rss': 'https://www.hkma.gov.hk/eng/rss/press-release.xml',
    'insuranceasia_rss': 'https://insuranceasia.com/rss.xml',
    'insuranceasia': 'https://insuranceasia.com/insurance',
    'ibm_asia': 'https://www.insurancebusinessmag.com/asia/news/breaking-news/',
    'ibm_rss': 'https://www.insurancebusinessmag.com/asia/rss/',
    'scmp_rss': 'https://www.scmp.com/rss/92/feed',
    'scmp_topic': 'https://www.scmp.com/topics/insurance',
    'govhk_rss': 'https://www.info.gov.hk/gia/rss/general_zh.xml',
    'govhk_rss_en': 'https://www.info.gov.hk/gia/rss/general_en.xml',
    'ian_api': 'https://insuranceasianews.com/wp-json/wp/v2/posts?per_page=25&_embed=1',
    'artemis': 'https://www.artemis.bm/news/',
    'artemis_rss': 'https://www.artemis.bm/feed/',
    'aia_pr': 'https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/',
    'manulife_nr': 'https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html',
    'prudential_nr': 'https://www.prudential.com.hk/tc/about-us/newsroom/',
    'axa_nr': 'https://www.axa.com.hk/zh/news-room/',
    'sunlife_nr': 'https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/',
    'hkfi_pr': 'https://www.hkfi.org.hk/en/media-centre/press-release',
    'nfra_index': 'https://www.nfra.gov.cn/cn/view/pages/index/index.html',
    'nfra_dyn': 'https://www.nfra.gov.cn/cn/static/data/DocInfo/SelectDocByItemIdAndChild/data_itemId=915,pageIndex=1,pageSize=18.json',
    'fstb_idx': 'https://www.fstb.gov.hk/en/',
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
