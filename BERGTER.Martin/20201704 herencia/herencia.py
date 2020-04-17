class Persona():
    def __init__(self, documento=0, apellido="", nombre=""):
        self.documento = documento
        self.apellido = apellido
        self.nombre = nombre

    def __str__(self):
        return "%d: %s, %s" % (self.documento, self.apellido, self.nombre)

class Alumno(Persona):
    def __init__(self, documento=0, apellido="", nombre="", chequera=0, nivel_de_facha=""):
        super().__init__(documento, apellido, nombre)
        self.chequera = chequera
        self.nivel_de_facha = nivel_de_facha
    def __str__(self):
        return "%d: %s, %s, %d, %s" % (self.documento, self.apellido, self.nombre, self.chequera, self.nivel_de_facha)

if __name__ == "__main__":
    persona=Persona(22343,"Rodriguez","Larreta Horacio")
    alumno=Alumno(123321,"Vilches","Josias",69,"2.3")
    print(persona)
    print(alumno)