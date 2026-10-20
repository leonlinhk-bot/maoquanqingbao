import json
p = 'data/live-items.json'
d = json.load(open(p, encoding='utf-8'))
fixed = 0
NEW = {'insuranceasianews-helvetia-asia-ceo-tan-20261021',
       'reinsurancenews-meta-muse-ai-claims-risk-20261020',
       'artemis-perils-july-scs-loss-2806m-20261020',
       'artemis-arbol-datacenter-moratorium-parametric-20261020',
       'artemis-jamaica-cat-bond-melissa-payout-20261020',
       'reinsurancenews-triplei-milliman-pc-2026-outlook-20261020',
       'artemis-gam-aviv-cat-bond-scalability-20261020',
       'insuranceasianews-mg-geraghty-phil-steel-20261020',
       'reinsurancenews-morningstar-dbrs-france-srcc-20261020',
       'insuranceasianews-cybercube-sompo-japan-20261020',
       'ia-enforcement-jian-yongqin-suspension-20261016'}
REAL_NOW = '2026-10-21T01:06:00+08:00'
for it in d['items']:
    if it.get('id') in NEW:
        it['ingestedAt'] = REAL_NOW
        fixed += 1
d['meta']['generatedAt'] = REAL_NOW
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('fixed ingestedAt:', fixed, 'generatedAt:', REAL_NOW)
