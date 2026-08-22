#!/usr/bin/env python3
import json, glob, os

for f in sorted(glob.glob('.tmp/0821/bing_*.json')):
    print('====', os.path.basename(f))
    try:
        d = json.load(open(f))
        for x in d:
            print(' ', x.get('date','')[:16], '|', x.get('title','')[:80])
            print('    ', x.get('link','')[:130])
    except Exception as e:
        print('ERR', e)
