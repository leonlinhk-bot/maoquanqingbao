#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append 2026-11-02 new items to data/live-items.json (prepend, newest first)."""
import json, datetime

PATH = '/Users/leonliang/maoquanqingbao/data/live-items.json'
NOW = '2026-11-02T10:40:00+08:00'

def mk(id, pub, url, skey, tier, score, kind, boards, themes, title, summ, why,
       tags_sc, tags_tc, acts, roles, src_sc, src_name, src_date, lang, vstat, short_sc, short_tc):
    return {
        "id": id,
        "publishedAt": pub,
        "originalUrl": url,
        "sourceKey": skey,
        "sourceTier": tier,
        "score": score,
        "contentKind": kind,
        "boards": boards,
        "themes": themes,
        "title": {"sc": title[0], "tc": title[1]},
        "summary": {"sc": summ[0], "tc": summ[1]},
        "why": {"sc": why[0], "tc": why[1]},
        "tags": {"sc": tags_sc, "tc": tags_tc},
        "actions": {
            "front": {"sc": acts[0][0], "tc": acts[0][1]},
            "midback": {"sc": acts[1][0], "tc": acts[1][1]},
            "lead": {"sc": acts[2][0], "tc": acts[2][1]},
            "cross": {"sc": acts[3][0], "tc": acts[3][1]},
        },
        "rolesImpact": {"front": roles[0], "midback": roles[1], "lead": roles[2], "cross": roles[3]},
        "source": {"sc": src_sc, "tc": src_sc, "name": src_name, "date": src_date, "lang": lang},
        "lang": lang,
        "verifyStatus": vstat,
        "clusterCount": 1,
        "ingestedAt": NOW,
        "summaryShort": {"sc": short_sc, "tc": short_tc},
    }

items = []

items.append(mk(
    "iaasia-prudential-mastercard-direct-billing-20261102",
    "2026-11-02T05:15:00+08:00",
    "https://insuranceasia.com/insurance/news/prudential-hong-kong-removes-upfront-payments-eligible-care",
    "insuranceasia", "media", 72, "news",
    ["product", "tech"],
    ["医疗理赔", "直接结算", "支付科技", "客户体验"],
    ("保诚香港联同 MediConCen 与万事达推医疗费用直接结算：合资格开支获批后以虚拟卡直付诊所医院，客户免垫付、免事后索偿",
     "保誠香港聯同 MediConCen 與萬事達推醫療費用直接結算：合資格開支獲批後以虛擬卡直付診所醫院，客戶免墊付、免事後索償"),
    ("保诚香港与本地初创 MediConCen、万事达合作，把预约、费用预先批核与 B2B 付款并入同一流程：合资格医疗开支经保诚批核后，由 MediConCen 以万事达虚拟卡直接向医疗提供者结账，客户毋须先垫付再索偿。诊所端另设专属门户处理个案与结算。Chiron Medical Group 为首家医疗伙伴，未来数月扩展至更多诊所、医院与医疗网络。[EN原文]",
     "保誠香港與本地初創 MediConCen、萬事達合作，把預約、費用預先批核與 B2B 付款併入同一流程：合資格醫療開支經保誠批核後，由 MediConCen 以萬事達虛擬卡直接向醫療提供者結賬，客戶毋須先墊付再索償。診所端另設專屬門戶處理個案與結算。Chiron Medical Group 為首家醫療夥伴，未來數月擴展至更多診所、醫院與醫療網絡。[EN原文]"),
    ("理赔体验是客户拿港险与内地险对比时最常提的一项；「免垫付」若铺开到主流医院网络，前线讲医疗险就多一个可验证的卖点，也少掉一半「先垫付、后交单」的指导工作量。目前仅一家医疗集团落地，谈卖点要说明覆盖范围。",
     "理賠體驗是客戶拿港險與內地險對比時最常提的一項；「免墊付」若鋪開到主流醫院網絡，前線講醫療險就多一個可驗證的賣點，也少掉一半「先墊付、後交單」的指導工作量。目前僅一家醫療集團落地，談賣點要說明覆蓋範圍。"),
    ["保诚香港", "万事达", "MediConCen", "医疗直付", "免垫付", "理赔体验"],
    ["保誠香港", "萬事達", "MediConCen", "醫療直付", "免墊付", "理賠體驗"],
    [("客户问「住院要不要先自己付钱」时，按此说明目前仅限合资格开支与已加入网络的医疗机构，不代表全网络通用", "客戶問「住院要不要先自己付錢」時，按此說明目前僅限合資格開支與已加入網絡的醫療機構，不代表全網絡通用"),
     ("整理医疗网络直付名单，标注已开通与未开通机构", "整理醫療網絡直付名單，標註已開通與未開通機構"),
     ("团队简报：理赔体验作为医疗险差异化", "團隊簡報：理賠體驗作為醫療險差異化"),
     ("待保诚官网新闻稿发布后补原始链接与生效日期", "待保誠官網新聞稿發布後補原始連結與生效日期")],
    (2, 1, 1, 1),
    "Insurance Asia 2026-11-02", "insuranceasia", "2026-11-02", "en", "verified",
    "保诚香港与 MediConCen、万事达合作，合资格医疗开支获批后由虚拟卡直接向医疗提供者结账，客户免垫付、免事后索偿。",
    "保誠香港與 MediConCen、萬事達合作，合資格醫療開支獲批後由虛擬卡直接向醫療提供者結賬，客戶免墊付、免事後索償。"))

