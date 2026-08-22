import subprocess, re, html, json

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def fetch(url):
    return subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA, url],
                          capture_output=True, text=True).stdout

# 1. Full ia_week article: find Chubb link + other product links
raw = fetch("https://insuranceasia.com/insurance/news/week-in-insurance-new-products-launch-insurers-expand-aia-and-ping-profits-surge")
print("ia_week len:", len(raw))
for m in re.finditer(r'href="(https://insuranceasia\.com[^"]+)"[^>]*>([^<]{10,90})<', raw):
    txt = html.unescape(m.group(2)).strip()
    if any(k in txt.lower() for k in ["chubb", "product", "launch", "critical", "new", "aia", "ping", "prudential", "hong kong"]):
        print("-", txt[:80], "|", m.group(1))

# 2. InsuranceBusiness breaking news page
raw2 = fetch("https://www.insurancebusinessmag.com/asia/news/breaking-news/")
print("\nIB page len:", len(raw2))
for m in re.finditer(r'href="([^"]+)"[^>]*>([^<]{15,100})<', raw2):
    txt = html.unescape(m.group(2)).strip()
    if "ETF" in txt or "Mainland insurers" in txt:
        print("-", txt[:80], "|", m.group(1))

# 3. SCMP insurance topic page
raw3 = fetch("https://www.scmp.com/topics/insurance")
print("\nSCMP len:", len(raw3))
for m in re.finditer(r'href="(https://www\.scmp\.com[^"]+)"[^>]*>([^<]{15,100})<', raw3):
    txt = html.unescape(m.group(2)).strip()
    if "Ping An" in txt or "ETF" in txt:
        print("-", txt[:90], "|", m.group(1))
