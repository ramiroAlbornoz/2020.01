import unittest
from excepciones import Persona
from parameterized import parameterized

def verufy_edad(self, edad):
    try:
        self.edad = int(edad)
    except ValueError:
        raise

class TestExeptions(unittest.TestCase):
    @parameterized.expand([("Fernandez", "Ofelia", 19, "Fernandez, Ofelia -> Edad 19")])
    def test_str(self, apellido, nombre, edad, test_str):
        persona = Persona(apellido, nombre, edad)
        self.assertEqual(persona.__str__(), test_str)


    def test_edad(self):
        persona = Persona ()
        with self.assertRaises(ValueError):
            persona.verify_edad("veinte")



if __name__ == "__main__":
    unittest.main()