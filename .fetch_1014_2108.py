#!/usr/bin/env python3
"""2026-10-14 21:08 run: grab reachable domestic sources, then poll for international recovery."""
import json, os, sys, time, zlib
import urllib.request

PROXY = 'http://127.0.0.1:17891'
op = urllib.request.build_opener(urllib.request.ProxyHandler({'http': PROXY, 'https': PROXY}))
op.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36')]
OUT = '/Users/leonliang/maoquanqingbao/data/_1014_2108'
os.makedirs(OUT, exist_ok=True)

INTL = {
    'ia_press': 'https://www.ia.org.hk/en/infocenter/press_releases.html',
    'ia_circular': 'https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html',
    'ia_stats': 'https://www.ia.org.hk/en/infocenter/statistics/statistics.html',
    'hkma_api': 'https://api.hkma.gov.hk/public/press-releases?segment=all&sortby=date_desc&pagesize=30',
    'insuranceasia': 'https://insuranceasia.com/rss.xml',
    'insurancebusinessmag': 'https://www.insurancebusinessmag.com/asia/rss/',
    'insuranceasianews': 'https://insuranceasianews.com/wp-json/wp/v2/posts?per_page=12',
    'artemis': 'https://www.artemis.bm/news/feed/',
    'scmp': 'https://www.scmp.com/rss/92/feed',
    'govhk': 'https://www.info.gov.hk/gia/rss/general_zh.xml',
    'hkfi': 'https://www.hkfi.org.hk/en/media-centre/press-release',
    'asiainsurancereview': 'https://www.asiainsurancereview.com/News',
    'aia': 'https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/',
    'manulife': 'https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html',
    'prudential': 'https://www.prudential.com.hk/tc/about-us/newsroom/',
    'axa': 'https://www.axa.com.hk/zh/news-room/',
    'sunlife': 'https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/',
    'ia_press_jina': 'https://r.jina.ai/https://www.ia.org.hk/en/infocenter/press_releases.html',
    'ia_circular_jina': 'https://r.jina.ai/https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html',
}
DOM = {
    'nfra': 'https://www.nfra.gov.cn/cn/view/pages/index/index.html',
    'nfra_stats': 'https://www.nfra.gov.cn/cn/view/pages/ItemList.html',
}


def get(url, timeout=20):
    try:
        r = op.open(url, timeout=timeout)
        raw = r.read()
        if r.headers.get('Content-Encoding') == 'gzip':
            raw = zlib.decompress(raw, 16 + zlib.MAX_WBITS)
        return raw.decode('utf-8', 'replace')
    except Exception as e:
        return f'__ERR__ {type(e).__name__}: {str(e)[:100]}'


def save(k, t):
    open(f'{OUT}/{k}.raw', 'w', encoding='utf-8').write(t)


res = {}
for k, u in DOM.items():
    t = get(u)
    res[k] = 'OK' if not t.startswith('__ERR__') else t
    if not t.startswith('__ERR__'):
        save(k, t)
print('domestic:', json.dumps(res, ensure_ascii=False))

# bounded poll for international recovery
ok = False
for attempt in range(1, 19):  # ~18 * 20s = 6 min
    t = get(INTL['insuranceasia'], timeout=15)
    if not t.startswith('__ERR__'):
        print(f'RECOVERED after {attempt} attempts')
        ok = True
        break
    print(f'attempt {attempt}: {t[:70]}', flush=True)
    time.sleep(20)

if ok:
    for k, u in INTL.items():
        t = get(u)
        st = 'OK' if not t.startswith('__ERR__') else t[:60]
        print(f'  {k}: {st}', flush=True)
        if not t.startswith('__ERR__'):
            save(k, t)
json.dump({'intl_ok': ok, 'ts': time.strftime('%Y-%m-%dT%H:%M:%S+08:00')}, open(f'{OUT}/_status.json', 'w'))
print('STATUS intl_ok=', ok)
