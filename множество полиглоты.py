n = int(input())
number = range(n)
lang = []
one_man_Lang = set()
allLang = set()
every_Lang = set()
a = ''
b = 0
i = len(number)
while i > 0:
    b = int(input())
    i -= 1
    while b > 0:
        a = input()
        one_man_Lang.add(a)
        b -= 1

    lang.append(one_man_Lang)
    allLang |= one_man_Lang
    if i == len(number) - 1:
        every_Lang = allLang & one_man_Lang
    else:
        every_Lang &= one_man_Lang
    one_man_Lang = set()


print(len(every_Lang))
for i in every_Lang:
    print(i)

print(len(allLang))
for i in allLang:
    print(i)
