inputFile = open('input.txt')
words = inputFile.read()
inputFile.close()
words = words.split()

print(len(set(words)))