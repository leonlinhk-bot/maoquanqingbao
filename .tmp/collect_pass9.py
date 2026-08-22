#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pass 9: resolve originals via r.jina.ai proxy + direct article fetches."""
import re, html, subprocess, urllib.parse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def fetch(url, ua=None):
    try:
        return subprocess.run(["curl", "-sL", "--max-time", "35", "-A", ua or UA, url],
                              capture_output=True, text=True, timeout=45).stdout
    except Exception:
        return ""

def strip_tags(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

# 1. 點新聞 Hengda via jina
print("=== hkcna Hengda via jina ===")
raw = fetch("https://r.jina.ai/https://www.hkcna.hk/docDetail.jsp?id=", UA)
print(f"len={len(raw)} head={raw[:200]}")

# try hkcna search
print("\n=== hkcna docList ===")
raw = fetch("https://www.hkcna.hk/channel/docList.jsp?channelId=4000&pageNo=1")
print(f"len={len(raw)}")
print(strip_tags(raw)[:800])

# 2. NFRA punishment announcements - try their site listing
print("\n=== NFRA 处罚 listing ===")
raw = fetch("https://www.nfra.gov.cn/cn/view/pages/ItemList.html?itemPId=923&itemId=931&itemUrl=ItemListRightList.html&itemName=%E5%A4%84%E7%BD%9A%E4%BF%A1%E6%81%AF&itemsiteId=9152")
print(f"len={len(raw)}")
print(strip_tags(raw)[:1000])

# 3. UBS AIA via aastocks (known financial portal)
print("\n=== aastocks search ===")
raw = fetch("https://www.aastocks.com/tc/stocks/market/stock-news.aspx?symbol=01299")
print(f"len={len(raw)}")
txt = strip_tags(raw)
m = re.findall(r'.{0,60}(?:瑞銀|友邦|102).{0,120}', txt)
for x in m[:8]:
    print("-", x)
