import json, copy, datetime

P='/Users/leonliang/maoquanqingbao/data/live-items.json'
HKT=datetime.timezone(datetime.timedelta(hours=8))
now=datetime.datetime.now(HKT).replace(second=0,microsecond=0).isoformat()

def mk(id_, pub, url, skey, tier, score, boards, themes, tsc, ttc, ssc, stc, wsc, wtc, tags_sc, tags_tc, acts, roles, lang='en', name=None, date=None, kind='news', status='verified', cluster=1):
    def a(v): return {'sc':v,'tc':v}
    src={'sc':(name or skey)+' '+ (date or pub[:10]), 'tc':(name or skey)+' '+(date or pub[:10]), 'name':name or skey, 'date':date or pub[:10], 'lang':lang}
    short_sc=ssc if len(ssc)<=108 else ssc[:107]+'…'
    short_tc=stc if len(stc)<=108 else stc[:107]+'…'
    return {
        'id':id_,'clusterCount':cluster,'verifyStatus':status,'contentKind':kind,
        'ingestedAt':now,'publishedAt':pub,'originalUrl':url,'sourceKey':skey,'sourceTier':tier,
        'score':score,'boards':boards,'themes':themes,
        'title':{'sc':tsc,'tc':ttc},'summary':{'sc':ssc,'tc':stc},'why':{'sc':wsc,'tc':wtc},
        'tags':{'sc':tags_sc,'tc':tags_tc},
        'actions':{k:a(v) for k,v in acts.items()},
        'rolesImpact':roles,'source':src,'lang':lang,
        'summaryShort':{'sc':short_sc,'tc':short_tc}
    }

items=[]

items.append(mk(
 'ibm-pingan-ai-82pct-service-20261029','2026-10-29T04:06:00+08:00',
 'https://www.insurancebusinessmag.com/asia/news/breaking-news/ping-ans-ai-now-handles-82-of-customer-service-as-insurer-posts-8-3-profit-rise-595370.aspx',
 'insurancebusinessmag','media',68,['tech'],['AI客服','智能核保','综合成本率'],
 '平安AI接管82%客服：九个月14.8亿次交互　95%寿险保单秒级核保',
 '平安AI接管82%客服：九個月14.8億次交互　95%壽險保單秒級核保',
 '中国平安前三季营运利润1,259亿元、同比升8.3%。AI已承担集团82%客服量，九个月处理14.8亿次交互、91%免人工解决；95%寿险保单秒级核保；产险AI反欺诈减损100.4亿元，综合成本率降至95.6%。9月日均token逾3,300亿，每token成本较去年12月降81%。[EN原文]',
 '中國平安前三季營運利潤1,259億元、同比升8.3%。AI已承擔集團82%客服量，九個月處理14.8億次交互、91%免人工解決；95%壽險保單秒級核保；產險AI反欺詐減損100.4億元，綜合成本率降至95.6%。9月日均token逾3,300億，每token成本較去年12月降81%。[EN原文]',
 '这是目前最完整的「AI铺到哪一步才算见效」公开标尺：客服占比、秒级核保、综合成本率三个数都能对回自家流程。给团队讲AI落地时，用它替代概念性案例；给客户讲时，只讲体验（秒级出单、免等人工），不承诺结果。',
 '這是目前最完整的「AI鋪到哪一步才算見效」公開標尺：客服佔比、秒級核保、綜合成本率三個數都能對回自家流程。給團隊講AI落地時，用它替代概念性案例；給客戶講時，只講體驗（秒級出單、免等人工），不承諾結果。',
 ['平安','AI客服','秒级核保','综合成本率'],['平安','AI客服','秒級核保','綜合成本率'],
 {'front':'客户沟通：AI核保与秒级出单的实际体验','midback':'流程盘点：客服与核保自动化率基准','lead':'团队培训：以平安为标尺设定AI落地KPI','cross':'内地保司AI进度跟踪'},
 {'front':2,'midback':3,'lead':3,'cross':2}
))

