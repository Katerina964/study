n = list(map(int, input().split()))

i = len(n) - 1
c = n[i]

while i >= 0:
    if i == 0:
        n[i] = c
        break

    n[i] = n[i - 1]
    i += -1

print(*n)
