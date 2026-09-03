#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""每日增量采集 2026-09-03 11:40 cron(补): 插入新条目到 live-items.json 最前, 更新 meta
窗口: 2026-09-02T16:55:00+08:00 (last-check) 之后
本轮新增(6): HKFI回应20%个税传闻(gmt8) + InsuranceAsia 4篇(富瑞友邦/新华银保/瑞再网络险/晨星人保) + InsuranceBusiness 1篇(三星并购Canopius+Principal)
信源覆盖: InsuranceAsia RSS 8新条取4; IA官网(Cloudflare拦截,经doubao/news检索确认无新公告); HKMA官网(顶部仍为9/1 HKICL); AIA/AXA/SunLife官网(无窗口内新公告); Manulife官网(最新9/1后偿票据,窗口外); Pru(检索无新); ibmag 2新条取1; NFRA/FSTB/SCMP(检索无窗口内重大新条目)
"""
import json, datetime

NOW = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
NOW_STR = NOW.strftime('%Y-%m-%dT%H:%M:%S+08:00')

NEW_ITEMS = [
    {
        "id": "hkfi-tax-rumor-response-20260903",
        "clusterCount": 1,
        "score": 63,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "gmteight",
        "title": {
            "sc": "香港保险业联会回应「内地拟对境外保单收益征20%个税」传闻：相关部门未发正式文件 [EN原文]",
            "tc": "香港保險業聯會回應「內地擬對境外保單收益徵20%個稅」傳聞：相關部門未發正式文件 [EN原文]"
        },
        "summary": {
            "sc": "香港保险业联会9月3日回应第一财经：就「内地拟对境外保单收益征20%个税」传闻，指相关部门尚未发布正式政策文件或实施细则，联会正密切跟进、不作猜测评论；并强调客户保障、财富传承与资产配置需求仍强，港险产品设计灵活、货币配置多元，整体仍具吸引力与竞争力。",
            "tc": "香港保險業聯會9月3日回應第一財經：就「內地擬對境外保單收益徵20%個稅」傳聞，指相關部門尚未發布正式政策文件或實施細則，聯會正密切跟進、不作猜測評論；並強調客戶保障、財富傳承與資產配置需求仍強，港險產品設計靈活、貨幣配置多元，整體仍具吸引力與競爭力。"
        },
        "why": {
            "sc": "近期该传闻发酵并拖累港险板块，业界机构首次正式回应：未见官方文件、需求基础未变，有助厘清政策预期、稳定客户与渠道信心，也是回应客户税务疑虑时的重要口径参考。",
            "tc": "近期該傳聞發酵並拖累港險板塊，業界機構首次正式回應：未見官方文件、需求基礎未變，有助釐清政策預期、穩定客戶與渠道信心，也是回應客戶稅務疑慮時的重要口徑參考。"
        },
        "actions": {
            "front": {"sc": "客户对20%个税疑虑的回应口径", "tc": "客戶對20%個稅疑慮的回應口徑"},
            "midback": {},
            "lead": {},
            "cross": {"sc": "跟踪内地对境外保单税务政策动向", "tc": "跟蹤內地對境外保單稅務政策動向"}
        },
        "rolesImpact": {"front": 1, "midback": 0, "lead": 0, "cross": 1},
        "source": {"sc": "GMT EIGHT 快讯（据第一财经报道）", "lang": "en"},
        "boards": ["market"],
        "themes": ["mainland-tax", "cross-border"],
        "tags": {
            "sc": ["香港保险业联会", "HKFI", "20%个税", "境外保单", "传闻回应"],
            "tc": ["香港保險業聯會", "HKFI", "20%個稅", "境外保單", "傳聞回應"]
        },
        "contentKind": "news",
        "publishedAt": "2026-09-03",
        "originalUrl": "https://www.gmt8press.com/flash/detail/1502684",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "aia-hk-hedgefunds-cautious-20260903",
        "clusterCount": 1,
        "score": 63,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insuranceasia",
        "title": {
            "sc": "富瑞：香港对冲基金对友邦新业务价值转审慎 国际长仓视回调为买点 [EN原文]",
            "tc": "富瑞：香港對沖基金對友邦新業務價值轉審慎 國際長倉視回調為買點 [EN原文]"
        },
        "summary": {
            "sc": "富瑞指部分香港对冲基金对友邦新业务价值(VONB)审慎：高基数已拖累首季、料续压第二三季；美国长仓视监管风波后的回调为买入机会，本地资金则观望，双方分歧扩大。友邦次季VONB较共识高0.4%、税后经营溢利高4.1%大致符预期；富瑞上调其2026年每股盈利预测3.5%。",
            "tc": "富瑞指部分香港對沖基金對友邦新業務價值(VONB)審慎：高基數已拖累首季、料續壓第二三季；美國長倉視監管風波後的回調為買入機會，本地資金則觀望，雙方分歧擴大。友邦次季VONB較共識高0.4%、稅後經營溢利高4.1%大致符預期；富瑞上調其2026年每股盈利預測3.5%。"
        },
        "why": {
            "sc": "反映税务传闻扰动下国际长仓与本地对冲基金对友邦估值框架(ROEV对比VONB增速)的分歧，是观察外资如何定价港险龙头监管风险、判断板块情绪的关键信号。",
            "tc": "反映稅務傳聞擾動下國際長倉與本地對沖基金對友邦估值框架(ROEV對比VONB增速)的分歧，是觀察外資如何定價港險龍頭監管風險、判斷板塊情緒的關鍵信號。"
        },
        "actions": {
            "front": {},
            "midback": {},
            "lead": {"sc": "跟踪大行对友邦及港险板块评级观点", "tc": "跟蹤大行對友邦及港險板塊評級觀點"},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 0, "lead": 1, "cross": 0},
        "source": {"sc": "InsuranceAsia 保险亚洲", "lang": "en"},
        "boards": ["insurer"],
        "themes": ["aia", "analyst"],
        "tags": {
            "sc": ["友邦", "富瑞", "对冲基金", "新业务价值", "港股保险"],
            "tc": ["友邦", "富瑞", "對沖基金", "新業務價值", "港股保險"]
        },
        "contentKind": "news",
        "publishedAt": "2026-09-03T06:15:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/aia-growth-concerns-keep-hong-kong-hedge-funds-cautious",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "ncl-bancassurance-margin-20260903",
        "clusterCount": 1,
        "score": 62,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insuranceasia",
        "title": {
            "sc": "新华保险次季新业务价值同比跌8% 银保价值率降至22% 下半年盈利承压 [EN原文]",
            "tc": "新華保險次季新業務價值同比跌8% 銀保價值率降至22% 下半年盈利承壓 [EN原文]"
        },
        "summary": {
            "sc": "新华保险次季新业务价值同比跌8%(首季曾增25%)；银保渠道NBV仅增2%、新业务价值利润率降至22%(同比降16个百分点)，该渠道仍贡献约48%的NBV。CGS国际指其约九成股权投资按公允价值入账，科技股回调或拖累三季度投资收益，料下半年净利润低于上半年228亿元人民币，银保监管不确定性为主要下行风险。",
            "tc": "新華保險次季新業務價值同比跌8%(首季曾增25%)；銀保渠道NBV僅增2%、新業務價值利潤率降至22%(同比降16個百分點)，該渠道仍貢獻約48%的NBV。CGS國際指其約九成股權投資按公允價值入賬，科技股回調或拖累第三季度投資收益，料下半年淨利潤低於上半年228億元人民幣，銀保監管不確定性為主要下行風險。"
        },
        "why": {
            "sc": "内地银保渠道费用管控与股市波动正传导至险企报表：头部银保系寿险价值率下滑、次季NBV转负，是观察内地监管新规实际冲击的典型样本。",
            "tc": "內地銀保渠道費用管控與股市波動正傳導至險企報表：頭部銀保系壽險價值率下滑、次季NBV轉負，是觀察內地監管新規實際衝擊的典型樣本。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "内地银保新规对险企价值率影响跟踪", "tc": "內地銀保新規對險企價值率影響跟蹤"},
            "lead": {"sc": "内地头部寿险业绩与渠道趋势参考", "tc": "內地頭部壽險業績與渠道趨勢參考"},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 1, "cross": 0},
        "source": {"sc": "InsuranceAsia 保险亚洲", "lang": "en"},
        "boards": ["market", "insurer"],
        "themes": ["bancassurance", "mainland"],
        "tags": {
            "sc": ["新华保险", "银保渠道", "新业务价值", "权益投资", "内地寿险"],
            "tc": ["新華保險", "銀保渠道", "新業務價值", "權益投資", "內地壽險"]
        },
        "contentKind": "news",
        "publishedAt": "2026-09-03T06:30:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/new-china-life-bancassurance-margins-fall-amid-rule-risks",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "swissre-cyber-gap-20260903",
        "clusterCount": 1,
        "score": 62,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insuranceasia",
        "title": {
            "sc": "瑞再：2026年全球网络险保费估164亿美元 亚太仅占一成 费率连跌四年 [EN原文]",
            "tc": "瑞再：2026年全球網絡險保費估164億美元 亞太僅佔一成 費率連跌四年 [EN原文]"
        },
        "summary": {
            "sc": "瑞再年度网络报告估计2026年全球网络险保费164亿美元、年复合增长约5%，北美占65%、欧洲21%、亚太仅10%；费率连跌四年，跌幅由13%收窄至5%。AI主要放大既有风险而非创造新损失类型，相关索赔仍有限；保额缺口突出，过去五年年均约10宗大型网络损失超出平均1.2亿美元的保单限额。",
            "tc": "瑞再年度網絡報告估計2026年全球網絡險保費164億美元、年複合增長約5%，北美佔65%、歐洲21%、亞太僅10%；費率連跌四年，跌幅由13%收窄至5%。AI主要放大既有風險而非創造新損失類型，相關索賠仍有限；保額缺口突出，過去五年年均約10宗大型網絡損失超出平均1.2億美元的保單限額。"
        },
        "why": {
            "sc": "网络险费率下行与AI风险敞口扩大并存，亚太渗透率远低于欧美，是企业客户网络保障缺口评估、再保安排与新产品机会的重要基准数据。",
            "tc": "網絡險費率下行與AI風險敞口擴大並存，亞太滲透率遠低於歐美，是企業客戶網絡保障缺口評估、再保安排與新產品機會的重要基準數據。"
        },
        "actions": {
            "front": {"sc": "企业客户网络险缺口沟通素材", "tc": "企業客戶網絡險缺口溝通素材"},
            "midback": {},
            "lead": {"sc": "网络险定价与承保趋势跟踪", "tc": "網絡險定價與承保趨勢跟蹤"},
            "cross": {}
        },
        "rolesImpact": {"front": 1, "midback": 0, "lead": 1, "cross": 0},
        "source": {"sc": "InsuranceAsia 保险亚洲", "lang": "en"},
        "boards": ["tech", "market"],
        "themes": ["cyber", "ai"],
        "tags": {
            "sc": ["瑞再", "网络保险", "网络风险", "AI", "保障缺口"],
            "tc": ["瑞再", "網絡保險", "網絡風險", "AI", "保障缺口"]
        },
        "contentKind": "news",
        "publishedAt": "2026-09-03T05:45:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/cyber-protection-gap-widens-digital-dependence-grows",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "samsung-insurers-ma-canopius-principal-20260903",
        "clusterCount": 1,
        "score": 64,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insurancebusiness",
        "title": {
            "sc": "三星旗下保险公司洽购Canopius余下股权并入股Principal Financial 涉资最高58亿美元 [EN原文]",
            "tc": "三星旗下保險公司洽購Canopius餘下股權並入股Principal Financial 涉資最高58億美元 [EN原文]"
        },
        "summary": {
            "sc": "韩媒引述业界消息：三星火灾海上保险拟以约20亿至22亿美元收购Lloyd's专业承保商Canopius余下60%股权(现持40%，Canopius为覆盖亚太、中东及澳新的最大Lloyd's辛迪加平台)；三星人寿洽购美国Principal Financial约15%股权、涉约36亿至44亿美元，Principal管理约7810亿美元资产。若成事将创韩资金融业最大跨境并购纪录。",
            "tc": "韓媒引述業界消息：三星火災海上保險擬以約20億至22億美元收購Lloyd's專業承保商Canopius餘下60%股權(現持40%，Canopius為覆蓋亞太、中東及澳新的最大Lloyd's辛迪加平台)；三星人壽洽購美國Principal Financial約15%股權、涉約36億至44億美元，Principal管理約7810億美元資產。若成事將創韓資金融業最大跨境併購紀錄。"
        },
        "why": {
            "sc": "韩国头部险企借并购把Lloyd's亚洲最大承保平台收入囊中、并跻身美国退休资产管理巨头主要股东，显示亚洲保险资本出海提速，对Lloyd's平台股权格局及全球退休资产竞争具参考意义。",
            "tc": "韓國頭部險企藉併購把Lloyd's亞洲最大承保平台收入囊中、並躋身美國退休資產管理巨頭主要股東，顯示亞洲保險資本出海提速，對Lloyd's平台股權格局及全球退休資產競爭具參考意義。"
        },
        "actions": {
            "front": {},
            "midback": {},
            "lead": {"sc": "亚洲险企跨境并购动向跟踪", "tc": "亞洲險企跨境併購動向跟蹤"},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 0, "lead": 1, "cross": 0},
        "source": {"sc": "Insurance Business 保险商业", "lang": "en"},
        "boards": ["insurer", "market"],
        "themes": ["ma", "korea"],
        "tags": {
            "sc": ["三星保险", "Canopius", "Principal", "并购", "韩国保险"],
            "tc": ["三星保險", "Canopius", "Principal", "併購", "韓國保險"]
        },
        "contentKind": "news",
        "publishedAt": "2026-09-03",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/samsungs-insurers-plot-record-5-8bn-ukus-buying-spree-588421.aspx",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "picc-life-health-trails-20260903",
        "clusterCount": 1,
        "score": 60,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insuranceasia",
        "title": {
            "sc": "晨星：人保集团寿险健康险新业务价值增速落后同业 长期险保费跌25% [EN原文]",
            "tc": "晨星：人保集團壽險健康險新業務價值增速落後同業 長期險保費跌25% [EN原文]"
        },
        "summary": {
            "sc": "晨星指人保集团上半年寿险、健康险新业务价值增速分别放缓至5%与1%，远低于同业11%-34%：主因依赖银保渠道而监管严控费用、分红险转型偏慢，长期险保费跌25%，料2026年寿险健康险NBV仅中个位数增长。财险端车险综合成本率93.5%、非车94.6%，惟巨灾损失正常化后非车综合成本率2026-2028年料达99%-100%。",
            "tc": "晨星指人保集團上半年壽險、健康險新業務價值增速分別放緩至5%與1%，遠低於同業11%-34%：主因依賴銀保渠道而監管嚴控費用、分紅險轉型偏慢，長期險保費跌25%，料2026年壽險健康險NBV僅中個位數增長。財險端車險綜合成本率93.5%、非車94.6%，惟巨災損失正常化後非車綜合成本率2026-2028年料達99%-100%。"
        },
        "why": {
            "sc": "人保个案展示「银保依赖+费用监管+分红转型慢」对内地头部险企价值增长的拖累，叠加财险巨灾成本正常化压力，是跟踪内地保险业中期盈利与监管传导的参考样本。",
            "tc": "人保個案展示「銀保依賴+費用監管+分紅轉型慢」對內地頭部險企價值增長的拖累，疊加財險巨災成本正常化壓力，是跟蹤內地保險業中期盈利與監管傳導的參考樣本。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "内地险企价值增长与渠道结构跟踪", "tc": "內地險企價值增長與渠道結構跟蹤"},
            "lead": {},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 0, "cross": 0},
        "source": {"sc": "InsuranceAsia 保险亚洲", "lang": "en"},
        "boards": ["insurer", "market"],
        "themes": ["analyst", "mainland"],
        "tags": {
            "sc": ["人保集团", "晨星", "新业务价值", "银保渠道", "综合成本率"],
            "tc": ["人保集團", "晨星", "新業務價值", "銀保渠道", "綜合成本率"]
        },
        "contentKind": "news",
        "publishedAt": "2026-09-03T06:00:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/picc-groups-life-and-health-growth-trails-peers",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    }
]


def main():
    # 摘要字数校验 (50-105字)
    for it in NEW_ITEMS:
        n = len(it['summary']['sc'])
        nt = len(it['summary']['tc'])
        flag = ''
        if not (50 <= n <= 105):
            flag += f' SC={n}'
        if not (50 <= nt <= 105):
            flag += f' TC={nt}'
        print(f"{'OK ' if not flag else 'WARN'} {n}/{nt}字: {it['id']}{flag}")

    path = 'data/live-items.json'
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    items = data['items']
    existing_ids = {it.get('id') for it in items}
    dup = [it['id'] for it in NEW_ITEMS if it['id'] in existing_ids]
    if dup:
        print('SKIP duplicates:', dup)
    fresh = [it for it in NEW_ITEMS if it['id'] not in existing_ids]
    titles = {(it.get('sourceKey'), it.get('title', {}).get('sc')) for it in items}
    fresh = [it for it in fresh if (it.get('sourceKey'), it.get('title', {}).get('sc')) not in titles]
    items[:0] = fresh
    data['items'] = items
    meta = data['meta']
    meta['itemCount'] = len(items)
    meta['generatedAt'] = NOW_STR
    meta['windowNote'] = {
        "sc": f"本库{len(items)}条。",
        "tc": f"本庫{len(items)}條。"
    }
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print(f'新增 {len(fresh)} 条 -> 总条数 {len(items)}')
    for it in fresh:
        print(' +', it['id'])


if __name__ == '__main__':
    main()
