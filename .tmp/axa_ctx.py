#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html
raw = open("data/_raw/t0822-axa.html", encoding="utf-8", errors="replace").read()
# find context around 2026-08-21 dates
for m in re.finditer(r"2026-08-21", raw):
    s = max(0, m.start()-400)
    e = min(len(raw), m.end()+400)
    ctx = re.sub(r"\s+", " ", raw[s:e])
    print("----")
    print(ctx[:800])
