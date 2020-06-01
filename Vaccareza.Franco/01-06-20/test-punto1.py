import unittest
from punto import Punto
class TestPunto(unittest.TestCase):
    def test_constructor_vacio(self):
        punto = Punto()
        self.assertDictEqual(punto.__dict__, {'_x': 0, '_y': 0})
    def test_uso_property(self):
        punto = Punto()
        punto.x = 1
        punto.y = 3
        self.assertDictEqual(punto.__dict__, {'_x': 1, '_y': 3})
    def test_constructor_con_valores_iniciales(self):
        punto = Punto(3, 4)
        self.assertDictEqual(punto.__dict__, {'_x': 3, '_y': 4})
if __name__ == '__main__':
    unittest.main()