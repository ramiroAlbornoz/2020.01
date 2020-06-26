from io import open
import pickle

class Pelicula:
    # Constructor de clase
    def __init__(self, codigo, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion
        self.codigo = codigo
        print('Se ha creado la película: ', self.titulo)​


    def __str__(self):
        return '{} ({})'.format(self.titulo, self.codigo)


class PeliculaRepo:
    peliculas = []

    def __init__(self):
        self.cargar()
        ​
    def add(self, p):
        self.peliculas.append(p)
        self.guardar()
        
    def find_all(self):
        if len(self.peliculas) == 0:
            print("El diccionario está vacío")
            return
        for p in self.peliculas:
            print(p)

    def cargar(self):
        fichero = open('PeliculaRepo.pckl', 'ab+')
        fichero.seek(0)
        try:
            self.peliculas = pickle.load(fichero)
        except Exception:
            print("El fichero está vacío")
        finally:
            fichero.close()
            print("Se han cargado {} películas".format(len(self.peliculas)))​
    
    def guardar(self):
        fichero = open('PeliculaRepo.pckl', 'wb')
        pickle.dump(self.peliculas, fichero)
        fichero.close()










