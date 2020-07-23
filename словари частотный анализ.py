inFile = open('input.txt')
words = inFile.read()
words = words.split()
inFile.close()
answer = {}

for word in words:
    answer[word] = answer.get(word, 0) + 1
answer = list(answer.items())
answer.sort(key=lambda x: (-x[1], x[0]))
for word in answer:
    print(word[0])
