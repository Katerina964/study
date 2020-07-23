inFile = open('input.txt')
words = inFile.read()
words = words.split()
inFile.close()
answer = {}

for word in words:
    answer[word] = answer.get(word, 0) + 1
answer = answer.items()
nowMax = 0
newMax = ''

for word in answer:
    if word[1] >= nowMax:
        nowMax = word[1]
        newMax = word[0]
for word in answer:
    if word[1] == nowMax and word[0] < newMax:
        newMax = word[0]

print(newMax)
