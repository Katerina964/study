n = int(input())
i = 1
m = 0
print(1, end=' ')
while m < n:
    m = i * 2
    i = m
    if m <= n:
        print(m, end=' ')
