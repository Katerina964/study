numList = list(map(int, input().split()))

nowMax = numList[0]
r2 = 0
r = -1

for i in numList:
    r += 1
    if i > nowMax:
        nowMax = i
        r2 = r

print(nowMax, r2)
