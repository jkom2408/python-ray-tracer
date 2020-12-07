import unittest
from raytracer.rtmath.matrix import Matrix
from raytracer.rtmath.tuple import Tuple


class TestMatrix(unittest.TestCase):

    def test_create_matrix_2x2(self):
        m = Matrix(
            [
                [-3, 5],
                [1, -2],
            ])
        self.assertEqual(m[0][0], -3)
        self.assertEqual(m[0][1], 5)
        self.assertEqual(m[1][0], 1)
        self.assertEqual(m[1][1], -2)

    def test_create_matrix_3x3(self):
        m = Matrix(
            [
                [-3, 5, 0],
                [1, -2, -7],
                [0, 1, 1],
            ])
        self.assertEqual(m[0][0], -3)
        self.assertEqual(m[1][1], -2)
        self.assertEqual(m[2][2], 1)

    def test_create_matrix_4x4(self):
        m = Matrix(
            [
                [1, 2, 3, 4],
                [5.5, 6.5, 7.5, 8.5],
                [9, 10, 11, 12],
                [13.5, 14.5, 15.5, 16.5]
            ])
        self.assertEqual(m[0][0], 1)
        self.assertEqual(m[0][3], 4)
        self.assertEqual(m[1][0], 5.5)
        self.assertEqual(m[1][2], 7.5)
        self.assertEqual(m[2][2], 11)
        self.assertEqual(m[3][0], 13.5)
        self.assertEqual(m[3][2], 15.5)

    def test_matrix_equality(self):
        a = Matrix([
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 8, 7, 6],
                [5, 4, 3, 2]
            ])
        b = Matrix([
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 8, 7, 6],
                [5, 4, 3, 2]
            ])
        self.assertEqual(a, b)

    def test_matrix_inequality(self):
        a = Matrix([
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 8, 7, 6],
                [5, 4, 3, 2]
            ])
        b = Matrix([
                [2, 3, 4, 5],
                [6, 7, 8, 9],
                [8, 7, 6, 5],
                [4, 3, 2, 1]
            ])
        self.assertTrue(a != b)

    def test_matrix_4x4_multiplication(self):
        a = Matrix([
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 8, 7, 6],
                [5, 4, 3, 2]
            ])
        b = Matrix([
                [-2, 1, 2, 3],
                [3, 2, 1, -1],
                [4, 3, 6, 5],
                [1, 2, 7, 8]
            ])
        self.assertEqual(a * b, Matrix([
            [20, 22, 50, 48],
            [44, 54, 114, 108],
            [40, 58, 110, 102],
            [16, 26, 46, 42]
        ]))

    def test_matrix_tuple_multiplication(self):
        a = Matrix([
            [1, 2, 3, 4],
            [2, 4, 4, 2],
            [8, 6, 4, 1],
            [0, 0, 0, 1]
        ])
        b = Tuple(1, 2, 3, 1)
        self.assertEqual(a * b, Tuple(18, 24, 33, 1))

    def test_identity_matrix(self):
        a = Matrix([
            [0, 1, 2, 4],
            [1, 2, 4, 8],
            [2, 4, 8, 16],
            [4, 8, 16, 32]
        ])
        self.assertEqual(Matrix.identity() * a, a)

    def test_transpose(self):
        a = Matrix([
            [0, 9, 3, 0],
            [9, 8, 0, 8],
            [1, 8, 5, 3],
            [0, 0, 5, 8]
        ])
        self.assertEqual(a.transpose(), Matrix([
            [0, 9, 1, 0],
            [9, 8, 8, 0],
            [3, 0, 5, 5],
            [0, 8, 3, 8]
        ]))

    def test_transpose_identity(self):
        self.assertEqual(Matrix.identity().transpose(), Matrix.identity())

    def test_determinant_2x2(self):
        a = Matrix([
            [1, 5],
            [-3, 2]
        ])
        self.assertEqual(Matrix.determinant(a), 17)

    def test_submatrix_3x3(self):
        a = Matrix([
            [1, 5, 0],
            [-3, 2, 7],
            [0, 6, -3]
        ])
        self.assertEqual(
            a.submatrix(0, 2),
            Matrix([
                [-3, 2],
                [0, 6]]
            )
        )

    def test_submarix_4x4(self):
        a = Matrix([
            [-6, 1, 1, 6],
            [-8, 5, 8, 6],
            [-1, 0, 8, 2],
            [-7, 1, -1, 1]
        ])
        self.assertEqual(
            a.submatrix(2, 1),
            Matrix([
                [-6, 1, 6],
                [-8, 8, 6],
                [-7, -1, 1]
            ]))
