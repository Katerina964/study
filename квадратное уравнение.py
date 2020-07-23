a = float(input())
b = float(input())
c = float(input())
d = b**2 - 4*a*c
res = []
if d == 0:
    x = -b / (2*a)
    print(x)

elif d > 0:
    x = (-b + d**0.5) / (2*a)
    x2 = (-b - d**0.5) / (2*a)
    res.append(x)
    res.append(x2)
    res.sort()
    print(*res)