items.append(mk(
 'hkma-fed-hold-response-20261029','2026-10-29',
 'https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/10/20261029-3/',
 'hkma','official',85,['market'],['利率环境','港元流动性','保费融资'],
 '金管局回应美联储维持利率3.75%–4%：港美息差持续　套息或令港元逐步回软',
 '金管局回應美聯儲維持利率3.75%–4%：港美息差持續　套息或令港元逐步回軟',
 '美联储维持联邦基金利率目标区间3.75%–4%不变，符合市场预期；会后声明指经济活动强劲、就业稳定但通胀仍偏高。金管局称香港货币与金融市场运作有序，因港美息差明显，套息活动或令港元逐步回软，提醒公众在置业、投资与借贷时管理利率风险。[EN原文]',
 '美聯儲維持聯邦基金利率目標區間3.75%–4%不變，符合市場預期；會後聲明指經濟活動強勁、就業穩定但通脹仍偏高。金管局稱香港貨幣與金融市場運作有序，因港美息差明顯，套息活動或令港元逐步回軟，提醒公眾在置業、投資與借貸時管理利率風險。[EN原文]',
 '保费融资与储蓄险的预缴、分红决策都吃利率。本次按兵不动＋港美息差仍在，意味着「港元拆息短期难快速下行」的判断可以维持——这是跟客户谈「现在要不要锁利率、要不要加杠杆」时的官方口径，也提醒别用「降息在即」做销售话术。',
 '保費融資與儲蓄險的預繳、分紅決策都吃利率。本次按兵不動＋港美息差仍在，意味著「港元拆息短期難快速下行」的判斷可以維持——這是跟客戶談「現在要不要鎖利率、要不要加槓桿」時的官方口徑，也提醒別用「降息在即」做銷售話術。',
 ['美联储','金管局','港元拆息','保费融资'],['美聯儲','金管局','港元拆息','保費融資'],
 {'front':'客户沟通：预缴与保费融资的利率窗口','midback':'研究：港美息差与HIBOR路径','lead':'团队简报：美联储路径与产品定价','cross':'宏观利率与资金流跟踪'},
 {'front':3,'midback':2,'lead':3,'cross':3}
))

items.append(mk(
 'ibm-korea-retirement-misselling-20261029','2026-10-29T04:01:00+08:00',
 'https://www.insurancebusinessmag.com/asia/news/life-insurance/koreas-retirement-insurance-push-raises-misselling-risk-for-older-buyers-academics-warn-595368.aspx',
 'insurancebusinessmag','media',65,['product'],['退休保障','适当性原则','产品披露'],
 '韩国退休险加保障功能　学者警告长者销售误导风险上升',
 '韓國退休險加保障功能　學者警告長者銷售誤導風險上升',
 '韩国寿险公司为长者设计含年金、照护与认知障碍保障的退休产品，但产品越复杂、客户越难理解。65岁以上今年占人口21.6%、2050年料逾40%；公共年金仅覆盖退休夫妇最低生活费的55.4%。学者建议统一披露年金计算方式、利率变动可能与提早退保条款。此前金监院指电视购物渠道误导率达其他渠道三倍。[EN原文]',
 '韓國壽險公司為長者設計含年金、照護與認知障礙保障的退休產品，但產品越複雜、客戶越難理解。65歲以上今年佔人口21.6%、2050年料逾40%；公共年金僅覆蓋退休夫婦最低生活費的55.4%。學者建議統一披露年金計算方式、利率變動可能與提早退保條款。此前金監院指電視購物渠道誤導率達其他渠道三倍。[EN原文]',
 '这是「产品越复杂、披露越要标准化」的现成案例，和香港长者/退休客群面对的多功能保单结构相似。学者列的三项披露（年金怎算、利率会不会变、提早退保成本）可直接当作前线对客解释清单，也是合规复核的检查项。',
 '這是「產品越複雜、披露越要標準化」的現成案例，和香港長者/退休客群面對的多功能保單結構相似。學者列的三項披露（年金怎算、利率會不會變、提早退保成本）可直接當作前線對客解釋清單，也是合規複核的檢查項。',
 ['韩国','退休保险','适当性','披露'],['韓國','退休保險','適當性','披露'],
 {'front':'客户沟通：退休产品三项必讲披露','midback':'合规复核：复杂产品解释清单','lead':'培训素材：长者客群KYC要点','cross':'亚洲监管对误导销售的处理'},
 {'front':3,'midback':3,'lead':2,'cross':2}
))

