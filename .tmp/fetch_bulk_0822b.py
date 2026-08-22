#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bulk fetch for 2026-08-22 18:08 cron run. Window: since 2026-08-20T21:14+08:00."""
import subprocess, os, time

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
OUT = "data/_raw/t0822b"
os.makedirs(OUT, exist_ok=True)

def fetch(name, url, t=40, headers=None):
    cmd = ["curl", "-sL", "--max-time", str(t), "-A", UA]
    for k, v in (headers or {}).items():
        cmd += ["-H", f"{k}: {v}"]
    cmd.append(url)
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        raw = r.stdout
        if len(raw) < 500:
            print(f"SMALL {len(raw):8d}  {name}  {url}")
        else:
            open(f"{OUT}/{name}.html", "w").write(raw)
            print(f"OK  {len(raw):8d}  {name}  {url}")
        return raw
    except Exception as e:
        print(f"ERR {e}  {name}  {url}")
        return ""

fetch("ia-press", "https://www.ia.org.hk/en/infocenter/press_releases.html")
fetch("ia-circ2026", "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html")
fetch("hkma-press", "https://www.hkma.gov.hk/eng/news-and-media/press-releases/", headers={"Accept-Language": "en"})
fetch("iaa-rss", "https://insuranceasia.com/insurance/rss.xml")
fetch("ibmag", "https://www.insurancebusinessmag.com/asia/news/breaking-news/")
fetch("scmp", "https://www.scmp.com/topics/insurance")
fetch("nfra", "https://www.nfra.gov.cn/", headers={"Accept-Language": "zh-CN,zh;q=0.9"})
fetch("fstb", "https://www.fstb.gov.hk/en/", headers={"Accept-Language": "en"})
fetch("aia", "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/", headers={"Accept-Language": "zh-CN,zh;q=0.9"})
fetch("manulife", "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html", headers={"Accept-Language": "zh-CN,zh;q=0.9"})
fetch("prudential", "https://www.prudential.com.hk/tc/about-us/newsroom/", headers={"Accept-Language": "zh-TW,zh;q=0.9"})
fetch("axa", "https://www.axa.com.hk/zh/news-room/", headers={"Accept-Language": "zh-CN,zh;q=0.9"})
fetch("sunlife", "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/", headers={"Accept-Language": "zh-TW,zh;q=0.9"})
fetch("ia-insurtech", "https://www.ia.org.hk/en/aboutus/task_force/")
time.sleep(2)
print("DONE")
