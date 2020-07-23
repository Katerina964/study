n = int(input())
numList = list(map(int, input().split()))
x = int(input())
nowNear = abs(x - numList[0])

r = 0
for i in numList:

    if abs(x - i) <= nowNear:
        nowNear = abs(x - i)
        r = i
print(r)
