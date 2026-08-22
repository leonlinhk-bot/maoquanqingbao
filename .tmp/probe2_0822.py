#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deeper inspection of ibmag/scmp/sunlife/aia/pru pages for article cards."""
import re, html, json

def unq(s):
    return html.unescape(re.sub(r"\s+", " ", s or "")).strip()

def probe(tag, path, pats, n=14):
    raw = open(path, encoding="utf-8", errors="replace").read()
    print(f"\n########## {tag} ({len(raw)} bytes) ##########")
    for name, pat in pats:
        ms = re.findall(pat, raw, re.S)
        print(f"--- {name}: {len(ms)}")
        for m in ms[:n]:
            if isinstance(m, tuple):
                print("   ", " || ".join(unq(x)[:80] for x in m)[:220])
            else:
                print("   ", unq(m)[:180])

probe("IBMAG", "data/_raw/t0822-ibmag.html", [
    ("article-card", r'<a[^>]+href="(/asia/news/[^"]+)"[^>]*>\s*<[^>]*>([^<]{8,160})'),
    ("news-link", r'href="(/asia/news/[a-z0-9\-]+/[a-z0-9\-]+\.html)"'),
])
probe("SUNLIFE", "data/_raw/t0822-sunlife.html", [
    ("news-item", r'<a[^>]+href="(/zh-hant/[^"]*(?:news|release)[^"]*)"[^>]*>([^<]{8,160})'),
    ("all-links-news", r'href="([^"]*(?:news|release|press)[^"]*)"'),
])
probe("AIA", "data/_raw/t0822-aia.html", [
    ("press-link", r'href="([^"]*(?:press|release)[^"]*)"'),
    ("json-date", r'"(?:date|publishDate|publishedDate|displayDate)"\s*:\s*"([^"]+)"'),
])
probe("PRU", "data/_raw/t0822-prudential.html", [
    ("news-link", r'href="([^"]*(?:news|announcement|release)[^"]*)"'),
    ("json-title", r'"(?:title|headline|name)"\s*:\s*"([^"]{10,140})"'),
])
