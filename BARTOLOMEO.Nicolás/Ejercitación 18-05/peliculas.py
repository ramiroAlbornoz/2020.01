class Pelicula:
    def __init__(self, codigo=0, titulo="", genero="", duracion=""):
        self.codigo = codigo
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion

    def input(self):
        self.codigo = int(input("Ingrese el código de la película que desea añadir."))
        self.titulo = input("Ingrese el título de la película que desea añadir.")
        self.genero = input("Ingrese el género de la película que desea añadir.")
        self.duracion = int(input("Ingrese la duración de la película que desea añadir."))

    def __str__(self):
        return '{} ({}) {} {}'.format(self.codigo , self.titulo, self.genero, self. duracion)

class PeliculaRepo:
    def __init__(self):
        self.peliculas = {}

    def add(self, pelicula):
        self.peliculas[pelicula.codigo] = pelicula

    def update(self, pelicula):
        self.peliculas[pelicula.codigo] = pelicula 

    def delete(self, pelicula):
        del self.peliculas[pelicula.codigo]

    def find_all(self):
        return (self.peliculas.values())

    def find_by_id(self):
        return (self.peliculas[self.pelicula.codigo].values)
    
    def __str__(self):
        string= ''
        for pelicula in self.find_all():
            string+=pelicula.__str__()
        return string

repo = PeliculaRepo()
peli2 = Pelicula()
peli1 = Pelicula()

peli1.codigo = '1234'
peli1.titulo = 'Timmy en la montaña'
peli1.genero = 'Aventura'
peli1.duracion = '300'

print(peli1)

repo.add(peli1)
repo.update(peli2)
repo.add(peli2)

repo.__str__



