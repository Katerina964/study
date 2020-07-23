numList = list(map(int, input().split()))

i = 0
while i + 1 < len(numList) and numList[i]*numList[i + 1] < 0:
    i += 1

if i + 1 < len(numList):
    print(numList[i], numList[i + 1])
