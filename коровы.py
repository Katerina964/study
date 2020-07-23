n = int(input())
m = n % 10
if 10 <= n <= 20:
    print(n, 'korov')
elif n > 20 and m == 0 or m == 5 or m == 6 or m == 7 or m == 8 or m == 9:
    print(n, 'korov')
elif n % 10 == 1:
    print(n, "korova")
else:
    print(n, 'korovy')
