peso = float(input("ingrese su peso en Kg\n"))
Altura = float(input("ingrese su altura en m\n"))
imc = round(float(peso)/float(Altura)**2,2)
print("Tu indice de masa corporal es "+ str(imc))