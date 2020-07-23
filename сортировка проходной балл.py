inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()
inFile.close()
n = lines[0:1]
lines = lines[1:]
nL = []
k = int(' '.join(n))

for line in lines:
    t = line.split()
    t1 = int(t[-1])
    t2 = int(t[-2])
    t3 = int(t[-3])

    if t1 >= 40 <= t2 and t3 >= 40:
        nL.append(t1 + t2 + t3)

nL.sort(reverse=True)
lenN = len(nL)

if lenN == 0 or k == 0:
    print('', file=outFile)

elif k >= lenN:
    print('0', file=outFile)

elif nL[0] == nL[k]:
    print('1', file=outFile)

elif nL[k - 1] == nL[k]:
    i = k - 2
    while nL[i] == nL[k - 1]:
        i -= 1
    print(nL[i], file=outFile)
else:
    print(nL[k - 1], file=outFile)

outFile.close()
