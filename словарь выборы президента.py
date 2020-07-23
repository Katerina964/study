inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')

words = inFile.read().splitlines()
number = len(words)
inFile.close()
answer = {}

for word in words:
    answer[word] = answer.get(word, 0) + 1

answer = list(answer.items())
answer.sort(key=lambda x: -x[1])

for word in answer[0:2]:
    if number / word[1] < 2:
        print(word[0], file=outFile)
        break
    print(word[0], file=outFile)
outFile.close()
