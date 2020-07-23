numList = list(map(int, input().split()))

r = -1
for i in numList:
    r += 1
    if i > numList[r - 1] and r != 0:

        print(str(i) + ' ', end='')
