import unittest
from alumnos import Persona
from parameterized import parameterized
class TestAlumno(unittest.TestCase):
    @parameterized.expand([(1,"Fernandez","Cristina","1, Fernandez, Cristinapip"),(2,"Fernandez","Alberto","2,Fernandez,Alberto"),(5,"guzman","martin","5,guzman,martin")])
    
    def test_str_persona(self,legajon,apellido,nombre,to_string):
        persona=Persona(1,"Fernandez","Cristina")
        self.assertEqual(persona.__str__(), to_string)
    
    def test_str_alumno(self):
        alumno=Alumno(8,"peron","juan domingo",3,3.14)
        self.assertEqual(alumno.__str__(), "8: Peron, Juan Domingo - Chequera: 3 - Nivel de Facha: 3.140000")
if __name__=="__main__":
    unittest.main()