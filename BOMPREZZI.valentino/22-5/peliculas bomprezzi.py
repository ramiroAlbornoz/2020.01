# encoding: utf-8
import sys
from io import open
import pickle

class Pelicula:
	def __init__(self, ):
		self.codigo = 0
		self.titulo = ""
		self.duracion = ""
		self.genero = ""
		@property
		def codigo(self):
			return self.codigo
		
		@codigo.setter 
		def codigo(self, value):
			if value == "":
				raise ValueError ("no puede ser vacio: ")
			self._codigo = value
			
	def input(self):
		self.codigo = int(input("ingrese el codigo de pelicula que desee anadir: "))
		self.titulo = (input("ingrese el titulo de pelicula que desea añadir: "))
		self.duracion = (input("ingrese el duracion de la pelicula que desea añadir: "))
		self.genero = (input("ingrese el genero de la pelicula que desea añadir: "))
		print("Se ha creado la pelicula: ", self.titulo)
	
	if __name__ == '__main__':
		pelicula = Pelicula ('ttre32r43','hulk', 'accion y aventuras',100)
	def __str__(self):
		 return '{} ({})'.format(self.codigo, self.titulo, self.duracion, self.genero)   
peli = Pelicula()
peli.input()

#PeliculaRepo

class PeliculaRepo:
	def __init__(self):
		self.peliculas = {}
	
	@property
	def peliculas(self):
		return self.peliculas
		
	@peliculas.setter
	def peliculas(self, value):
		self.peliculas = value
		
	def add(self, pelicula):
		if pelicula.codigo in self.peliculas:
			raise KeyError('codigo repetido')
		self.peliculas[pelicula.codigo] = pelicula
	
	def update(self, pelicula, codigo):
		self.peliculas[codigo] = pelicula
	
	def delete(self, codigo):
		del self.peliculas[codigo]
		
	def find_all(self):
		pelicula = []
		for pelicula in self.peliculas.values():
			peliculas.append(pelicula)
		return peliculas
	
	def find_by_id(self, codigo):
        return self.peliculas[codigo]
        
    def str(self):
        string = ''
        for pelicula in self.find.all():
            string += pelicula.str()+ '\n'
        return string
	
	if __name__ == '__main__':
		pelicula = Pelicula ('ttre32r43','hulk', 'accion y aventuras',100)
	
	repo = PeliculaRepo()
	repo.add(pelicula)
	
	print (repo.__str__())
