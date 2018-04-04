'''
函数对象有一个__name__属性，可以拿到函数的名字
在代码运行期间动态增加功能的方式，称之为“装饰器”，
本质上，decorator就是一个返回函数的高阶函数。
'''

def log(func):
    def wrapper(*args,**kw):
        print('call %s()' %func.__name__)
        return func(*args,**kw)
    return wrapper