def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)


b = float(input())
c = int(input())
print(power(b, c))