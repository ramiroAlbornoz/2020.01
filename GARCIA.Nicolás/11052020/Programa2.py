from io import open
import pickle
​
​
class Pelicula:
    def __init__(self,codigo, titulo, genero, duracion):
        self.codigo = codigo
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion
        print('Se ha creado la película:', self.titulo)
	def input(self):
		
	def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)
​class Catalogo:
    peliculas = []
​
    # Constructor de clase
    def __init__(self):
        self.cargar()
​
    def agregar(self, p):
        self.peliculas.append(p)
        self.guardar()
​
    def mostrar(self):
        if len(self.peliculas) == 0:
            print("El catálogo está vacío")
            return
        for p in self.peliculas:
            print(p)
​
    def cargar(self):
        fichero = open('catalogo.pckl', 'ab+')
        fichero.seek(0)
        try:
            self.peliculas = pickle.load(fichero)
        except Exception:
            print("El fichero está vacío")
        finally:
            fichero.close()
            print("Se han cargado {} películas".format(len(self.peliculas)))
​
    def guardar(self):
        fichero = open('catalogo.pckl', 'wb')
        pickle.dump(self.peliculas, fichero)
        fichero.close()
​
​
# Creamos un catálogo
c = Catalogo()
​
# Mostramos el contenido
c.mostrar()
​
# Agregamos una película
c.agregar(Pelicula("Endgame", 181, 2019))
​
# Mostramos el catálogo de nuevo
c.mostrar()
