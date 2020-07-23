n = int(input())
i = 1
a = '+___ '
b = "|i / "
c = '|__\ '
d = '|    '
sumK = ''
allK = ''
while i <= n:
    f = str(i)
    k = b.replace('i', f)
    i += 1
    sumK = allK + k
    allK = sumK
print(a*n)
print(allK)
print(c*n)
print(d*n)
