numList = list(map(int, input().split()))
a = len(numList) - 1
b = numList[a::-1]

for i in b:
    print(str(i)+' ', end='')
