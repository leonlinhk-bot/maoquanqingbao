import re
ex=open('.tmp/0922-1808/existing.txt',encoding='utf-8').read()
tests=[
 "global-insurers-face-rising-systemic-risk",
 "swiss-re-earns-28b-profit",
 "reinsurers-lose-pricing-power",
 "niva-bupa-absorbs-underwriting-losses",
 "india-data-centres-expose-gaps",
 "iumis-denefle-fully-digitised",
 "marine-insurers-count-2bn",
 "tower-grows-reinsurance-limit",
 "iag-denies-greensill",
 "qbe-hires-shahrezal",
 "chiba-torrential",
 "asuransi-bintang",
 "envest-labuan-re",
 "vesttoo-bribery",
 "hong-kong-plan-puts-new-insurance-markets",
 "20260922-5",
 "20260922-4",
 "20260922-3",
 "hkfi",
 "20%",
 "tax",
 "fstb",
 "govhk",
 "tender",
]
for t in tests:
    hits=[l for l in ex.split('\n') if t.lower() in l.lower()]
    print(('HIT ' if hits else 'MISS'), t, '->', hits[:3])
