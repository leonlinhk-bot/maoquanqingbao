#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html
D = '/Users/leonliang/maoquanqingbao/data/_1016_0029/'
raw = open(D + 'ibm.out', encoding='utf-8', errors='replace').read()
i = raw.find('593667')
print(raw[max(0, i - 900):i + 300])
