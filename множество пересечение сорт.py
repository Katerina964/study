n = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*sorted(list(set(n) & set(b))))
