import subprocess, re, html

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def fetch(url):
    return subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA, url],
                          capture_output=True, text=True).stdout

# SCMP: find URL near headline
raw = fetch("https://www.scmp.com/topics/insurance")
i = raw.find("Ping An eyes Hong Kong ETFs")
print("SCMP idx:", i)
seg = raw[max(0, i-3000):i+500]
for m in re.finditer(r'href="(https://www\.scmp\.com[^"]+)"', seg):
    u = m.group(1)
    if "topics" not in u and "css" not in u:
        print("URL candidate:", u[:130])
# summary
j = raw.find("Component-Summary", i)
if j > 0:
    s = raw[j:j+900]
    s2 = re.sub(r"<[^>]+>", " ", s)
    print("SUMMARY:", re.sub(r"\s+", " ", html.unescape(s2))[:400])

# insurer official pages reachability
for u in ["https://www.aia.com.hk/en/about-aia/media-centre/press-releases",
          "https://www.manulife.com.hk/en/individual/about/newsroom.html",
          "https://www.prudential.com.hk/en/about-us/newsroom/",
          "https://www.axa.com.hk/en/news-room",
          "https://www.nfra.gov.cn/"]:
    code = subprocess.run(["curl", "-sL", "--max-time", "20", "-o", "/dev/null", "-w", "%{http_code}", "-A", UA, u],
                          capture_output=True, text=True).stdout
    print(code, u)
