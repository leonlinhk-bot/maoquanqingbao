import subprocess, re, html, json
from pathlib import Path

D = Path('/Users/leonliang/maoquanqingbao/data/_1022_0037')
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'

urls = {
 'ibm_chubb': 'https://www.insurancebusinessmag.com/asia/news/breaking-news/chubbs-asia-life-and-consumer-lines-drive-growth-as-commercial-pricing-softens-594349.aspx',
 'ibm_pacific': 'https://www.insurancebusinessmag.com/asia/news/breaking-news/pacific-rates-fall-12-but-not-every-client-gets-the-cut-594421.aspx',
 'ian_skuld': 'https://insuranceasianews.com/skulds-wei-fan-take-hong-kong-helm-in-late-2027-patrick-wang-to-chair-far-east-unit/',
 'ian_cyclone': 'https://insuranceasianews.com/australias-cyclone-pool-swings-back-into-profitability-in-fy26-on-lower-claims-provisions/',
 'rn_cybercube': 'https://www.reinsurancene.ws/cybercube-and-blackpanda-partner-to-bring-cyber-risk-analytics-to-brokers-across-asia/',
 'art_chubb': 'https://www.artemis.bm/news/theres-a-lot-of-hungry-and-extremely-naive-capacity-available-chubb-ceo-greenberg/',
 'rn_crc': 'https://www.reinsurancene.ws/property-renewal-rate-reductions-begin-to-moderate-in-q326-crc-group/',
 'art_marsh': 'https://www.artemis.bm/news/global-property-insurance-rates-fall-10-in-q326-as-terms-improve-for-buyers-marsh-risk/',
 'art_acorn': 'https://www.artemis.bm/news/hannover-re-targets-75-upsized-350m-of-limit-from-new-acorn-re-parametric-cat-bond/',
 'art_easton': 'https://www.artemis.bm/news/hamilton-returns-with-250m-target-to-upsize-and-renew-easton-re-catastrophe-bond/',
 'ibm_mas': 'https://www.insurancebusinessmag.com/asia/news/professional-liability/mas-ai-governance-rules-put-tech-eando-in-the-spotlight-as-sea-prepares-enterprise-platform-594246.aspx',
 'rn_aon': 'https://www.reinsurancene.ws/uk-pension-risk-settlement-activity-to-rebound-after-subdued-start-to-2026-aon/',
}

def clean(t):
    t = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', t, flags=re.S)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t)
    return re.sub(r'[ \t\xa0]+', ' ', t)

for name, u in urls.items():
    out = D / f'body_{name}.html'
    r = subprocess.run(['curl', '-sL', '-m', '30', '-A', UA, '-o', str(out), '-w', '%{http_code}', u],
                       capture_output=True, text=True)
    txt = out.read_text(encoding='utf-8', errors='ignore') if out.exists() else ''
    print(f'\n######## {name}  HTTP {r.stdout}  bytes={len(txt)}')
    body = clean(txt)
    # cut nav noise: find first long paragraph
    lines = [l.strip() for l in body.split('\n') if len(l.strip()) > 80]
    joined = ' '.join(lines)
    print(joined[:2200])
