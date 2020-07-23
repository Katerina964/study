n = int(input())
b = 1
segSum = 0
c = 0
while b <= n:
    c = 1 / (b**2)
    b += 1
    segSum += c
print('{0:.5f}'.format(segSum))
