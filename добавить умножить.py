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

    def __add__(self, other):
        r = 0
        res = []
        all = []

        for i in range(len(self.mat)):
            while r < len(self.mat[0]):
                c = self.mat[i][r] + other.mat[i][r]
                r += 1
                res.append(c)
            all.append(res)
            r = 0
            res = []
        new = Matrix(all)
        return new

    def __mul__(self, other):
        r = 0
        res = []
        all = []

        for i in range(len(self.mat)):
            while r < len(self.mat[0]):
                c = self.mat[i][r] * other
                r += 1
                res.append(c)
            all.append(res)
            r = 0
            res = []
        new = Matrix(all)
        return new

    __rmul__ = __mul__


m = Matrix([[10, 10], [0, 0], [1, 1]])
print(m.size())
m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m1 + m2)
m = Matrix([[1, 1, 0], [0, 2, 10], [10, 15, 30]])
alpha = 15
print(m * alpha)
print(alpha * m)
