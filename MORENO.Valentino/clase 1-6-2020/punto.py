class Punto():
    
    def __init__(self,x=0, y=0):
        self.x = x
        self.y = y
    
    @property
    def x (self):
        return self.__x
    @property
    def y (self):
        return self.__y
    @x.setter 
    def x(self, x):
        self.__x = x
    @y.setter 
    def y(self, y):
        self.__y = y

if __name__ == '__main__':
    print("ola")