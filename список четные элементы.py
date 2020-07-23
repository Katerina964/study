numList = list(map(int, input().split()))


for i in numList:
    r = i % 2
    if r == 0:
        print(str(i)+" ", end='')
