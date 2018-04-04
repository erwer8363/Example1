def is_palindrome(n):
    s = str(n)
    ss = s[::-1]
    # l = len(s)
    # arr = [0]*l
    # i = 0
    # for ss in s:
    #     arr[l-i-1] = ss
    #     i += 1
    return ss == s

output = filter(is_palindrome,range(1,1000))
print(list(output))

for i,value in enumerate(['a','b','c']):
    print(i,value)