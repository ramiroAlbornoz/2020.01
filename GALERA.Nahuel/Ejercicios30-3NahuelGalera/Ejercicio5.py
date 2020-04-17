inversion = float(input("¿Cuánto desea invertir? "))
interes = float(input("Porcentaje de intereses "))
años = int(input("¿Por cuántos años? "))
for i in range(años):
    inversion *= 1 + interes / 100 
    print("Su capital tras " + str(i+1) + " años de intereses es de: " + str(round(inversion, 2)))







