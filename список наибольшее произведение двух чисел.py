n = list(map(int, input().split()))
min1 = 0
min2 = 0
max1 = 0
max2 = 0

for i in n:

    if max1 < i > 0 and max1 <= max2:
        max1 = i
        continue
    elif max2 < i > 0:
        max2 = i

for i in n:
    if min1 > i < 0 and min1 > min2:
        min1 = i
        continue
    elif min2 > i < 0:
        min2 = i


if max1*max2 >= min1*min2:
    if max1 <= max2:
        print(max1, max2)
    else:
        print(max2, max1)


if max1*max2 < min1*min2:
    if min1 <= min2:
        print(min1, min2)

    else:
        print(min2, min1)