items.append(mk(
 'ian-scor-bs-apac-specialty-20261029','2026-10-29T07:30:00+08:00',
 'https://insuranceasianews.com/scor-business-solutions-sets-sights-on-profitable-apac-build-out-with-specialty-push/',
 'insuranceasianews','pro',72,['insurer'],['专业险','亚太扩张','承保能力'],
 'Scor Business Solutions 拟12个月内在亚洲铺专业险：海运、网络安全、另类风险',
 'Scor Business Solutions 擬12個月內在亞洲鋪專業險：海運、網絡安全、另類風險',
 '据 InsuranceAsia News，Scor Business Solutions（SBS）计划未来12个月把专业险业务扩展至亚洲，聚焦海运、网络安全与另类风险解决方案，以「有利润的增长」为目标。报道归入「人才」与「数据中心」主题，指向区域承保与团队同步扩建。原文付费墙，仅见导语。[EN原文]',
 '據 InsuranceAsia News，Scor Business Solutions（SBS）計劃未來12個月把專業險業務擴展至亞洲，聚焦海運、網絡安全與另類風險解決方案，以「有利潤的增長」為目標。報道歸入「人才」與「數據中心」主題，指向區域承保與團隊同步擴建。原文付費牆，僅見導語。[EN原文]',
 '再保系专业险平台进亚洲，是香港做「区域风险管理中心」的直接注脚：海运、网络安全、数据中心这几个险种，正是本地经纪能对接的企业险缺口。团队可据此梳理「哪些企业险可以往外找容量」。',
 '再保系專業險平台進亞洲，是香港做「區域風險管理中心」的直接注腳：海運、網絡安全、數據中心這幾個險種，正是本地經紀能對接的企業險缺口。團隊可據此梳理「哪些企業險可以往外找容量」。',
 ['SCOR','专业险','亚太','承保能力'],['SCOR','專業險','亞太','承保能力'],
 {'front':'客户沟通：企业险容量来源','midback':'研究：亚太专业险供给变化','lead':'团队简报：可外找容量的险种清单','cross':'香港区域风险管理中心进展'},
 {'front':1,'midback':3,'lead':2,'cross':3}
))

items.append(mk(
 'ian-elseco-asia-ah-coverholder-20261029','2026-10-29T15:31:00+08:00',
 'https://insuranceasianews.com/elseco-expands-into-asia-with-singapore-ah-lloyds-coverholder-launch/',
 'insuranceasianews','pro',70,['market'],['MGA','意外及健康险','劳合社亚洲'],
 '迪拜专业险MGA elseco 进亚洲：新加坡设劳合社 coverholder　先做意外及健康险',
 '迪拜專業險MGA elseco 進亞洲：新加坡設勞合社 coverholder　先做意外及健康險',
 '迪拜专业险 MGA elseco 进军亚洲，在新加坡设立劳合社亚洲（Lloyd\'s Asia）coverholder「elseco Asia」，先以意外及健康（A&H）业务起步。报道同时标注中国与平安为相关标签，指向亚太 A&H 与航空险的分销与容量布局。原文付费墙，仅见导语。[EN原文]',
 '迪拜專業險 MGA elseco 進軍亞洲，在新加坡設立勞合社亞洲（Lloyd\'s Asia）coverholder「elseco Asia」，先以意外及健康（A&H）業務起步。報道同時標註中國與平安為相關標籤，指向亞太 A&H 與航空險的分銷與容量布局。原文付費牆，僅見導語。[EN原文]',
 'A&H 与跨境医疗是高客服务的邻近赛道：中东资本＋劳合社平台落地新加坡，意味着细分容量与产品供给增加，也可能出现新的分销合作口。对做跨境医疗、团体意外与高额医疗的团队，这是「容量从哪来」的一条线索。',
 'A&H 與跨境醫療是高客服務的鄰近賽道：中東資本＋勞合社平台落地新加坡，意味著細分容量與產品供給增加，也可能出現新的分銷合作口。對做跨境醫療、團體意外與高額醫療的團隊，這是「容量從哪來」的一條線索。',
 ['elseco','MGA','A&H','劳合社亚洲'],['elseco','MGA','A&H','勞合社亞洲'],
 {'front':'客户沟通：跨境医疗保障的容量来源','midback':'研究：亚太A&H新进入者','lead':'团队简报：新加坡MGA生态','cross':'中东资本进亚洲保险'},
 {'front':2,'midback':2,'lead':1,'cross':3}
))

