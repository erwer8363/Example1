'''
 第一行和第二行是标准注释，第一行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，
 第二行注释表示文件是使用Utf-8编码
 第四行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释
 导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能

 sys模块有个argv变量，用list存储了命令行的所有参数，argv至少有一个元素，因为第一个参数永远是该.py文件的名称，
'''
#!/user/bin/env python3
#-*- coding:utf-8 -*-

'a test module'

__author__ = 'Michael Liao'

import sys

from functools import reduce

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world')
    elif len(args)==2:
        print('Hello, %s!'%args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    test()

def mySum():
    ss = 0
    for n in range(1,101):
        ss = ss + n
    return ss
print(mySum())

testSum = reduce(lambda a,b:a+b,range(1,50));
print('the testSum is {}'.format(testSum))

print(list(map(lambda x:x*x,range(1,5))))

myStr = 'Ever'
print('hello,%s'%myStr)

print(__doc__);

