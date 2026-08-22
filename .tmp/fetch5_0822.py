#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fetch exact SunLife release pages and extract title/date/content."""
import subprocess, re, html

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
def fetch(url, out):
    try:
        r = subprocess.run(["curl", "-sL", "--max-time", "35", "-A", UA, url],
                           capture_output=True, text=True, timeout=45)
        raw = r.stdout
        open(out, "w").write(raw)
        return raw
    except Exception as e:
        print(f"ERR {e} {url}")
        return ""

def unq(s):
    return html.unescape(re.sub(r"\s+", " ", s or "")).strip()

URLS = [
    ("sl-pw", "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2026/sun-life-launches-private-wealth-integrated-platform/"),
    ("sl-mpf", "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2026/sun-life-mpf-nearly-20-of-mpf-members-adopt-concentrated-investment-strategies/"),
    ("sl-hsu", "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2026/sun-life-and-the-hang-seng-university-of-hong-kong-partner-to-nurture-the-next-generation-of-insurance-talent/"),
]
for tag, url in URLS:
    raw = fetch(url, f"data/_raw/t0822-{tag}.html")
    if not raw:
        continue
    print(f"\n===== {tag} ({len(raw)} bytes) =====")
    t = re.search(r"<title>(.*?)</title>", raw, re.S)
    print("TITLE:", unq(t.group(1)) if t else "")
    # look for h1
    for h in re.findall(r"<h1[^>]*>(.*?)</h1>", raw, re.S)[:3]:
        print("H1:", unq(h)[:120])
    # dates
    for pat in [r"(20\d\d[-/.]\d{1,2}[-/.]\d{1,2})", r"([A-Z][a-z]{2,8}\s+\d{1,2},?\s+20\d\d)", r"(\d{1,2}\s+[A-Z][a-z]{2,8},?\s+20\d\d)", r"(\d{4}年\d{1,2}月\d{1,2}日)"]:
        ms = re.findall(pat, raw)
        if ms:
            print(f"DATES[{pat[:20]}]:", ms[:8])
    body = re.sub(r"<script.*?</script>", " ", raw, flags=re.S)
    body = re.sub(r"<style.*?</style>", " ", body, flags=re.S)
    body = re.sub(r"<[^>]+>", " ", body)
    body = unq(body)
    # find content around the headline
    idx = body.find("永明")
    print("BODY:", body[:1200])
