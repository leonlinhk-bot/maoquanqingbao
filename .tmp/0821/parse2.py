#!/usr/bin/env python3
"""Parse HKMA / IBMag / SCMP fetched HTML for recent links."""
import re, html, json
from datetime import datetime, timezone, timedelta

TZ = timezone(timedelta(hours=8))
NOW = datetime.now(TZ)
WIN = (NOW - timedelta(hours=26)).isoformat()
print(f"window_start={WIN}")

def clean(s):
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()

# ---- HKMA: look for date-annotated links ----
raw = open('.tmp/0821/hkma.html', encoding='utf-8', errors='replace').read()
print(f"\n===== HKMA (size {len(raw)}) =====")
# HKMA press pages usually have <a href="...">Title</a> with dates nearby like 21 Aug 2026
# Try to find patterns: "20 Aug 2026" etc within text
dates = re.findall(r'(\d{1,2}\s+(?:Aug|Sep|Jul|Jun|May|Apr|Mar|Feb|Jan|Oct|Nov|Dec)\s+2026)', raw)
print("date mentions found:", dates[:20])
# find links with their text
links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S)
hits = []
for href, txt in links:
    t = clean(txt)
    if len(t) < 15 or 'javascript' in href or href.startswith('#'):
        continue
    if any(k in t.lower() for k in ['insurance', 'insurer', 'digital asset', 'stablecoin', 'bank', 'fintech', 'fund', 'money', 'fraud', 'scam', 'bonds', 'treasury', 'interest']):
        hits.append((href, t))
seen = set()
for href, t in hits:
    if t in seen: continue
    seen.add(t)
    print(f"- {t[:80]} | {href[:100]}")
print("total candidate links:", len(seen))

# ---- IBMag breaking news ----
raw = open('.tmp/0821/ibmag.html', encoding='utf-8', errors='replace').read()
print(f"\n===== IBMag (size {len(raw)}) =====")
links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S)
seen = set()
for href, txt in links:
    t = clean(txt)
    if len(t) < 20 or 'javascript' in href:
        continue
    if '/asia/news/' in href or '/news/' in href:
        if t in seen: continue
        seen.add(t)
        print(f"- {t[:80]} | {href[:110]}")
print("total ibmag links:", len(seen))
