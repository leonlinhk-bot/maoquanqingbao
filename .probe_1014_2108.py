#!/usr/bin/env python3
"""Reachability matrix across collector sources (2026-10-14 21:08 run)."""
import concurrent.futures as cf
import urllib.request

PROXY = 'http://127.0.0.1:17891'
op = urllib.request.build_opener(urllib.request.ProxyHandler({'http': PROXY, 'https': PROXY}))
op.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36')]

URLS = {
    'ia_press': 'https://www.ia.org.hk/en/infocenter/press_releases.html',
    'ia_circular': 'https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html',
    'ia_stats': 'https://www.ia.org.hk/en/infocenter/statistics/statistics.html',
    'hkma_api': 'https://api.hkma.gov.hk/public/press-releases?segment=all&sortby=date_desc&pagesize=30',
    'aia': 'https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/',
    'manulife': 'https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html',
    'prudential': 'https://www.prudential.com.hk/tc/about-us/newsroom/',
    'axa': 'https://www.axa.com.hk/zh/news-room/',
    'sunlife': 'https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/',
    'insuranceasia': 'https://insuranceasia.com/rss.xml',
    'insurancebusinessmag': 'https://www.insurancebusinessmag.com/asia/rss/',
    'insuranceasianews': 'https://insuranceasianews.com/wp-json/wp/v2/posts?per_page=10',
    'artemis': 'https://www.artemis.bm/news/feed/',
    'scmp': 'https://www.scmp.com/rss/92/feed',
    'govhk': 'https://www.info.gov.hk/gia/rss/general_zh.xml',
    'hkfi': 'https://www.hkfi.org.hk/en/media-centre/press-release',
    'fsc_tw': 'https://www.fsc.gov.tw/ch/home.jsp?id=96&parentpath=0,2',
    'nfra': 'https://www.nfra.gov.cn/cn/view/pages/index/index.html',
    'asiainsurancereview': 'https://www.asiainsurancereview.com/News',
    'fta_hk': 'https://www.fstb.gov.hk/en/',
}


def probe(item):
    k, u = item
    try:
        r = op.open(u, timeout=15)
        b = r.read(4000)
        return k, r.status, len(b), ''
    except Exception as e:
        return k, 'ERR', 0, f'{type(e).__name__}: {str(e)[:70]}'


with cf.ThreadPoolExecutor(max_workers=8) as ex:
    for k, st, n, err in ex.map(probe, URLS.items()):
        print(f'{k:22} {st} {n:>6} {err}')
