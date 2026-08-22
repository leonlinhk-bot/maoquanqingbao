#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, re, html

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def fetch(name, url, t=35):
    try:
        r = subprocess.run(["curl", "-sL", "--max-time", str(t), "-A", UA,
                            "-H", "Accept-Language: zh-TW,zh;q=0.9", url],
                           capture_output=True, text=True, timeout=50)
        raw = r.stdout
        open(f"data/_raw/t0822b/{name}.html", "w").write(raw)
        tm = re.search(r"<title>(.*?)</title>", raw, flags=re.S)
        dates = set()
        for pat in [r"(\d{4}年\d{1,2}月\d{1,2}日)", r"(\d{4}-\d{2}-\d{2}T\d{2}:\d{2})", r'"(datePublished|publishedAt)"\s*:\s*"([^"]+)"']:
            for m in re.finditer(pat, raw):
                dates.add(m.group(1) if m.lastindex == 1 else m.group(2))
        print(f"{'OK' if len(raw)>3000 else 'SMALL'} {len(raw):8d} {name} | {html.unescape(re.sub(chr(10),' ',tm.group(1) if tm else '?'))[:60]} | dates={sorted(dates)[:5]}")
    except Exception as e:
        print(f"ERR {name} {e}")

fetch("sl-mpf2", "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2026/sun-life-mpf-nearly-20-of-mpf-members-adopt-concentrated-investment-strategies/")
fetch("sl-hsu2", "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2026/sun-life-and-the-hang-seng-university-of-hong-kong-partner-to-nurture-the-next-generation-of-insurance-talent/")
fetch("sl-135b", "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2026/sun-life-deeply-cultivates-hong-kong-market-heading-towards-135-years-customer-needs-drive-development/")
fetch("sl-finlit2", "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2026/sun-life-deepens-community-commitment-through-financial-literacy-programme-to-empower-families/")
fetch("sl-col2", "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2026/sun-life-survey-rising-cost-of-living-weighs-on-hong-kong-households-weakening-financial-resilience/")
fetch("sl-bbawards", "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2026/sun-life-celebrates-18-wins-at-the-bloomberg-businessweek-award/")
print("DONE")
