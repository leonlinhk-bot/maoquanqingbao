#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Decode Google News rss/articles base64 token to real URL."""
import base64, re, sys

def decode_gn(url):
    m = re.search(r"/articles/([A-Za-z0-9_-]+)", url)
    if not m:
        return None
    tok = m.group(1)
    # add padding
    pad = "=" * (-len(tok) % 4)
    try:
        raw = base64.urlsafe_b64decode(tok + pad)
    except Exception as e:
        return f"decode error: {e}"
    # find URLs inside
    urls = re.findall(rb"https?://[^\x00-\x1f\x7f\"'<> ]+", raw)
    out = []
    for u in urls:
        try:
            s = u.decode("utf-8", "replace")
        except Exception:
            s = str(u)
        out.append(s)
    return out

if __name__ == "__main__":
    for url in sys.argv[1:]:
        print(url[:60], "->", decode_gn(url))
