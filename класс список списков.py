from sys import stdin
import copy


class Matrix:
    def __init__(self, m):
        self.mat = copy.deepcopy(m)

    def __str__(self):
        return str(self.mat).replace('], ', '\n').replace(
            ', ', '\t').replace('[[', '').replace(
            ']]', '').replace('[', '')

    def size(self):
        x = len(self.mat)
        y = len(self.mat[1])
        return x, y


exec(stdin.read())
