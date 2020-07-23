def xor(x, y):
    if x == 0 and y != 0:
        return y
    elif y == 0 and x != 0:
        return x


x = int(input())
y = int(input())

if xor(x, y):
    print('1')
else:
    print(0)
