n = int(input())
now_Max = n
new_Sum = 1
res = []
while n != 0:
    n = int(input())
    if n == now_Max:
        new_Sum += 1
    else:
        res.append(new_Sum)
        now_Max = n
        new_Sum = 1
print(max(res))
