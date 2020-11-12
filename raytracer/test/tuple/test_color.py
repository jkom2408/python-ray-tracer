import unittest
from rtmath.color import Color


class TestColor(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # colors are (red, green, blue) tuples
    def test_color(self):
        color = Color(-0.5, 0.4, 1.7)
        self.assertEqual(color.r() == -0.5, True)
        self.assertEqual(color.g() == 0.4, True)
        self.assertEqual(color.b() == 1.7, True)


if __name__ == '__main__':
    unittest.main()
