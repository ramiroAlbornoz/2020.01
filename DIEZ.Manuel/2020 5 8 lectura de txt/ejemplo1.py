#para abrir, escribir y cerrar.
archivo = open('manolo.txt', 'w')
archivo.write("Hola")
archivo.close() 
#para abrir, leer y cerrar.
archivo = open('manolo.txt', 'r')
for linea in archivo.readlines():
    print (linea)
archivo.close()