nc = int(input())
country = list(map(int, input().split()))
nb = int(input())
bomb = list(map(int, input().split()))
bombK = []
r = 0
for i in bomb:
    bombN = i, r
    bombK.append(bombN)
    r += 1
bombK.sort()
countryK = []
r = 0
for i in country:
    countryN = i, r
    countryK.append(countryN)
    r += 1
countryK.sort()
r1 = 0
lenB = len(bombK)

answer = []

for j in range(len(countryK)):
    dist = countryK[j][0] - bombK[r1][0]
    
    while r1 < lenB - 1 and dist > abs(countryK[j][0] - bombK[r1 + 1][0]):
        dist = abs(countryK[j][0] - bombK[r1 + 1][0])
        r1 += 1

    answer.append((countryK[j][1], bombK[r1][1] + 1))

answer.sort()
for i in range(len(answer)):
    print(answer[i][1], sep=' ', end=' ')
