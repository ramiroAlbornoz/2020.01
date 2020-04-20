import unittest
from alumno import Persona
from parameterized import parameterized

class TestAlumno(unittest.TestCase):
    @parameterized.expand([(1, "Fernandez", "Cristina", "1: Fernandez, Cristina")])
    def test_str_persona(self, legajo, apellido, nombre, to_string):
        persona = Persona(legajo, apellido, nombre)
        self.assertEqual(persona.__str__(), to_string)

if __name__ == "__main__":
    unittest.main()