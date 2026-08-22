#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dump readable text of an HTML file (article body). Usage: python3 htmltext.py file.html"""
import re, html, sys

raw = open(sys.argv[1], encoding='utf-8', errors='replace').read()
# drop scripts/styles
raw = re.sub(r'<script.*?</script>', ' ', raw, flags=re.S)
raw = re.sub(r'<style.*?</style>', ' ', raw, flags=re.S)
# find main content region heuristically: div with class containing 'article' or 'content' or 'body'
m = re.search(r'(<div[^>]*(?:article|content|body)[^>]*>.*?)(?:<div[^>]*footer|<footer)', raw, re.S)
if m:
    raw = m.group(1)
txt = re.sub(r'<[^>]+>', '\n', raw)
txt = html.unescape(txt)
lines = [re.sub(r'\s+', ' ', l).strip() for l in txt.split('\n')]
lines = [l for l in lines if len(l) > 30]
for l in lines[:25]:
    print('-', l[:400])
