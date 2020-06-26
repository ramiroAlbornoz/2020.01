class Punto():
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,x):
        if x<0:
            raise ValueError("no puede ser negativo")
        self._x=x

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self,y):
        self._y=y
    def __str__(self):
        return "(%s, %s)" %(self.x, self.y)

    