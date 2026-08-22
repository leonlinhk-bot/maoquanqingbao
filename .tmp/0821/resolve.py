#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Resolve Google News redirect URLs to final URLs + fetch pages."""
import subprocess, sys, re
from urllib.parse import urlparse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126"

def resolve(gn_url):
    """Follow redirects from a Google News rss/articles URL."""
    try:
        r = subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA,
                            "-w", "\\nFINAL_URL:%{url_effective}\\n", gn_url],
                           capture_output=True, text=True, timeout=40)
        out = r.stdout
        m = re.search(r"FINAL_URL:(.*)$", out, re.S)
        final = m.group(1).strip() if m else gn_url
        return final, out
    except Exception as e:
        return gn_url, ""

if __name__ == "__main__":
    name = sys.argv[1]
    url = sys.argv[2]
    final, body = resolve(url)
    print(f"NAME={name}\nFINAL={final}")
    # strip the final-url marker from body
    body = re.sub(r"\nFINAL_URL:.*$", "", body, flags=re.S)
    if body:
        fn = f".tmp/0821/res-{name}.html"
        open(fn, "w", encoding="utf-8", errors="replace").write(body)
        print(f"SAVED={fn} size={len(body)}")
