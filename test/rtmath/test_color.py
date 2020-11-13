import unittest
from rtmath.color import Color


class TestColor(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # colors are (red, green, blue) tuples
    def test_color(self):
        c = Color(-0.5, 0.4, 1.7)
        self.assertEqual(c.r() == -0.5, True)
        self.assertEqual(c.g() == 0.4, True)
        self.assertEqual(c.b() == 1.7, True)

    def test_add_color(self):
        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)
        self.assertEqual(c1 + c2 == Color(1.6, 0.7, 1.0), True)

    def test_subtract_color(self):
        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)
        self.assertEqual(c1 - c2 == Color(0.2, 0.5, 0.5), True)

    def test_multiply_color_by_scalar(self):
        c = Color(0.2, 0.3, 0.4)
        self.assertEqual(c * 2 == Color(0.4, 0.6, 0.8), True)

    def test_multiply_color_by_color(self):
        c1 = Color(1, 0.2, 0.4)
        c2 = Color(0.9, 1, 0.1)
        self.assertEqual(c1 * c2 == Color(0.9, 0.2, 0.04), True)
