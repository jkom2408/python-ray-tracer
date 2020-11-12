from .tuple import Tuple
from .vector import Vector


class Point(Tuple):

    def __init__(self, x, y, z):
        super().__init__(x, y, z, 1.0)

    @classmethod
    def new(cls, tuple):
        return cls(
            tuple.x,
            tuple.y,
            tuple.z)

    def __add__(self, other):
        res = super().__add__(other)
        if res.isPoint():
            return Point.new(res)
        elif res.isVector():
            return Vector.new(res)
        else:
            raise TypeError

    def __sub__(self, other):
        res = super().__sub__(other)
        if res.isPoint():
            return Point.new(res)
        elif res.isVector():
            return Vector.new(res)
        else:
            raise TypeError
