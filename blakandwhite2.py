k1 = int(input())
s1 = int(input())
k2 = int(input())
s2 = int(input())
if k1 % 2 == 0 and s1 % 2 == 0 or k1 % 2 == 1 and s1 % 2 == 1:
    if k2 % 2 == 0 and s2 % 2 == 0:
        print('YES')
    if k2 % 2 == 1 and s2 % 2 == 1:
        print('YES')
    if k2 % 2 == 0 and s2 % 2 == 1:
        print('NO')
    if k2 % 2 == 1 and s2 % 2 == 0:
        print('NO')
elif k1 % 2 == 0 and s1 % 2 == 1 or k1 % 2 == 1 and s1 % 2 == 0:
    if k2 % 2 == 0 and s2 % 2 == 1:
        print('YES')
    if k2 % 2 == 1 and s2 % 2 == 0:
        print('YES')
    if k2 % 2 == 0 and s2 % 2 == 0:
        print('NO')
    if k2 % 2 == 1 and s2 % 2 == 1:
        print('NO')
