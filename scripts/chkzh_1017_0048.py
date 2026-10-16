import importlib
for m in ['zhconv', 'zhconv.convert']:
    try:
        mod = importlib.import_module(m)
        print('OK', m, getattr(mod, '__file__', ''))
    except Exception as e:
        print('FAIL', m, e)
