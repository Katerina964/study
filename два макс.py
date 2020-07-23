n = int(input())
prev_max = 0
max = n
while n != 0:
    n = int(input())
    if n >= max:
        prev_max = max
        max = n
    elif prev_max == 0 or n > prev_max:
        prev_max = n

print(prev_max)
