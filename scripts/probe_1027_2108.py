#!/usr/bin/env python3
"""Probe RSS/list sources for anything newer than 2026-10-27T18:10."""
import re, sys, time
import urllib.request, urllib.error

CUT = "2026-10-27T18:10:44+08:00"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"}

FEEDS = {
 "insurance_asia": "https://insuranceasia.com/insurance/rss.xml",
 "insuranceasianews": "https://insuranceasianews.com/wp-json/wp/v2/posts?per_page=8",
 "hkma_press": "https://www.hkma.gov.hk/eng/news-and-media/press-releases/",
 "ibm": "https://www.insurancebusinessmag.com/asia/news/breaking-news/",
 "scmp_rss": "https://www.scmp.com/rss/92/feed",
 "govhk": "https://www.info.gov.hk/gia/rss/general_zh.xml",
 "hkfi": "https://www.hkfi.org.hk/en/media-centre/press-release",
 "artemis": "https://www.artemis.bm/news/",
 "ia_press": "https://www.ia.org.hk/en/infocenter/press_releases.html",
 "ia_circular": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html",
 "aia": "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/",
 "manulife": "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html",
 "prudential": "https://www.prudential.com.hk/tc/about-us/newsroom/",
 "axa": "https://www.axa.com.hk/zh/news-room/",
 "sunlife": "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/",
}

def get(url, timeout=25):
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read()
            return r.status, raw.decode("utf-8", "ignore")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:
        return -1, str(e)[:120]

for name, url in FEEDS.items():
    st, body = get(url)
    print(f"\n=== {name} [{st}] len={len(body)}")
    if st != 200:
        print("   ", body[:120])
        continue
    # pull dates
    dates = re.findall(r"(2026-10-\d{2}[T ]\d{2}:\d{2}[:0-9]*\+?0?8?:?0?0?)", body)
    dates += re.findall(r"(\d{1,2}\s+(?:Oct|October|October)\s+2026)", body)
    dates += re.findall(r"(2026年10月\d{1,2}日)", body)
    from collections import Counter
    c = Counter(dates)
    print("   date-hits:", list(c.most_common(8)))
    # a few titles
    ts = re.findall(r"<title><!\[CDATA\[(.{5,120}?)\]\]></title>", body) or re.findall(r"<title>(.{5,120}?)</title>", body)
    print("   titles:", [t for t in ts[:6]])
