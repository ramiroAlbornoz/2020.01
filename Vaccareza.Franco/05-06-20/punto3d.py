from punto2d import Punto2D

class Punto3D(Punto2D):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError
        self.__x = value
    @property
    def z(self):
        return self.__z
    @z.setter
    def z(self, value):
        self.__z = value
if __name__ == '__main__':
    punto = Punto3D()

    print(punto.__dict__)
