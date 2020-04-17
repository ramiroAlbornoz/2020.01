peso = input("Escriba su peso: ")
altura = input("Escriba su altura: ")

ind = round(float(peso)/float(altura)**2,2)
print("El indice resultante es: ", str(ind))