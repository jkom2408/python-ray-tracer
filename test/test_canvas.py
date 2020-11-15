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

    def test_construct_ppm_header(self):
        canvas = Canvas(5, 3)
        ppm = canvas.to_ppm()
        lines = ppm.split('\n')
        self.assertTrue(lines[0] == 'P3')
        self.assertTrue(lines[1] == '5 3')
        self.assertTrue(lines[2] == '255')

    def test_construct_ppm_pixel_data(self):
        canvas = Canvas(5, 3)
        c1 = Color(1.5, 0, 0)
        c2 = Color(0, 0.5, 0)
        c3 = Color(-0.5, 0, 1)
        canvas.write_pixel(0, 0, c1)
        canvas.write_pixel(2, 1, c2)
        canvas.write_pixel(4, 2, c3)
        ppm = canvas.to_ppm()
        lines = ppm.split('\n')
        self.assertTrue(lines[3] == '255 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
        self.assertTrue(lines[4] == '0 0 0 0 0 0 0 128 0 0 0 0 0 0 0')
        self.assertTrue(lines[5] == '0 0 0 0 0 0 0 0 0 0 0 0 0 0 255')

    def test_wrap_ppm_pixel_data_at_70_chars(self):
        canvas = Canvas(10, 2, Color(1, 0.8, 0.6))
        ppm = canvas.to_ppm()
        lines = ppm.split('\n')
        self.assertTrue(lines[3] == '255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204')
        self.assertTrue(lines[4] == '153 255 204 153 255 204 153 255 204 153 255 204 153')
        self.assertTrue(lines[5] == '255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204')
        self.assertTrue(lines[6] == '153 255 204 153 255 204 153 255 204 153 255 204 153')
