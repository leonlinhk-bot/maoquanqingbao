import subprocess, re, html, json

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def fetch(url):
    return subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA, url],
                          capture_output=True, text=True).stdout

def resolve(url):
    return subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA, "-o", "/dev/null", "-w", "%{url_effective}", url],
                          capture_output=True, text=True).stdout

def clean_text(raw):
    raw = re.sub(r"<script.*?</script>|<style.*?</style>", " ", raw, flags=re.S)
    raw = re.sub(r"<[^>]+>", " ", raw)
    raw = html.unescape(raw)
    raw = re.sub(r"\s+", " ", raw)
    return raw.strip()

URLS = {
    "ia_week": "https://insuranceasia.com/insurance/news/week-in-insurance-new-products-launch-insurers-expand-aia-and-ping-profits-surge",
    "ia_aia": "https://insuranceasia.com/insurance/news/aia-profit-surges-692-43b-in-h1-2026",
    "ia_offshore": "https://insuranceasia.com/insurance/news/offshore-reinsurance-expands-despite-slower-annuity-growth",
}
out = {}
for k, u in URLS.items():
    raw = fetch(u)
    t = re.search(r'<meta property="og:title" content="([^"]+)"', raw)
    d = re.search(r'<meta property="og:description" content="([^"]+)"', raw)
    txt = clean_text(raw)
    out[k] = {"url": u, "title": html.unescape(t.group(1)) if t else "",
              "desc": html.unescape(d.group(1)) if d else "", "text": txt[:2500]}
    print("=" * 30, k)
    print("TITLE:", out[k]["title"])
    print("DESC:", out[k]["desc"][:300])
    # find body snippet
    m = re.search(r"(HONG KONG|Hong Kong|Singapore|The insurer|AIA|Prudential|reinsur)", txt[500:])
    print("SNIPPET:", txt[500:1600])

# resolve gnews redirects
G = {
    "scmp_pingan": "https://news.google.com/rss/articles/CBMi3wFBVV95cUxPcUI4emlxMmpxVHR2aDBTelFudC1CTkZYVnhIQktKUzJmNmllRjhFMUpRelF2Mi1KZFBWSEFxamNPQjYtTUpDTEdYc01RVVlvX2F5UDFraUVEUnNyRjR6anlaRk9HcG1ibHVJMzk3V1dJb3Rsb2lEZkQ5dENMODBjbUdRNU1JQ0FXeVpOa2xpRWtLRVo3RDY0TXM2NmxDNUVKOHFRUmFuT0lSWW5OcEFQd0VlS3Q3a0QyblB4ZVlabWNvS3dTaVgyT0FNaE1JbktpZkhOc0o2Y2dRMHdmZG1J0gHfAUFVX3lxTE9xQjh6aXEyanFUdHZoMFN6UW50LUJORlhWeEhCS0pTMmY2aWVGOEUxSlF6UXYyLUpkUFZIQXFqY09CNi1NSkNMR1hzTVFVWW9fYXlQMWtpRURSc3JGNHpqeVpGT0dwbWJsdUkzOTdXV0lvdGxvaURmRDl0Q0w4MGNtR1E1TUlDQVd5Wk5rbGlFa0tFWjdENjRNczY2bEM1RUo4cVFSYW5PSVJZbk5wQVB3RWVLdDdrRDJuUHhlWVptY29Ld1NpWDJPQU1oTUluS2lmSE5zSjZjZ1Ewd2ZkbUk?oc=5",
    "ib_mainland": "https://news.google.com/rss/articles/CBMizAFBVV95cUxOTXZablUxVHEyQm5JYzdrME5qVEFnWXFUNkJFLUVpSXEyVGUxdXRVVW4xN29nZkhaUUI5XzNJLWVMRGpaYlpyeC1xdlhZMzdZY1o5dkpZYWtZaThFUDFzZ3lSUHdxRkJuMUprc0xHeXpQYUFLdXFLU2VWMmFLS2ZOM0REM3YwUkp1bUNZNmp1WDlpcndUTkFnLTYxVFdDcHJaZGRIbnhaREVQRGV2QmNUQTBkVkh2VVIxc01DaVVwcDY3Y2pMdUtXNFY0Z2k?oc=5",
    "ia_people": "https://news.google.com/rss/articles/CBMirAFBVV95cUxNRm5hQVR4d2dBRm9OSG9Wd0V0N2FyY0RaMnZXZjdacnBRNWRwRDV3VV9GNm9IYUxpZkhFZnc2QWt2b1IycWZhQVBQSFBmek51QWZ3Yi03OGwwUEtQeE5fTWtTTnIxUlVNdThOejlRSG5rRDJBWjJGajRQYWkzSXN4ZGkwS1ZURXBDQkV6azJEUUlsOW9QNHBWMHdYSy01aHQxTnAxQWlhbi1JNDRE?oc=5",
    "crntt_aia": "http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6a894820906641e99f5437cf4046ea70&url=https%3a%2f%2fhk.crntt.com%2fdoc%2f7_0_107226380_1_0822004037.html&c=4422871644085858039&mkt=en-us",
}
out["resolved"] = {}
for k, u in G.items():
    try:
        real = resolve(u)
        out["resolved"][k] = real
        print("RESOLVED", k, "->", real[:120])
    except Exception as e:
        print("RESOLVE FAIL", k, e)

json.dump(out, open(".tmp/articles.json", "w"), ensure_ascii=False, indent=1)
