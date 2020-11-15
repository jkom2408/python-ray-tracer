import math
from raytracer.rtmath.color import Color


class Canvas:

    def __init__(self, width, height, color=Color(0, 0, 0)):
        self.width = width
        self.height = height
        self.canvas = [[
            [color.r(), color.g(), color.b()]
            for w in range(width)]
            for h in range(height)]

    def write_pixel(self, x, y, color):
        self.canvas[y][x][0] = color.r()
        self.canvas[y][x][1] = color.g()
        self.canvas[y][x][2] = color.b()

    def pixel_at(self, x, y):
        return Color(
           self.canvas[y][x][0],
           self.canvas[y][x][1],
           self.canvas[y][x][2])

    def to_ppm(self):
        header = f'P3\n{self.width} {self.height}\n255'
        body = (
            '\n'.join(
                Canvas.__insert_newline_at_column(70,
                    ' '.join(
                        ' '.join(
                                map(str, 
                                    map(Canvas.__float_to_byte, x)
                                    )
                                ) for x in y
                            )
                        )
                    for y in self.canvas
                )
            )
        return f'{header}\n{body}\n'

    def sum(self):
        return sum(sum(sum(c) for c in w) for w in self.canvas)

    @staticmethod
    def __float_to_byte(f):
        if f > 1:
            return 255
        elif f < 0:
            return 0
        else:
            return int(math.ceil(255 * f))

    @staticmethod
    def __insert_newline_at_column(column_number, char_array, start_index=0):
        if len(char_array) <= start_index + column_number:
            return ''.join(char_array)
        else:
            if isinstance(char_array, str):
                return Canvas.__insert_newline_at_column(column_number, list(char_array), start_index)

            i = start_index + column_number
            while char_array[i] != ' ':
                i -= 1
            else:
                char_array[i] = '\n'
                return Canvas.__insert_newline_at_column(column_number, char_array, i + 1)
