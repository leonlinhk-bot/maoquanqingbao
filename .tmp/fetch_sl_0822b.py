#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, re, html, os

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def fetch(name, url, t=35):
    try:
        r = subprocess.run(["curl", "-sL", "--max-time", str(t), "-A", UA,
                            "-H", "Accept-Language: zh-TW,zh;q=0.9", url],
                           capture_output=True, text=True, timeout=50)
        raw = r.stdout
        open(f"data/_raw/t0822b/{name}.html", "w").write(raw)
        print(f"{'OK' if len(raw)>3000 else 'SMALL'} {len(raw):8d}  {name}")
        return raw
    except Exception as e:
        print(f"ERR {name} {e}")
        return ""

fetch("sl-mpf", "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2026/sun-life-mpf-nearly-20-of-mpf-members-adopt-concentrated-investm")
fetch("sl-hsu", "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2026/sun-life-and-the-hang-seng-university-of-hong-kong-partner-to-nu")
fetch("sl-free-ride", "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2026/free-ride-campaign/")
fetch("sl-135", "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2026/sun-life-deeply-cultivates-hong-kong-market-heading-towards-135-")
fetch("sl-pw2", "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2026/sun-life-launches-private-wealth-integrated-platform/")
fetch("sl-finlit", "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2026/sun-life-deepens-community-commitment-through-financial-literacy")
fetch("sl-col", "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2026/sun-life-survey-rising-cost-of-living-weighs-on-hong-kong-househ")
print("DONE")
