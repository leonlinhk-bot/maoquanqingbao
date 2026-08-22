import subprocess, os

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
urls = {
    "aia": "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/",
    "manulife": "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html",
    "prudential": "https://www.prudential.com.hk/tc/about-us/newsroom/",
    "axa": "https://www.axa.com.hk/zh/news-room/",
    "sunlife": "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/",
    "ibmag": "https://www.insurancebusinessmag.com/asia/news/breaking-news/",
    "scmp": "https://www.scmp.com/topics/insurance",
    "iaasia_home": "https://insuranceasia.com/insurance",
    "fstb": "https://www.fstb.gov.hk/en/",
}
os.makedirs(".tmp/0821", exist_ok=True)
for name, u in urls.items():
    out = f".tmp/0821/{name}.html"
    r = subprocess.run(["curl", "-sL", "--max-time", "35", "-A", UA, u, "-o", out],
                       capture_output=True, text=True)
    size = os.path.getsize(out) if os.path.exists(out) else 0
    print(f"{name}: {size} bytes")
