import unittest


def validar(edad):
    if int(edad) > 0 and int(edad) < 123:
        return True
    else:
        raise Exception('poné un número entre 1 y 122 bruto!!!')


class TestValidarEdad(unittest.TestCase):
    def test_validar_edad_no_numero(self):
        with self.assertRaises(Exception):
            validar('hola')

    def test_validar_edad_grande(self):
        with self.assertRaises(Exception):
            validar(200)

    def test_validar_edad_chica(self):
        with self.assertRaises(Exception):
            validar(-1)

    def test_validar_edad_correcta(self):
        self.assertTrue(validar(10))


if __name__ == '__main__':
    unittest.main()
