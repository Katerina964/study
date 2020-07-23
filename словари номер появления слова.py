inputFile = open('input.txt')
words = inputFile.read()
inputFile.close()

words = words.split()

answer = {}
for word in words:
    answer[word] = answer.get(word, 0) + 1
    print(answer[word] - 1, end=' ')
