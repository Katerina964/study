numList = list(map(int, input().split()))

segMax = 0
r = 0
r1 = 0
for i in numList:
    r += 1
    if i >= segMax or numList[0] < 0:
        segMax = i
        r1 = r


print(segMax, r1 - 1)