items.append(mk(
    "iaasia-fitch-ai-disruption-score-20261102",
    "2026-11-02T05:00:00+08:00",
    "https://insuranceasia.com/insurance/in-focus/insurers-face-ai-competition-technology-firms-target-retail",
    "insuranceasia", "media", 74, "news",
    ["tech", "market"],
    ["AI冲击", "信用评级", "分销格局", "再保模型"],
    ("惠誉AI压力测试：保险各子板块业务中断评分同为20（五年期「中度」），零售险受科技公司冲击大于商业险、再保面临定价模型失真",
     "惠譽AI壓力測試：保險各子板塊業務中斷評分同為20（五年期「中度」），零售險受科技公司衝擊大於商業險、再保面臨定價模型失真"),
    ("惠誉把AI纳入五年期信用压力测试，对全部保险子板块给出业务中断评分20（0-100，越高越差），判断对评级影响有限。护城河来自监管与资本要求、既有分销网络、以及保单数据与客户关系。但零售险产品更标准化、客户偏好变化快，被科技公司以新触达方式绕过分销的风险高于商业险；再保较少受「中介角色被削弱」影响，却可能因风险相关性变化令历史数据与模型失准，导致定价与准备金偏差。[EN原文]",
     "惠譽把AI納入五年期信用壓力測試，對全部保險子板塊給出業務中斷評分20（0-100，越高越差），判斷對評級影響有限。護城河來自監管與資本要求、既有分銷網絡、以及保單數據與客戶關係。但零售險產品更標準化、客戶偏好變化快，被科技公司以新觸達方式繞過分銷的風險高於商業險；再保較少受「中介角色被削弱」影響，卻可能因風險相關性變化令歷史數據與模型失準，導致定價與準備金偏差。[EN原文]"),
    ("给「AI会不会取代代理人」一个可引用的量化锚：评级机构把五年内定为中度冲击，并把数据与分销网络列为护城河。对内训与客户沟通都比「AI取代一切」的极端说法站得住，也提醒零售标准化的产品线最先被切。",
     "給「AI會不會取代代理人」一個可引用的量化錨：評級機構把五年內定為中度衝擊，並把數據與分銷網絡列為護城河。對內訓與客戶溝通都比「AI取代一切」的極端說法站得住，也提醒零售標準化的產品線最先被切。"),
    ["惠誉", "AI冲击", "压力测试", "零售保险", "分销", "信用评级"],
    ["惠譽", "AI衝擊", "壓力測試", "零售保險", "分銷", "信用評級"],
    [("客户问AI会不会让代理人消失：引用「五年内中度、评级影响有限」，并说明护城河在数据与关系", "客戶問AI會不會讓代理人消失：引用「五年內中度、評級影響有限」，並說明護城河在數據與關係"),
     ("把评分口径与三大不利情景（过度投资／资产减值／业务中断）存入培训素材", "把評分口徑與三大不利情景（過度投資／資產減值／業務中斷）存入培訓素材"),
     ("团队简报：标准化零售产品最先被科技公司切入", "團隊簡報：標準化零售產品最先被科技公司切入"),
     ("", "")],
    (2, 1, 2, 0),
    "Insurance Asia 2026-11-02", "insuranceasia", "2026-11-02", "en", "verified",
    "惠誉五年期AI压力测试对全部保险子板块给出业务中断评分20，属中度；零售险受科技公司绕过分销的冲击大于商业险。",
    "惠譽五年期AI壓力測試對全部保險子板塊給出業務中斷評分20，屬中度；零售險受科技公司繞過分銷的衝擊大於商業險。"))

