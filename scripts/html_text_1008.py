#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract readable text from a gov.hk GIA press release HTML page."""
import re
import html
import sys

path = sys.argv[1]
raw = open(path, encoding='utf-8', errors='replace').read()
raw = re.sub(r'<script.*?</script>', ' ', raw, flags=re.S | re.I)
raw = re.sub(r'<style.*?</style>', ' ', raw, flags=re.S | re.I)
txt = re.sub(r'<[^>]+>', '\n', raw)
txt = html.unescape(txt)
lines = [ln.strip() for ln in txt.split('\n')]
out = [ln for ln in lines if ln]
print('\n'.join(out))
