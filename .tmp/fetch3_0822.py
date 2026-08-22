#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check IBMAG AIA article, parse SCMP cards w/ dates, NFRA parse, fetch SunLife releases."""
import subprocess, re, html, time

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
def fetch(url, out):
    try:
        r = subprocess.run(["curl", "-sL", "--max-time", "35", "-A", UA, url],
                           capture_output=True, text=True, timeout=45)
        raw = r.stdout
        open(out, "w").write(raw)
        print(f"OK  {len(raw):8d}  {url}")
        return raw
    except Exception as e:
        print(f"ERR {e}  {url}")
        return ""

def unq(s):
    return html.unescape(re.sub(r"\s+", " ", s or "")).strip()

# 1. IBMAG AIA article
raw = open("data/_raw/t0822-ib-aia-broker.html", encoding="utf-8", errors="replace").read()
print("=== IBMAG AIA broker: title/date ===")
for pat in [r"<title>(.*?)</title>", r'"datePublished"\s*:\s*"([^"]+)"', r'"dateModified"\s*:\s*"([^"]+)"', r'(20\d\d[-/]\d{1,2}[-/]\d{1,2}[^<"]{0,20})']:
    for m in re.findall(pat, raw, re.S)[:4]:
        print("  ", unq(m)[:120])
body = re.sub(r"<script.*?</script>", " ", raw, flags=re.S)
body = re.sub(r"<style.*?</style>", " ", body, flags=re.S)
body = re.sub(r"<[^>]+>", " ", body)
body = unq(body)
print("  BODY:", body[:900])

# 2. SCMP cards with dates
raw = open("data/_raw/t0822-scmp.html", encoding="utf-8", errors="replace").read()
print("\n=== SCMP article cards ===")
# find blocks: link + time
blocks = re.findall(r'href="(/news/[^"]+)"[^>]*>.*?<time[^>]*>(.*?)</time>', raw, re.S)
seen = set()
for href, t in blocks:
    if href in seen: continue
    seen.add(href)
    print("-", unq(t)[:20], "|", href[:110])
print("total blocks:", len(blocks))

# 3. NFRA parse
raw = open("data/_raw/t0822-nfra2.html", encoding="utf-8", errors="replace").read()
print("\n=== NFRA candidates ===")
for m in re.finditer(r'href="([^"]*view/pages[^"]*)"[^>]*>([^<]{8,120})</a>', raw):
    t = unq(m.group(2))
    if any(k in t for k in ["保险", "金融", "监管", "风险"]):
        print("-", t[:90], "|", m.group(1)[:80])
print("NFRA date pats:", len(re.findall(r"2026-08-2\d", raw)))
