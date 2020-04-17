import unittest
import unittest
from alumno import Persona
from parameterized import parameterized


class TestAlumno(unittest.TestCase):
    @parameterized.expand([(1, "Fernandez", "Cristina", "1: Fernandez, Cristina"),
                            (2, "Fernandez", "Alberto", "2: Fernandez, Alberto"),
                            (5, "Guzman", "Martin", "5: Guzman, Martin")])
    def test_str_persona(self, legajo, apellido, nombre, to_string):
        persona = Persona(legajo, apellido, nombre)
        self.assertEqual(persona.__str__(), to_string)


if __name__ == "__main__":
    unittest.main()