from pelicula import Pelicula


class PeliculaRepo():
    def __init__(self):
        self.peliculas = {}

    @property
    def peliculas(self):
        return self._peliculas

    @peliculas.setter
    def peliculas(self, value):
        self._peliculas = value

    def add(self, pelicula):
        if pelicula.codigo in self.peliculas:
            raise KeyError
        self.peliculas[pelicula.codigo] = pelicula

    def update(self, pelicula, codigo):
        self.peliculas[codigo] = pelicula

    def delete(self, codigo):
        del self.peliculas[codigo]

    def find_all(self):
        peliculas = []
        for pelicula in self.peliculas.values():
            peliculas.append(pelicula)
        return peliculas

    def find_by_id(self, codigo):
        return self.peliculas[codigo]

    def __str__(self):
        string = ""
        for pelicula in self.find_all():
            string += pelicula.__str__() + "\n"
        return string

if __name__ == "__main__":
    pelicula = Pelicula("19","Titanic","Crimen", 100)

    repo = PeliculaRepo()
    repo.add(pelicula)


    pelicula = Pelicula("19","Barnie","Drama", 200)

    try:
        repo.add(pelicula)
    except KeyError as e:
        print(e.args[0])

    print(repo.__str__())





