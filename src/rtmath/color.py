from .tuple import Tuple


class Color(Tuple):

    def __init__(self, r, g, b):
        super().__init__(r, g, b, 1)

    def r(self):
        return self.x

    def g(self):
        return self.y

    def b(self):
        return self.z

    def a(self):
        return self.w
