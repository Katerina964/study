inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()

inFile.close()
peopleList = []


class Man:
    surname = ''
    name = ''
    school = 0
    ass = 0


def manKey(man):
    return man.surname, man.name, man.ass


for line in lines:
    t = line.split()

    man = Man()
    man.surname = t[0]
    man.name = t[1]
    man.school = int(t[2])
    man.ass = int(t[3])
    peopleList.append(man)

peopleList.sort(key=manKey)
for man in peopleList:
    print(man.surname, man.name, man.ass, file=outFile)

outFile.close()
