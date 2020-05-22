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
    def add (self, pelicula):
        if pelicula.codigo in self.peliculas:
            raise KeyError("Codigo repetido hermane")
        self.peliculas[pelicula.codigo] = pelicula
    def update (self, pelicula, codigo):
        self.peliculas[codigo] = pelicula
    def delete (self, codigo):
        del self.peliculas[codigo]
    def find_by_id(self, codigo):
        return self.peliculas[codigo]
    def find_all(self):
            peliculas = []
            for pelicula in self.peliculas.values():
                peliculas.append(pelicula)
            return peliculas
    def __str__(self):
        string= ''
        for pelicula in self.find_all():
            string += pelicula._str_() + '\n'
        return string

if __name__ == '__main__':
    pelicula = Pelicula("tt7713068", 
                         "IT", 
                         "Terror y suspenso", 
                         300)
                         
    repo = PeliculaRepo()
    repo.add(pelicula)
    
    pelicula = Pelicula("tt6036650", 
                         "Son como niños", 
                         "Comedia", 
                         123)

    repo.add(pelicula)
    print (repo.__str__())