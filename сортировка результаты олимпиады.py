n = int(input())
newList = []

for line in range(n):
    t = input().split()
    newList.append(t)

newList.sort(key=lambda x: -int(x[1]))
for i in newList:
    print(i[0])
