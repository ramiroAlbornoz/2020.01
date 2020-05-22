from io import open
import pickle

class Pelicula:
    def __init__(self, codigo="", titulo="", genero="", duracion=0):
        self.codigo = codigo
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion
        print("Se ha creado la película: ", self.titulo)

    @property
    def codigo(self):
        return self._codigo   
    @codigo.setter
    def codigo(self, value):
        if value == "":
            raise ValueError("No puede ser vacío")
        self._codigo = value
    
    def input(self):
        self.codigo = input("Ingrese el codigo: ")
        self.titulo = input("Ingrese el titulo: ")
        self.genero = input("Ingrese el genero: ")
        self.duracion = int(input("Ingrese la duracion: "))

    def __str__(self):
        return "%s %s %s %d" % (self.codigo, self.titulo, self.genero, self.duracion)

if __name__ == "__main__":
    pelicula = Pelicula("19","Titanic","Crimen", 100)
    
    print(pelicula)
    print(pelicula.__dict__)



