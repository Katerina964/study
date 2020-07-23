z = int(input())
s = ''
for i in range(0, z):
    s += str(input())
print(s.count('0'))
m = range(0, z).count(0)
print(m)
