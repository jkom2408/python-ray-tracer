from raytracer.rtmath.tuple import Tuple


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

    def __eq__(self, m):
        return (
            self.float_eq(self[0][0], m[0][0]) and
            self.float_eq(self[0][1], m[0][1]) and
            self.float_eq(self[0][2], m[0][2]) and
            self.float_eq(self[0][3], m[0][3]) and
            self.float_eq(self[1][0], m[1][0]) and
            self.float_eq(self[1][1], m[1][1]) and
            self.float_eq(self[1][2], m[1][2]) and
            self.float_eq(self[1][3], m[1][3]) and
            self.float_eq(self[2][0], m[2][0]) and
            self.float_eq(self[2][1], m[2][1]) and
            self.float_eq(self[2][2], m[2][2]) and
            self.float_eq(self[2][3], m[2][3]) and
            self.float_eq(self[3][0], m[3][0]) and
            self.float_eq(self[3][1], m[3][1]) and
            self.float_eq(self[3][2], m[3][2]) and
            self.float_eq(self[3][3], m[3][3])
        )

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

    @staticmethod
    def transpose(m):
        return Matrix([
            [m[r][c] for r in range(len(m))] for c in range(len(m[0]))
        ])