items.append(mk(
    "ian-sirc-2026-hk-ils-pcc-20261102",
    "2026-11-02T07:30:00+08:00",
    "https://insuranceasianews.com/softening-rates-hong-kongs-ils-ambitions-indias-opening-market-to-dominate-in-singapore/",
    "insuranceasianews", "media", 66, "news",
    ["market", "family"],
    ["ILS", "专属自保", "另类风险转移", "区域竞争"],
    ("新加坡SIRC本周登场：续保费率下行、香港做区域再保与另类风险转移中心的野心、印度经Gift City开放再保成三大议题",
     "新加坡SIRC本週登場：續保費率下行、香港做區域再保與另類風險轉移中心的野心、印度經Gift City開放再保成三大議題"),
    ("InsuranceAsia News 会前分析列出本周新加坡国际再保险会议（SIRC）焦点：一是传统与另类资本充裕下，续保不仅压价还要求放宽附着点、多年期与结构化方案；二是香港争取成为区域再保与另类风险转移枢纽——港府9月已提出引入保护单元公司（PCC）架构以降低设立自保与发行ILS的成本，并拟检讨ILS投资者限制、扩大巨灾风险转移容量；三是印度经Gift City开放再保，2025-26财年该地再保费逾6.08亿美元、增逾四倍。[EN原文]",
     "InsuranceAsia News 會前分析列出本週新加坡國際再保險會議（SIRC）焦點：一是傳統與另類資本充裕下，續保不僅壓價還要求放寬附著點、多年期與結構化方案；二是香港爭取成為區域再保與另類風險轉移樞紐——港府9月已提出引入保護單元公司（PCC）架構以降低設立自保與發行ILS的成本，並擬檢討ILS投資者限制、擴大巨災風險轉移容量；三是印度經Gift City開放再保，2025-26財年該地再保費逾6.08億美元、增逾四倍。[EN原文]"),
    ("香港的PCC与ILS是家办与高客「非保单」配置的入口，也是跟新加坡抢同一批资本的故事线。可用作区域叙事素材；但PCC仍是9月的政策提案、未落地，对客户讲必须说清「拟引入」。",
     "香港的PCC與ILS是家辦與高客「非保單」配置的入口，也是跟新加坡搶同一批資本的故事線。可用作區域敘事素材；但PCC仍是9月的政策提案、未落地，對客戶講必須說清「擬引入」。"),
    ["SIRC", "ILS", "PCC", "专属自保", "香港", "新加坡", "Gift City"],
    ["SIRC", "ILS", "PCC", "專屬自保", "香港", "新加坡", "Gift City"],
    [("", ""),
     ("把港府9月PCC/ILS提案列入「待落地政策」跟踪表，标状态=咨询/提案", "把港府9月PCC/ILS提案列入「待落地政策」跟蹤表，標狀態=諮詢/提案"),
     ("家办客户区域叙事：香港 vs 新加坡的另类风险转移定位", "家辦客戶區域敘事：香港 vs 新加坡的另類風險轉移定位"),
     ("关注SIRC会后是否有PCC细则或ILS税务安排新表述", "關注SIRC會後是否有PCC細則或ILS稅務安排新表述")],
    (0, 2, 2, 1),
    "InsuranceAsia News 2026-11-02", "insuranceasianews", "2026-11-02", "en", "verified",
    "SIRC本周在新加坡举行，焦点包括续保费率下行、香港以PCC与ILS争取成为另类风险转移枢纽、印度经Gift City开放再保。",
    "SIRC本週在新加坡舉行，焦點包括續保費率下行、香港以PCC與ILS爭取成為另類風險轉移樞紐、印度經Gift City開放再保。"))

items.append(mk(
    "sunlife-my-sunlife-migration-20261102",
    "2026-11-02T00:00:00+08:00",
    "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2026/",
    "sunlife", "insurer", 76, "notice",
    ["insurer"],
    ["系统升级", "客户服务", "强积金"],
    ("永明：My Sun Life HK 与 Sun Life MPF 应用今日18:00起停服至明日08:00　迁移至全新 My Sunlife Hong Kong",
     "永明：My Sun Life HK 與 Sun Life MPF 應用今日18:00起停服至明日08:00　遷移至全新 My Sunlife Hong Kong"),
    ("永明香港公告，为推出全新 My Sunlife Hong Kong，现有 My Sun Life HK 与 Sun Life MPF 手机应用及网上服务于2026年11月2日18:00至11月3日08:00暂停。恢复后 My Sun Life HK 用户更新至最新版本，Sun Life MPF 用户改下载全新应用，两者均沿用原有帐户登入。公告建议有需要者提前办理相关服务。",
     "永明香港公告，為推出全新 My Sunlife Hong Kong，現有 My Sun Life HK 與 Sun Life MPF 手機應用及網上服務於2026年11月2日18:00至11月3日08:00暫停。恢復後 My Sun Life HK 用戶更新至最新版本，Sun Life MPF 用戶改下載全新應用，兩者均沿用原有帳戶登入。公告建議有需要者提前辦理相關服務。"),
    ("今天就能用的一条：客户若今晚要查保单、看强积金或赶在月内递交申请，先提醒避开18:00-次日08:00窗口；停服期间客户看到「登入不了」别当成系统故障或帐户出事。",
     "今天就能用的一條：客戶若今晚要查保單、看強積金或趕在月內遞交申請，先提醒避開18:00-次日08:00窗口；停服期間客戶看到「登入不了」別當成系統故障或帳戶出事。"),
    ["永明", "Sun Life MPF", "应用迁移", "停服", "强积金"],
    ["永明", "Sun Life MPF", "應用遷移", "停服", "強積金"],
    [("今日18:00前提醒有强积金/保单查询或申请在办的客户先办完，并说明停服至明早8时", "今日18:00前提醒有強積金/保單查詢或申請在辦的客戶先辦完，並說明停服至明早8時"),
     ("更新客户服务常见问题：新应用名称与登入方式", "更新客戶服務常見問題：新應用名稱與登入方式"),
     ("团队通知：今晚停服窗口，避免误报系统故障", "團隊通知：今晚停服窗口，避免誤報系統故障"),
     ("", "")],
    (2, 1, 1, 0),
    "永明香港 2026-11-02", "sunlife", "2026-11-02", "zh", "verified",
    "永明香港为迁移至 My Sunlife Hong Kong，My Sun Life HK 与 Sun Life MPF 应用及网上服务11月2日18:00至3日08:00暂停。",
    "永明香港為遷移至 My Sunlife Hong Kong，My Sun Life HK 與 Sun Life MPF 應用及網上服務11月2日18:00至3日08:00暫停。"))

