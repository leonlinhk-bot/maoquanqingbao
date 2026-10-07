#!/bin/bash
cd /Users/leonliang/maoquanqingbao/.tmp/1008_0007
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36"
curl -sL -m 25 -A "$UA" -o ibm_calib.html "https://www.insurancebusinessmag.com/asia/news/professional-liability/hdi-global-expands-medical-malpractice-into-global-healthcare-unit-592443.aspx"
grep -oE '"(datePublished|dateModified)": *"[^"]+"' ibm_calib.html | head -4
