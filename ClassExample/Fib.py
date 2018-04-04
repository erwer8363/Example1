class Fib(object):
    '''生成斐波拉西数列的迭代器'''
    def __init__(self,max):
        self.max = max
    def __iter__(self):
        self.a = 0
        self.b = 1
        return self
    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration

        self.a,self.b = self.b, self.a + self.b

        return fib

for n in Fib(1000):
    print(n,end=' ')

    '''
    1,从无到有创建一个迭代器，fib应是一个类，而不是一个函数
    2，“调用”Fib(max)会创建该类一个真实的实例，并以max作为参数调用__init__()方法，
        __init__()方法以实例变量保存最大值，以便随后的其他方法可以调用
    3，当有人调用iter(fib)的时候，__iter__()就会被调用。（正如你等下会看到，for循环会自动调用它，你也可以手动调用）在完成迭代器初始化后，
    __iter__()方法就会返回任何实现了__next__()方法的对象，在本例子中，__iter__()仅简单返回了self，因为该类实现了自己的__next__()方法。
    4，当有人在迭代器的实例中调用next()方法时，__next__()会自动调用，
    5，当__next__()方法抛出StopIteration异常，这是给调用者表示迭代用完了的信号
    6，为了分离出下一个值，迭代器的__next__()方法简单return该值，不要使用yield；该语法的小甜头仅用于你使用生成器的时候
    '''