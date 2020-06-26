class Punto():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = y

if __name__ == '__main__':
    print("holis")