import unittest
from rtmath.tuple import Tuple


class TestTuple(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # A tuple with w=1.0 is a point
    def test_is_point(self):
        tupl = Tuple(4.3, -4.2, 3.1, 1.0)
        self.assertEqual(tupl.x, 4.3)
        self.assertEqual(tupl.y, -4.2)
        self.assertEqual(tupl.z, 3.1)
        self.assertEqual(tupl.w, 1.0)
        self.assertEqual(tupl.isPoint(), True)
        self.assertEqual(tupl.isVector(), False)

    # A tuple with w=0 is a vector
    def test_is_vector(self):
        tupl = Tuple(4.3, -4.2, 3.1, 0.0)
        self.assertEqual(tupl.x, 4.3)
        self.assertEqual(tupl.y, -4.2)
        self.assertEqual(tupl.z, 3.1)
        self.assertEqual(tupl.w, 0.0)
        self.assertEqual(tupl.isPoint(), False)
        self.assertEqual(tupl.isVector(), True)

    def test_add_two_tuples(self):
        tuple1 = Tuple(3, -2, 5, 1)
        tuple2 = Tuple(-2, 3, 1, 0)
        self.assertEqual(tuple1 + tuple2 == Tuple(1, 1, 6, 1), True)

    def test_negating_a_tuple(self):
        tupl = Tuple(1, -2, 3, -4)
        self.assertEqual(-tupl == Tuple(-1, 2, -3, 4), True)

    def test_multiply_tuple_by_scalar(self):
        tupl = Tuple(1, -2, 3, -4)
        self.assertEqual(tupl * 3.5 == Tuple(3.5, -7, 10.5, -14), True)

        tupl = Tuple(1, -2, 3, -4)
        self.assertEqual(tupl * 0.5 == Tuple(0.5, -1, 1.5, -2), True)
