class Persona():
    def __init__(self, documento=0, apellido="", nombre=""):
        self.documento = documento
        self.apellido = apellido
        self.nombre = nombre

    def __str__(self):
        return "%d: %s, %s" % (self.documento, self.apellido, self.nombre)


class Alumno(Persona):
    def __init__(self, documento=0, apellido="", nombre="", legajo=0):
        super().__init__(documento, apellido, nombre)
        self.legajo = legajo

    def __str__(self):
        return "%s -> %d" % (super().__str__(), self.legajo)


if __name__ == "__main__":
    persona = Persona(3, "Fernandez", "Alberto")
    alumno = Alumno(2, "Suarez", "Rodolfo", 3)

    print(persona)
    print(alumno)
