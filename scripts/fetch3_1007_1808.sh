#!/bin/bash
cd /Users/leonliang/maoquanqingbao
OUT=data/_raw_1007_1808
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
fetch() {
  curl -sSL --noproxy '*' --max-time 40 -A "$UA" "$2" -o "$OUT/$1" -w "%{http_code} %{size_download} $1\n" || echo "FAIL $1"
}
fetch art_hiscox.html "https://www.insurancebusinessmag.com/asia/news/breaking-news/cyber-is-now-the-risk-most-likely-to-trigger-everything-else-hiscox-592641.aspx"
fetch art_cfc.html "https://www.insurancebusinessmag.com/asia/news/cyber/cfc-adds-executive-protection-ai-cover-to-cyber-policy-592583.aspx"
fetch art_ship.html "https://www.insurancebusinessmag.com/asia/news/marine/ship-sunk-crew-missing-after-drone-strike-inside-nato-members-economic-zone-592511.aspx"
fetch art_philhealth.html "https://www.insurancebusinessmag.com/asia/news/life-insurance/philhealth-targets-benefit-overlap-with-hmos-and-private-insurers-592521.aspx"
fetch art_facult.html "https://insuranceasia.com/insurance/news/insurers-boost-facultative-cover-markets-soften"
fetch art_reins.html "https://insuranceasia.com/insurance/news/reinsurers-lift-returns-capital-hits-record-688b"
fetch art_airline.html "https://insuranceasia.com/insurance/news/airline-insurers-brace-q4-claims-pressure"
fetch art_cyber.html "https://insuranceasia.com/insurance/news/cyber-insurers-gain-sharper-risk-view-digital-footprints"
fetch art_assets.html "https://insuranceasia.com/insurance/in-focus/insurance-assets-lose-ground-securities-surge"
fetch art_alliance.html "https://insuranceasianews.com/australia-new-zealand-join-uk-canada-to-launch-joint-alliance-to-confront-escalating-shared-risks/"
fetch art_india.html "https://insuranceasianews.com/brokers-warn-indias-distribution-reform-plan-risks-job-cuts-sector-disruption/"
fetch art_bloodstock.html "https://insuranceasianews.com/many-dont-appreciate-what-can-go-wrong-bloodstock-insurance-finds-its-footing-in-north-asia/"
fetch art_hkma_fx.html "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/10/20261007-3/"
fetch art_hk01_legco.html "https://www.hk01.com/article/60397142"
fetch art_scmp_fo.html "https://www.scmp.com/native/business/topics/fostering-future-innovators/article/3369878/family-offices-branch-out-private-equity-infrastructure-and-alternative-investments"
fetch art_scmp_mpf.html "https://www.scmp.com/business/money/investment-products/article/3369945/hong-kongs-mpf-has-gained-nearly-hk100b-year-despite-september-loss"
echo DONE
