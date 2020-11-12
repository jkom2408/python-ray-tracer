import unittest
import math
from rtmath.tuple import Tuple
from rtmath.vector import Vector


class TestVector(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # vector() creates tuples with w=0
    def test_vector_creates_tuple_wth_w_equals_0(self):
        vector = Vector(4, -4, 3)
        self.assertEqual(vector == Tuple(4, -4, 3, 0), True)

    # subtracting two vectors results in a vector
    def test_subtract_vector_from_vector(self):
        vector1 = Vector(3, 2, 1)
        vector2 = Vector(5, 6, 7)
        self.assertEqual(vector1 - vector2 == Vector(-2, -4, -6), True)

    def test_divide_vector_by_fraction(self):
        tupl = Tuple(1, -2, 3, -4)
        self.assertEqual(tupl / 2 == Tuple(0.5, -1, 1.5, -2), True)

    def test_vector_magnitude(self):
        vector = Vector(1, 0, 0)
        self.assertEqual(Tuple.float_eq(vector.magnitude(), 1), True)

        vector = Vector(0, 1, 0)
        self.assertEqual(Tuple.float_eq(vector.magnitude(), 1), True)

        vector = Vector(1, 2, 3)
        self.assertEqual(
            Tuple.float_eq(vector.magnitude(), math.sqrt(14)),
            True)

        vector = Vector(-1, -2, -3)
        self.assertEqual(
            Tuple.float_eq(vector.magnitude(), math.sqrt(14)),
            True)

    def test_normalization(self):
        vector = Vector(4, 0, 0)
        self.assertEqual(vector.normalize() == Vector(1, 0, 0), True)

        vector = Vector(1, 2, 3)
        self.assertEqual(
            # vector(1/√14, 2/√14, 3/√14)
            vector.normalize() == Vector(0.26726, 0.53452, 0.80178),
            True)

        # magnitude of a normalized vector equals 1
        vector = Vector(1, 2, 3)
        norm = vector.normalize()
        self.assertEqual(norm.magnitude() == 1, True)

    def test_dot_product(self):
        vector_a = Vector(1, 2, 3)
        vector_b = Vector(2, 3, 4)
        self.assertEqual(vector_a.dot(vector_b) == 20, True)

    def test_cross_product(self):
        vector_a = Vector(1, 2, 3)
        vector_b = Vector(2, 3, 4)
        self.assertEqual(vector_a.cross(vector_b) == Vector(-1, 2, -1), True)
        self.assertEqual(vector_b.cross(vector_a) == Vector(1, -2, 1), True)
