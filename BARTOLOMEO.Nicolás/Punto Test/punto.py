class Punto():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)       

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter 
    def x(self, x):
        if x < 0:
            raise ValueError("No puede ser negativo")
        self._x = x

    @y.setter
    def y(self, y):
        if y < 0:
            raise ValueError("No puede ser negativo")
        self._y = y
