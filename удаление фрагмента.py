string = input()
substring = 'h'
kst = len(string)

pos = string.find(substring)
pos3 = string[:0:-1].find(substring)
pos2 = kst - (pos3 + 1)

print(string[0:pos] + string[pos2 + 1:])
