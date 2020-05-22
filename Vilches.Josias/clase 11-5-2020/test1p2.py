class Pelicula:
    def __init__(self, codigo, titulo, genero, duracion):
        self.codigo = codigo
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion
        
    def input (self):
        self.codigo = int(input("Ingrese el codigo de la pelicula que va a ingresar al sistema: "))
        #no tengo enie
        self.titulo = input("Ingrese el titulo de la pelicula que va a ingresar al sistema: ")
        self.genero = input ("Ingrese el genero de la pelicula que va a ingresar al sistema: ")
        self.duracion = int(input("Ingrese la duracion de la pelicula que va a ingresar al sistema: "))

    def __str__ (self):
        return '{} ({}) {} {}'.format(self.codigo, self.titulo, self.genero, self.duracion)
    
class PeliculaRepo:
    def __init__(self):
        self.pelicula = {}

    def add(self, pelicula):
        self.pelicula[pelicula.codigo] = pelicula

    def update(self, titulo, genero, duracion):
        nuevoObjeto = Pelicula()
        nuevoObjeto.titulo = input("Ingrese el titulo de la pelicula que va a ingresar al sistema: ")
        nuevoObjeto.genero = input("Ingrese el genero de la pelicula que va a ingresar al sistema: ")
        nuevoObjeto.duracion = input("Ingrese la duracion de la pelicula que va a ingresar al sistema: ")
        pelicula[pelicula.codigo] = nuevoObjeto

    def delete(self):
        del self.pelicula[pelicula.codigo]

    def find_all(self):
        return(self.pelicula.values())

    def find_by_id(self):
        return (self.pelicula[pelicula.codigo].values)

if __name__ == "__main__":
    pelicula = Pelicula()
