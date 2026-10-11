try:
    import zhconv
    print('zhconv OK', zhconv.convert('保险监管总局发布规定', 'zh-hant'))
except Exception as e:
    print('zhconv ERR', e)
try:
    import opencc
    print('opencc OK', opencc.OpenCC('s2t').convert('保险监管总局发布规定'))
except Exception as e:
    print('opencc ERR', e)
