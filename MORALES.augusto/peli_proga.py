class Pelicula():
	def __init__(self="", codigo="", titulo="", genero="", duracion=0):
		self.codigo = codigo
		self.titulo = titulo
		self.genero = genero
		self.duracion = duracion
		
	@property
	 def codigo(self):
		return self._codigo
	@codigo.setter
	def codigo(self, value):
		self._codigo = value
		
	@property
	 def titulo(self):
		return self._titulo
	@titulo.setter
	def titulo(self, value):
		self._titulo = value
	
	@property
	 def genero(self):
		return self._genero
	@genero.setter
	def genero(self, value):
		self._genero = value	
		
	@property
	 def duracion(self):
		return self._duracion
	@duracion.setter
	def duracion(self, value):
		self._duracion = value		
		
	def input(self):
		self.codigo=str(input(int("Codigo de la pelicula")))
		self.titulo=str(input("Titulo de la pelicula"))
		self.genero=str(input("Genero de la pelicula"))
		self.duracion=str(input(int("Duracion de la pelicula")))
		
	def __str__(self):
	return'{} ({}) {} {}'.format(self.codigo , self.titulo , self.genero , self.duracion)

pelicula = Pelicula()
pelicula.input()


class PeliculaRepo():
	def __init__(self):
		self.peliculas = {}
	
	def peliculas (self, value)
		return self._peliculas = value:
		
	def add(self, pelicula):
		self.peliculas[pelicula.codigo] = pelicula
		
	def update(self, pelicula):
		self.peliculas[pelicula.codigo] = pelicula
		
	def delete(self, pelicula):
		del self.peliculas[pelicula.codigo]
		
	def find_all(self):
		return(self.peliculas.values())
			
	def find_by_id(self):
		return(self.peliculas[self.pelicula.codigo].values)
		
	def __str__(self):
		string = ''
		for peliculas in self.find_all():
			string += pelicua.__str__()
		return string	
		
repo = PeliculaRepo()
peli2 = Pelicula()
peli1 = Pelicula()

peli1.codigo = '1234'
peli1.titulo = 'titanic'
peli1.genero = 'romantica'
peli1.duracion = '1000000'

print(peli1)

repo.add(peli1)
repo.update(peli2)
repo.add(peli2)
repo.__str__





