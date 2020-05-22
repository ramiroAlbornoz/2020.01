#Importa módulo pickle
import pickle
# Declara lista
lista = ['Perl', 'Python', 'Ruby']
# Abre archivo binario para escribir   
with open('lenguajes.dat', 'wb') as archivo:
    # Escribe lista en archivo
    pickle.dump(lista, archivo)
# Borra de memoria la lista
del lista  
# Abre archivo binario para leer
archivo = open('lenguajes.dat', 'rb')
# carga lista desde archivo
lista = pickle.load(archivo)
# Muestra lista  
print(lista)
# Cierra archivo
archivo.close() 