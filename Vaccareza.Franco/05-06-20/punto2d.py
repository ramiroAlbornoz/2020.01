class Punto2D():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        self.__x = value
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        self.__y = value
if __name__ == '__main__':
    punto = Punto2D()
    print(punto.__dict__)
