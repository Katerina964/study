def power(a, n):
    i = 1
    k = 1
    d = 0
    while i <= abs(n):
        d = k*a
        k = d
        i += 1
    if n < 0:
        return 1 / d
    if n == 0:
        return 1
    return d


b = float(input())
c = int(input())
print(power(b, c))
