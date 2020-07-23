n = list(map(int, input().split()))
i = 0
b = []
a = len(n)

while i < a:

    if i > 0 and i % 2 == 0:

        b.append(n[i - 1])
        b.append(n[i])
print(*b)
