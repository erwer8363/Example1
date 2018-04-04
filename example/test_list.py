#-*-coding:utf-8-*-

L = [
    ['Apple','Google','Microsoft'],
    ['Java','Python','Ruby','PHP'],
    ['Adam','Bart','Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])

for item in L:
    for name in item:
        print(name,end=' ')

sum = 0
for x in range(101):
    sum += x
print(sum)