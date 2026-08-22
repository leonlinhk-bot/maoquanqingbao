#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check HKEX pagination: fetch page 1 and page 2, compare first rows; print distinct date coverage."""
import json, subprocess, os, sys

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def _env():
    e = os.environ.copy()
    for k in list(e):
        if "proxy" in k.lower():
            del e[k]
    return e

def fetch(url):
    r = subprocess.run(["curl", "-s", "-m", "30", "-L", "-A", UA, url],
                       capture_output=True, text=True, env=_env())
    return r.stdout

base = ("https://www1.hkexnews.hk/search/titleSearchServlet.do?sortDir=0&sortByOptions=DateTime"
        "&category=0&market=SEHK&stockId=-1&documentType=-1"
        "&fromDate=20260820&toDate=20260821&title=&searchType=1"
        "&t1code=-2&t2Gcode=-2&t2code=-2&rowRange=100&lang=EN")

for page in [1, 2, 11]:
    raw = fetch(base + f"&page={page}")
    try:
        rows = json.loads(json.loads(raw)["result"])
    except Exception as e:
        print(f"page {page}: FAIL {e}")
        continue
    print(f"page {page}: {len(rows)} rows; first: {rows[0]['DATE_TIME']} {rows[0]['STOCK_NAME']} {rows[0]['TITLE'][:40]}; last: {rows[-1]['DATE_TIME']} {rows[-1]['STOCK_NAME']}")
    news_ids = [r["NEWS_ID"] for r in rows]
    if page == 1:
        p1 = set(news_ids)
    else:
        print(f"  overlap with page1: {len(p1 & set(news_ids))} of {len(news_ids)}")
