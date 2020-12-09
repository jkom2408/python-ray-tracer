from raytracer.rtmath.tuple import Tuple
from copy import deepcopy


class Matrix:
    def __init__(self, m):
        self.m = m

    @classmethod
    def fromdim(cls, rows, columns):
        return cls([[0 for c in range(columns)] for r in range(rows)])

    def __getitem__(self, i):
        return self.m[i]

    def __len__(self):
        return len(self.m)

    def __eq__(self, other):
        return self.m == other.m

    def __mul__(self, other):
        if isinstance(other, Matrix):
            return self.__matrix_multiply(self, other)
        elif isinstance(other, Tuple):
            return self.__tuplemultiply(self, other)
        else:
            raise TypeError

    @staticmethod
    def __matrix_multiply(a, b):
        # Number of columns on A must equal number of rows on B
        if len(a[0]) != len(b):
            raise ValueError

        res = Matrix.fromdim(4, 4)
        for r in range(4):
            for c in range(4):
                res[r][c] = (
                    a[r][0] * b[0][c] +
                    a[r][1] * b[1][c] +
                    a[r][2] * b[2][c] +
                    a[r][3] * b[3][c]
                )

        return res

    @staticmethod
    def __tuplemultiply(a, b):
        return Tuple(
            a[0][0] * b.x + a[0][1] * b.y + a[0][2] * b.z + a[0][3] * b.w,
            a[1][0] * b.x + a[1][1] * b.y + a[1][2] * b.z + a[1][3] * b.w,
            a[2][0] * b.x + a[2][1] * b.y + a[2][2] * b.z + a[2][3] * b.w,
            a[3][0] * b.x + a[3][1] * b.y + a[3][2] * b.z + a[3][3] * b.w
        )

    @staticmethod
    def float_eq(a, b):
        EPSILON = 0.00001
        return abs(a - b) < EPSILON

    @staticmethod
    def identity():
        return Matrix([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

    def transpose(self):
        return Matrix([
            [self[r][c] for r in range(len(self))] for c in range(len(self[0]))
        ])

    def determinant(self):
        return self[0][0] * self[1][1] - self[0][1] * self[1][0]

    def submatrix(self, row, col):
        res = Matrix(deepcopy(self.m))
        del(res.m[row])
        for r in res.m:
            del(r[col])
        return res

    def minor(self, row, col):
        res = self.submatrix(row, col)
        return res.determinant()
