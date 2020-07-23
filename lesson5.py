from sys import stdin
import copy


class MatrixError(BaseException):
    def __init__(self, Matrix, other):
        self.matrix1 = Matrix
        self.matrix2 = other


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

        if len(self.mat) == len(other. mat):
            for i in range(len(self.mat)):
                while r < len(self.mat[0]):
                    c = self.mat[i][r] + other.mat[i][r]
                    r += 1
                    res.append(c)
                all.append(res)
                r = 0
                res = []
            new = Matrix(all)

        else:
            raise MatrixError(self, other)
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

    def transpose(self):
        self.mat = list(map(list, zip(*self.mat)))
        new = Matrix(self.mat)
        return new

    def transposed(self):
        trans = list(map(list, zip(*self.mat)))
        new = Matrix(trans)
        return new


m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m1 + m2)

m2 = Matrix([[0, 1, 0], [20, 0, -1]])
try:
    m = m1 + m2
    print('WA\n' + str(m))
except MatrixError as e:
    print(e.matrix1)
    print(e.matrix2)

