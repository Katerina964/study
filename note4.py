a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
v2 = a2*b2*c2
if a1 == b1 == c1 and a2 == b2 == c2:
    if b1 >= a2 <= a1 and a2 <= c1 and b1 >= b2 <= a1 and b2 <= c1 and b1 >= c2 <= a1 and c2 <= c1:
        print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
elif b1 >= a2 <= a1 and a2 <= c1 and b1 >= b2 <= a1 and b2 <= c1 and b1 >= c2 <= a1 and c2 <= c1:
    if a1 <= b1 <= c1:
        if a2 <= b2 <= c2:
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
        if a2 <= c2 <= b2:
            (a2, b2, c2) = (a2, c2, b2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
        if c2 <= b2 <= a2:
            (a2, b2, c2) = (c2, b2, a2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
        if b2 <= a2 <= c2:
            (a2, b2, c2) = (b2, a2, c2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
        if c2 <= a2 <= b2:
            (a2, b2, c2) = (c2, a2, b2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
        if b2 <= c2 <= a2:
            (a2, b2, c2) = (b2, c2, a2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
    if a1 <= c1 <= b1:
        (a1, b1, c1) = (a1, c1, b1)
        if a2 <= b2 <= c2:
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
        if a2 <= c2 <= b2:
            (a2, b2, c2) = (a2, c2, b2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
        if c2 <= b2 <= a2:
            (a2, b2, c2) = (c2, b2, a2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
        if b2 <= a2 <= c2:
            (a2, b2, c2) = (b2, a2, c2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
        if c2 <= a2 <= b2:
            (a2, b2, c2) = (c2, a2, b2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
        if b2 <= c2 <= a2:
            (a2, b2, c2) = (b2, c2, a2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
    if c1 <= b1 <= a1:
        (a1, b1, c1) = (c1, b1, a1)
        if a2 <= b2 <= c2:
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
        if a2 <= c2 <= b2:
            (a2, b2, c2) = (a2, c2, b2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
        if c2 <= b2 <= a2:
            (a2, b2, c2) = (c2, b2, a2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
        if b2 <= a2 <= c2:
            (a2, b2, c2) = (b2, a2, c2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
        if c2 <= a2 <= b2:
            (a2, b2, c2) = (c2, a2, b2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
        if b2 <= c2 <= a2:
            (a2, b2, c2) = (b2, c2, a2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
    if b1 <= a1 <= c1:
        (a1, b1, c1) = (b1, a1, c1)
        if a2 <= b2 <= c2:
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
        if a2 <= c2 <= b2:
            (a2, b2, c2) = (a2, c2, b2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
        if c2 <= b2 <= a2:
            (a2, b2, c2) = (c2, b2, a2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
        if b2 <= a2 <= c2:
            (a2, b2, c2) = (b2, a2, c2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
        if c2 <= a2 <= b2:
            (a2, b2, c2) = (c2, a2, b2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
        if b2 <= c2 <= a2:
            (a2, b2, c2) = (b2, c2, a2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
    if c1 <= a1 <= b1:
        (a1, b1, c1) = (c1, a1, b1)
        if a2 <= b2 <= c2:
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
        if a2 <= c2 <= b2:
            (a2, b2, c2) = (a2, c2, b2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
        if c2 <= b2 <= a2:
            (a2, b2, c2) = (c2, b2, a2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
        if b2 <= a2 <= c2:
            (a2, b2, c2) = (b2, a2, c2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
        if c2 <= a2 <= b2:
            (a2, b2, c2) = (c2, a2, b2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
        if b2 <= c2 <= a2:
            (a2, b2, c2) = (b2, c2, a2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) / v2)
    if b1 <= c1 <= a1:
        (a1, b1, c1) = (b1, c1, a1)
        if a2 <= b2 <= c2:
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) // v2)
        if a2 <= c2 <= b2:
            (a2, b2, c2) = (a2, c2, b2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) // v2)
        if c2 <= b2 <= a2:
            (a2, b2, c2) = (c2, b2, a2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) // v2)
        if b2 <= a2 <= c2:
            (a2, b2, c2) = (b2, a2, c2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) // v2)
        if c2 <= a2 <= b2:
            (a2, b2, c2) = (c2, a2, b2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) // v2)
        if b2 <= c2 <= a2:
            (a2, b2, c2) = (b2, c2, a2)
            print(((a1 - (a1 % a2)) * (b1 - (b1 % b2)) * (c1 - (c1 % c2))) // v2)
else:
    print('0')
