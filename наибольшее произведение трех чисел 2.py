n = list(map(int, input().split()))


max2 = 0
a, b, c = n[0], n[1], n[2]
max1 = a*b*c
for i in range(len(n)):
    for j in range(len(n)):
        for r in range(len(n)):
            if i < j < r:
                max2 = n[i]*n[j]*n[r]
                if max2 > max1:
                    a, b, c = n[i], n[j], n[r]
                    max1 = max2

print(a,  b, c)
