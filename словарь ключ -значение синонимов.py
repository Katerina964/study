n = int(input())

myDict = {}
elseDict = {}
i = 0
while i < n:
    par = list((input().split()))
    myDict[par[0]] = par[1]
    elseDict[par[1]] = par[0]
    i += 1
ask = input()
if ask in myDict:
    print(myDict[ask])
else:
    print(elseDict[ask])
