import unittest
from herencia import Persona,Alumno
from parameterized import parameterized

class Testalumno(unittest.TestCase):
    @parameterized.expand([(123, "Diacono", "Luquitas", "123: Diacono, Luquitas")])
    def test_str_persona(self, legajo, apellido, nombre, to_string):
        persona = Persona(legajo, apellido, nombre)
        self.assertEqual(persona.__str__(),to_string)
    def test_str_alunmo(self):
        alumno = Alumno(1,"Biritos","Santiago","123","200000")
        self.assertEqual(alumno.__str__(), "1: Biritos, Sanitago, 123, 200000")
if __name__ == "__main__":
    unittest.main()