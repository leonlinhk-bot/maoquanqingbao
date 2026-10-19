for mod in ('opencc', 'zhconv'):
    try:
        __import__(mod)
        print('OK', mod)
    except Exception as e:
        print('NO', mod, e)
