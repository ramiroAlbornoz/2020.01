class Pelicula:
    def __init__(self, codigo="", titulo="", genero="", duracion=0):
        self.codigo = codigo
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        if value == "":
            raise ValueError("No puede ser vacío")
        self._codigo = value

    def input(self):
        self.codigo = int(input("Ingrese el codigo de la pelicula."))
        self.titulo = str(input("Ingrese el titulo de la pelicula."))
        self.genero = str(input("Ingrese el genero de la pelicula."))
        self.duracion = int(input("Ingrese la duracion de la pelicula."))

    def __str__(self):
        return "%s %s %s %d" % (self.codigo, self.titulo,
                                self.genero, self.duracion)


if __name__ == '__main__':
    pelicula = Pelicula('tt7713068',
                        'Birds of Prey: And the Fantabulous Emancipation' +
                        ' of One Harley Quinn', 'Action, Adventure, Crime',
                        109)

    print(Pelicula)

    print(Pelicula.__dict__)
