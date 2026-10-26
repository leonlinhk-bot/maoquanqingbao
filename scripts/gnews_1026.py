import subprocess, re, html, urllib.parse
import xml.etree.ElementTree as ET

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36"

def get(u, t=25):
    return subprocess.run(["curl", "-m", str(t), "-sL", "-A", UA, u], capture_output=True, text=True, errors="replace").stdout

# 1) Goldman body
u = "https://www.scmp.com/business/china-business/article/3372055/goldman-sachs-steps-asia-hiring-wealthy-clients-eye-us-assets-diversification"
t = get(u)
dp = re.findall(r'"datePublished"\s*:\s*"([^"]+)"', t)
print("== GOLDMAN bytes", len(t), "date", dp[:2])
body = re.sub(r"<script.*?</script>|<style.*?</style>", " ", t, flags=re.S)
paras = [html.unescape(re.sub(r"<[^>]+>", "", p)).strip() for p in re.findall(r"<p[^>]*>(.*?)</p>", body, re.S)]
for p in [x for x in paras if len(x) > 70][:12]:
    print("  -", p[:450])

# 2) Google News RSS queries for HK insurance news
queries = [
    "香港 保险 保监局",
    "香港保险 内地客户",
    "Hong Kong insurance regulator",
    "香港 保险业 新造保单",
]
for q in queries:
    url = "https://news.google.com/rss/search?q=" + urllib.parse.quote(q) + "&hl=zh-HK&gl=HK&ceid=HK:zh-Hant"
    x = get(url)
    print("=" * 25, q, "bytes", len(x))
    try:
        root = ET.fromstring(x.encode("utf-8", "replace"))
    except Exception as e:
        print(" parse err", e)
        continue
    n = 0
    for it in root.iter():
        if it.tag.split("}")[-1] != "item":
            continue
        title = link = date = ""
        for ch in it:
            nm = ch.tag.split("}")[-1]
            if nm == "title":
                title = (ch.text or "").strip()
            elif nm == "link":
                link = (ch.text or "").strip()
            elif nm == "pubDate":
                date = (ch.text or "").strip()
        if "25 Oct 2026" in date or "26 Oct 2026" in date:
            print("  *", date[:22], "|", html.unescape(title)[:90])
            n += 1
    print("  fresh items:", n)
