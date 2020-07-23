a = list(map(int, input().split()))
b1 = list(map(int, input().split()))
k = []
lenb = len(b1)


def merge(c, d):
    j = 0
    lenB = lenb
    b = b1
    for i in a:

        while lenB > 0 and i > b[j]:
            k.append(b[j])
            j += 1
            lenB -= 1

        if lenB == 0 or i < b[j]:
            k.append(i)

        elif lenB > 0 and i == b[j]:
            k.append(i)
            k.append(b[j])
            j += 1
            lenB -= 1
    return print(*k + b[j:])


merge(a, b1)