items.append(mk(
    "ian-cyclone-arnab-andhra-losses-20261101",
    "2026-11-01T16:17:00+08:00",
    "https://insuranceasianews.com/cyclone-arnab-leads-to-us480m-in-losses-in-indias-andhra-pradesh/",
    "insuranceasianews", "media", 60, "news",
    ["market"],
    ["巨灾", "气候变化", "再保定价"],
    ("气旋Arnab袭印度安得拉邦　邦政府估损失约4.8亿美元",
     "氣旋Arnab襲印度安得拉邦　邦政府估損失約4.8億美元"),
    ("据安得拉邦首席部长 N. Chandrababu Naidu 表述，气旋 Arnab 在该邦造成约4.8亿美元损失；该数字见于 Aon 每周巨灾报告的报道，原文置于付费墙后，仅首段可核。今年亚太巨灾损失整体偏温和、缺大型登陆飓风，但次生灾害与累积性损失仍是再保定价焦点。[EN原文]",
     "據安得拉邦首席部長 N. Chandrababu Naidu 表述，氣旋 Arnab 在該邦造成約4.8億美元損失；該數字見於 Aon 每週巨災報告的報道，原文置於付費牆後，僅首段可核。今年亞太巨災損失整體偏溫和、缺大型登陸颶風，但次生災害與累積性損失仍是再保定價焦點。[EN原文]"),
    ("对前线没有直接动作，作用是给「今年损失偏轻、再保费率继续软」这个判断补一个注脚。做大型商业险转介的，可在谈费率环境时引用，但别把单一邦的估值当成行业损失口径。",
     "對前線沒有直接動作，作用是給「今年損失偏輕、再保費率繼續軟」這個判斷補一個註腳。做大型商業險轉介的，可在談費率環境時引用，但別把單一邦的估值當成行業損失口徑。"),
    ["气旋Arnab", "印度", "巨灾损失", "再保定价"],
    ["氣旋Arnab", "印度", "巨災損失", "再保定價"],
    [("", ""),
     ("费率环境素材：年度巨灾损失与再保定价对照", "費率環境素材：年度巨災損失與再保定價對照"),
     ("", ""),
     ("", "")],
    (0, 1, 1, 0),
    "InsuranceAsia News 2026-11-01", "insuranceasianews", "2026-11-01", "en", "pending",
    "安得拉邦首席部长称气旋Arnab造成约4.8亿美元损失，数字源自Aon每周巨灾报告相关报道；原文付费墙后仅首段可核。",
    "安得拉邦首席部長稱氣旋Arnab造成約4.8億美元損失，數字源自Aon每週巨災報告相關報道；原文付費牆後僅首段可核。"))

d = json.load(open(PATH))
existing = d['items']
existing_ids = {i['id'] for i in existing}
new = [i for i in items if i['id'] not in existing_ids]
print('to add:', len(new))
d['items'] = new + existing
d['meta']['generatedAt'] = NOW
d['meta']['itemCount'] = len(d['items'])
d['meta']['windowNote'] = {"sc": f"本库{len(d['items'])}条。", "tc": f"本庫{len(d['items'])}條。"}
json.dump(d, open(PATH, 'w'), ensure_ascii=False, indent=1)
print('total now:', len(d['items']))
for i in new:
    print(' +', i['publishedAt'][:16], i['sourceKey'], i['id'])
