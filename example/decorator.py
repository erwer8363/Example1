def decorator(func):
    def g(*args,**kw):
        print('begin call %s()'%func.__name__)
        return func(*args,**kw)
    print('end call')
    return g

@decorator
def f():
    print('hello,python')

f();