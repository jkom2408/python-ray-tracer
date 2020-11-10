
class Tuple:

    def __init__(self, x, y ,z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def isPoint(self):
        return self.w == 0.0

    def isVector(self):
        return self.w == 1.0

    @staticmethod
    def point(x, y, z):
        return Tuple(x, y, z, 1.0)
    
    @staticmethod
    def vector(x, y, z):
        return Tuple(x, y, z, 0.0)

    @staticmethod
    def __float_equals(a, b):
        EPSILON = 0.00001
        return abs(a - b) < EPSILON

    def __eq__(self, other):
        return \
            self.__float_equals(self.x, other.x) and \
            self.__float_equals(self.y, other.y) and \
            self.__float_equals(self.z, other.z) and \
            self.__float_equals(self.w, other.w)

    def __add__(self, other):
        return Tuple( \
            self.x + other.x, \
            self.y + other.y, \
            self.z + other.z, \
            self.w + other.w)

    def __sub__(self, other):
        return Tuple( \
            self.x - other.x, \
            self.y - other.y, \
            self.z - other.z, \
            self.w - other.w)

    def __neg__(self):
        return Tuple(-self.x, -self.y, -self.z, -self.w)

    def __mul__(self, other):
        return Tuple(
            self.x * other, \
            self.y * other, \
            self.z * other, \
            self.w * other)

    def __truediv__(self, other):
        return Tuple(
            self.x / other, \
            self.y / other, \
            self.z / other, \
            self.w / other)