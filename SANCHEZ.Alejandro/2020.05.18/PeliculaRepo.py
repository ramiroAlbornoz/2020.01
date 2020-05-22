class Pelicula():
    # Constructor de clase
    def __init__(self, codigo =0, titulo ="", duracion =0, genero =""):
        self.codigo=codigo
        self.titulo = titulo
        self.duracion = duracion
        self.genero = genero
        print('Se ha creado la película:',self.titulo)

    def input (self):
        self.codigo=input("Codigo de la pelicula")
        self.titulo=input("Titulo de la pelicula")
        self.duracion=int(input("Duracion de la pelicula"))
        self.genero=input("Genero de la pelicula")

    def __str__(self):
        return '.[%s,%s,%s].' % (self.duracion, self.titulo, self.genero)

class PeliculaRepo(Pelicula):
    # Constructor de clase

    def __init__(self):
        self.peliculas={}

    def add (self,pelicula):
        self.peliculas[pelicula.codigo] = pelicula

    def update (self,peliculas,codigo):
        self.peliculas[codigo]=pelicula

    def delete (self,codigo):
        del self.peliculas[codigo]

    def find_all (self):
        peliculas=[]
        for pelicula in self.peliculas.values():
            peliculas.append(pelicula)
        return peliculas

    def find_by_id (self,codigo):
        return self.peliculas[codigo]
    
    def __str__(self):
        str1=""
        for pelicula in self.find_all():
            str1+=pelicula.__str__()
        return str1



pelicula = Pelicula(input("Codigo: "),input("Titulo: "),input("Duracion: "),input("Genero: "))
pelicula2 = Pelicula(input("Codigo: "),input("Titulo: "),input("Duracion: "),input("Genero: "))
pelicularepo=PeliculaRepo()
pelicularepo.add(pelicula)
pelicularepo.add(pelicula2)

print (pelicularepo.__str__())

pelicularepo.delete(input("Codigo(Para eliminar): "))

print (pelicularepo.__str__())
pelicularepo.add(pelicula)
pelicularepo.add(pelicula2)

pelicularepo.update(pelicula, input("codigo: "))

print (pelicularepo.__str__())

pelicularepo.find_all()
pelicularepo.find_by_id(input("Codigo de la pelicula a encontrar"))

