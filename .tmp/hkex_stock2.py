#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Query HKEX announcements for additional insurers."""
import json, subprocess, os, sys, html, time

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

def resolve(ticker):
    url = f"https://www1.hkexnews.hk/search/prefix.do?callback=cb&lang=EN&type=A&name={ticker}&market=SEHK"
    raw = fetch(url)
    m = raw[raw.find("(") + 1: raw.rfind(")")] if "(" in raw and raw.rfind(")") > raw.find("(") else raw
    try:
        data = json.loads(m)
        for it in data.get("stockInfo", []):
            if it.get("code") == "0" + ticker or it.get("code") == ticker:
                return it.get("stockId")
    except Exception:
        return None
    return None

TICKERS = ["1339", "2328", "2601", "0966", "6060", "6963", "1508", "1336"]

def main():
    fromdate, todate = sys.argv[1], sys.argv[2]
    for tk in TICKERS:
        sid = resolve(tk)
        if not sid:
            print(f"--- {tk}: no stockId")
            continue
        url = ("https://www1.hkexnews.hk/search/titleSearchServlet.do?sortDir=0&sortByOptions=DateTime"
               "&category=0&market=SEHK"
               f"&stockId={sid}&documentType=-1&fromDate={fromdate}&toDate={todate}"
               "&title=&searchType=1&t1code=-2&t2Gcode=-2&t2code=-2&rowRange=100&lang=EN")
        raw = fetch(url)
        try:
            rows = json.loads(json.loads(raw)["result"])
        except Exception as e:
            print(f"--- {tk}: query fail {e}")
            time.sleep(0.3)
            continue
        print(f"=== {tk} (stockId {sid}): {len(rows)} ===")
        for r in rows:
            print(f"  [{r.get('DATE_TIME','')}] {html.unescape(r.get('TITLE',''))[:90]} | {r.get('FILE_TYPE','')}")
        time.sleep(0.3)

if __name__ == "__main__":
    main()
