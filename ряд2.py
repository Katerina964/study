a = int(input())
b = int(input())


if a > b:
    myTuple = tuple(range(a, b - 1, -1))
    for i in myTuple:
        print(i, end=' ')
elif a < b:
    myTuple = tuple(range(a, b + 1))
    for i in myTuple:
        print(i, end=' ')
else:
    print(a)
