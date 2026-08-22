#!/usr/bin/env python3
import json
live = json.load(open('data/live-items.json'))
items = live['items']
by_id = {it['id']: it for it in items}

ids = """ia-aia-h1-profit-20260821
ia-week-in-insurance-20260822
scmp-pingan-hk-etf-20260821
ib-mainland-etf-access-20260821
crntt-aia-mcv-demand-20260822
ia-premium-financing-circular-20260820
aia-h1-2026-results-20260820
aia-h1-results-market-reaction-20260820
hkma-fake-doc-scam-alert-20260820
chinalife-h1-2026-briefing-20260819
hkex-h1-2026-results-20260819
ibmag-gallagherre-digital-risk-20260819
aastocks-ubs-fwd-coverage-20260819
prudential-taikoo-hq-20260819
ia-cyber-factory-gaps-20260819
bowtie-stillcover-20260818
manulife-new-fluidity-20260818
stcn-sfc-hkex-etf-20260818
scmp-beijing-insurers-hk-etfs-20260818
ibmag-aon-working-capital-apac-20260819
ibmag-qbe-data-centre-20260819
ib-china-life-slower-growth-20260818
ia-reinsurers-record-663b-20260818
ia-insurtech-asia-600m-q2-20260818
caixin-hk-banks-sfof-decl-20260818
aia-h1-2026-results-date-20260818
nfra-xiao-hui-hk-20260818
ibmag-aon-sidecarx-20260817
toutiao-h1-insurers-profit-20260817
toutiao-dadi-fine-20260818
boclife-hygge-eldercare-alliance-20260817
nfra-solvency-q2-5-insurers-20260817
ce-insurance-funds-40trillion-20260817
chubb-care-crit-illness-series-20260817
fwd-ebeyond-medical-20260817
steadfast-takeover-final-stages-20260817""".split()

for iid in ids:
    it = by_id.get(iid)
    if not it:
        print("MISSING:", iid); continue
    print("="*90)
    print(iid, "| kind:", it.get('contentKind'), "| tier:", it.get('sourceTier'), "| key:", it.get('sourceKey'))
    print("summary.sc:", it['summary']['sc'])
    print("summary.tc:", it['summary']['tc'])
