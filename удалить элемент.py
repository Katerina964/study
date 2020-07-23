numList = list(map(int, input().split()))
k = int(input())
r = -1
for i in numList:
    r += 1
    if r == k:
        continue
    print(str(i) + ' ', end='')
