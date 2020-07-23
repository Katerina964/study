numList = list(map(int, input().split()))


def IsAscending(numList):
    i = 0
    while i + 1 < len(numList) and numList[i] < numList[i + 1]:
        i += 1
    return i + 1 == len(numList)


if IsAscending(numList):
    print('YES')
else:
    print('NO')
