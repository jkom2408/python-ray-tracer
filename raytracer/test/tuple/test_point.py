import unittest
from rtmath.tuple import Tuple
from rtmath.vector import Vector
from rtmath.point import Point


class TestPoint(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # point() creates tuples with w=1
    def test_point_creates_tuple_wth_w_equals_1(self):
        p = Point(4, -4, 3)
        self.assertEqual(p == Tuple(4, -4, 3, 1), True)

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
