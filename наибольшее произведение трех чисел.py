n = list(map(int, input().split()))

min1 = 0
min2 = 0
max1 = 0
max2 = 0
max3 = 0
x = 0
y = 0
m = []
for i in n:
    if max1 < i > 0 and max1 <= max2:
        max1 = i
        x += 1
        continue
    elif max2 < i > 0:
        max2 = i
        y += 1

for i in n:
    if min1 > i < 0 and min1 > min2:
        min1 = i
        continue
    elif min2 > i < 0:
        min2 = i

h = n[0:]
if len(h) == 3 or len(h) == 4:
    m = h[0:]

elif x > 0 < y:
    n.remove(max1)
    n.remove(max2)
    max3 = max(n)
    m = (max1, max2, max3, min1, min2)
elif x == 0 == y:
    max1 = max(n)
    n.remove(max1)
    max2 = max(n)
    n.remove(max2)
    max3 = max(n)
    m = max1, max2, max3
elif x > 0 == y:
    m = (max1, min1, min2)

a, b, c = m[0], m[1], m[2]
maxX = m[0]*m[1]*m[2]

for i in range(len(m)):
    for j in range(len(m)):
        for r in range(len(m)):
            if i < j < r:
                k = m[i]*m[j]*m[r]
                if k > maxX:
                    a, b, c = m[i], m[j], m[r]
                    maxX = k

print(a, b, c)