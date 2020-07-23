a = list(map(int, input().split()))
b = list(map(int, input().split()))
k = []
j = 0


def merge(c, d):
    lenB = len(b)
    for i in a:

        while lenB > 0 and i > b[j]:
            k.append(b[j])
            b.remove(b[j])
            lenB -= 1

        if lenB == 0 or i < b[j]:
            k.append(i)

        elif lenB > 0 and i == b[j]:
            k.append(i)
            k.append(b[j])
            b.remove(b[j])
            lenB -= 1
    return print(*k + b)


merge(a, b)
