#-*- coding:utf-8 -*-

from functools import reduce

def prod(L):
    def fn(x,y):
        return x * y
    return reduce(fn,L)

print('3*5*6=',prod([3,5,6]))


def normalize(name):
    return name.capitalize()

L1 = ['adam','LISA','barT']
L2 = list(map(normalize,L1))
print(L2)

def str2float(s):
    def fn(x,y):
        return x * 10 + y
    def str2int(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(fn,map(str2int,s))

# print(str2float('123.45'))
testStr = '123.4'
tl=len(testStr)
print(tl,testStr.find('.'));