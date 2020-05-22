import unittest
from parameterized import parameterized
from excepciones2 import Persona

class TestExceptions(unittest.TestCase):
    @parameterized.expand([("Fernandez", "Ofelia", 19,
                            "Fernandez, Ofelia -> Edad 19"),
                           ("Fernandez", "Alberto", 60,
                            "Fernandez, Alberto -> Edad 60")])
    def test_str(self, apellido, nombre, edad, test_str):
        persona = Persona(apellido, nombre, edad)
        self.assertEqual(persona.__str__(), test_str)

if __name__ == "__main__":
    unittest.main()