#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dump existing items published >= 2026-10-12 for dedup + check candidate URLs."""
import json, sys
from datetime import datetime, timezone, timedelta

HKT = timezone(timedelta(hours=8))
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json', encoding='utf-8'))
items = d['items']
print('TOTAL', len(items), 'generatedAt', d.get('meta', {}).get('generatedAt'))
print('meta keys:', list(d.get('meta', {}).keys()))

def dt(s):
    try:
        v = datetime.fromisoformat(s)
    except Exception:
        return None
    if v.tzinfo is None:
        v = v.replace(tzinfo=HKT)
    return v

cut = datetime(2026, 10, 12, 0, 0, tzinfo=HKT)
recent = [it for it in items if (dt(it.get('publishedAt') or '') or cut) >= cut]
print(f'\n-- items publishedAt >= 2026-10-12: {len(recent)} --')
for it in sorted(recent, key=lambda x: x.get('publishedAt') or '', reverse=True):
    print(f"{it.get('publishedAt')} | {it.get('sourceKey'):20s} | {it.get('sourceTier'):8s} | {it.get('id')}")
    print(f"    {it.get('title', {}).get('sc', '')[:80]}")
    print(f"    {it.get('originalUrl', '')}")

urls = {(it.get('originalUrl') or '').rstrip('/') for it in items}
print('\n-- candidate URL check --')
for u in [
 'https://insuranceasia.com/insurance/news/hsbc-life-expands-cross-border-healthcare-four-new-lounges',
 'https://insuranceasia.com/insurance/news/nat-res-capital-strength-opens-door-higher-underwriting-volumes',
 'https://insuranceasia.com/insurance/in-focus/life-insurers-face-pressure-retirement-savings-shift',
 'https://www.insurancebusinessmag.com/asia/business-strategy/demographic-changes-to-shrink-canadas-workforce-bank-of-canada-593491.aspx',
 'https://www.insurancebusinessmag.com/asia/news/breaking-news/credit-cover-alone-will-not-scale-emergingmarket-climate-finance-moodys-says-59',
 'https://www.insurancebusinessmag.com/asia/news/life-insurance/manulife-launches-enterprise-ai-platform-as-it-targets-1-billion-in-value-by-2',
]:
    print(('DUP ' if u.rstrip('/') in urls else 'NEW '), u)
