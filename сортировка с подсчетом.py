myList = list(map(int, input().split()))
myCount = [0]*(max(myList) + 1)
for i in myList:
    myCount[i] += 1
for j in range(len(myCount)):
    if myCount[j] != 0:
        print((str(str(j)) + ' ') * myCount[j], end='')
