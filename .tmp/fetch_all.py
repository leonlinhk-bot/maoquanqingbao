import subprocess, urllib.parse, os, time, json

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fetch')

def fetch(url, name, timeout=30):
    try:
        r = subprocess.run(["curl", "-sL", "--compressed", "--max-time", str(timeout), "-A", UA, url],
                           capture_output=True, text=True, timeout=timeout+10)
        raw = r.stdout
        open(os.path.join(OUT, name), 'w', encoding='utf-8').write(raw)
        print(f"[OK] {name} {len(raw)}b  {url[:90]}")
        return raw
    except Exception as e:
        print(f"[ERR] {name} {e}  {url[:90]}")
        return ""

os.makedirs(OUT, exist_ok=True)

# 1. Official HK feeds
fetch("https://www.ia.org.hk/en/infocenter/press_releases.html", "ia_press.html")
fetch("https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters.html", "ia_circular.html")
fetch("https://www.hkma.gov.hk/eng/news-and-media/press-releases/", "hkma.html")
fetch("https://insuranceasia.com/insurance/rss.xml", "ia-rss.xml")
fetch("https://www.scmp.com/rss/91/feed", "scmp-rss.xml")
fetch("https://www.nfra.gov.cn/", "nfra.html")
fetch("https://www.fstb.gov.hk/en/", "fstb.html")

# 2. Google News RSS (date-filtered searches, zh + en)
gq = {
  "g_hkins": "香港保險 when:2d",
  "g_ia": "保監局 when:2d",
  "g_hkma": "金管局 when:2d",
  "g_aia": "友邦 when:2d",
  "g_manulife": "宏利 when:2d",
  "g_prudential": "保誠 when:2d",
  "g_axa": "安盛 when:2d",
  "g_sunlife": "永明 when:2d",
  "g_nfra": "金融監管總局 when:2d",
  "g_family": "家族辦公室 when:2d",
  "g_insurtech": "保險科技 when:2d",
  "g_en_hkins": "Hong Kong insurance when:2d",
  "g_en_ia": "Insurance Authority Hong Kong when:2d",
  "g_en_manulife": "Manulife Hong Kong when:2d",
  "g_en_prudential": "Prudential Hong Kong when:2d",
  "g_en_axa": "AXA Hong Kong when:2d",
  "g_en_sunlife": "Sun Life Hong Kong when:2d",
  "g_en_aia": "AIA Hong Kong when:2d",
}
for name, q in gq.items():
    url = "https://news.google.com/rss/search?q=" + urllib.parse.quote(q) + "&hl=zh-HK&gl=HK&ceid=HK:zh-Hant"
    fetch(url, name + ".xml", timeout=20)
    time.sleep(0.4)

print("DONE")
