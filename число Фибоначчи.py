a = 1
b = 1
c = 2


def fib(a, b, n, c):
    if c == n or n == 1:
        return b

    a, b = b, a + b

    return fib(a, b, n, c + 1)


n = int(input())
print(fib(a, b, n, c))
