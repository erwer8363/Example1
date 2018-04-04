# -*- coding:utf-8 -*-

def triangles():
    for i in range(1,11):
        print('--------',i)
        for j in range(i):
            print(j,end=' ')

print(triangles())