n = int(input())
a = ''
c = map(str, list(range(n + 1)))
c = set(c) - {'0'}
b = []
r = 0
while a != ['HELP']:
    a = list(input().split())
    r += 1
    if r % 2 == 1 and a != ['HELP']:
        b = set(a)

    elif a == ['YES']:
        c &= b

    elif a == ['NO']:
        c -= b
f = list(c)
f.sort()
print(*f)
