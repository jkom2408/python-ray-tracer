class Matrix:
    def __init__(self, m):
        self.m = m

    def __getitem__(self, i):
        return self.m[i]
