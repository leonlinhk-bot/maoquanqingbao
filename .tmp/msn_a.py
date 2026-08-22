import subprocess, re, html

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def fetch(url):
    return subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA, url],
                          capture_output=True, text=True).stdout

raw = fetch("https://www.msn.com/en-xl/money/investment/chinese-insurer-ping-an-eyes-hong-kong-etfs-as-beijing-greenlights-cross-border-investment/ar-AA2aEauA")
print("len:", len(raw))
# canonical / original link
for m in re.finditer(r'<link rel="canonical" href="([^"]+)"', raw):
    print("CANONICAL:", m.group(1))
for m in re.finditer(r'href="(https://www\.scmp\.com[^"]+)"', raw):
    print("SCMP link:", m.group(1)[:150])
# title + article body
t = re.search(r'<meta property="og:title" content="([^"]+)"', raw)
print("OG TITLE:", html.unescape(t.group(1)) if t else "")
d = re.search(r'<meta property="og:description" content="([^"]+)"', raw)
print("OG DESC:", html.unescape(d.group(1))[:300] if d else "")
body = re.sub(r"<script.*?</script>|<style.*?</style>", " ", raw, flags=re.S)
body = re.sub(r"<[^>]+>", " ", body)
body = re.sub(r"\s+", " ", html.unescape(body))
i = body.find("Ping An")
print("BODY:", body[max(0, i-200):i+2200])
