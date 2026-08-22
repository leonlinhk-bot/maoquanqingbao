import subprocess, re, html, json, urllib.parse, datetime

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
TZ8 = datetime.timezone(datetime.timedelta(hours=8))
UTC = datetime.timezone.utc
LAST = datetime.datetime(2026, 8, 20, 21, 14, 53, tzinfo=TZ8)

def fetch(url):
    return subprocess.run(["curl", "-sL", "--max-time", "25", "-A", UA, url],
                          capture_output=True, text=True).stdout

def parse_pubdate(s):
    if not s:
        return None
    for fmt in ("%a, %d %b %Y %H:%M:%S %Z", "%a, %d %b %Y %H:%M:%S %z", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%SZ"):
        try:
            dt = datetime.datetime.strptime(s.strip(), fmt)
            return dt.replace(tzinfo=UTC) if dt.tzinfo is None else dt
        except Exception:
            continue
    return None

def bing_rss(q):
    url = f"https://www.bing.com/news/search?q={urllib.parse.quote(q)}&format=rss&setlang=en"
    out = []
    for it in re.findall(r"<item>(.*?)</item>", fetch(url), re.S):
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        l = re.search(r"<link>(.*?)</link>", it, re.S)
        d = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
        out.append({"title": html.unescape(t.group(1)) if t else "",
                    "link": html.unescape(l.group(1)) if l else "",
                    "dt": parse_pubdate(d.group(1)) if d else None})
    return out

def gnews(q, hl="en", gl="HK"):
    url = f"https://news.google.com/rss/search?q={urllib.parse.quote(q)}&hl={hl}&gl={gl}&ceid={gl}:{hl}"
    out = []
    for it in re.findall(r"<item>(.*?)</item>", fetch(url), re.S):
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        l = re.search(r"<link>(.*?)</link>", it, re.S)
        d = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
        s = re.search(r"<source[^>]*>(.*?)</source>", it, re.S)
        out.append({"title": html.unescape(t.group(1)) if t else "",
                    "link": html.unescape(l.group(1)) if l else "",
                    "dt": parse_pubdate(d.group(1)) if d else None,
                    "source": html.unescape(s.group(1)) if s else ""})
    return out

QUERIES = [
    ("bing", "AXA Hong Kong insurance 2026"),
    ("bing", "Sun Life Hong Kong 2026"),
    ("bing", "FWD Insurance Hong Kong"),
    ("bing", "宏利 香港 2026年8月"),
    ("bing", "保誠 香港 2026"),
    ("bing", "安盛 香港 保險"),
    ("bing", "香港保險 新產品"),
    ("bing", "国家金融监督管理总局 通知 2026年8月"),
    ("bing", "香港 家族辦公室 2026"),
    ("bing", "香港 保險科技 2026"),
    ("bing", "HSBC Life Hong Kong"),
    ("bing", "BOC Life Hong Kong"),
    ("bing", "Hong Kong insurance authority August 21"),
    ("gnews", "Hong Kong insurance industry news"),
    ("gnews", "AIA 友邦 中报 2026"),
    ("gnews", "宏利 友邦 保誠 業績 2026"),
    ("gnews", "香港 保险 新闻"),
]
allres = {}
for eng, q in QUERIES:
    try:
        res = bing_rss(q) if eng == "bing" else gnews(q)
    except Exception as e:
        print("ERR", q, e)
        continue
    fresh = [r for r in res if r["dt"] and r["dt"].astimezone(TZ8) >= LAST]
    allres[q] = fresh
    print(f"=== {eng}:{q} -> {len(fresh)} fresh ===")
    for r in fresh[:8]:
        print("-", r["dt"].astimezone(TZ8).strftime("%m-%d %H:%M"), "|", r.get("source", "")[:14], "|", r["title"][:80])

json.dump(allres, open(".tmp/extra-cands.json", "w"), ensure_ascii=False, indent=1, default=str)
