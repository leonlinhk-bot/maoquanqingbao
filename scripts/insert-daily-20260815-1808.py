#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert daily collected items (2026-08-15 18:08 run) into live-items.json + update last-check.json."""
import json
from pathlib import Path
from datetime import datetime, timezone, timedelta

ROOT = Path(__file__).resolve().parent.parent
LIVE = ROOT / 'data/live-items.json'
LASTCHECK = ROOT / 'data/last-check.json'
HKT = timezone(timedelta(hours=8))
INGESTED = datetime.now(HKT).isoformat(timespec='seconds')


def item(id_, score, verify, tier, key, title_sc, title_tc, sum_sc, sum_tc,
         why_sc, why_tc, actions, roles, src_sc, lang, boards, themes,
         tags_sc, tags_tc, kind, published, url):
    return {
        "id": id_, "clusterCount": 1, "score": score, "verifyStatus": verify,
        "sourceTier": tier, "sourceKey": key,
        "title": {"sc": title_sc, "tc": title_tc},
        "summary": {"sc": sum_sc, "tc": sum_tc},
        "why": {"sc": why_sc, "tc": why_tc},
        "actions": actions, "rolesImpact": roles,
        "source": {"sc": src_sc, "lang": lang},
        "boards": boards, "themes": themes,
        "tags": {"sc": tags_sc, "tc": tags_tc},
        "contentKind": kind, "publishedAt": published, "originalUrl": url,
        "ingestedAt": INGESTED,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False, "evergreen": False,
    }


def L(sc, tc):
    return {"sc": sc, "tc": tc}


