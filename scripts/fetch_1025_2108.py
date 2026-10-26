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
 'insuranceasia': 'https://insuranceasia.com/insurance/rss.xml',
 'insuranceasia2': 'https://insuranceasia.com/rss.xml',
 'ibm_asia': 'https://www.insurancebusinessmag.com/asia/rss/',
 'ian': 'https://insuranceasianews.com/wp-json/wp/v2/posts?per_page=10',
 'artemis': 'https://www.artemis.bm/news/feed/',
 'rn': 'https://www.reinsurancene.ws/feed/',
 'govhk_zh': 'https://www.info.gov.hk/gia/rss/general_zh.xml',
 'govhk_en': 'https://www.info.gov.hk/gia/rss/general_en.xml',
 'hkma': 'https://www.hkma.gov.hk/eng/news-and-media/press-releases/',
 'scmp': 'https://www.scmp.com/rss/92/feed',
 'ia_press': 'https://www.ia.org.hk/en/infocenter/press_releases.html',
 'hkfi': 'https://www.hkfi.org.hk/en/media-centre/press-release',
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

os.makedirs('.cache1025_2108', exist_ok=True)
for k, v in out.items():
    if v.get('ok'):
        open(f'.cache1025_2108/{k}.raw', 'w').write(v['body'])
json.dump({k: {kk: vv for kk, vv in v.items() if kk != 'body'} for k, v in out.items()},
          open('.cache1025_2108/_meta.json', 'w'), indent=1)
print('saved', len(out), 'ok=', sum(1 for v in out.values() if v.get('ok')))
