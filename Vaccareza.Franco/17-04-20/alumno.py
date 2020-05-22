class Persona():
    def __init__(self, documento=0, apellido="", nombre=""):
        self.documento = documento
        self.apellido = apellido
        self.nombre = nombre

    def __str__(self):
        return "%d: %s, %s" % (self.documento, self.apellido, self.nombre)


class Alumno(Persona):
    def __init__(self, documento=0, apellido="", nombre="", chequera=0, nivel_de_facha=0):
        super().__init__(documento, apellido, nombre)
        self.chequera = chequera
        self.nivel_de_facha = nivel_de_facha

    def __str__(self):
        return "%s - Chequera: %d - Nivel de Facha: %f" % (super().__str__(), self.chequera, self.nivel_de_facha)


if __name__ == "__main__":
    persona = Persona(2345, "Horacio", "Rodriguez Larreta")

    print(persona)

    alumno = Alumno(3456, "Galera", "No tengo", 1, 72)

    print(alumno)
