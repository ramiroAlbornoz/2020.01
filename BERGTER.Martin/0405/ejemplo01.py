import unittest
from unittest.mock import patch


def saludar():
    name = input('Hola, como te llamas?')
    apellido = input('Apellido ?')
    return 'Como va %s %s!!!' % (name, apellido)


def saludar_nombre():
    name = input('Hola, como te llamas?')
    return 'Como va %s!!!' % name


class TestSaludar(unittest.TestCase):
    def test_saludar(self):
        with patch('builtins.input', side_effect=['Gabriel', 'Perez']):
            self.assertEqual(saludar(), 'Como va Gabriel Perez!!!')

    def test_saludar_nombre(self):
        with patch('builtins.input', side_effect=['Gabriel']):
            self.assertEqual(saludar_nombre(), 'Como va Gabriel!!!')


if __name__ == '__main__':
    unittest.main()
    
#el builtins.input es decirle al with que reemplace el input de la funcion por el return_valve
#el return value y es escribir el input por un valor al igual que el 
#side_efect nada mas que a este se le pueden meter varios valores en una lista