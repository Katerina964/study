import math


def distance(a1, b1, a2, b2):
    ab = (b2 - b1)**2 + (a2-a1)**2
    return math.sqrt(abs(ab))


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print('{0:.5f}'.format(distance(x1, y1, x2, y2)))
