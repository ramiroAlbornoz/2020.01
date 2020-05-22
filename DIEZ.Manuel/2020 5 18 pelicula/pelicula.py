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

    def str(self):
        return '%s %s %s %d' % (self.codigo, self.titulo, self.duracion, self.genero)
    
pelicula = Pelicula()
pelicula.input()
