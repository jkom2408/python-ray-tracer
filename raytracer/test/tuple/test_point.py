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
        point = Point(4, -4, 3)
        self.assertEqual(point == Tuple(4, -4, 3, 1), True)

    # two points should cancel each other out to become a vector
    def test_subtract_two_points(self):
        point1 = Point(3, 2, 1)
        point2 = Point(5, 6, 7)
        self.assertEqual(point1 - point2 == Vector(-2, -4, -6), True)

    # subtract vector from point should give a different point
    def test_subtract_vector_from_point(self):
        point = Point(3, 2, 1)
        vector = Vector(5, 6, 7)
        self.assertEqual(point - vector == Point(-2, -4, -6), True)
