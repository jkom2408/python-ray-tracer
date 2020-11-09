
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
