import math

a = float(input())
b = float(input())
c = float(input())
p = ((a + b + c) / 2)
prevs = (p*(p-a)*(p-b)*(p-c))

print('{0:.6f}'.format(math.sqrt(prevs)))
