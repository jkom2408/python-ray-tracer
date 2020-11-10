
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

    def __eq__(self, other):
        return \
        self.__float_equals(self.x, other.x) and \
        self.__float_equals(self.y, other.y) and \
        self.__float_equals(self.z, other.z) and \
        self.__float_equals(self.w, other.w)

    @staticmethod
    def __float_equals(a, b):
        EPSILON = 0.00001
        return abs(a - b) < EPSILON