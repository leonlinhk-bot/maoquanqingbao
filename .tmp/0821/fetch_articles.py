import subprocess, os

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
urls = {
    "iaa_prudential_tkpl": "https://insuranceasia.com/insurance/news/prudential-hong-kong-expands-taikoo-place-footprint-83000-sq-ft",
    "iaa_hdi": "https://insuranceasia.com/insurance/news/hdi-global-net-income-rises-7-2496m-in-h1-2026",
    "iaa_sumitomo": "https://insuranceasia.com/insurance/news/sumitomo-life-returns-profit-premiums-jump-298-in-q1-2026",
    "iaa_rates": "https://insuranceasia.com/insurance/news/asia-insurance-rates-fall-5-in-q2-2026-competition-intensifies",
    "iaa_manulife_sg": "https://insuranceasia.com/insurance/news/manulife-unveils-two-wealth-plans-singapores-mass-affluent",
    "iaa_msad": "https://insuranceasia.com/insurance/news/msad-profit-growth-eases-favourable-tailwinds-fade",
    "iaa_hanwha": "https://insuranceasia.com/insurance/news/hanwha-life-profit-jumps-96-investment-returns-soar",
    "iaa_jp_credit": "https://insuranceasia.com/insurance/in-focus/japanese-life-insurers-strike-global-deals-private-credit",
    "iaa_sompo": "https://insuranceasia.com/insurance/news/sompo-revenue-seen-rising-123-2026-rebound-takes-hold",
    "ib_pingan": "https://www.insurancebusinessmag.com/asia/news/breaking-news/ping-ans-new-business-growth-trails-chinas-insurance-pack-586912.aspx",
    "ib_allianz": "https://www.insurancebusinessmag.com/asia/news/breaking-news/allianz-trade-names-china-ceo-as-insolvency-forecasts-hit-10-586909.aspx",
    "ib_aia_broker": "https://www.insurancebusinessmag.com/asia/news/life-insurance/aia-narrows-broker-access-as-new-business-grows-21-586906.aspx",
    "ib_hk_postcode": "https://www.insurancebusinessmag.com/asia/news/life-insurance/hong-kongs-insurance-sector-is-quietly-concentrating-in-one-postcode-586726.aspx",
    "ib_gallagher": "https://www.insurancebusinessmag.com/asia/news/breaking-news/gallagher-re-creates-digital-risk-unit-as-ai-reshapes-accumulation-586647.aspx",
    "ib_rebuild": "https://www.insurancebusinessmag.com/asia/news/life-insurance/why-global-insurers-are-rebuilding-their-life-insurance-books-586773.aspx",
    "ib_oona": "https://www.insurancebusinessmag.com/asia/news/mergers-acquisitions/oona-plays-buyer-in-sea-acquisitions--but-was-it-recently-for-sale-586903.aspx",
}
os.makedirs(".tmp/0821", exist_ok=True)
for name, u in urls.items():
    out = f".tmp/0821/{name}.html"
    r = subprocess.run(["curl", "-sL", "--max-time", "35", "-A", UA, u, "-o", out],
                       capture_output=True, text=True)
    size = os.path.getsize(out) if os.path.exists(out) else 0
    print(f"{name}: {size}")
