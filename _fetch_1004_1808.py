import json, urllib.request

OUT = 'data/_raw_1004_1808.json'
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36'

TARGETS = {
 'ia_press': 'https://www.ia.org.hk/en/infocenter/press_releases.html',
 'ia_circular': 'https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html',
 'hkma_press': 'https://www.hkma.gov.hk/eng/news-and-media/press-releases/',
 'insuranceasia_rss': 'https://insuranceasia.com/rss.xml',
 'ibm_asia': 'https://www.insurancebusinessmag.com/asia/news/breaking-news/',
 'insuranceasianews_api': 'https://insuranceasianews.com/wp-json/wp/v2/posts?per_page=20',
 'artemis': 'https://www.artemis.bm/news/',
 'scmp_insurance': 'https://www.scmp.com/topics/insurance',
 'govhk_zh': 'https://www.info.gov.hk/gia/rss/general_zh.xml',
 'hkfi': 'https://www.hkfi.org.hk/en/media-centre/press-release',
 'nfra': 'https://www.nfra.gov.cn/cn/view/pages/index/index.html',
 'aia_news': 'https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/',
 'manulife_news': 'https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html',
 'prudential_news': 'https://www.prudential.com.hk/tc/about-us/newsroom/',
 'axa_news': 'https://www.axa.com.hk/zh/news-room/',
 'sunlife_news': 'https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/',
 'insuranceasia_list': 'https://insuranceasia.com/insurance',
 'chinalife_hk': 'https://www.chinalife.com.hk/zh-hk/about-us/news-centre',
 'boclife': 'https://www.boclife.com.hk/tc/about-us/media-centre/press-release.html',
}

res = {}
for k, url in TARGETS.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': '*/*'})
        with urllib.request.urlopen(req, timeout=25) as r:
            raw = r.read()
        try:
            txt = raw.decode('utf-8')
        except UnicodeDecodeError:
            txt = raw.decode('latin-1', 'ignore')
        res[k] = {'url': url, 'len': len(txt), 'text': txt[:600000]}
        print(f'OK {k} {len(txt)}')
    except Exception as e:
        res[k] = {'url': url, 'error': str(e)}
        print(f'ERR {k} {e}')

json.dump(res, open(OUT, 'w'))
print('saved', OUT)
