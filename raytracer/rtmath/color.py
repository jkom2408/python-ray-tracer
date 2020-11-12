from numbers import Number
from .tuple import Tuple


class Color(Tuple):

    def __init__(self, r, g, b):
        super().__init__(r, g, b, 1)

    @classmethod
    def new(cls, tuple):
        return cls(
            tuple.x,
            tuple.y,
            tuple.z)

    def r(self):
        return self.x

    def g(self):
        return self.y

    def b(self):
        return self.z

    def a(self):
        return self.w

    def __add__(self, other):
        res = super().__add__(other)
        return Color.new(res)

    def __sub__(self, other):
        res = super().__sub__(other)
        return Color.new(res)

    def __mul__(self, other):
        if isinstance(other, Number):
            res = super().__mul__(other)
            return Color.new(res)
        elif type(other) is Color:
            return Color.hadamard_product(self, other)
        else:
            raise TypeError

    @staticmethod
    def hadamard_product(c1, c2):
        return Color(
                c1.x * c2.x,
                c1.y * c2.y,
                c1.z * c2.z)
