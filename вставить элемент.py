numList = list(map(int, input().split()))
kc = list(map(int, input().split()))
k, c = kc
r = -1
for i in numList:
    r += 1
    if k == 0 == r:
        print(str(c) + ' ', end='')

    print(str(i) + ' ', end='')
    if r + 1 == k:
        print(str(c) + " ", end='')
