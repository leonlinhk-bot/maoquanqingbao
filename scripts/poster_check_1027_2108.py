#!/usr/bin/env python3
"""Show poster cards' titles."""
import re
h = open('/Users/leonliang/maoquanqingbao/posters/poster-2026-10-27.html', encoding='utf-8').read()
for m in re.finditer(r'<h3>(.*?)</h3>', h, re.S):
    print("-", re.sub(r'<[^>]+>', '', m.group(1)).strip())
print("date line:", re.findall(r'\d{1,2}月 · 星期.', h)[:2])
