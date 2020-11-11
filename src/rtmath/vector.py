from .tuple import Tuple


class Vector(Tuple):

    def __init__(self, x, y, z):
        super().__init__(x, y, z, 0)

    @staticmethod
    def new(tuple):
        return Vector(
            tuple.x,
            tuple.y,
            tuple.z)

    def cross(self, other):
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x)

    def __add__(self, other):
        res = super().__add__(other)
        if res.isVector():
            return Vector.new(res)
        else:
            return TypeError

    def __sub__(self, other):
        res = super().__sub__(other)
        if res.isVector():
            return Vector.new(res)
        else:
            raise TypeError
