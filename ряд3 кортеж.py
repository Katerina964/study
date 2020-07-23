n = int(input())


a = 10**n - 1
b = a // 10
for i in range(a, b, -2):
    print(i, end=' ')
