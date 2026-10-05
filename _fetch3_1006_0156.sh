#!/usr/bin/env bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
O=/Users/leonliang/maoquanqingbao/data/_cache1006_0156
g() { curl -sL -m 30 -A "$UA" -H "Accept: text/html,application/xhtml+xml" -o "$O/$1" -w "$1 %{http_code} " "$2"; wc -c < "$O/$1" | tr -d ' '; }
# IA alternate paths
g ia_en_press.html  "https://ia.org.hk/english/infocenter/press_releases.html"
g ia_en_circ.html   "https://ia.org.hk/english/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html"
g ia_en_circ2.html  "https://www.ia.org.hk/english/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html"
# IBM specific articles for date verification
g ibm_conduct.html  "https://www.insurancebusinessmag.com/asia/news/breaking-news/broker-leadership-churn-emerges-as-conduct-risk-signal-in-hong-kong-ia-report-591783.aspx"
g ibm_mas.html      "https://www.insurancebusinessmag.com/asia/news/breaking-news/mas-moves-to-approve-who-chairs-insurer-nominating-committees-592300.aspx"
g ibm_camb.html     "https://www.insurancebusinessmag.com/asia/news/life-insurance/cambodia-bancassurance-deals-squeeze-out-independent-brokers-592"
g ibm_collins.html  "https://www.insurancebusinessmag.com/asia/news/breaking-news/dominic-collins-to-step-down-as-howdens-executive-chairman-592300"
echo DONE
