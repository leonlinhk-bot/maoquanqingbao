#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Query HKEX titleSearchServlet for announcements, page through results, filter insurance cos."""
import json, subprocess, sys, html, os

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

def main():
    fromdate, todate = sys.argv[1], sys.argv[2]
    pages = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    out = []
    for page in range(1, pages + 1):
        url = ("https://www1.hkexnews.hk/search/titleSearchServlet.do?sortDir=0&sortByOptions=DateTime"
               "&category=0&market=SEHK&stockId=-1&documentType=-1"
               f"&fromDate={fromdate}&toDate={todate}&title=&searchType=1"
               f"&t1code=-2&t2Gcode=-2&t2code=-2&rowRange=100&page={page}&lang=EN")
        raw = fetch(url)
        try:
            data = json.loads(raw)
            rows = json.loads(data.get("result", "[]"))
        except Exception as e:
            print(f"page {page} parse fail: {e}", file=sys.stderr)
            continue
        if not rows:
            break
        out.extend(rows)
    print(f"TOTAL fetched: {len(out)}")
    with open("/tmp/hkex_rows.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False)
    for r in out:
        print(f"[{r.get('DATE_TIME','')}] {r.get('STOCK_NAME','')} | {html.unescape(r.get('TITLE',''))[:80]}")

if __name__ == "__main__":
    main()
