string = input()
k = len(string)
if k == 1:
    print(string)
elif k > 1:
    r = string[1:k - 1].replace('', '*')
    print(string[0] + r + string[k - 1])
