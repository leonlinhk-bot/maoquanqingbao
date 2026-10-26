import subprocess, re, html

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36"

def get(u, t=25):
    r = subprocess.run(["curl", "-m", str(t), "-sL", "-A", UA, u], capture_output=True, text=True, errors="replace")
    return r.stdout

targets = {
    "prudential": "https://www.prudential.com.hk/tc/about-us/newsroom/",
    "scmp_ins": "https://www.scmp.com/rss/92/feed",
    "nfra": "https://www.nfra.gov.cn/cn/view/pages/index/index.html",
    "fstb": "https://www.fstb.gov.hk/en/",
    "hkfi": "https://www.hkfi.org.hk/en/media-centre/press-release/",
}
for k, u in targets.items():
    t = get(u)
    print("=" * 28, k, "bytes", len(t))
    dates = re.findall(r"(2026[-/年]\s?1[01][-/月]\s?\d{1,2})", t)
    print(" date tokens:", sorted(set(dates), reverse=True)[:10])
    txt = re.sub(r"<script.*?</script>|<style.*?</style>", " ", t, flags=re.S)
    anchors = re.findall(r"<a[^>]*>(.*?)</a>", txt, re.S)
    clean = []
    for a in anchors:
        x = html.unescape(re.sub(r"<[^>]+>", " ", a)).strip()
        x = re.sub(r"\s+", " ", x)
        if 12 < len(x) < 160:
            clean.append(x)
    print(" anchors:", len(clean))
    for x in clean[:18]:
        print("   ", x[:120])
