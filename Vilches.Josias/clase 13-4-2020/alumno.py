class Persona():
    def __init__(self, documento=0, apellido="", nombre=""):
        self.documento = documento
        self.apellido = apellido
        self.nombre = nombre

    def __str__(self):
        return "%d: %s, %s" % (self.documento, self.apellido, self.nombre)

    def input(self, titulo=True):
        if titulo:
            print("Ingresando persona...")
        self.documento = int(input("Ingrese Documento: "))
        self.apellido = input("Ingrese Apellido: ")
        self.nombre = input("Ingrese Nombre: ")

class Alumno(Persona):
    def __init__(self, documento=0, apellido="", nombre="", legajo=0):
        
        super().__init__(documento, apellido, nombre)
        self.legajo = legajo

    def __str__(self):
        return "%s leg: %d" % (super().__str__(), self.legajo)

    def input(self):
        print("Ingresando alumno...")
        super().input(False)
        self.legajo = int(input("Ingrese Legajo: "))
        
if __name__ == "__main__":
    persona = Persona()
    persona.input()

    alumno = Alumno()
    alumno.input()

    print(persona)
    print(alumno)
    
