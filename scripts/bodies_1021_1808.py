import json, re, html, subprocess
D = 'data/_1021_1808/bodies'
import os
os.makedirs(D, exist_ok=True)

urls = {
 'perils': 'https://www.artemis.bm/news/perils-lifts-july-european-convective-storms-insured-market-loss-estimate-to-e2-8bn/',
 'arbol': 'https://www.artemis.bm/news/arbol-launches-parametric-insurance-for-gov-imposed-data-center-construction-moratoriums/',
 'jamaica': 'https://www.artemis.bm/news/jamaicas-parametric-cat-bond-payout-funded-electricity-restoration-chief-fiscal-economist-francis/',
 'gam': 'https://www.artemis.bm/news/deepening-cat-bond-market-offers-investors-liquidity-scale-and-broader-diversification-gams-aviv/',
 'muse': 'https://www.reinsurancene.ws/metas-muse-ai-agents-could-pose-longer-term-risk-to-loss-costs-autonomous/',
 'triplei': 'https://www.reinsurancene.ws/us-insurers-forecast-to-sustain-underwriting-gains-in-2026-despite-economic-pressures-triple-i-milliman/',
 'france': 'https://www.reinsurancene.ws/unrest-in-france-underlines-cat-like-risks-of-riots-and-civil-commotion-morningstar-dbrs/',
 'helvetia': 'https://insuranceasianews.com/siew-choo-tan-to-succeed-ivan-chan-as-helvetia-asia-ceo/',
 'geraghty': 'https://insuranceasianews.com/mg-geraghty-hires-howdens-phil-steel-as-head-of-business-development/',
 'cybercube': 'https://insuranceasianews.com/cybercube-adds-sompo-japan-to-growing-apac-client-base/',
}
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'
for k, u in urls.items():
    p = f'{D}/{k}.html'
    subprocess.run(['curl', '-sL', '-m', '30', '-A', UA, '-o', p, u])
    raw = open(p, encoding='utf-8', errors='replace').read()
    raw = re.sub(r'<script.*?</script>', ' ', raw, flags=re.S)
    raw = re.sub(r'<style.*?</style>', ' ', raw, flags=re.S)
    txt = re.sub(r'<[^>]+>', ' ', raw)
    txt = re.sub(r'\s+', ' ', html.unescape(txt))
    open(f'{D}/{k}.txt', 'w', encoding='utf-8').write(txt)
    print(f'--- {k} ({len(txt)}) ---')
    # find start by first occurrence of a keyword-ish sentence
    print(txt[:60])
