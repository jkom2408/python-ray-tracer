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
        v = Vector(4, -4, 3)
        self.assertEqual(v == Tuple(4, -4, 3, 0), True)

    # subtracting two vectors results in a vector
    def test_subtract_vector_from_vector(self):
        v1 = Vector(3, 2, 1)
        v2 = Vector(5, 6, 7)
        self.assertEqual(v1 - v2 == Vector(-2, -4, -6), True)

    def test_vector_magnitude(self):
        v = Vector(1, 0, 0)
        self.assertEqual(Tuple.float_eq(v.magnitude(), 1), True)

        v = Vector(0, 1, 0)
        self.assertEqual(Tuple.float_eq(v.magnitude(), 1), True)

        v = Vector(1, 2, 3)
        self.assertEqual(
            Tuple.float_eq(v.magnitude(), math.sqrt(14)),
            True)

        v = Vector(-1, -2, -3)
        self.assertEqual(
            Tuple.float_eq(v.magnitude(), math.sqrt(14)),
            True)

    def test_normalization(self):
        v = Vector(4, 0, 0)
        self.assertEqual(v.normalize() == Vector(1, 0, 0), True)

        v = Vector(1, 2, 3)
        self.assertEqual(
            # vector(1/√14, 2/√14, 3/√14)
            v.normalize() == Vector(0.26726, 0.53452, 0.80178),
            True)

        # magnitude of a normalized vector equals 1
        v = Vector(1, 2, 3)
        n = v.normalize()
        self.assertEqual(n.magnitude() == 1, True)

    def test_dot_product(self):
        a = Vector(1, 2, 3)
        b = Vector(2, 3, 4)
        self.assertEqual(a.dot(b) == 20, True)

    def test_cross_product(self):
        a = Vector(1, 2, 3)
        b = Vector(2, 3, 4)
        self.assertEqual(a.cross(b) == Vector(-1, 2, -1), True)
        self.assertEqual(b.cross(a) == Vector(1, -2, 1), True)
