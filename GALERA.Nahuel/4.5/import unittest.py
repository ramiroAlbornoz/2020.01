import unittest
from unittest.mock import patch


def saludar():
    name = input('Hola, como te llamas?')
    apellido = input("Apellido? ")
    return "Como va %s %s!!!" % (name, apellido)​

def saludar_nombre():
    name = input('Hola, como te llamas?')
    return "Como va %s!!!" % name


class TestSaludar(unittest.TestCase):
    def test_saludar(self):
        with patch('builtins.input', side_effect=['Gabriel', "Perez"]):
            self.assertEqual(saludar(), 'Como va Gabriel Perez!!!')
    def test_saludar_nombre(self):
        with patch('builtins.input', return_value="Gabriel"):
            self.assertEqual(saludar_nombre(), 'Como va Gabriel!!!')


if __name__ == '__main__':
    unittest.main()