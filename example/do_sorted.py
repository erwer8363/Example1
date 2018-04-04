L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]

def by_name(t):
    return t[0].lower()

def by_score(t):
    return t[1]

r = map(by_name, L)
print(list(r))
# L2 = sorted(L,key= by_name)
# L2 = sorted(L,key=by_score,reverse=True)
L2 = sorted(L,key=lambda t:t[1])
print(L2)
#关键字lambda表示匿名函数，冒号前面的x表示函数参数。 匿名函数有个限制，就是只能有一个表达式，不用写return，
#返回值就是该表达式的结果
print(list(map(lambda j:j*j,range(1,4))))

#返回一个函数时，牢记该函数并没有立即执行，返回函数中不要引用任何可能变化的变量

def count():
    def f(j):
        return lambda :j*j
    fs =[]
    for i in range(1,4):
        fs.append(f(i))
    return fs

f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())