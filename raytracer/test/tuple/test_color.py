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


if __name__ == '__main__':
    unittest.main()
