import subprocess, os

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0"
urls = {
    "air_96629_etf": "https://www.asiainsurancereview.com/News/View-NewsLetter-Article/id/96629/Type/eCin/Regulator-relaxes-rules-for-insurance-funds-oversea",
    "air_96628_health": "https://www.asiainsurancereview.com/News/View-NewsLetter-Article/id/96628/Type/eCin/China-s-new-5-year-healthcare-insurance-plan-target",
    "air_96627_pingan": "https://www.asiainsurancereview.com/News/View-NewsLetter-Article/id/96627/Type/eCin/Ping-An-posts-strong-1H2026-results-as-net-profit-s",
    "air_96605_reins": "https://www.asiainsurancereview.com/News/View-NewsLetter-Article/id/96605/Type/eDaily/Global-Reinsurance-capital-to-hit-new-record-US-7",
    "air_96609_kyrgyz": "https://www.asiainsurancereview.com/News/View-NewsLetter-Article/id/96609/Type/eDaily/Kyrgyzstan-Insurance-part-of-pensions-to-increase",
    "air_96603_actuaries": "https://www.asiainsurancereview.com/News/View-NewsLetter-Article/id/96603/Type/AirPlus/Asia-Actuaries-urged-to-master-new-tools-navigat",
    "air_96602_mas": "https://www.asiainsurancereview.com/News/View-NewsLetter-Article/id/96602/Type/AirPlus/MAS-boosts-Singapore-s-asset-management-competit",
    "air_96590_hnwi": "https://www.asiainsurancereview.com/News/View-NewsLetter-Article/id/96590/Type/AirPlus/Asia-s-HNWI-insurance-demand-presents-US-140bn-p",
}
os.makedirs(".tmp/0821", exist_ok=True)
for name, u in urls.items():
    out = f".tmp/0821/{name}.html"
    r = subprocess.run(["curl", "-sL", "--max-time", "35", "-A", UA, u, "-o", out], capture_output=True, text=True)
    size = os.path.getsize(out) if os.path.exists(out) else 0
    print(f"{name}: {size}")
