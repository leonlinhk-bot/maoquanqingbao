import re, html, subprocess, os, json

D = '/Users/leonliang/maoquanqingbao/.cache1023_0023/bodies'
os.makedirs(D, exist_ok=True)
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"

urls = {
 'ibm_osaka_cyber': 'https://www.insurancebusinessmag.com/asia/news/cyber/osaka-brokerage-breach-raises-thirdparty-cyber-risk-questions-for-insurers-594580.aspx',
 'ibm_pvi_vietnam': 'https://www.insurancebusinessmag.com/asia/news/breaking-news/pvi-insurance-takes-vietnams-largest-nonlife-book-into-central-asia-and-the-middle-east-594577.aspx',
 'ibm_syariah_brokers': 'https://www.insurancebusinessmag.com/asia/news/breaking-news/syariah-spinoff-deadline-creates-new-counterparties-for-indonesia-brokers-594586.aspx',
 'art_wfp_ccrif': 'https://www.artemis.bm/news/world-food-programme-buys-parametric-tropical-cyclone-insurance-from-ccrif/',
 'art_acorn_450': 'https://www.artemis.bm/news/hannover-re-raises-acorn-re-parametric-cat-bond-target-size-again-to-450m/',
 'scmp_hk_fin_innovation': 'https://www.scmp.com/business/banking-finance/article/3371810/hong-kong-targets-financial-innovation-help-ease-economic-pain-points',
 'iaa_cn_medical': 'https://insuranceasia.com/insurance/in-focus/chinas-medical-insurance-costs-rise-6-in-2027',
 'iaa_20t': 'https://insuranceasia.com/insurance/news/global-insurance-market-hit-20t-2035t',
 'iaa_pingan': 'https://insuranceasia.com/insurance/news/ping-ans-new-business-value-plunge-44-in-q3-2026',
 'iaa_luenfung': 'https://insuranceasia.com/insurance/news/luen-fung-hang-stays-profitable-despite-macau-insurance-slowdown',
 'ian_beazley': 'https://insuranceasianews.com/beazley-navigating-geopolitical-risks-at-sea/',
 'axa_ai_mental': 'https://macaubusiness.com/axa%E5%AE%89%E7%9B%9B%E7%A0%94%E7%A9%B62026%EF%BC%9A%E4%B8%89%E5%88%86%E4%B9%8B%E4%BA%8C%E6%B8%AF%E4%BA%BA%E4%BD%BF%E7%94%A8ai%E5%B0%B0%E6%B1%82%E5%BF%83%E7%90%86%E5%81%A5%E5%BA%B7%E6%94%AF%E6%8F%B4/',
}

def text_of(raw):
    t = re.sub(r'(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>', ' ', raw)
    t = re.sub(r'(?is)<(nav|footer|header)[^>]*>.*?</\1>', ' ', t)
    t = re.sub(r'<[^>]+>', '\n', t)
    t = html.unescape(t)
    ls = [re.sub(r'\s+', ' ', l).strip() for l in t.split('\n')]
    return [l for l in ls if len(l) > 40]

for name, u in urls.items():
    p = f'{D}/{name}.html'
    subprocess.run(['curl', '-sL', '-m', '35', '-A', UA, '-o', p, u])
    if not os.path.exists(p):
        print('FAIL', name); continue
    raw = open(p, encoding='utf-8', errors='ignore').read()
    ls = text_of(raw)
    print(f'\n===== {name}  ({len(raw)} bytes)')
    for l in ls[:8]:
        print('  ', l[:400])
