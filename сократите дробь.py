def qsd(a, b):
    if b % a == 0:
        return a
    elif a % b == 0:
        return b
    elif a < b:
        if b % a == 0:
            a, b = a, b / a

        elif b % a != 0:
            a, b = a, b % a

    elif a > b:
        if a % b == 0:
            a, b = b, a / b

        elif a % b != 0:
            a, b = b, a % b

    return qsd(a, b)


k = int(input())
c = int(input())
print(k // qsd(k, c), c // qsd(k, c))
