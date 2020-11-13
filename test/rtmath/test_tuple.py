import unittest
from raytracer.rtmath.tuple import Tuple


class TestTuple(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # A tuple with w=1.0 is a point
    def test_is_point(self):
        a = Tuple(4.3, -4.2, 3.1, 1.0)
        self.assertEqual(a.x, 4.3)
        self.assertEqual(a.y, -4.2)
        self.assertEqual(a.z, 3.1)
        self.assertEqual(a.w, 1.0)
        self.assertEqual(a.isPoint(), True)
        self.assertEqual(a.isVector(), False)

    # A tuple with w=0 is a vector
    def test_is_vector(self):
        a = Tuple(4.3, -4.2, 3.1, 0.0)
        self.assertEqual(a.x, 4.3)
        self.assertEqual(a.y, -4.2)
        self.assertEqual(a.z, 3.1)
        self.assertEqual(a.w, 0.0)
        self.assertEqual(a.isPoint(), False)
        self.assertEqual(a.isVector(), True)

    def test_add_two_tuples(self):
        a = Tuple(3, -2, 5, 1)
        b = Tuple(-2, 3, 1, 0)
        self.assertEqual(a + b == Tuple(1, 1, 6, 1), True)

    def test_negating_a_tuple(self):
        a = Tuple(1, -2, 3, -4)
        self.assertEqual(-a == Tuple(-1, 2, -3, 4), True)

    def test_multiply_tuple_by_scalar(self):
        a = Tuple(1, -2, 3, -4)
        self.assertEqual(a * 3.5 == Tuple(3.5, -7, 10.5, -14), True)

        a = Tuple(1, -2, 3, -4)
        self.assertEqual(a * 0.5 == Tuple(0.5, -1, 1.5, -2), True)

    def test_divide_vector_by_fraction(self):
        a = Tuple(1, -2, 3, -4)
        self.assertEqual(a / 2 == Tuple(0.5, -1, 1.5, -2), True)
