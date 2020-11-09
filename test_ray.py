import unittest
from ray import Tuple

class TestCalc(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()