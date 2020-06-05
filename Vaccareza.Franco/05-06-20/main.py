from punto2d import Punto2D
from punto3d import Punto3D

if __name__ == '__main__':
    punto2d = Punto2D(-2, -3)
    punto3d = Punto3D(2, -3, -4)
    print(punto2d.__dict__)
    print(punto3d.__dict__)
