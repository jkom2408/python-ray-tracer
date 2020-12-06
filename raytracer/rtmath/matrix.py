class Matrix:
    def __init__(self, m):
        self.m = m

    @classmethod
    def fromdim(cls, rows, columns):
        return cls([[0 for c in range(columns)] for r in range(rows)])

    def __getitem__(self, i):
        return self.m[i]

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
        # Number of columns on A must equal number of rows on B
        if len(self[0]) != len(other):
            raise ValueError

        res = Matrix.fromdim(4, 4)
        for r in range(4):
            for c in range(4):
                res[r][c] = (
                    self[r][0] * other[0][c] +
                    self[r][1] * other[1][c] +
                    self[r][2] * other[2][c] +
                    self[r][3] * other[3][c]
                )

        return res

    def __len__(self):
        return len(self.m)

    @staticmethod
    def float_eq(a, b):
        EPSILON = 0.00001
        return abs(a - b) < EPSILON