new_items = [
    # 1. IA plans to redefine "Mainland visitors" client definition (SCMP + Ming Pao via GMT EIGHT)
    item(
        "scmp-ia-mainland-client-definition-20260815", 85, "pending", "official",
        "scmp",
        "保监局拟重新界定「内地访客」身份定义 下季咨询 非内地户籍人士或可免亲身来港投保",
        "保監局擬重新界定「內地訪客」身份定義 下季諮詢 非內地戶籍人士或可免親身來港投保",
        "据南华早报及明报报道，保监局执行董事Gordon Leung透露，局方正计划重新界定「内地访客」投保人身份定义。现行规例要求内地居民须亲身来港签署投保文件；新定义下，非内地户籍人士（如旅居海外的华人）或可毋须亲身来港购买保险，被视为吸引海外华人高端客户的重要举措。正式咨询拟于下季度展开，客户定义指引及相关规例料年内出台。[EN原文]",
        "據南華早報及明報報道，保監局執行董事Gordon Leung透露，局方正計劃重新界定「內地訪客」投保人身份定義。現行規例要求內地居民須親身來港簽署投保文件；新定義下，非內地戶籍人士（如旅居海外的華人）或可毋須親身來港購買保險，被視為吸引海外華人高端客戶的重要舉措。正式諮詢擬於下季度展開，客戶定義指引及相關規例料年內出台。[EN原文]",
        "内地访客新单是香港寿险增长引擎，「身份定义」重划直接改变MCV客群边界与销售流程，是比征税更根本的渠道变量，咨询落地进度值得持续跟踪。",
        "內地訪客新單是香港壽險增長引擎，「身份定義」重劃直接改變MCV客群邊界與銷售流程，是比徵稅更根本的渠道變量，諮詢落地進度值得持續跟蹤。",
        {"front": {}, "midback": L("MCV定义重划=客群边界变量", "MCV定義重劃=客群邊界變量"), "lead": L("咨询下季启动=政策节奏锚点", "諮詢下季啟動=政策節奏錨點"), "cross": L("海外华人客群=渠道新想象", "海外華人客群=渠道新想象")},
        {"front": 0, "midback": 2, "lead": 2, "cross": 2},
        "南华早报SCMP（据明报报道）", "en",
        ["reg"], ["reg", "mcv"],
        ["保监局", "内地访客", "MCV", "身份定义", "咨询"], ["保監局", "內地訪客", "MCV", "身份定義", "諮詢"],
        "news", "2026-08-15T00:00:00+08:00",
        "https://www.scmp.com/business/banking-finance/article/3364040/hong-kongs-insurance-authority-aims-broaden-regional-clientele-base-reappointed-ceo",
    ),
    # 2. NFRA Q2 2026 banking & insurance regulatory indicators (official stats)
    item(
        "nfra-q2-insurance-indicators-20260814", 85, "verified", "official",
        "nfra",
        "金融监管总局：二季度末保险业总资产43.9万亿元 较年初增6.2% 综合偿付能力充足率180.6%",
        "金融監管總局：二季度末保險業總資產43.9萬億元 較年初增6.2% 綜合償付能力充足率180.6%",
        "金融监管总局8月14日发布2026年二季度银行业保险业主要监管指标：二季度末保险公司及保险资管公司总资产43.9万亿元，较年初增长6.2%，其中人身险公司38.7万亿元；上半年原保险保费收入3.9万亿元，同比增长3.2%，新增保单件数668亿件、增长27.4%。保险公司平均综合偿付能力充足率180.6%、核心偿付能力充足率133.5%，均高于监管标准。",
        "金融監管總局8月14日發佈2026年二季度銀行業保險業主要監管指標：二季度末保險公司及保險資管公司總資產43.9萬億元，較年初增長6.2%，其中人身險公司38.7萬億元；上半年原保險保費收入3.9萬億元，同比增長3.2%，新增保單件數668億件、增長27.4%。保險公司平均綜合償付能力充足率180.6%、核心償付能力充足率133.5%，均高於監管標準。",
        "内地行业总盘子、保费增速与偿付能力数据是判断行业景气与监管空间的基准盘，也为评估内地客资金实力与购买力提供宏观参照。",
        "內地行業總盤子、保費增速與償付能力數據是判斷行業景氣與監管空間的基準盤，也為評估內地客資金實力與購買力提供宏觀參照。",
        {"front": {}, "midback": L("行业总资产增速=景气温度计", "行業總資產增速=景氣溫度計"), "lead": {}, "cross": L("偿付能力=政策空间参照", "償付能力=政策空間參照")},
        {"front": 0, "midback": 2, "lead": 1, "cross": 1},
        "国家金融监督管理总局（中国经济网/证券日报转载）", "zh",
        ["reg"], ["reg", "stats"],
        ["金融监管总局", "保险业", "总资产", "偿付能力", "保费收入"], ["金融監管總局", "保險業", "總資產", "償付能力", "保費收入"],
        "stats", "2026-08-14T18:25:00+08:00",
        "http://www.ce.cn/xwzx/gnsz/gdxw/202608/t20260815_3148603.shtml",
    ),
    # 3. HashKey x YF Life (万通保险) first HKDAP real transaction
    item(
        "stheadline-hashkey-yflife-hkdap-20260814", 75, "verified", "insurer",
        "stheadline",
        "HashKey与万通保险完成港元稳定币HKDAP首笔真实交易 保费结算或由2-3日缩至近实时",
        "HashKey與萬通保險完成港元穩定幣HKDAP首筆真實交易 保費結算或由2-3日縮至近實時",
        "HashKey（3887）宣布旗下持牌平台HashKey Exchange与万通保险国际完成香港首个受规管港元稳定币HKDAP的真实交易，以真实资金走完申购及赎回全流程。HKDAP由持牌发行人碇点金融科技发行，HashKey为主要认可分销商。测试显示HKDAP链上支付保费可近实时到帐，较传统2-3个工作日大幅缩短；万通保险计划未来支持客户以HKDAP缴付保费，力争成为首批支持该支付的保司之一。",
        "HashKey（3887）宣佈旗下持牌平台HashKey Exchange與萬通保險國際完成香港首個受規管港元穩定幣HKDAP的真實交易，以真實資金走完申購及贖回全流程。HKDAP由持牌發行人碇點金融科技發行，HashKey為主要認可分銷商。測試顯示HKDAP鏈上支付保費可近實時到帳，較傳統2-3個工作日大幅縮短；萬通保險計劃未來支持客戶以HKDAP繳付保費，力爭成為首批支持該支付的保司之一。",
        "受规管稳定币首次进入香港保险支付场景，标志数字资产与传统保险资金流打通落地，是观察港险支付与产品数字化的前沿样本。",
        "受規管穩定幣首次進入香港保險支付場景，標誌數字資產與傳統保險資金流打通落地，是觀察港險支付與產品數字化的前沿樣本。",
        {"front": {}, "midback": L("稳定币支付=保费流程数字化", "穩定幣支付=保費流程數字化"), "lead": {}, "cross": L("HKDAP场景=港府Web3落地实证", "HKDAP場景=港府Web3落地實證")},
        {"front": 0, "midback": 2, "lead": 1, "cross": 2},
        "星岛头条（HashKey/万通保险公告）", "zh",
        ["insurtech"], ["insurtech", "product"],
        ["HashKey", "万通保险", "HKDAP", "稳定币", "保费支付"], ["HashKey", "萬通保險", "HKDAP", "穩定幣", "保費支付"],
        "news", "2026-08-14T21:22:00+08:00",
        "https://www.stheadline.com/zh-hans/realtime-finance/3604503/HashKey%E4%B8%8E%E4%B8%87%E9%80%9A%E4%BF%9D%E9%99%A9%E5%AE%8C%E6%88%90%E6%B8%AF%E5%85%83%E7%A8%B3%E5%AE%9A%E5%B8%81HKDAP%E7%9C%9F%E5%AE%9E%E4%BA%A4%E6%98%93-%E6%9C%AA%E6%9D%A5%E7%A0%94%E6%94%AF%E6%8F%B4%E4%BA%A4%E4%BF%9D%E8%B4%B9",
    ),
    # 4. FWD (富卫) takes 20% of mainland national brokerage Juntian
    item(
        "toutiao-fwd-juntian-broker-20260815", 75, "pending", "insurer",
        "toutiao",
        "富卫经「富卫财务策划」入股内地全国性保险经纪隽天20% 李泽楷布局内地渠道",
        "富衛經「富衛財務策劃」入股內地全國性保險經紀雋天20% 李澤楷佈局內地渠道",
        "据天眼查工商信息，2026年8月隽天保险经纪（上海）股东名单新增港资「富卫财务策划有限公司」，持股20%。隽天成立于2012年，持全国性保险经纪牌照、销售网络成熟；分析指富卫以20%参股规避外资控股红线与牌照审批门槛，属轻资产探路内地中介市场，反映香港本土红利递减下富卫加码内地渠道布局。",
        "據天眼查工商信息，2026年8月雋天保險經紀（上海）股東名單新增港資「富衛財務策劃有限公司」，持股20%。雋天成立於2012年，持全國性保險經紀牌照、銷售網絡成熟；分析指富衛以20%參股規避外資控股紅線與牌照審批門檻，屬輕資產探路內地中介市場，反映香港本土紅利遞減下富衛加碼內地渠道佈局。",
        "港资险企参股内地持牌中介的架构样本：20%持股既不触碰外资红线又可合规接入全国经纪渠道，是观察富卫内地战略与跨境中介监管尺度的窗口。",
        "港資險企參股內地持牌中介的架構樣本：20%持股既不觸碰外資紅線又可合規接入全國經紀渠道，是觀察富衛內地戰略與跨境中介監管尺度的窗口。",
        {"front": {}, "midback": L("20%参股=外资渠道探路范式", "20%參股=外資渠道探路範式"), "lead": {}, "cross": L("内地经纪牌照=稀缺资源", "內地經紀牌照=稀缺資源")},
        {"front": 0, "midback": 2, "lead": 1, "cross": 2},
        "钛媒体APP（今日头条，据天眼查）", "zh",
        ["insurer"], ["market", "distribution"],
        ["富卫", "隽天", "保险经纪", "参股", "内地市场"], ["富衛", "雋天", "保險經紀", "參股", "內地市場"],
        "news", "2026-08-15T12:57:26+08:00",
        "http://m.toutiao.com/group/7674118008847057448/",
    ),
    # 5. 豹变 deep-dive on 20% offshore insurance tax enforcement
    item(
        "toutiao-baobian-tax-20260815", 64, "verified", "media",
        "toutiao",
        "深度：港险补税20%风声紧但「子弹还在飞」 各地执行标准尚未统一",
        "深度：港險補稅20%風聲緊但「子彈還在飛」 各地執行標準尚未統一",
        "豹变8月15日发文复盘港险补税风波：8月初杭州、北京出现投保人因香港保单收益被要求补缴20%税款的个案，8月6日友邦收跌5.92%、单日市值蒸发逾400亿港元，保诚跌4.57%。报道引述从业者与税务律师指，港险补税最早可追溯至2018年CRS信息交换启动后，个案此前已有（如2024年湖北投保人被追缴2022-2023年境外所得），惟各地对如何认定、如何计税尚无统一明确标准，市场恐慌或超事件本身影响。",
        "豹變8月15日發文復盤港險補稅風波：8月初杭州、北京出現投保人因香港保單收益被要求補繳20%稅款的個案，8月6日友邦收跌5.92%、單日市值蒸發逾400億港元，保誠跌4.57%。報道引述從業者與稅務律師指，港險補稅最早可追溯至2018年CRS信息交換啟動後，個案此前已有（如2024年湖北投保人被追繳2022-2023年境外所得），惟各地對如何認定、如何計稅尚無統一明確標準，市場恐慌或超事件本身影響。",
        "在监管与官方表态之外补上「执行层」视角：CRS追溯、个案税基认定与各地标准不一，是判断港险征税实际落地节奏的关键信息面。",
        "在監管與官方表態之外補上「執行層」視角：CRS追溯、個案稅基認定與各地標準不一，是判斷港險徵稅實際落地節奏的關鍵信息面。",
        {"front": {}, "midback": L("执行标准未统一=落地变量", "執行標準未統一=落地變量"), "lead": L("CRS追溯=存量保单风险坐标", "CRS追溯=存量保單風險座標"), "cross": {}},
        {"front": 0, "midback": 2, "lead": 2, "cross": 1},
        "豹变（今日头条）", "zh",
        ["market"], ["reg", "market"],
        ["港险", "补税", "20%", "CRS", "执行标准"], ["港險", "補稅", "20%", "CRS", "執行標準"],
        "news", "2026-08-15T08:00:00+08:00",
        "http://m.toutiao.com/group/7673890688060097074/",
    ),
]


