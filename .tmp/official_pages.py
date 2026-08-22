import subprocess, re, html

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def fetch(url):
    return subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA, url],
                          capture_output=True, text=True).stdout

def clean(raw):
    raw = re.sub(r"<script.*?</script>|<style.*?</style>", " ", raw, flags=re.S)
    raw = re.sub(r"<[^>]+>", " ", raw)
    return re.sub(r"\s+", " ", html.unescape(raw)).strip()

# SCMP anchor extraction
raw = fetch("https://www.scmp.com/topics/insurance")
i = raw.find("Ping An eyes Hong Kong ETFs")
seg = raw[max(0, i-8000):i+200]
# find the nearest <a ...> before the headline
anchors = [(m.start(), m.group(1)) for m in re.finditer(r'<a[^>]+href="(https://www\.scmp\.com[^"]+)"[^>]*>', seg)]
if anchors:
    print("SCMP URL:", anchors[-1][1][:140])
else:
    # maybe the link wraps the headline after it
    after = raw[i:i+3000]
    for m in re.finditer(r'href="(https://www\.scmp\.com[^"]+)"', after):
        u = m.group(1)
        if "topics" not in u:
            print("SCMP URL(after):", u[:140])
            break

# Prudential HK newsroom
raw = fetch("https://www.prudential.com.hk/en/about-us/newsroom/")
txt = clean(raw)
print("\n=== PRU newsroom (len %d) ===" % len(txt))
print(txt[:1800])

# AXA HK newsroom
raw = fetch("https://www.axa.com.hk/en/news-room")
txt = clean(raw)
print("\n=== AXA newsroom (len %d) ===" % len(txt))
print(txt[:1500])

# NFRA main page
raw = fetch("https://www.nfra.gov.cn/")
txt = clean(raw)
print("\n=== NFRA (len %d) ===" % len(txt))
print(txt[:1500])
