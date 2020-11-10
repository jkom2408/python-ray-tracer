import unittest
from tuple import Tuple

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
        self.assertEqual(tuple.isPoint(), False)
        self.assertEqual(tuple.isVector(), True)

    # A tuple with w=0 is a vector
    def test_is_vector(self):
        tuple = Tuple(4.3, -4.2, 3.1, 0.0)
        self.assertEqual(tuple.x, 4.3)
        self.assertEqual(tuple.y, -4.2)
        self.assertEqual(tuple.z, 3.1)
        self.assertEqual(tuple.w, 0.0)
        self.assertEqual(tuple.isPoint(), True)
        self.assertEqual(tuple.isVector(), False)

    # point() creates tuples with w=1
    def test_point_creates_tuple_wth_w_equals_1(self):
        point = Tuple.point(4, -4, 3)
        self.assertEqual(point == Tuple(4, -4, 3, 1), True)

    # vector() creates tuples with w=0
    def test_vector_creates_tuple_wth_w_equals_0(self):
        vector = Tuple.vector(4, -4, 3)
        self.assertEqual(vector == Tuple(4, -4, 3, 0), True)

    def test_add_two_tuples(self):
        a1 = Tuple(3, -2, 5, 1)
        a2 = Tuple(-2, 3, 1, 0)
        self.assertEqual(a1 + a2 == Tuple(1, 1, 6, 1), True)

    def test_subtract_two_points(self):
        p1 = Tuple.point(3, 2, 1)
        p2 = Tuple.point(5, 6, 7)
        self.assertEqual(p1 - p2 == Tuple.vector(-2, -4, -6), True)

    def test_subtract_vector_from_point(self):
        p = Tuple.point(3, 2, 1)
        v = Tuple.vector(5, 6, 7)
        self.assertEqual(p - v == Tuple.point(-2, -4, -6), True)

if __name__ == '__main__':
    unittest.main()