#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-10 补采插入 第三部分（SCMP / 媒体层）"""
import json

ING = '2026-10-10T01:45:00+08:00'


def S(a, b=None):
    return {'sc': a, 'tc': b or a}


def item(**kw):
    return {
        'clusterCount': 1,
        'score': kw['score'],
        'verifyStatus': kw.get('verify', 'pending'),
        'sourceTier': kw['tier'],
        'sourceKey': kw['key'],
        'contentKind': kw.get('kind', 'news'),
        'actions': {
            'front': S(kw['a_front']),
            'midback': S(kw['a_mid']),
            'lead': S(kw['a_lead']),
            'cross': S(kw['a_cross']),
        },
        'rolesImpact': kw['roles'],
        'boards': kw['boards'],
        'themes': kw['themes'],
        'tags': {'sc': kw['tags'], 'tc': kw['tags']},
        'contentRole': S('本站导读', '本站導讀'),
        'featured': False,
        'evergreen': False,
        'ingestedAt': ING,
        'id': kw['id'],
        'publishedAt': kw['pub'],
        'originalUrl': kw['url'],
        'title': S(kw['title']),
        'summary': S(kw['summary']),
        'why': S(kw['why']),
        'source': {'sc': '南華早報（SCMP）%s' % kw['sdate'], 'tc': '南華早報（SCMP）%s' % kw['sdate'],
                   'lang': 'en', 'name': 'South China Morning Post', 'date': kw['sdate'], 'note': None},
    }


NEW = []

NEW.append(item(
    id='scmp-sfc-liquidity-reforms-20261009',
    score=62, verify='pending', tier='media', key='scmp',
    pub='2026-10-09T18:01:00+08:00', sdate='2026-10-09',
    url='https://www.scmp.com/business/banking-finance/article/3370363/hong-kong-outlines-new-liquidity-reforms-us-market-rally-pulls-funds-away',
    title='南華早報：證監會再推市場流動性改革 延長交易時段、縮短結算週期入列',
    summary='南華早報10月9日18:01報道：香港證券及期貨事務監察委員會（SFC）再度推動提升市場流動性的改革，在美國股市上升、美元走強令新興市場面對資金外流壓力之際公布新措施。SFC 行政總裁梁鳳儀在亞洲證券業與金融市場協會（Asifma）會議上提出，措施涵蓋延長交易時段、縮短結算週期、跨市場保證金安排，以及每手股數（board lot）改革等，目標是提升市場流動性與效率。 [EN原文]，正文受限，此條按標題、導語及圖說整理，待補充原文後覆核。',
    why='交易時段與結算週期改革屬跨市場競爭的結構性議題，會影響香港作為資產與財富管理中心的交易成本與吸引力，亦與南韓延長交易時段的競爭壓力互相呼應。',
    a_front='不作投資建議，僅作市場環境背景',
    a_mid='納入市場流動性與結算制度監察',
    a_lead='用於說明香港應對區域交易市場競爭的制度回應',
    a_cross='港股與亞洲其他市場交易制度改革競賽',
    roles={'front': 0, 'midback': 1, 'lead': 2, 'cross': 2},
    boards=['market'],
    themes=['market-liquidity', 'sfc', 'settlement', 'hong-kong'],
    tags=['證監會', '梁鳳儀', '流動性', '結算週期', 'Asifma'],
))

