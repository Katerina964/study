def sum(a, b):
    if b == 0:
        return a

    return a + sum(1, b - 1)


d = int(input())
c = int(input())
print(sum(d, c))
