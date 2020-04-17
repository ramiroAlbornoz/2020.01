import unittest
from alumno import Persona
from alumno import Alumno
from parameterized import parameterized

class TestAlumno(unittest.TestCase):
    @parameterized.expand([(1, "Fernandez", "Cristina", "1,: Fernandez, Cristina, "), 
                            (2, "Fernandez", "Alberto", "2,: Fernandez, Alberto, "), 
                            (5, "Guzman", "Martin", "5,: Guzman, Martin, ")])
    def test_str_persona(self, legajo, apellido, nombre, to_string):
        persona = Persona(legajo, apellido, nombre)
        self.assertEqual(persona.__str__(), to_string)

    def test_str_alumno(self):
        alumno = Alumno (8, "Peron", "Juan Domingo", 3, 3.14)
        self.assertEqual(alumno.__str__(), "8: Peron, Juan Domingo - Chequera: 3 - Nivel de Facha: 3.14")

if __name__ == "__main__":
    unittest.main()