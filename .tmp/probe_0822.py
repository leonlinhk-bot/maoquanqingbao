#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inspect structures of insurer/ibmag/scmp pages to build parsers."""
import re

def probe(tag, path, patterns, n=12):
    raw = open(path, encoding="utf-8", errors="replace").read()
    print(f"\n########## {tag} ({len(raw)} bytes) ##########")
    for name, pat in patterns:
        ms = re.findall(pat, raw, re.S)
        print(f"--- {name}: {len(ms)}")
        for m in ms[:n]:
            s = m if isinstance(m, str) else " | ".join(str(x)[:70] for x in m)
            print("   ", s[:180])

probe("AIA", "data/_raw/t0822-aia.html", [
    ("a-tag", r'<a[^>]+href="([^"]*press[^"]*)"[^>]*>([^<]{5,140})</a>'),
    ("date-pat", r'\d{4}[-/.]\d{1,2}[-/.]\d{1,2}'),
])
probe("PRU", "data/_raw/t0822-prudential.html", [
    ("a-tag", r'<a[^>]+href="([^"]*news[^"]*)"[^>]*>([^<]{5,140})</a>'),
    ("date-pat", r'\d{4}[-/.]\d{1,2}[-/.]\d{1,2}'),
])
probe("AXA", "data/_raw/t0822-axa.html", [
    ("a-tag", r'<a[^>]+href="([^"]*)"[^>]*>([^<]{5,140})</a>'),
    ("date-pat", r'\d{4}[-/.]\d{1,2}[-/.]\d{1,2}'),
])
probe("SUNLIFE", "data/_raw/t0822-sunlife.html", [
    ("a-tag", r'<a[^>]+href="([^"]*)"[^>]*>([^<]{5,140})</a>'),
    ("date-pat", r'\d{4}[-/.]\d{1,2}[-/.]\d{1,2}'),
])
probe("IBMAG", "data/_raw/t0822-ibmag.html", [
    ("a-tag", r'<a[^>]+href="([^"]*)"[^>]*>([^<]{5,140})</a>'),
    ("date-pat", r'\d{4}[-/.]\d{1,2}[-/.]\d{1,2}'),
])
