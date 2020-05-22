    
class Pelicula:
    
    def __init__(self):
        self.codigo = 0
        self.titulo = ""
        self.genero = ""
        self.duracion = 0
    
    def input(self):
        self.codigo = int(input("Ingrese el codigo en numero: "))
        self.titulo = input("Ingrese el titulo de la pelicula: ")
        self.genero = input("ingrese el genero: ")
        self.duracion = int(input("ingrese la duracion en minutos: "))
        print(f"Se creo la pelicula {self.titulo} correctamente")

    def __str__(self):
        return '{} ({}) {} {}'.format(self.codigo , self.titulo, self.genero, self. duracion)

class PeliRepo:
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

repo = PeliRepo()
peli2 = Pelicula()
peli1 = Pelicula()

peli1.codigo = '1234'
peli1.titulo = 'Batman III'
peli1.genero = 'accion'
peli1.duracion = '130'


repo.add(peli1)


repo.__str__
    


h = int(input("Ingrese 1 para ver el repositorio y 2 para agregar tu pelicula: "))
if h == 1:
    print(peli1)
else: 
    peli2 = Pelicula()
    peli2.input()
    repo.update(peli2)
    repo.add(peli2)