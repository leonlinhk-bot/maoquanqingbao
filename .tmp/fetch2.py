import subprocess, re, html

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def fetch(url):
    return subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA, url],
                          capture_output=True, text=True).stdout

def clean(raw):
    raw = re.sub(r"<script.*?</script>|<style.*?</style>", " ", raw, flags=re.S)
    raw = re.sub(r"<[^>]+>", " ", raw)
    return re.sub(r"\s+", " ", html.unescape(raw)).strip()

# Chubb article
raw = fetch("https://insuranceasia.com/insurance/news/chubb-life-hong-kong-launches-health-plan-covers-146-conditions")
txt = clean(raw)
print("=== CHUBB ===")
print(txt[800:1900])
print()

# IB article
raw = fetch("https://www.insurancebusinessmag.com/asia/news/life-insurance/mainland-insurers-gain-etf-access-retail-traders-just-lost-587035.aspx")
txt = clean(raw)
print("=== IB ETF ===")
print(txt[500:1800])
print()

# SCMP grep
raw3 = fetch("https://www.scmp.com/topics/insurance")
print("=== SCMP matches ===")
for m in re.finditer(r'href="(https://www\.scmp\.com[^"]*)"[^>]*>([^<]{10,120})<', raw3):
    t = html.unescape(m.group(2)).strip()
    if "Ping" in t or "ETF" in t or "insurance" in t.lower() and "topics" not in m.group(1):
        print("-", t[:100], "|", m.group(1)[:110])
i = raw3.find("Ping An eyes")
print("idx:", i)
if i > 0:
    print(raw3[i-300:i+300])
