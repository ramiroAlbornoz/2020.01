class Persona():
    def __init__(self, documento=0, apellido="", nombre=""):
        self.documento = documento
        self.apellido = apellido
        self.nombre = nombre

    def __str__(self):
        return "%d: %s, %s" % (self.documento, self.apellido, self.nombre)

if __name__ == "__main__":
    persona = Persona()
    persona.documento = 2
    persona.apellido = "Suarez"
    persona.nombre = "Rodolfo"

    print(persona)
