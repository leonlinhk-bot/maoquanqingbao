#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os
ROOT = os.path.dirname(os.path.abspath(__file__))
NOW = "2026-09-23T18:08:00+08:00"
p = os.path.join(ROOT, "data", "last-check.json")
d = json.load(open(p))
d["lastCheck"] = NOW
for k, v in d.get("sources", {}).items():
    v["last"] = NOW
json.dump(d, open(p, "w"), ensure_ascii=False, indent=2)
print("lastCheck ->", NOW, "| sources updated:", len(d.get("sources", {})))
