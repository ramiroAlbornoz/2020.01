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
        self.apellido = input("Ingrese Apellido: ")
        self.nombre = input("Ingrese Nombre: ")
        while True:
            try:
                self.edad = int(input("Ingrese Edad: "))
                if self.edad >= 125 or self.edad <= 0:
                    raise EdadError
                break
            except ValueError:
                print("maquina, la edad en numero...")
            except EdadError:
                print("che capo, es imposible que tengas mas de 124 años o menos de 1")

if __name__ == "__main__":
    persona = Persona("Fernandez", "Alberto", 60)
    persona.input()
    print(persona)