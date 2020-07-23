n = int(input())
nowSum = 0
segSum = 0
for i in range(1, n + 1):
    a = i**2

    segSum = nowSum + a
    nowSum = segSum
print(nowSum)