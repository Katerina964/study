n = int(input())
a = 0
pal = ''
i = 0
k = 10
r = 0
m = 0
while n >= k != 0:
    a = k % 10
    k = m
    pal = pal + str(a)
    k = k // 10
    if k > 0:
        continue
    r = int(pal)
    if r == m:
        i = i + 1

print(pal)
print(i)
print(m)
