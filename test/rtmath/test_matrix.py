import unittest
from raytracer.rtmath.matrix import Matrix


class TestMatrix(unittest.TestCase):

    def test_create_matrix_4x4(self):
        m = Matrix(
            [
                [1, 2, 3, 4],
                [5.5, 6.5, 7.5, 8.5],
                [9, 10, 11, 12],
                [13.5, 14.5, 15.5, 16.5]
            ])
        self.assertTrue(m[0][0] == 1)
        self.assertTrue(m[0][3] == 4)
        self.assertTrue(m[1][0] == 5.5)
        self.assertTrue(m[1][2] == 7.5)
        self.assertTrue(m[2][2] == 11)
        self.assertTrue(m[3][0] == 13.5)
        self.assertTrue(m[3][2] == 15.5)

    def test_create_matrix_3x3(self):
        m = Matrix(
            [
                [-3, 5, 0],
                [1, -2, -7],
                [0, 1, 1],
            ])
        self.assertTrue(m[0][0] == -3)
        self.assertTrue(m[1][1] == -2)
        self.assertTrue(m[2][2] == 1)

    def test_create_matrix_2x2(self):
        m = Matrix(
            [
                [-3, 5],
                [1, -2],
            ])
        self.assertTrue(m[0][0] == -3)
        self.assertTrue(m[0][1] == 5)
        self.assertTrue(m[1][0] == 1)
        self.assertTrue(m[1][1] == -2)
