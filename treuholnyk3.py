a = int(input())
b = int(input())
c = int(input())
if c < a + b and a < c + b and b < a + c:
    if a <= c >= b:
        if a**2 + b**2 == c**2:
            print('rectangular')
        if a ** 2 + b ** 2 > c**2:
            print('acute')
        if a ** 2 + b ** 2 < c**2:
            print('obtuse')
    if c < a >= b:
        if a**2 == c**2 + b**2:
            print('rectangular')
        if a ** 2 < c ** 2 + b ** 2:
            print('acute')
        if a ** 2 > c ** 2 + b ** 2:
            print('obtuse')
    if a < b >= c:
        if b**2 == a**2 + c**2:
            print('rectangular')
        if b ** 2 < c ** 2 + a ** 2:
            print('acute')
        if b ** 2 > c ** 2 + a ** 2:
            print('obtuse')
else:
    print('impossible')
