k1 = int(input())
s1 = int(input())
k2 = int(input())
s2 = int(input())
if k2 == k1 and s2 == s1 + 1 or s1 == s1 - 1:
    print('YES')
elif k2 == k1 + 1 and s2 == s1 or s2 == s1 + 1 or s1 == s1 - 1:
    print('YES')
elif k2 == k1 - 1 and s2 == s1 or s2 == s1 + 1 or s1 == s1 - 1:
    print('YES')
else:
    print('NO')
