
malas = int(input("Introduce el número de barras vendidas que no son frescas: "))

descuento = 0.6
precio = 3.49 
precio = malas * precio * (1 - descuento)

print("El precio de una barra fresca es $" + str(round(precio)))
print("El descuento en una barra mala es " + str(descuento * 100) + "%")
print("Precio final: $" + str(round(precio, 2)))

5

