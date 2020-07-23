from math import sqrt


def minDivisor(n):
    i = 2
    if n % 2 == 0:
        return 2
    while n % i != 0 and i <= sqrt(n):
        i += 1
    if i <= sqrt(n):
        return i
    return n


n = int(input())

print(minDivisor(n))