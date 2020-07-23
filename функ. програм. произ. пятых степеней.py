import functools
print(functools.reduce(lambda x, y, : x * (y**5), map(int, ('1 ' + input()).split())))
