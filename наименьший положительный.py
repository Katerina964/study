numList = list(map(int, input().split()))

segMin = 0

for i in numList:

    if i > 0 == segMin:
        segMin = i


for i in numList:

    if 0 < i < segMin:
        segMin = i

print(segMin)