items.append(mk(
 'boclife-h1-2026-results-20261023','2026-10-23',
 'https://www.boclife.com.hk/tc/news/boc-life-delivers-strong-growth-across-key-business-metrics-in-first-half-of2026-standard-new-business-premiums-and-new-business-value-reach-record-highs.html',
 'boclife','insurer',78,['insurer'],['中期业绩','渠道结构','人民币保险'],
 '中银人寿上半年新造标准保费升27%、新造业务价值升56%　人民币业务市占近五成',
 '中銀人壽上半年新造標準保費升27%、新造業務價值升56%　人民幣業務市占近五成',
 '中银人寿公布2026年上半年业绩：新造标准保费同比升27%、新造业务价值升56%，同创历史新高；人民币保险业务连续逾十年市场第一、市占近五成；直接销售渠道新造标准保费升83%，银保升24%、专属代理升20%、经纪升10%。行政总裁邓子平称将深化养老金融与「银行+保险」协同。',
 '中銀人壽公佈2026年上半年業績：新造標準保費同比升27%、新造業務價值升56%，同創歷史新高；人民幣保險業務連續逾十年市場第一、市占近五成；直接銷售渠道新造標準保費升83%，銀保升24%、專屬代理升20%、經紀升10%。行政總裁鄧子平稱將深化養老金融與「銀行+保險」協同。',
 '渠道结构在往银行与直销倾斜（银保+24%、直销+83%），经纪只+10%——这是跟团队谈「经纪的相对位置」时的硬数据，配合保监局上半年统计一起看更有说服力。人民币业务近五成市占，也说明跨境客群的产品偏好仍集中。',
 '渠道結構在往銀行與直銷傾斜（銀保+24%、直銷+83%），經紀只+10%——這是跟團隊談「經紀的相對位置」時的硬數據，配合保監局上半年統計一起看更有說服力。人民幣業務近五成市占，也說明跨境客群的產品偏好仍集中。',
 ['中银人寿','中期业绩','银保渠道','人民币保险'],['中銀人壽','中期業績','銀保渠道','人民幣保險'],
 {'front':'客户沟通：人民币保单的需求基础','midback':'研究：渠道份额此消彼长','lead':'团队简报：上半年同业成绩对照','cross':'银行系保司策略'},
 {'front':2,'midback':3,'lead':3,'cross':2},
 lang='zh', name='boclife', date='2026-10-23', kind='press'
))

d=json.load(open(P))
old=d['items']
ids={i['id'] for i in old}
add=[i for i in items if i['id'] not in ids]
d['items']=add+old
d['meta']['itemCount']=len(d['items'])
d['meta']['generatedAt']=now
n=len(d['items'])
d['meta']['windowNote']={'sc':'本库%d条。'%n,'tc':'本庫%d條。'%n}
json.dump(d,open(P,'w'),ensure_ascii=False,indent=1)
print('added',len(add),'total',n)
for i in add: print(' ',i['publishedAt'],i['id'],len(i['summary']['sc']))
