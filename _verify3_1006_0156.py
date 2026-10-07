import subprocess, json, time
out = subprocess.run(['curl', '-sL', '-m', '25',
                      'https://hkmaoquanqingbao.com/feed/all.json?cb=' + str(int(time.time()))],
                     capture_output=True, text=True).stdout
d = json.loads(out)
ids = {i['id'] for i in d['items']}
print('deployed itemCount:', d.get('itemCount'), '| generatedAt', d.get('generatedAt'))
for p in ['hkma-bakai-bank-restricted-licence-20261005',
          'ibm-ia-conduct-focus-broker-ro-tenure-20260930',
          'insurtech-corgi-datacentre-ai-infrastructure-cover-20261005',
          'reinasia-cpic-hk-liquidity-sp-ratings-20261005',
          'iaasia-datacentre-boom-insurance-rates-20261005',
          'artemis-picc-great-wall-re-cat-bond-2-20261005',
          'scmp-schroders-nuveen-hk-expansion-20261005',
          'ian-marsh-re-parametric-wind-bushfire-apac-20261005']:
    print('  ', 'LIVE' if p in ids else 'MISSING', p)
core = json.loads(subprocess.run(['curl', '-sL', '-m', '25',
    'https://hkmaoquanqingbao.com/data/core.json?cb=' + str(int(time.time()))], capture_output=True, text=True).stdout)
print('core.json items:', len(core.get('items', [])))
top = [i.get('title', '')[:60] for i in core.get('items', [])[:5]]
for t in top:
    print('   core首屏:', t)
