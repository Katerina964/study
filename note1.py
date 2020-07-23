a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
v1 = (a1 // a2) * (b1 // b2) * (c1 // c2)
v2 = (a1 // b2) * (b1 // c2) * (c1 // a2)
v3 = (a1 // c2) * (b1 // a2) * (c1 // b2)
if v3 <= v1 >= v2:
    print(v1)
elif v1 < v2 >= v3:
    print(v2)
else:
    print(v3)
