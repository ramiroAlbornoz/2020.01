class Punto():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, x):
        if x<0:
            raise ValueError("no puede ser -1")
        self._x = x
    @y.setter
    def y(self, y):
        self._y = y

    def __str__(self):
        printear = "(%d, %d)" % (self.x, self.y)
        return printear



if __name__ == '__main__':
    punto = Punto(1, 3)
    print(str(punto))