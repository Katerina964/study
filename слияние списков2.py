a = list(map(int, input().split()))
b = list(map(int, input().split()))


def merge(c, d):
    ab = a + b
    k = len(ab)
    i = 0
    ba = []
    while i < k:
        i += 1
        c = min(ab)
        ba.append(c)
        ab.remove(c)
    return print(*ba, *ab)


merge(a, b)
