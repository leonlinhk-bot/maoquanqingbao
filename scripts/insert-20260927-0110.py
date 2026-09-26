#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-27 01:10 增量采集：窗口(9/26 12:55 → 9/27 01:10)各 RSS/API 无新增；
补入 9/24 遗漏的 NFRA 8月行业经营数据（官方月度统计，14 信源之一 nfra 归档补缺）。
另：9/25 两条 InsuranceAsia 漏采条目已由 23:50 批次入库（本次一并发布）。"""
import json, shutil, os

BASE = '/Users/leonliang/maoquanqingbao'
NOW = '2026-09-27T01:10:00+08:00'


def item(**kw):
    d = {
        'clusterCount': 1, 'score': 65, 'verifyStatus': 'pending',
        'sourceTier': 'media', 'sourceKey': '', 'contentKind': 'news',
        'actions': {'front': {}, 'midback': {}, 'lead': {}, 'cross': {}},
        'rolesImpact': {'front': 0, 'midback': 0, 'lead': 0, 'cross': 0},
        'boards': [], 'themes': [], 'tags': {'sc': [], 'tc': []},
        'contentRole': {'sc': '本站导读', 'tc': '本站導讀'},
        'featured': False, 'evergreen': False, 'ingestedAt': NOW,
    }
    d.update(kw)
    return d


T = lambda sc, tc=None: {'sc': sc, 'tc': tc or sc}

NEW = [
    item(id='nfra-monthly-premium-aug2026-20260924', score=86, verifyStatus='verified',
         sourceTier='official', sourceKey='nfra', contentKind='stats',
         publishedAt='2026-09-24',
         title=T('内地保险业2026年前8月原保费48,192亿元仅增0.4%：人身险单月转负13.6%（高基数），财险增2.2%保持稳健'),
         summary=T('国家金融监督管理总局公布2026年8月保险业经营情况，共四张表：保险业经营情况表、人身险公司、财产险公司经营情况表及全国各地区原保险保费收入情况表（发布日2026-09-24）。按市场点评口径：2026年前8月行业累计原保险保费48,192亿元，同比+0.4%，较前7月放缓1.5个百分点；其中人身险35,719亿元、同比-0.2%（8月单月4,011亿元，同比-13.6%，主因去年同期预定利率下调前「炒停」高基数），寿险29,757亿元基本持平、健康险5,721亿元-1.1%、意外险241亿元-10.0%；保户投资款新增交费4,973亿元+8.4%，投连险独立账户新增交费75亿元-42.1%。财险累计12,473亿元、同比+2.2%，车险6,006亿元基本持平、非车险6,467亿元+4.4%（占比51.8%）；8月单月财险1,291亿元+1.8%。'),
         why=T('内地保费增速是港险需求的先行参照：储蓄类需求仍在但增速回落、投连与投资款分化，可直接用于评估跨境客户资金配置节奏与产品结构变化，也是本站月度官方口径的数据底座。'),
         actions={'front': {},
                  'midback': T('把月度保费与险种结构纳入月度市场简报，作为客户资金面与需求侧的官方参照'),
                  'lead': T('以官方月度口径（前8月4.82万亿、+0.4%）替换二手估算，统一对内汇报的数据基础'),
                  'cross': T('投连独立账户与保户投资款分化，可作为跨境客户资产配置偏好变化的观察指标')},
         rolesImpact={'front': 1, 'midback': 3, 'lead': 2, 'cross': 2},
         source={'sc': '国家金融监督管理总局 · 统计信息（2026-09-24 发布）；数值口径参考券商2026年8月保费数据点评（2026-09-25）',
                 'tc': '國家金融監督管理總局 · 統計信息（2026-09-24 發布）；數值口徑參考券商2026年8月保費數據點評（2026-09-25）',
                 'lang': 'zh'},
         boards=['market', 'reg'], themes=['market', 'results'],
         tags={'sc': ['金融监管总局', '月度保费', '人身险', '财产险', '投连险', '2026年8月'],
               'tc': ['金融監管總局', '月度保費', '人身險', '財產險', '投連險', '2026年8月']},
         originalUrl='https://www.nfra.gov.cn/cn/view/pages/ItemList.html?itemPId=953&itemId=954'),
]

path = os.path.join(BASE, 'data/live-items.json')
shutil.copy(path, os.path.join(BASE, 'data/live-items.json.bak-0927-0110'))
doc = json.load(open(path, encoding='utf-8'))
old_ids = {it['id'] for it in doc['items']}
old_urls = {it.get('originalUrl', '').split('?')[0].rstrip('/') for it in doc['items']}
added, skipped = [], []
for it in NEW:
    u = it['originalUrl'].split('?')[0].rstrip('/')
    if it['id'] in old_ids or u in old_urls:
        skipped.append(it['id'])
        continue
    added.append(it)
doc['items'] = added + doc['items']
n = len(doc['items'])
doc['meta']['itemCount'] = n
doc['meta']['generatedAt'] = NOW
doc['meta']['windowNote'] = {'sc': f'本库{n}条。', 'tc': f'本庫{n}條。'}
json.dump(doc, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'added={len(added)} skipped={len(skipped)} total={n}')
for a in added:
    print('  +', a['publishedAt'], a['sourceKey'], a['id'])
if skipped:
    print('SKIPPED DUPES:', skipped)
