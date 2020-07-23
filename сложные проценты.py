p = int(input())
x = int(input())
y = int(input())
k = int(input())
i = 1
segSum = 0
oneYear = x*100 + y

while i <= k:
    segSum = oneYear / 100*p + oneYear
    oneYear = int(segSum)
    i += 1

bucks = oneYear // 100
cents = oneYear % 100
print(bucks, cents)
