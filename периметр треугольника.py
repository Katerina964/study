import math


def dist(a1, b1, a2, b2):
    ab = (b2 - b1)**2 + (a2-a1)**2
    return math.sqrt(abs(ab))


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())

perimeter = dist(x1, y1, x2, y2) + dist(x1, y1, x3, y3) + dist(x3, y3, x2, y2)

print('{0:.6f}'.format(perimeter))