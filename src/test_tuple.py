import unittest
import math
from rtmath.tuple import Tuple
from rtmath.vector import Vector
from rtmath.point import Point
from rtmath.color import Color


class TestCalc(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # A tuple with w=1.0 is a point
    def test_is_point(self):
        tuple = Tuple(4.3, -4.2, 3.1, 1.0)
        self.assertEqual(tuple.x, 4.3)
        self.assertEqual(tuple.y, -4.2)
        self.assertEqual(tuple.z, 3.1)
        self.assertEqual(tuple.w, 1.0)
        self.assertEqual(tuple.isPoint(), True)
        self.assertEqual(tuple.isVector(), False)

    # A tuple with w=0 is a vector
    def test_is_vector(self):
        tuple = Tuple(4.3, -4.2, 3.1, 0.0)
        self.assertEqual(tuple.x, 4.3)
        self.assertEqual(tuple.y, -4.2)
        self.assertEqual(tuple.z, 3.1)
        self.assertEqual(tuple.w, 0.0)
        self.assertEqual(tuple.isPoint(), False)
        self.assertEqual(tuple.isVector(), True)

    # point() creates tuples with w=1
    def test_point_creates_tuple_wth_w_equals_1(self):
        point = Point(4, -4, 3)
        self.assertEqual(point == Tuple(4, -4, 3, 1), True)

    # vector() creates tuples with w=0
    def test_vector_creates_tuple_wth_w_equals_0(self):
        vector = Vector(4, -4, 3)
        self.assertEqual(vector == Tuple(4, -4, 3, 0), True)

    def test_add_two_tuples(self):
        a1 = Tuple(3, -2, 5, 1)
        a2 = Tuple(-2, 3, 1, 0)
        self.assertEqual(a1 + a2 == Tuple(1, 1, 6, 1), True)

    # two points should cancel each other out to become a vector
    def test_subtract_two_points(self):
        p1 = Point(3, 2, 1)
        p2 = Point(5, 6, 7)
        self.assertEqual(p1 - p2 == Vector(-2, -4, -6), True)

    # subtract vector from point should give a different point
    def test_subtract_vector_from_point(self):
        p = Point(3, 2, 1)
        v = Vector(5, 6, 7)
        self.assertEqual(p - v == Point(-2, -4, -6), True)

    # subtracting two vectors results in a vector
    def test_subtract_vector_from_vector(self):
        v1 = Vector(3, 2, 1)
        v2 = Vector(5, 6, 7)
        self.assertEqual(v1 - v2 == Vector(-2, -4, -6), True)

    def test_negating_a_tuple(self):
        a = Tuple(1, -2, 3, -4)
        self.assertEqual(-a == Tuple(-1, 2, -3, 4), True)

    def test_multiply_vector_by_scalar(self):
        a = Tuple(1, -2, 3, -4)
        self.assertEqual(a * 3.5 == Tuple(3.5, -7, 10.5, -14), True)

        a = Tuple(1, -2, 3, -4)
        self.assertEqual(a * 0.5 == Tuple(0.5, -1, 1.5, -2), True)

    def test_divide_vector_by_fraction(self):
        a = Tuple(1, -2, 3, -4)
        self.assertEqual(a / 2 == Tuple(0.5, -1, 1.5, -2), True)

    def test_vector_magnitude(self):
        v = Vector(1, 0, 0)
        self.assertEqual(Tuple.float_eq(v.magnitude(), 1), True)

        v = Vector(0, 1, 0)
        self.assertEqual(Tuple.float_eq(v.magnitude(), 1), True)

        v = Vector(1, 2, 3)
        self.assertEqual(Tuple.float_eq(v.magnitude(), math.sqrt(14)), True)

        v = Vector(-1, -2, -3)
        self.assertEqual(Tuple.float_eq(v.magnitude(), math.sqrt(14)), True)

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
        norm = v.normalize()
        self.assertEqual(norm.magnitude() == 1, True)

    def test_dot_product(self):
        a = Vector(1, 2, 3)
        b = Vector(2, 3, 4)
        self.assertEqual(a.dot(b) == 20, True)

    def test_cross_product(self):
        a = Vector(1, 2, 3)
        b = Vector(2, 3, 4)
        self.assertEqual(a.cross(b) == Vector(-1, 2, -1), True)
        self.assertEqual(b.cross(a) == Vector(1, -2, 1), True)

    # colors are (red, green, blue) tuples
    def test_color(self):
        c = Color(-0.5, 0.4, 1.7)
        self.assertEqual(c.r() == -0.5, True)
        self.assertEqual(c.g() == 0.4, True)
        self.assertEqual(c.b() == 1.7, True)


if __name__ == '__main__':
    unittest.main()
