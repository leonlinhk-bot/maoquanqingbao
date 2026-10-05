import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items']
for it in items:
    if it.get('id') in ('ia-conduct-in-focus-issue-13-20260930', 'hkma-ip-financing-sandbox-first-batch-20260930', 'ian-john-neal-lusyi-chairman-20261005', 'artemis-casualty-ils-exit-mechanisms-srs-20261002', 'ibm-hanwha-life-acuon-capital-20261002'):
        print(json.dumps(it, ensure_ascii=False, indent=1))
        print('=' * 100)
