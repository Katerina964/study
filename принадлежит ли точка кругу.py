from math import sqrt


def isPointInCircle(x, y, xc, yc, r):
    ab = sqrt(abs((yc - y)**2 + (xc-x)**2))
    return ab <= r


x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
if isPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
