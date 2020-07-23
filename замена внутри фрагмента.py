string = input()
pos = string.find('h')
pos2 = string.rfind('h')
r = string[pos + 1:pos2].replace('h', 'H')


print(string[0:pos + 1] + r + string[pos2:])
