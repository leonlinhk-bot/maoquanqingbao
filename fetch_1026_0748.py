import os, sys, json, re, time
import urllib.request, urllib.error

PROXY = os.environ.get('HTTP_PROXY') or 'http://127.0.0.1:17891'
HDRS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'}

def get(url, timeout=25, use_proxy=True):
    req = urllib.request.Request(url, headers=HDRS)
    if use_proxy:
        op = urllib.request.build_opener(urllib.request.ProxyHandler({'http': PROXY, 'https': PROXY}))
    else:
        op = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    with op.open(req, timeout=timeout) as r:
        return r.read().decode('utf-8', 'replace')

urls = {
 'ia_press': 'https://www.ia.org.hk/en/infocenter/press_releases.html',
 'ia_circ': 'https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html',
 'hkma': 'https://www.hkma.gov.hk/eng/news-and-media/press-releases/',
 'hkma_rss': 'https://www.hkma.gov.hk/eng/news-and-media/press-releases/rss/',
 'insuranceasia': 'https://insuranceasia.com/insurance/rss.xml',
 'insuranceasia2': 'https://insuranceasia.com/rss.xml',
 'ibm_asia': 'https://www.insurancebusinessmag.com/asia/rss/',
 'ian': 'https://insuranceasianews.com/wp-json/wp/v2/posts?per_page=15',
 'artemis': 'https://www.artemis.bm/news/feed/',
 'rn': 'https://www.reinsurancene.ws/feed/',
 'govhk_zh': 'https://www.info.gov.hk/gia/rss/general_zh.xml',
 'govhk_en': 'https://www.info.gov.hk/gia/rss/general_en.xml',
 'scmp': 'https://www.scmp.com/rss/92/feed',
 'hkfi': 'https://www.hkfi.org.hk/en/media-centre/press-release',
 'aia': 'https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/',
 'manulife': 'https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html',
 'prudential': 'https://www.prudential.com.hk/tc/about-us/newsroom/',
 'axa': 'https://www.axa.com.hk/zh/news-room/',
 'sunlife': 'https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/',
 'nfra': 'https://www.nfra.gov.cn/cn/view/pages/index/index.html',
 'fstb': 'https://www.fstb.gov.hk/en/',
}

out = {}
for k, u in urls.items():
    t0 = time.time()
    try:
        body = get(u)
        out[k] = {'ok': True, 'len': len(body), 'ms': int((time.time()-t0)*1000), 'body': body}
        print(f'OK   {k:16s} {len(body):8d} chars {int((time.time()-t0)*1000):5d}ms')
    except Exception as e:
        print(f'FAIL {k:16s} {type(e).__name__}: {str(e)[:120]}')

os.makedirs('.cache1026_0748', exist_ok=True)
for k, v in out.items():
    if v.get('ok'):
        open(f'.cache1026_0748/{k}.raw', 'w').write(v['body'])
json.dump({k: {kk: vv for kk, vv in v.items() if kk != 'body'} for k, v in out.items()},
          open('.cache1026_0748/_meta.json', 'w'), indent=1)
print('saved', len(out), 'ok=', sum(1 for v in out.values() if v.get('ok')))
