barras = int(input(" Número de panes vendidos no frescos: "))
precio = 3.49 
descuento = 0.6
coste = barras * precio * (1 - descuento)
print("El coste de pan fresco es: " + str(precio) + "€")
print("El descuento de pan no fresco es: " + str(descuento * 100) + "%")
print("El coste total es: " + str(round(coste, 2)) + "€")