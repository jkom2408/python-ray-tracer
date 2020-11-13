import math
from raytracer.rtmath.color import Color


class Canvas:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.canvas = [[
            [0 for c in range(3)]
            for w in range(width)]
            for h in range(height)]

    def write_pixel(self, x, y, color):
        self.canvas[y][x][0] = color.r()
        self.canvas[y][x][1] = color.g()
        self.canvas[y][x][2] = color.b()

    @staticmethod
    def to_byte(f):
        if f > 1:
            return 255
        elif f < 0:
            return 0
        else:
            return int(math.ceil(255 * f))

    def pixel_at(self, x, y):
        return Color(
           self.canvas[y][x][0],
           self.canvas[y][x][1],
           self.canvas[y][x][2])

    def sum(self):
        return sum(sum(sum(c) for c in w) for w in self.canvas)

    def to_ppm(self):
        header = f'P3\n{self.width} {self.height}\n255'
        body = (
            '\n'.join(
                ' '.join(
                    ' '.join(
                        map(str, map(Canvas.to_byte, c))
                    ) for c in h
                ) for h in self.canvas)
            )
        return header + '\n' + body
