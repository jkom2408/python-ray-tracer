from raytracer.rtmath.color import Color


class Canvas:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.canvas = [[
            [0 for c in range(4)]
            for w in range(width)]
            for h in range(height)]

    def write_pixel(self, x, y, color):
        self.canvas[y - 1][x - 1][0] = color.r()
        self.canvas[y - 1][x - 1][1] = color.g()
        self.canvas[y - 1][x - 1][2] = color.b()
        self.canvas[y - 1][x - 1][3] = color.a()

    def pixel_at(self, x, y):
        return Color(
            self.canvas[y - 1][x - 1][0],
            self.canvas[y - 1][x - 1][1],
            self.canvas[y - 1][x - 1][2])

    def sum(self):
        return sum(sum(sum(c) for c in w) for w in self.canvas)

    def to_ppm(self):
        return f'P3\n{self.width} {self.height}\n255'
