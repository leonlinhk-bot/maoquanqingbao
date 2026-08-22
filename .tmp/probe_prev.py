#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, os
for p in ["data/_raw/t0822-wb-ia-press.html", "data/_raw/t0822-wb-ia-circ.html"]:
    if not os.path.exists(p):
        print(p, "MISSING")
        continue
    raw = open(p, encoding="utf-8", errors="ignore").read()
    print(f"===== {p} ({len(raw)}B) =====")
    text = re.sub(r"<script.*?</script>", " ", raw, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    print(text[:1500])
    print()
