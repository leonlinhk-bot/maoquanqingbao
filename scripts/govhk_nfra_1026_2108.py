import re, subprocess
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36"

def get(url, t=25):
    r = subprocess.run(["curl", "-m", str(t), "-sL", "-A", UA, url], capture_output=True, text=True, errors="replace")
    return r.stdout

h = get("https://www.info.gov.hk/gia/general/202610/26/P2026102600464.htm")
body = re.sub(r"<script.*?</script>", " ", h, flags=re.S)
body = re.sub(r"<[^>]+>", "\n", body)
lines = [l.strip() for l in body.split("\n") if l.strip()]
print("=== GOVHK fintech meeting ===")
for l in lines[:40]:
    print(l[:160])

print("\n=== NFRA ===")
n = get("https://www.nfra.gov.cn/cn/view/pages/ItemList.html?itemPId=923&itemId=915&itemUrl=ItemListRightList.html&itemName=监管动态", 30)
print("bytes", len(n))
txt = re.sub(r"<script.*?</script>", " ", n, flags=re.S)
for m in re.findall(r"(20\d\d-\d\d-\d\d)[^<]{0,3}<[^>]*>([^<]{6,90})", txt)[:15]:
    print(m[0], "|", m[1].strip())
print(n[:300])
