# -*- coding:utf-8 -*-

L1 = ['Hello','World',18,'Apple',None]

L2 = [s.lower() for s in L1 if isinstance(s,str)]

print(L2)

g = (x*x for x in range(10))

while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break
print(g)