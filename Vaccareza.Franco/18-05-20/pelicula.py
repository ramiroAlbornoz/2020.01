class Pelicula():
    def _init_(self, codigo="", titulo="", genero="", duracion=0):
        self.codigo = codigo
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion

    @property
    def codigo (self):
        return self._codigo

    @codigo.setter
    def codigo (self, value):
        if value == "":
            raise ValueError("No puede ser vacio")
        self._codigo = value 

    def input (self):
        self.codigo = input ("Ingrese el codigo: ")
        self.titulo = input ("Ingrese el titulo: ")
        self.genero = input ("Ingrese el genero: ")
        self.duracion = int (input ("Ingrese la duracion: "))

    def _str_(self):
        return '%s, %s, %s, %d' % (self.codigo, self.titulo, 
                                   self.genero, self.duracion)

if __name__ == '__main__':
    pelicula = Pelicula ("tt7713068", 
                         "IT", 
                         "Terros y suspenso", 
                         300)

    print(pelicula)
    print(pelicula.__dict__)