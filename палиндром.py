n = int(input())
a = 0
pal = ''
i = 0
k = 0
while n != k + 1:
    k = k + 1

    while k != 0:
        a = k % 10
        k = k // 10
        pal = str(pal) + str(a)

        if int(pal) == k:
            i = i + 1
print(pal)
print(i)