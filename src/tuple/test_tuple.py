import unittest
from tuple import Tuple

class TestCalc(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_is_point(self):
        tuple = Tuple(4.3, -4.2, 3.1, 1.0)
        self.assertEqual(tuple.x, 4.3)
        self.assertEqual(tuple.y, -4.2)
        self.assertEqual(tuple.z, 3.1)
        self.assertEqual(tuple.w, 1.0)
        self.assertEqual(tuple.isPoint(), False)
        self.assertEqual(tuple.isVector(), True)

    def test_is_vector(self):
        tuple = Tuple(4.3, -4.2, 3.1, 0.0)
        self.assertEqual(tuple.x, 4.3)
        self.assertEqual(tuple.y, -4.2)
        self.assertEqual(tuple.z, 3.1)
        self.assertEqual(tuple.w, 0.0)
        self.assertEqual(tuple.isPoint(), True)
        self.assertEqual(tuple.isVector(), False)

    def test_point_creates_tuple_wth_w_equals_1(self):
        point = Tuple.point(4, -4, 3)
        self.assertEqual(point == Tuple(4, -4, 3, 1), True)

    def test_vector_creates_tuple_wth_w_equals_0(self):
        vector = Tuple.vector(4, -4, 3)
        self.assertEqual(vector == Tuple(4, -4, 3, 0), True)

if __name__ == '__main__':
    unittest.main()