from io import open
import pickle


class Pelicula():

    # Constructor de clase
    def __init__(self, codigo=0, titulo="", duracion=0, lanzamiento=0, genero=0):
        self.codigo = codigo
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        self.genero = genero
        print('Se ha creado la película:',self.titulo)

    def __str__(self):
        return "{} {} ({}) duracion:{} {}".format(self.codigo, self.titulo, self.lanzamiento, self.duracion, self.genero)

    def inputpeli(self):
        self.titulo = input("ingrese titulo: ")
        self.lanzamiento = input("ingrese lanzamiento: ")
        self.duracion = input("ingrese duracion: ")
        self.genero = input("ingrese genero: ")


class PeliculaRepo():


    def __init__(self, catalogo):
        print("accediendo el catalogo")
        self.catalogo = {}

    def add(self):
            peli = Pelicula()
            peli.inputpeli()
            peli.codigo = len(self.catalogo) + 1
            self.catalogo[peli.codigo] = peli
        
    def mostrar(self):
        print("Mostrar: ")
        if len(self.catalogo) <= 0:
            print("no hay nada")
        for i in self.catalogo:
            prueba = self.catalogo[i]
            print(prueba)
    
    def update(self):
        print("update: ")
        u = int(input("ingrese el codigo de pelicula que desea cambiar: "))
        if not(u in self.catalogo):
            print("esa pelicula no existe")
        else:
            peli = Pelicula()
            peli.inputpeli()
            peli.codigo = u
            self.catalogo[u] = peli
    def borrar(self):
        print("delete: ")
        u = int(input("ingrese el codigo de pelicula que desea borrar: "))
        if not(u in self.catalogo):
            print("esa pelicula no existe")
        else:
            del self.catalogo[u]
            print("la pelicula numero ", u, " se ha eliminado satisfactoriamente")

    def mostrar_por_numero(self):
        print("mostrar por id: ")
        u = int(input("ingrese el codigo de pelicula que desea mostrar: "))
        if not(u in self.catalogo):
            print("esa pelicula no existe")
        else:
            print(self.catalogo[u])


if __name__ == "__main__":
    c = PeliculaRepo({0})
    print("Bienvenido al software de peliculas, ingrese que desea hacer:")
    print("1 para ver peliculas")
    print("2 para agregar peliculas")
    print("3 para actualizar pelicula")
    print("4 para borrar peliculas")
    print("5 para mostrar la pelicula por codigo")
    print("6 para salir")


while True:
    eleccion = int(input("elija: "))

    if eleccion == 1:
        print("1")
        c.mostrar()

    elif eleccion == 2:
        print("2")
        c.add()

    elif eleccion == 3:
        print("3")
        c.update()

    elif eleccion == 4:
        print("4")
        c.borrar()

    elif eleccion == 5:
        print("5")
        c.mostrar_por_numero()
    else:
        print("6")
        break


