class EdadError(Exception):
    pass


class Persona():
    def __init__(self, apellido="", nombre="", edad=0):
        self.apellido = apellido
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "%s, %s -> Edad %d" % (self.apellido, self.nombre, self.edad)

    def input(self):
        self.apellido = input("Ingrese apellido: ")
        self.nombre = input("Ingrese nombre: ")
        while True:
            try:
                self.edad = int(input("Ingrese edad: "))
                if self.edad < 1 or self.edad > 122:
                    raise EdadError
                break
            except ValueError:
                print("Bruto, tenés que poner un número")
            except EdadError:
                print("Esas no son edades de planes, taradito")


if __name__ == "__main__":
    persona = Persona("Fernandez", "Alberto", 60)
    print(persona)
    persona.input()
