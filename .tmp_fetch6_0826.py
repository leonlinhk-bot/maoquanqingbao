import re, urllib.request, urllib.parse, html as htmllib, json

UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/126.0.0.0 Safari/537.36')

def fetch(url, timeout=30, referer=None, accept='text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'):
    hdrs = {'User-Agent': UA, 'Accept': accept,
            'Accept-Language': 'zh-HK,zh;q=0.9,en;q=0.8', 'Accept-Encoding': 'identity'}
    if referer:
        hdrs['Referer'] = referer
    req = urllib.request.Request(url, headers=hdrs)
    return urllib.request.urlopen(req, timeout=timeout).read().decode('utf-8', 'ignore')

def clean(txt):
    txt = re.sub(r'<[^>]+>', ' ', txt)
    txt = htmllib.unescape(txt)
    return re.sub(r'\s+', ' ', txt).strip()

print('===== InsuranceAsia new articles (body snippets) =====')
arts = [
    ('manulife-ai', 'https://insuranceasia.com/insurance/exclusive/manulife-asia-pushes-ai-drive-health-wealth-growth'),
    ('tw-spillover', 'https://insuranceasia.com/insurance/news/taiwan-spillover-effect-premiums-surge-152'),
    ('id-health', 'https://insuranceasia.com/insurance/news/indonesia-health-rules-impose-5-co-pay-claims'),
    ('in-life', 'https://insuranceasia.com/insurance/news/india-life-premiums-rise-1745-16b-in-july-2026'),
    ('tw-fc-life', 'https://insuranceasia.com/insurance/news/taiwan-foreign-currency-life-premiums-surge-54-in-may-2026'),
    ('ph-penetration', 'https://insuranceasia.com/insurance/news/philippine-insurance-penetration-rises-196-in-q2-2026'),
    ('vn-bank', 'https://insuranceasia.com/insurance/news/vietnamese-bank-ventures-non-life-insurance'),
    ('tw-labour', 'https://insuranceasia.com/insurance/news/taiwan-labour-insurance-hike-adds-413m-business-costs'),
    ('jp-export', 'https://insuranceasia.com/insurance/news/japan-export-insurer-covers-2b-us-gas-plant-loan'),
]
for tag, u in arts:
    try:
        html = fetch(u)
        title = re.search(r'<title>(.*?)</title>', html, re.S)
        dp = re.findall(r'"datePublished"\s*:\s*"([^"]+)"', html)
        # body: common article containers
        body = ''
        m = re.search(r'<article[^>]*>(.*?)</article>', html, re.S)
        if m:
            body = clean(m.group(1))
        if not body:
            m = re.search(r'<div class="[^"]*(?:article|content|story)[^"]*"[^>]*>(.*?)</div>', html, re.S)
            if m:
                body = clean(m.group(1))
        print(f'--- {tag} | title: {(title.group(1).strip()[:80] if title else "?")} | datePublished: {dp[:1]}')
        print('   body:', body[:700])
    except Exception as e:
        print(f'--- {tag} ERR {e}')

print()
print('===== Insurance Business articles dates =====')
ibm = [
    ('steadfast', 'https://www.insurancebusinessmag.com/asia/news/breaking-news/steadfast-lifts-profit-as-us-consortium-moves-to-take-it-private-587463.aspx'),
    ('sg-west-island', 'https://www.insurancebusinessmag.com/asia/news/construction/singapores-new-western-island-will-need-insurance-tools-that-do-not-yet-exist-587445.aspx'),
    ('sg-cfo', 'https://www.insurancebusinessmag.com/asia/news/professional-liability/singapores-cfo-confidence-crash-conceals-a-broker-opening-587444.aspx'),
    ('vn-credit', 'https://www.insurancebusinessmag.com/asia/news/breaking-news/vietnams-trade-boom-outpaces-its-credit-insurance-market-587443.aspx'),
]
for tag, u in ibm:
    try:
        html = fetch(u)
        dp = re.findall(r'"datePublished"\s*:\s*"([^"]+)"', html)
        dt = re.findall(r'datetime="([^"]+)"', html)
        title = re.search(r'<title>(.*?)</title>', html, re.S)
        print(f'--- {tag} | title: {(title.group(1).strip()[:80] if title else "?")} | datePublished: {dp[:1]} | datetime: {dt[:2]}')
    except Exception as e:
        print(f'--- {tag} ERR {e}')

print()
print('===== IA via r.jina.ai =====')
for u in ['https://r.jina.ai/https://www.ia.org.hk/en/infocenter/press_releases.html',
          'https://r.jina.ai/https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html']:
    try:
        txt = fetch(u, timeout=45)
        print(f'--- {u[:80]} len={len(txt)}')
        print(txt[:1500])
    except Exception as e:
        print(f'--- ERR {e}')

print()
print('===== NFRA via r.jina.ai =====')
try:
    txt = fetch('https://r.jina.ai/https://www.nfra.gov.cn/cn/view/pages/ItemList.html?itemPId=921&itemId=922&itemUrl=ItemListRightList.html&itemName=%E9%87%8D%E8%A6%81%E5%85%AC%E5%91%8A', timeout=45)
    print('len=', len(txt))
    print(txt[:2000])
except Exception as e:
    print('ERR', e)
