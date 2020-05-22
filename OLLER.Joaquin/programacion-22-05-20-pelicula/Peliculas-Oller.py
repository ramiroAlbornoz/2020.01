class Pelicula:
    # Constructor de clase
    def __init__(self, titulo="", duracion="", codigo=0, genero=""):
        self.titulo = titulo
        self.duracion = duracion
        self.codigo = codigo
        self.genero = genero

    def input(self):
        self.titulo = str(input("Ingrese el titulo: " ))
        self.duracion = int(str(input("Ingrese la duracion en min: " )))
        self.codigo = int(str(input("Ingrese el codigo: " )))
        self.genero = str(input("Ingrese el genero: " ))
        print('Se ha creado la película:', self.titulo)
    
    def str(self):
         return '%s %s %s %d' % (self.codigo, self.titulo, self.duracion, self.genero)

peli=Pelicula()
peli.input()

class PeliculaRepo:
    #Metodos
    def __init__(self):
        self.peliculas = {}

    @property
    def peliculas(self):
        return self._peliculas

    @peliculas.setter
    def peliculas(self, value):
        self._peliculas = value

    def add(self, pelicula):
        self.peliculas[pelicula.codigo] = pelicula

    def update(self, pelicula, codigo):
        self.peliculas[codigo] = pelicula

    def delete(self, codigo):
        del self.peliculas[codigo]

    def find_all(self):
        peliculas=[]
        for pelicula in self.peliculas.values():
            peliculas.append(pelicula)
        return peliculas

    def find_by_id(self, codigo):
        return self.peliculas[codigo]

    def __str__(self):
        string = ''
        for pelicula in self.find_all():
            string += pelicula.__str__()
        return string

if __name__ == '__main__':
    pelicula = Pelicula('0001', 'Programador en Windows', 'Accion', 120)