import subprocess, re, html, json

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36"

def get(u):
    r = subprocess.run(["curl", "-m", "30", "-sL", "-A", UA, u], capture_output=True, text=True, errors="replace")
    return r.stdout

urls = [
    "https://insuranceasia.com/insurance/news/3-in-10-uninsured-firms-dismiss-cyberattack-risks-glob",
    "https://insuranceasia.com/insurance/news/regulatory-risks-threaten-asian-insurers-growth-jeffer",
    "https://insuranceasia.com/insurance/news/ping-good-doctor-profit-rises-35-amidst-ai-healthcare-",
    "https://insuranceasia.com/insurance/news/global-insured-catastrophe-losses-fall-92b-in-2026",
    "https://insuranceasianews.com/231651-2/",
]

for u in urls:
    t = get(u)
    title = re.search(r"<title>(.*?)</title>", t, re.S)
    # try to find date strings
    dates = re.findall(r'"datePublished"\s*:\s*"([^"]+)"', t)
    tds = re.findall(r'<time[^>]*>(.*?)</time>', t, re.S)
    print("=" * 30)
    print(u)
    print("title:", html.unescape(title.group(1)).strip()[:120] if title else None)
    print("datePublished:", dates[:3], "time:", [x.strip()[:40] for x in tds[:3]])
    body = re.sub(r"<script.*?</script>|<style.*?</style>", " ", t, flags=re.S)
    paras = re.findall(r"<p[^>]*>(.*?)</p>", body, re.S)
    clean = []
    for p in paras:
        x = html.unescape(re.sub(r"<[^>]+>", "", p)).strip()
        if len(x) > 40:
            clean.append(x)
    print("paras:", len(clean))
    for x in clean[:12]:
        print("  -", x[:400])
