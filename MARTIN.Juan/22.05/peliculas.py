class Pelicula():
	def __init__(self, titulo="", duracion="", genero="", codigo=0):
		self.titulo = titulo
		self.duracion = duracion
		self.codigo = codigo
		self.genero = genero
        
	@property
	def codigo(self):
		return self._codigo

	@codigo.setter
	def codigo(self, value):
		self._codigo = value
        
	def input(self):
		self.titulo = str(input("titulo: "))
		self.duracion = str(input("duracion: "))
		self.codigo = int(input("codigo: "))
		self.genero = str(input("genero: "))
		print("Se ha creado la película:", self.titulo)

	def __str__(self):
		return '{} ({})'.format(self.titulo, self.duracion, self.codigo, self.genero)

pelicula = Pelicula()
pelicula.input()

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
			string += pelicula.__str__()
		return string

pelicularepo = PeliculaRepo()
pelicularepo.add(pelicula)
print (pelicularepo.__str__())

