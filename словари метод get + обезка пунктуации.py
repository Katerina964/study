inputFile = open('input.txt')
words = inputFile.read()
inputFile.close()
number = []
words = words.split()
for word in words:
    if word.isalpha():
        number.append(word)
    else:
        number.append(word[:-1])
answer = {}
for word in number:
    answer[word] = answer.get(word, 0) + 1




print(number)
print(answer)