def main():
    data = json.loads(LIVE.read_text(encoding='utf-8'))
    items = data['items']

    existing_ids = {i['id'] for i in items}
    existing_urls = {i.get('originalUrl', '') for i in items}
    added = []
    for it in new_items:
        if it['id'] in existing_ids or it['originalUrl'] in existing_urls:
            print(f"SKIP duplicate: {it['id']}")
            continue
        added.append(it)

    if not added:
        print("Nothing to add.")
        return

    items[0:0] = added
    data['items'] = items
    data['meta']['itemCount'] = len(items)
    data['meta']['generatedAt'] = INGESTED
    data['meta']['windowNote'] = {
        "sc": f"本库{len(items)}条。",
        "tc": f"本庫{len(items)}條。"
    }
    LIVE.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding='utf-8')

    # update last-check.json: all source timestamps -> now
    lc = json.loads(LASTCHECK.read_text(encoding='utf-8'))
    lc['lastCheck'] = INGESTED
    for k in lc['sources']:
        lc['sources'][k]['last'] = INGESTED
    LASTCHECK.write_text(json.dumps(lc, ensure_ascii=False, indent=2), encoding='utf-8')

    print(f"INSERTED {len(added)} items; total now {len(items)}")
    for it in added:
        print(' +', it['id'], '|', it['sourceTier'], it['score'], '|', it['publishedAt'])


if __name__ == '__main__':
    main()
