n = list(map(int, input().split()))

i = -1


while i < len(n) - 1:
    i += 1

    if i != 0 and i % 2 == 1:
        n[i - 1], n[i] = n[i], n[i - 1]


print(*n)
