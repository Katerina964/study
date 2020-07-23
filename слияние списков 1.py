a = list(map(int, input().split()))
b = list(map(int, input().split()))


def merge(c, d):
    ab = a + b
    ba = []
    for i in range(len(ab)):
        if i == 0 or ab[i] >= ba[i - 1]:
            ba. append(ab[i])

        elif ab[i] < ba[i - 1]:
            ba.insert(i - 1, ab[i])
            while ba[i - 1] < ba[i - 2] and i >= 2:
                ba.insert(i - 2, ba[i - 1])
                ba.pop(i)
                i -= 1
    return print(*ba)


merge(a, b)
