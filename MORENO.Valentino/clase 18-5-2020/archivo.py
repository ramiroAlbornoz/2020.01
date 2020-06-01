class Pelicula:
    
    def __init__(self, codigo="", titulo="", genero="", duracion=""):
        self.codigo = codigo 
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion
        print('Se ha creado la película:', self.titulo)
        
    def input(self):
        self.codigo = input("ingrese el codigo de pelicula")
        self.titulo = input("ingrese el titulo de pelicula")
        self.genero = input("ingrese el genero de pelicula")
        self.duracion = input("ingrese el duracion de pelicula")
        
    def __str__(self):
        return '{} ({}) {} {}'% (self.codigo, self.titulo, self.genero, self.duracion)

class PeliculaRepo:
    def __init__(self, peliculas=""):
        self.peliculas = {}
    
    def agregar(self, pelicula):
        self.peliculas[self.codigo] = pelicula 
        
    def modify(self):
        peliculas[self.codigo] = (pelicula)
