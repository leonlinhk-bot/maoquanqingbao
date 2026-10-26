import subprocess, re, html, json

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36"

def get(u, t=25):
    r = subprocess.run(["curl", "-m", str(t), "-sL", "-A", UA, u], capture_output=True, text=True, errors="replace")
    return r.stdout

def show(u, npara=14, plen=420):
    t = get(u)
    title = re.search(r"<title>(.*?)</title>", t, re.S)
    dp = re.findall(r'"datePublished"\s*:\s*"([^"]+)"', t)
    print("=" * 30)
    print(u, "| bytes", len(t))
    print("title:", html.unescape(title.group(1)).strip()[:130] if title else None, "| datePublished:", dp[:2])
    body = re.sub(r"<script.*?</script>|<style.*?</style>", " ", t, flags=re.S)
    paras = re.findall(r"<p[^>]*>(.*?)</p>", body, re.S)
    out = []
    for p in paras:
        x = html.unescape(re.sub(r"<[^>]+>", "", p)).strip()
        if len(x) > 60:
            out.append(x)
    for x in out[:npara]:
        print("  -", x[:plen])

for u in [
    "https://insuranceasia.com/insurance/news/3-in-10-uninsured-firms-dismiss-cyberattack-risks-globaldata",
    "https://insuranceasia.com/insurance/news/regulatory-risks-threaten-asian-insurers-growth-jefferies",
    "https://insuranceasia.com/insurance/news/ping-good-doctor-profit-rises-35-amidst-ai-healthcare-push",
]:
    show(u)
