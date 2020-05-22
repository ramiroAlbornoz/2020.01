# Importa módulo pickle
import pickle
​
# Declara lista
lista = ['Perl', 'Python', 'Ruby']
​
# Abre archivo binario para escribir   
archivo = open('lenguajes.dat', 'wb')
​
# Escribe lista en archivo
pickle.dump(lista, archivo)
​
# Cierra archivo
archivo.close()
​
# Borra de memoria la lista
del lista  
​
# Abre archivo binario para leer
archivo = open('lenguajes.dat', 'rb')
​
# carga lista desde archivo
lista = pickle.load(archivo)
​
# Muestra lista  
print(lista)
​
# Cierra archivo
archivo.close()