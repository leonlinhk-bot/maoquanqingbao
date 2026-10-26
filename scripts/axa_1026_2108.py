import re, subprocess, html
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36"

def get(url, t=25):
    r = subprocess.run(["curl", "-m", str(t), "-sL", "-A", UA, url], capture_output=True, text=True, errors="replace")
    return r.stdout

h = get("https://www.axa.com.hk/zh/news-room/")
txt = re.sub(r"<script.*?</script>", " ", h, flags=re.S)
txt = re.sub(r"<style.*?</style>", " ", txt, flags=re.S)
txt = re.sub(r"<[^>]+>", "\n", txt)
lines = [l.strip() for l in txt.split("\n") if l.strip()]
print("AXA lines", len(lines))
for i, l in enumerate(lines[:120]):
    print(i, l[:120])
