import math


class Tuple:

    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def isPoint(self):
        return self.w == 1.0

    def isVector(self):
        return self.w == 0.0

    def magnitude(self):
        return math.sqrt(
            self.x * self.x +
            self.y * self.y +
            self.z * self.z +
            self.w * self.w)

    def normalize(self):
        magnitude = self.magnitude()
        return Tuple(
            self.x / magnitude,
            self.y / magnitude,
            self.z / magnitude,
            self.w / magnitude)

    def dot(self, other):
        return (
            self.x * other.x +
            self.y * other.y +
            self.z * other.z +
            self.w * other.w)

    @staticmethod
    def float_eq(a, b):
        EPSILON = 0.00001
        return abs(a - b) < EPSILON

    def __eq__(self, other):
        return (
            self.float_eq(self.x, other.x) and
            self.float_eq(self.y, other.y) and
            self.float_eq(self.z, other.z) and
            self.float_eq(self.w, other.w))

    def __add__(self, other):
        return Tuple(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
            self.w + other.w)

    def __sub__(self, other):
        return Tuple(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
            self.w - other.w)

    def __neg__(self):
        return Tuple(-self.x, -self.y, -self.z, -self.w)

    def __mul__(self, other):
        return Tuple(
            self.x * other,
            self.y * other,
            self.z * other,
            self.w * other)

    def __truediv__(self, other):
        return Tuple(
            self.x / other,
            self.y / other,
            self.z / other,
            self.w / other)
