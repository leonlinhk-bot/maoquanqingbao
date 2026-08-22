#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pass 7: DuckDuckGo HTML search + direct NFRA site for originals."""
import re, html, json, subprocess, urllib.parse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def fetch(url):
    try:
        return subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA, url],
                              capture_output=True, text=True, timeout=40).stdout
    except Exception:
        return ""

def ddg(q):
    raw = fetch("https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(q))
    res = re.findall(r'<a[^>]+class="result__a"[^>]+href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S)
    out = []
    for u, t in res[:8]:
        # ddg wraps in uddg redirect
        m = re.search(r'uddg=([^&]+)', u)
        if m:
            u = urllib.parse.unquote(m.group(1))
        t = html.unescape(re.sub(r'<[^>]+>', '', t)).strip()
        out.append((t, u))
    return out, len(raw)

queries = [
    ("hengda", "恒大人寿 保险 业务许可证 吊销 金融监管总局"),
    ("hengda2", "恒大人寿 保险许可证 撤销"),
    ("ubs-aia", "瑞银 友邦保险 目标价 102 港元"),
    ("manulife-airside", "宏利 AIRSIDE 樂活節奏健康節"),
    ("silverbond", "銀色債券 2026 認購 4.25厘"),
    ("aia-tax", "友邦 稅策無礙內地客需求 新業務價值"),
]
for tag, q in queries:
    out, ln = ddg(q)
    print(f"\n=== DDG[{tag}] '{q}' (len={ln}) ===")
    for t, u in out:
        print(f"* {t[:85]}\n  {u[:150]}")
