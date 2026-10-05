import importlib, sys
for m in ['zhconv', 'opencc', 'zhconv.convert']:
    try:
        mod = importlib.import_module(m)
        print('OK', m, mod)
    except Exception as e:
        print('NO', m, type(e).__name__, e)
try:
    from zhconv import convert
    s = '保险业监管局对保险经纪的佣金上限与客户保障、分红保单、风险为本资本制度、为、行为、里面、台湾'
    print(convert(s, 'zh-hant'))
    print(convert(s, 'zh-hk'))
except Exception as e:
    print('convert fail', e)
