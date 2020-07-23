def rec():
    n = int(input())
    if n == 0:
        return print(0)

    rec()
    if n != 0:
        print(n)


rec()
