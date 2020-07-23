n = list(map(int, input().split()))
b = [0]*(max(n) + 1)
for i in n:
    if b[i] == 0:
        print('NO')
        b[i] += 1
    else:
        print('YES')
