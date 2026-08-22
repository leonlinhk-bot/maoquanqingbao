#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
raw = open("data/_raw/t0822-iaa-rss.html", encoding="utf-8", errors="replace").read()
items = re.findall(r"<item>(.*?)</item>", raw, re.S)
print("items:", len(items))
print(raw[:1200])
print("=== first item raw ===")
print(items[0][:1500])
