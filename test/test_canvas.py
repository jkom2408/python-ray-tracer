import unittest
from raytracer.canvas import Canvas
from raytracer.rtmath.color import Color


class TestCanvas(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_canvas(self):
        canvas = Canvas(10, 20)
        self.assertEqual(canvas.width == 10, True)
        self.assertEqual(canvas.height == 20, True)
        self.assertEqual(canvas.sum(),  0)

    def test_write_pixel_to_canvas(self):
        canvas = Canvas(10, 20)
        red = Color(1, 0, 0)
        canvas.write_pixel(2, 3, red)
        self.assertTrue(canvas.pixel_at(2, 3) == red)

