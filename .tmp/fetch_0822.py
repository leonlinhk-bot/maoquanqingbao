#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-08-22 18:08 collection: batch fetch all sources via curl."""
import subprocess, os, time

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
os.makedirs("data/_raw", exist_ok=True)

TARGETS = [
    ("ia-press", "https://www.ia.org.hk/en/infocenter/press_releases.html"),
    ("ia-circ", "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters.html"),
    ("hkma", "https://www.hkma.gov.hk/eng/news-and-media/press-releases/"),
    ("iaa-rss", "https://insuranceasia.com/rss.xml"),
    ("iaa-rss2", "https://insuranceasia.com/insurance/rss.xml"),
    ("aia", "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases.html"),
    ("manulife", "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html"),
    ("prudential", "https://www.prudential.com.hk/tc/about-us/newsroom/"),
    ("axa", "https://www.axa.com.hk/zh/news-room/"),
    ("sunlife", "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/"),
    ("ibmag", "https://www.insurancebusinessmag.com/asia/news/breaking-news/"),
    ("scmp", "https://www.scmp.com/topics/insurance"),
    ("nfra", "https://www.nfra.gov.cn/"),
    ("fstb", "https://www.fstb.gov.hk/en/"),
    ("ia-insurtech", "https://www.ia.org.hk/en/aboutus/task_force/"),
]

for tag, url in TARGETS:
    out = f"data/_raw/t0822-{tag}.html"
    try:
        r = subprocess.run(["curl", "-sL", "--max-time", "35", "-A", UA, url],
                           capture_output=True, text=True, timeout=45)
        raw = r.stdout
        with open(out, "w") as f:
            f.write(raw)
        print(f"OK  {tag:12s} {len(raw):8d} bytes  {out}")
    except Exception as e:
        print(f"ERR {tag:12s} {e}")
    time.sleep(1)
