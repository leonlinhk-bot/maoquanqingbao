#!/usr/bin/env bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128 Safari/537.36"
OUT=/Users/leonliang/maoquanqingbao/data/_cache1005_1808
f() { printf '%-24s ' "$1"; curl -sL -m 30 --noproxy '*' -A "$UA" -o "$OUT/$1" -w "%{http_code} %{size_download}\n" "$2"; }
f scmp_topic.html   "https://www.scmp.com/topics/insurance"
f scmp_rss.xml      "https://www.scmp.com/rss/92/feed"
f fstb_rss.xml      "https://www.info.gov.hk/gia/rss/finance_zh.xml"
f manu_global.html  "https://www.manulife.com/en/newsroom.html"
f sunlife_bm.html   "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/"
f iaasia_uni.html   "https://insuranceasia.com/insurance/news/unimed-recovers-two-years-losses-premium-increases-kick-in"
f iaasia_aero.html  "https://insuranceasia.com/insurance/news/aerospace-insurers-tighten-scrutiny-despite-stable-price-and-capacity"
f iaasia_drought.html "https://insuranceasia.com/insurance/news/australian-insurers-face-29b-drought-risk"
f iaasia_cyber.html "https://insuranceasia.com/insurance/news/insurers-face-apac-cyber-regulatory-divergence-enforcement-tightens"
f ian_everest.html  "https://insuranceasianews.com/everest-names-adrian-di-pasquale-as-apac-financial-lines-director-for-wholesale-specialty/"
f ian_frag.html     "https://insuranceasianews.com/same-asset-different-market-why-regulatory-fragmentation-changes-how-insurance-responds-in-asia/"
f ian_bajaj.html    "https://insuranceasianews.com/bajaj-finserv-picks-ex-gic-chairman-ramaswamy-narayanan-to-lead-reinsurance-foray-report/"
f ian_marshre.html  "https://insuranceasianews.com/as-apac-risk-transfer-market-opens-up-marsh-re-eyes-parametric-wind-bushfire-cover/"
echo DONE
