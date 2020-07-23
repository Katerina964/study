a, b = list(map(int, input().split()))
c = []
i = 0
while i < b:
    i += 1
    k = int(input())
    c.append(k)
c.sort()
segSum = c[0]
r = 0
while r < len(c) - 1 and segSum <= a:
    r += 1
    segSum += c[r]

if r == len(c) - 1 and segSum <= a:
    print(r + 1)
else:
    print(r)
