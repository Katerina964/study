

def power(a, n):
    an = a**(n / 2)
    return an


def res(a, n):
    if n % 2 == 0:
        return power(a, n)*power(a, n)
    else:
        n = n - 1
        return a * power(a, n)*power(a, n)


b = float(input())
c = int(input())
print(res(b, c))
