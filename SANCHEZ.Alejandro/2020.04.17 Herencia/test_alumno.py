import unittest
from alumnos import Persona
from parameterized import parameterized
class TestAlumno(unittest.TestCase):
    @parameterized.expand([(1,"Fernandez","Cristina","1, Fernandez, Cristina")])
    def test_str_persona(self):
        persona=Persona(1,"Fernandez","Cristina")
        self.assertEqual(persona.__str__(), "1,Fernandez,Cristina")
if __name__=="__main__":
    unittest.main()