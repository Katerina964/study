string = input()
substring = 'f'
kst = len(string)

pos = string.find(substring)
newString = string[pos + 1:]
if pos == -1:
    print(-2)
elif pos != -1:
    pos2 = newString.find(substring)
    if pos2 == -1:
        print(pos2)
    else:
        print(pos2 + pos + 1)
