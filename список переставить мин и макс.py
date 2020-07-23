n = list(map(int, input().split()))

a = min(n)
b = max(n)
for i in range(len(n)):

    if n[i] == a:
        n[i] = b

    elif n[i] == b:
        n[i] = a

print(*n)
