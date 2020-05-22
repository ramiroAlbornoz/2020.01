import unittest
from parameterized import parameterized
from excepciones import Persona

class TestExceptions(unittest.TestCase):
    @parameterized.expand ([("Fernandez", "Ofelia", 19, 
                            "Fernandez, Ofelia -> Edad 19"),
                            ("Fernandez", "Alberto", 60, 
                            "Fernandez, Alberto -> Edad 60")])
    def test_str(self, apellido, nombre, edad, test_str):
        persona = Persona(apellido, nombre, edad)
        self.assertEqual(persona.__str__(), test_str)

    @parameterized.expand ([("Fernandez", "Ofelia", 19, 
                            "Fernandez, Ofelia -> Edad 19"),
                            ("Fernandez", "Alberto", 60, 
                            "Fernandez, Alberto -> Edad 60")])
    def test_input(self, apellido, nombre, edad, test_str):
        persona = Persona()
        with patch ('builtins.input', 
                    side_effect = [apellido, nombre, edad]):
            persona.input()
        self.assertEqual(persona.__str__(), test_str)

    def test_edad(self):
        persona = Persona()
        with patch('builtins.input', return_value = 'hola'):
            with self.assertRaises(Exception):
                persona.input_edad()

    def test_validar_edad_no_numero(self):
        with self.assertRaises(Exception):
            validar('hola')

    def test_validar_edad_fuera_rango(self):
        persona = Persona()
        with patch('builtins.input', return_value = '10'):
            persona.input_edad()

    def test_validar_edad_correcta(self):
        persona = Persona()
        with patch('builtins.input', return_value = '10'):
            persona.input_edad()

if __name__ == "__main__":
    unittest.main()