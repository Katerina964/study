numList = list(map(float, input().split()))

r = -1
r1 = 0
b = len(numList) - 1
for i in numList:
    r += 1
    if r != 0:
        if b > r:
            if i > numList[r - 1] + numList[r + 1]:
                r1 += 1
print(r1)
