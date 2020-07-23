numList = list(map(int, input().split()))

segMin = 0

for i in numList:

    if i % 2 == 1 and segMin == 0:
        segMin = i


for i in numList:

    if i % 2 == 1 and i < segMin:
        segMin = i

print(segMin)