NEW.append(item(
    id='scmp-kk-one-stanley-six-year-structural-warranty-20261009',
    score=62, verify='pending', tier='media', key='scmp',
    pub='2026-10-09T21:50:00+08:00', sdate='2026-10-09',
    url='https://www.scmp.com/business/article/3370397/kk-offers-extra-warranty-one-stanley-homebuyers-amid-building-defects-furore',
    title='南華早報：K&K向One Stanley業主提供六年結構保養 圖平息施工爭議',
    summary='南華早報10月9日21:50報道：發展商 K&K Property 宣布向旗下豪宅項目 One Stanley 的業主提供六年結構保養（structural warranty），以平息有關施工缺陷的持續爭議。報道背景：該項目早前被指鋼筋不足而遭調查，銀行亦對其按揭轉趨審慎。 [EN原文]，正文受限，此條按標題、導語及延伸報道標題整理，待補充原文後覆核。',
    why='建築結構保養的年限與執行力，直接關係到家居保險、樓宇結構風險與按揭審批的風險判斷；發展商主動延長保養期，是本地物業風險議題的即時案例。',
    a_front='客戶問及物業保修與家居保險分野時，可說明發展商結構保養與保險保障責任範圍不同',
    a_mid='納入本地物業風險與理賠案例觀察',
    a_lead='用於說明發展商保養與保險責任的界線',
    a_cross='樓宇結構風險與按揭審慎取態的關聯',
    roles={'front': 1, 'midback': 1, 'lead': 1, 'cross': 1},
    boards=['market', 'product'],
    themes=['property-risk', 'warranty', 'construction', 'hong-kong'],
    tags=['One Stanley', 'K&K Property', '結構保養', '施工爭議', '按揭'],
))

NEW.append(item(
    id='scmp-prediction-markets-asia-regulatory-clarity-20261009',
    score=60, verify='pending', tier='media', key='scmp',
    pub='2026-10-09T09:00:00+08:00', sdate='2026-10-09',
    url='https://www.scmp.com/business/markets/article/3370249/finance-or-gambling-prediction-market-players-push-regulatory-clarity-asia',
    title='南華早報：亞洲預測市場業界爭取監管清晰 力圖與賭博劃清界線',
    summary='南華早報10月9日09:00報道：金融科技業界加強游說，要求就預測市場（prediction markets）訂立更清晰監管規則，一方面試圖把業務與賭博區分，另一方面淡化其風險。相關訴求在週四的會議上提出。 [EN原文]，正文受限，此條按標題與摘要整理，待補充原文後覆核。',
    why='預測市場的監管定性之爭，反映新型金融產品在既有牌照框架下的分類難題；與香港近年對虛擬資產、眾籌等新形態的處理邏輯有共通之處。',
    a_front='不對客提及',
    a_mid='納入新型金融產品監管分類觀察',
    a_lead='用於說明「投資 vs 博彩」界線的監管難題',
    a_cross='亞洲各市場對新金融形態的分類處理',
    roles={'front': 0, 'midback': 1, 'lead': 2, 'cross': 1},
    boards=['reg', 'market'],
    themes=['regulation', 'fintech', 'prediction-market', 'asia'],
    tags=['預測市場', '監管', '金融科技', '博彩', '亞洲'],
))

NEW.append(item(
    id='scmp-central-retail-shop-bought-by-swiss-heir-20261009',
    score=60, verify='pending', tier='media', key='scmp',
    pub='2026-10-09T07:00:00+08:00', sdate='2026-10-09',
    url='https://www.scmp.com/property/article/3370181/central-retail-shop-bought-swiss-heir-rare-hong-kong-market-move',
    title='南華早報：瑞士家族繼承人購中環商舖 本地發展商持貨55年後易手',
    summary='南華早報10月9日07:00報道：本地發展商協成行（Hip Shing Hong）出售中環亞畢諾道一個地舖，持貨55年後易手，買家為一名瑞士家族繼承人，被形容為香港市場的「罕見」交易。 [EN原文]，正文受限，此條按標題、導語及副題整理，待補充原文後覆核。',
    why='超高淨值家族直接購入香港核心商用物業，屬家族辦公室資產配置與香港物業市場交匯的具體個案，可用於觀察跨境家族資本的實物資產取向。',
    a_front='不對客引用，作家族資本流向觀察',
    a_mid='納入家族辦公室資產配置案例',
    a_lead='用於說明香港核心資產對境外家族資本的吸引力',
    a_cross='境外家族資本與香港物業市場的互動',
    roles={'front': 0, 'midback': 1, 'lead': 2, 'cross': 2},
    boards=['family', 'market'],
    themes=['family-office', 'property', 'hnw', 'hong-kong'],
    tags=['家族辦公室', '中環商舖', '協成行', '瑞士', '物業投資'],
))

print('part3 items:', len(NEW))
json.dump(NEW, open('/tmp/_new_part3.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
