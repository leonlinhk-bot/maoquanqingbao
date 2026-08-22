#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pass 15: follow Google News redirect chain to canonical URLs."""
import re, html, subprocess, urllib.parse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def follow(url):
    try:
        r = subprocess.run(["curl", "-sL", "--max-time", "35", "-A", UA, "-w", "\\nFINAL_URL:%{url_effective}", url],
                           capture_output=True, text=True, timeout=45)
        return r.stdout
    except Exception as e:
        return f"ERR {e}"

urls = {
    "hengda_wenweipo": "https://news.google.com/articles/CBMid0FVX3lxTE1yV014cDJiUndJLUhTSnJOMTJ6Tnh1Z3VyOTdLVU1ZRlQ2emRWZEFZT2xhbzUxcFdrcHo?hl=zh-HK&gl=HK&ceid=HK:zh-HK",
    "hengda_dianxin": "https://news.google.com/articles/CBMiekFVX3lxTE1aNHBwc3pCS0ZnenlQUm5feVpjN1BBUERqejBGYlhxM1o1anJGeWI4OFZqdjlUWDBjMlp?hl=zh-HK&gl=HK&ceid=HK:zh-HK",
    "aia_tax_hkej": "https://news.google.com/articles/CBMitwJBVV95cUxPZlJCQ2ZhQ0FBT2xQdnUyNTBYaEJQRW56cGZIMjRCMXJFcTRVenpjNi15bXFnNmItTVlSYzZkeC00MER1dDltNm5ZdVlncVdQc?hl=zh-HK&gl=HK&ceid=HK:zh-HK",
    "ubs_aia": "https://news.google.com/articles/CBMicEFBVV95cUxOb2tEWFZ0a1NvVnpzUUh0ZmdDVElOdjJwVkdmWUF1bmZKc1JCMGE5cm1jNm5EaGF1Qlk2a24zTlZ0SlJfZzJyU3RDaU9ESWU3b?hl=zh-HK&gl=HK&ceid=HK:zh-HK",
    "manulife_airside": "https://news.google.com/articles/CBMiggRBVV95cUxNWHlpMF9wWDJrTGhraHZWRDJ6ZzR6YUxfSF9GSHBnR1RTRjd6bTVydHRuRGdnM2ZXTHZsN3pzeU9sbGhTTVQ5QjdNM3FZQ05Uc?hl=zh-HK&gl=HK&ceid=HK:zh-HK",
    "silverbond": "https://news.google.com/articles/CBMiYkFVX3lxTFBFdC00Rl8xMHc2ZU1fX0FkSXpLdmJKdExRSVZOYTJBVmhsME05RGVHQ1QzRnlkZmhzZ2FoZEx6eWZJVWVtMTlaLWdwazk5aUFsM?hl=zh-HK&gl=HK&ceid=HK:zh-HK",
}
for tag, u in urls.items():
    out = follow(u)
    m = re.search(r"FINAL_URL:(\S+)$", out)
    final = m.group(1) if m else "?"
    print(f"[{tag}] -> {final[:200]}")
